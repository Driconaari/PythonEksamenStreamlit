import streamlit as st
from pages import calculator, about

def show():
    st.title("Om renter og opsparing")
    st.write("Her forklarer vi renters rente, bidrag mv...")

page = st.sidebar.radio(
    "Vælg side / Choose page",
    ("Millionærberegner", "Om renter og opsparing")
)

if page == "Millionærberegner":
    calculator.show()
elif page == "Om renter og opsparing":
    show()