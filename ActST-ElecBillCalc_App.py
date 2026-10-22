import streamlit as st

st.title("ELECTRICITY BILL CALCULATOR APPLICATION")
name = st.text_input("Enter your name: ")
acc = st.text_input("Enter your Account Number: ")
type = st.radio(
    "Select your Customer Type: ",
    ["Residental", "Commercial", "Industrial"],
)
month = st.selectbox(
    "Select your Billing Month: ",
    ["January", "February", "March", "April"]
)
usage = st.text_input("Enter your Electricity Usage (kWh): ")
calc = st.button("Calculate Bill")

if calc:
    if name == "" or acc == "" or usage == "":
        st.error("Field cannot be empty!")
    else:
        try:
            if type == "Residental":
                rate = 0.50
            elif type == "Commercial":
                rate = 0.80
            else:
                rate = 1.00
            electric = int(usage) * rate

            if electric >= 100:
                service = 10
            elif electric >= 50:
                service = 5
            else:
                service = 0
            total = electric + service
        except ValueError:
            st.error("Electricity Usage must contain a valid numerical value!")
        except ZeroDivisionError:
            st.error("Electricity Usage must be greater than 0!")
        else:
            st.subheader("~~~CUSTOMER INFORMATION~~~")
            st.write("Name: " + name)
            st.write("Account Number: " + acc)
            st.write("Customer Type: " + type)
            st.write("Billing Month: " + month)
            st.write("Usage: " + usage + "kWh")

            st.subheader("~~~BILL DETAILS~~~")
            st.write("Rate per kWh: RM " + str(rate))
            st.write("Electricity Charge: RM " + str(electric))
            st.write("Service Charge: RM " + str(service))
            st.write("Total Bill: RM " + str(total))
        finally:
            st.write("Electricity Bill Calculation process has been completed.")
else:
    st.write("Please fill in all fields.")