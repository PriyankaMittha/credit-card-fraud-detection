import numpy as np
import streamlit as st
import pickle

# -------------------------------
# Load Model
# -------------------------------
model = pickle.load(open("cc_fraud.pkl", "rb"))

# Feature names (from dataset)
feature_names = [
    "Time","V1","V2","V3","V4","V5","V6","V7","V8","V9",
    "V10","V11","V12","V13","V14","V15","V16","V17","V18","V19",
    "V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"
]

# -------------------------------
# UI
# -------------------------------
st.title("💳 Credit Card Fraud Detection")

st.markdown("""
### 📌 Enter Transaction Details
👉 Fill values below to check if transaction is **SAFE or RISKY**
""")

# -------------------------------
# Input Fields
# -------------------------------
input_data = []

# Show only first 10 inputs for simplicity
for col in feature_names[:10]:
    val = st.number_input(f"{col}", value=0.0)
    input_data.append(val)

# Fill remaining features with 0
remaining = len(feature_names) - len(input_data)
input_data.extend([0] * remaining)

input_array = np.array(input_data).reshape(1, -1)

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔍 Check Transaction"):

    prediction = model.predict(input_array)

    st.markdown("---")

    if prediction[0] == 0:
        st.success("✅ SAFE Transaction")
        st.write("This looks like a normal transaction.")

    else:
        st.error("⚠️ RISKY Transaction")
        st.write("This may be a fraudulent transaction. Please verify!")

# -------------------------------
# Info Section
# -------------------------------
st.markdown("---")
st.markdown("""
### 🧠 Understanding Results:
- **SAFE ✅** → Legitimate Transaction  
- **RISKY ⚠️** → Fraudulent Transaction  
""")