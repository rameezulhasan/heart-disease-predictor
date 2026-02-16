# 🩺 Heart Disease Prediction App

A Machine Learning web application that predicts whether a patient is at risk of heart disease based on medical attributes.  

This project uses **Logistic Regression** as the final selected model and is deployed using **Streamlit**.

---

## 📸 Application Preview

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://heart-disease-predictor-ap.streamlit.app/)


![App Screenshot](/heart-disease-img.png)



---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide.  
This project aims to build a predictive model that can assess heart disease risk based on patient medical data.

The application allows users to:

- Enter patient medical information
- Process the data using trained ML model
- Receive a simple risk prediction:
  - ✅ Not At Risk
  - ⚠️ At Risk

---

## 🧠 Machine Learning Approach

### 🔹 Problem Type
Binary Classification

Target Variable:
- `HeartDisease` (0 = No, 1 = Yes)

---

### 🔹 Models Tested

The following supervised learning models were trained and evaluated:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Decision Tree
- Support Vector Machine (SVM)

After evaluation using:
- Accuracy
- Precision
- Recall
- F1 Score

**Logistic Regression** was selected as the final model due to its balanced performance and interpretability.

---

## 📊 Final Model Performance (Logistic Regression)

- Accuracy: ~87%
- Precision: ~91%
- Recall: ~86%
- F1 Score: ~88%

This provides a strong and reliable balance for medical risk prediction.

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 🛠️ Project Workflow

1. Data Cleaning & Preprocessing
2. One-Hot Encoding of Categorical Variables
3. Train-Test Split
4. Feature Scaling (StandardScaler)
5. Model Training & Comparison
6. Model Evaluation
7. Model Saving using Joblib
8. Streamlit UI Integration
9. Deployment Ready Structure

---

## 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── Logistic_Regression_hearDisease.pkl
├── scaler_heart.pkl
├── columns_hear.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rameezulhasan/heart-disease-predictor.git
cd heart-disease-prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

## 🌍 Deployment

This project can be deployed on:

- Streamlit Community Cloud  
- Render  
- Railway  
- Hugging Face Spaces  

---

## 🖥️ Application Features

- Clean and professional user interface  
- Real-time prediction  
- Automatic feature alignment  
- Proper feature scaling  
- Production-ready project structure  

---
