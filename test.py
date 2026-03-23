import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st

# Load the dataset
cc_data = pd.read_csv('creditcard.csv')

# Separate the legitimate and fraudulent transactions
legit = cc_data[cc_data.Class == 0]
fraud = cc_data[cc_data.Class == 1]

# Under sampling
legit_sample = legit.sample(n=len(fraud), random_state = 2)
new_df = pd.concat([legit_sample, fraud], axis = 0)

# Splitting the data into features and target variables
X = new_df.drop(columns = 'Class', axis = 1)
y = new_df['Class']


# Split the data into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = 2)

# Training of model
model = LogisticRegression()
model.fit(X_train, y_train)

# Train logistic regression model
train_acc = accuracy_score(model.predict(X_train), y_train)
test_acc = accuracy_score(model.predict(X_test), y_test)

# -------------------------------
# UI
# -------------------------------
st.title("💳 Credit Card Fraud Detection")

st.markdown("""
### 📌 Enter Transaction Details
👉 Fill values below to check if transaction is **SAFE or RISKY**
""")

# -------------------------------
# Input Fields (Better than text input)
# -------------------------------
input_data = []

# Take first few important features for demo
for col in X.columns[:10]:   # you can increase this
    val = st.number_input(f"{col}", value=0.0)
    input_data.append(val)

# Fill remaining features as 0 automatically
remaining = len(X.columns) - len(input_data)
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

