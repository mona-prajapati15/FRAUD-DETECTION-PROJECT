import streamlit as st
import streamlit as st

st.set_page_config(page_title="Fraud Detection", layout="centered")

st.title("💳 Online Payment Fraud Detection")

st.write("Enter transaction details below")

amount = st.number_input("Transaction Amount")
oldbalanceOrg = st.number_input("Old Balance")
newbalanceOrig = st.number_input("New Balance")

type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT"]
)

if st.button("Detect Fraud"):

    if amount > 100000:
        st.error("🚨 Fraudulent Transaction Detected")
    else:
        st.success("✅ Safe Transaction")
import joblib
import numpy as np
