import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("3-MONTH BMI TRACKING APPLICATION")
st.subheader("Patient Information")
name = st.text_input("Full Name: ")
age = st.number_input("Age: ")
height = st.number_input("Height (m): (e.g. 1.49)")
st.subheader("Enter Weight (kg) for 3 Months")
weight1 = st.number_input("Weight for 1st Month: ")
weight2 = st.number_input("Weight for 2nd Month: ")
weight3 = st.number_input("Weight for 3rd Month: ")

def calc_bmi (h, w):
    bmi = w / (h * h)
    return round(bmi, 2)

def bmi_status(avg):
    if avg < 18.5:
        status = "Under Weight"
    elif avg < 25:
        status = "Normal Weight"
    else:
        status = "Over Weight"
    return status

if st.button("GENERATE"):
    try:
        if name == "":
            st.warning("Please fill in all fields")
        elif age < 1:
            st.warning("Age cannot be 0")
        elif height < 1.00 or height > 2.50:
            st.warning("Height must be in centimeters")
        elif weight1 <= 1 or weight2 <= 1 or weight3 < 1:
            raise ValueError("Weight must be in kilogram")
        else:
            bmi1 = calc_bmi(float(height), weight1)
            bmi2 = calc_bmi(float(height), weight2)
            bmi3 = calc_bmi(float(height), weight3)
            bmi_array = np.array([bmi1, bmi2, bmi3])
            month = np.array(["1st Month", "2nd Month", "3rd Month"])
            avg_bmi = np.mean(bmi_array)

            st.success("Calculation Successful!")
            st.divider()
            st.header("BMI Tracking Details")
            st.subheader("Patient Details")
            st.write("Name: ", name)
            st.write("Age: ", int(age), "years")
            st.write("Height: ", round(height, 2), "m")
            st.divider()

            st.subheader("BMI Information")
            st.write("1st Month BMI: ", bmi1)
            st.write("2nd Month BMI:", bmi2)
            st.write("3rd Month BMI: ", bmi3)
            st.write("Average BMI: ", round(avg_bmi, 2))
            st.write("BMI Status: ", bmi_status(avg_bmi))
            st.write("Highest BMI: ", np.max(bmi_array))
            st.write("Lowest BMI: ", np.min(bmi_array))
            st.divider()

            st.subheader("BMI Tracking Graph")
            plt.figure()
            plt.bar(month, bmi_array)
            plt.title("BMI Trend Over 3 Months")
            plt.xlabel("MONTH")
            plt.ylabel("BMI")
            for i, bmi in enumerate(bmi_array):
                plt.text(i, bmi + 0.1, str(bmi))
            st.pyplot(plt)
    except ValueError as ve:
        st.error(f"Error occur: {ve}")
    finally:
        st.divider()
        st.info("System run successfully")
else:
    st.info("Your result will shown here")
