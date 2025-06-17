
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from current_account import CurrentAccount

st.set_page_config(page_title="Maten Bank", layout="centered")


currents = CurrentAccount(50000)

st.title("Welcome to Maten Bank")


with st.form('current_form'):
    amount = st.number_input("Enter amount", min_value=0, step=1)
    operation = st.selectbox("Select operation", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

if submit:
    with st.spinner("Processing..."):
        if operation == "Withdraw":
            if amount <= currents.balance:
                currents.withdraw(amount)
                st.success(f"Transaction successful! New balance: {currents.balance}")
            else:
                st.error("Insufficient funds.")
        else:  
            currents.deposit(amount)
            st.success(f"Transaction successful! New balance: {currents.balance}")
