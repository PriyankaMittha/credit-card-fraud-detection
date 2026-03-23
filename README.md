# 💳 Credit Card Fraud Detection System

A Machine Learning web application that detects whether a credit card transaction is **SAFE ✅ (Legitimate)** or **RISKY ⚠️ (Fraudulent)** using Logistic Regression.

---

## 📊 Dataset

This project uses the **Credit Card Fraud Detection Dataset** from Kaggle.

🔗 Dataset Link:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud 

### 📌 Dataset Information:

* Contains transactions made by European cardholders in September 2013 
* Total Transactions: **284,807**
* Fraudulent Transactions: **492 (0.172%)** 
* Highly **imbalanced dataset** (real-world scenario)
* Features:

  * `V1 – V28` → PCA transformed features
  * `Time` → Time elapsed between transactions
  * `Amount` → Transaction amount
  * `Class` → Target variable (0 = Legitimate, 1 = Fraud)

---

⚠️ **Note:**
Due to confidentiality, original feature names are not available and are transformed using PCA. 

---

## 🚀 Features

* 🔍 Real-time fraud detection
* 📊 Machine Learning model (Logistic Regression)
* 🌐 Interactive web app using Streamlit
* 🧠 User-friendly output (SAFE / RISKY)
* ⚡ Fast and lightweight

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
credit-card-fraud-detection-streamlit/
│── test.py
│── creditcard.csv
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/credit-card-fraud-detection-streamlit.git
cd credit-card-fraud-detection-streamlit
```

### 2️⃣ Create Virtual Environment

```
python -m venv myenv
myenv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Application

```
streamlit run app.py
```

---

## 🧪 Sample Test Transactions

### 🟢 Legitimate Transaction (SAFE)

```
0, -1.359807, -0.072781, 2.536346, 1.378155, -0.338321, 0.462388, 0.239599, 0.098698, 0.363787, 0.090794, -0.551600, -0.617801, -0.991390, -0.311169, 1.468177, -0.470401, 0.207971, 0.025791, 0.403993, 0.251412, -0.018307, 0.277838, -0.110474, 0.066928, 0.128539, -0.189115, 0.133558, -0.021053, 149.62
```

👉 Output: **SAFE ✅**

---

### 🔴 Fraudulent Transaction (RISKY)

```
0, -2.312227, 1.951992, -1.609851, 3.997906, -0.522188, -1.426545, -2.537387, 1.391657, -2.770089, -2.772272, 3.202033, -2.899907, -0.595222, -4.289254, 0.389724, -1.140747, -2.830056, -0.016822, 0.416956, 0.126911, 0.517232, -0.035049, -0.465211, 0.320198, 0.044519, 0.177840, 0.261145, -0.143276, 0.00
```

👉 Output: **RISKY ⚠️ (Fraudulent Transaction)**

---

## 📊 Model Details

* Algorithm: Logistic Regression
* Data Handling: Under-sampling technique
* Evaluation: Accuracy Score

---

## 💡 Future Enhancements

* 📈 Add visualization dashboard
* 📂 Upload CSV for bulk detection
* 🤖 Use advanced models (Random Forest, XGBoost)
* 🌍 Deploy on cloud (Streamlit Cloud / AWS)

---

## 👩‍💻 Author

Priyanka Mittha
📧 [mitthapriyanka16@gmail.com](mailto:mitthapriyanka16@gmail.com)

🔗 LinkedIn: https://www.linkedin.com/in/priyanka-mittha

---

## ⭐ If you like this project, give it a star!
