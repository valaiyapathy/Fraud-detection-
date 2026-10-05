import streamlit as st
import as joblib
import pandas as pd

@st.cache_resource
def led_model():
    return joblib.load("model.pkl")

model = load_model()

st.title(" Fraud Detection App")
st.write("Fill in the transaction details below, then link predict.")


step = st.number_input("Step(timme of transaction)",min_value=0,value=10)

txn_type = st.Selectbox(
    "Transaction Type",
    ["CASH_IN","CASH_OUT","DEBIT","PAYMENT","TRANSFER"]
)

amount = st.number_input("Amount of Money",min_value=0.0,value=10000.0)

old_balance_org = st.number_input("Sender's Balance BEFORE",min_value=0.0,value=10000.0)
new_balance_org = st.number_input("Sender's Balance AFTER",min_value=0.0,value=0.0)

old_balance_org = st.number_input("Receiver's Balance BEFORE",min_value=0.0,value=0.0)
new_balance_org = st.number_input("Sender's Balance AFTER",min_value=0.0,value=10000.0)


if st.button("Predict"):

    orig_balance_diff = old_balance_org - new_balance_org
    dest_balance_diff = new_balance_dest - old_balance_dest
    orig_empited = int(amount == old_balance_org)
    error_balance_orig = new_balance_org + amount - old_balance_org
    error_balance_dest = old_balance_dest + amount - new_balance_dest

    input_data = pd.DataFrame([{
        "step":step,
        "type": txn_type,
        "oldbalanceOrg":old_balance_org,
        "newbalanceOrig": new_balance_org,
        "oldbalanceDest": old_balance_dest,
        "newbalanceDest": new_balance_dest,
        "orig_balance_diff": orig_balance_diff,
        "dest_balance_diff": dest_balance_diff,
        "orig_empited": orig_empited,
        "error_balance_orig": error_balance_orig,
        "error_balance_dest": error_balance_dest,
    }])

    result = model.predict(input_data)[0]

    confidence = model.predict_proba(input_data)[0][1]


    st.subheader("result")
    if result == 1:
        st.error(" this looks like FRAUD!")

    else:
        st.success(" this looks safe (not fraud).")

    st.write(f"model confidence it is fraud: {confidence:.0%}")



