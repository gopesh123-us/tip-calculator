import streamlit as st

st.title("Tip Calculator")

st.write("@Author: Gopesh Sharma")
st.write("@Date: 5/13/2026")

bill = st.number_input(
    "What is the amount of the total bill?",
    min_value=0.0,
    step=1.0
)

no_of_people = st.number_input(
    "How many people do you want to split the bill?",
    min_value=1,
    step=1
)

tip_percent = st.selectbox(
    "How much percentage do you want to tip?",
    [10, 15, 20]
)

if st.button("Calculate"):
    total_bill_with_tip = bill + ((bill * tip_percent) / 100)
    bill_per_person = total_bill_with_tip / no_of_people

    st.success(f"Each person should pay ${bill_per_person:.2f}")