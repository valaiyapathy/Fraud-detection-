"""
Simple Fraud Detection App
---------------------------
This app asks the user for details about a money transaction,
then uses our trained model to guess if it is FRAUD or NOT FRAUD.
"""

import streamlit as st
import joblib
import pandas as pd

# Step 1: Load the saved model (the "brain" we trained earlier)
# We only want to load it once, so we use @st.cache_resource
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# Step 2: Show a title and short message
st.title("💳 Fraud Detection App")
st.write("Fill in the transaction details below, then click Predict.")

# Step 3: Create input boxes so the user can type in transaction info
step = st.number_input("Step (time of transaction)", min_value=0, value=10)

txn_type = st.selectbox(
    "Transaction Type",
    ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"]
)

amount = st.number_input("Amount of Money", min_value=0.0, value=10000.0)

old_balance_org = st.number_input("Sender's Balance BEFORE", min_value=0.0, value=10000.0)
new_balance_orig = st.number_input("Sender's Balance AFTER", min_value=0.0, value=0.0)

old_balance_dest = st.number_input("Receiver's Balance BEFORE", min_value=0.0, value=0.0)
new_balance_dest = st.number_input("Receiver's Balance AFTER", min_value=0.0, value=10000.0)

# Step 4: When the user clicks the button, make a prediction
if st.button("Predict"):

    # These are extra clues we taught the model to look for.
    # We must create them here the SAME way we did during training.
    orig_balance_diff = old_balance_org - new_balance_orig      # how much money left the sender
    dest_balance_diff = new_balance_dest - old_balance_dest     # how much money the receiver got
    orig_emptied = int(amount == old_balance_org)               # 1 if sender's account was fully emptied
    error_balance_orig = new_balance_orig + amount - old_balance_org
    error_balance_dest = old_balance_dest + amount - new_balance_dest

    # Put everything into one row of a table, because that's what the model expects
    input_data = pd.DataFrame([{
        "step": step,
        "type": txn_type,
        "amount": amount,
        "oldbalanceOrg": old_balance_org,
        "newbalanceOrig": new_balance_orig,
        "oldbalanceDest": old_balance_dest,
        "newbalanceDest": new_balance_dest,
        "orig_balance_diff": orig_balance_diff,
        "dest_balance_diff": dest_balance_diff,
        "orig_emptied": orig_emptied,
        "errorBalanceOrig": error_balance_orig,
        "errorBalanceDest": error_balance_dest,
    }])

    # Ask the model: is this fraud or not?
    result = model.predict(input_data)[0]

    # Ask the model: how sure are you? (a number between 0 and 1)
    confidence = model.predict_proba(input_data)[0][1]

    # Step 5: Show the answer to the user
    st.subheader("Result")
    if result == 1:
        st.error("🚨 This looks like FRAUD!")
    else:
        st.success("✅ This looks SAFE (not fraud).")

    st.write(f"Model confidence it is fraud: {confidence:.0%}")

