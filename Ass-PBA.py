import streamlit as st

st.title("Student Specialisation Recommendation System")

# user input assign to variables
student_name = st.text_input("Enter student name: ")
matric_num = st.text_input("Enter student matric number: ")
pf_mark = st.text_input("Enter Programming Fundamentals mark: ")
ca_mark = st.text_input("Enter Computer Architecture mark: ")
os_mark = st.text_input("Enter Operating Systems mark: ")


# functions
def calc_software_score(pf, ca, os):
    return (pf * 0.50) + (ca * 0.25) + (os * 0.25)

def calc_networking_score(pf, ca, os):
    return (pf * 0.20) + (ca * 0.40) + (os * 0.40)

def determine_specialisation(sw_score, nw_score):
    if sw_score > nw_score:
        return "Software Application Development"
    elif nw_score > sw_score:
        return "Networking System"
    else:
        return "Both specialisations are suitable"


# validation and exception handling
if st.button("Recommend Specialisation"):

    # checks if input is null
    if not student_name or not matric_num:
        st.error("Please enter both Student Name and Matric Number.")
    try:
        # convert string to float
        pf_mark = float(pf_mark)
        ca_mark = float(ca_mark)
        os_mark = float(os_mark)

        # checks if the value entered is between 0 - 100
        if not (0 <= pf_mark <= 100 and 0 <= ca_mark <= 100 and 0 <= os_mark <= 100):
            st.error("Please make sure marks is between 0 - 100.")
        else: # if user input correctly

            # create variables and assign parameters to functions
            software_score = calc_software_score(pf_mark, ca_mark, os_mark)
            networking_score = calc_networking_score(pf_mark, ca_mark, os_mark)
            recommendation = determine_specialisation(software_score, networking_score)

            # Result Display
            st.success("Analysis completed successfully!")
            st.subheader("-- Student Information --")
            st.write(f"Student Name: {student_name.strip('!@#$%^&*()-_=+')}") # perform clean output if user input special character
            st.write(f"Student Matric Number: {matric_num.strip('!@#$%^&*()-_=+')}") # perform clean output if user input special character

            st.subheader("-- Academic Performance --")
            st.write(f"Programming Fundamentals: {pf_mark}")
            st.write(f"Computer Architecture: {ca_mark}")
            st.write(f"Operating Systems: {os_mark}")

            st.subheader("Suitability Scored")
            st.write(f"Software Application Development Score: {software_score:.2f}")
            st.write(f"Network System Score: {networking_score:.2f}")

            st.subheader("Recommendation")
            st.info(f"{recommendation}")

    except ValueError: # if user input string in the number field
        st.error("Invalid input! Please enter valid numeric marks!")