# 💻 Laptop Price Prediction using Machine Learning

![Python](https://img.shields.io/badge/python-3.13-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.30-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Overview

This project presents a complete **end-to-end machine learning pipeline** for predicting laptop prices based on hardware specifications. It covers everything from data preprocessing and feature engineering to model training, evaluation, and deployment.

The final solution is deployed using **Streamlit**, offering an interactive interface for real-world usage.

### 🚀 Key Features
- 🔹 Single laptop price prediction  
- 🔹 Batch prediction via CSV upload  
- 🔹 Interactive web interface  

---

## 🎯 Problem Statement

Laptop prices depend on multiple interacting features such as processor type, RAM, storage, GPU, and display characteristics. These relationships are often **non-linear and complex**, making manual estimation unreliable.

### Objective:
- Learn complex feature relationships  
- Provide accurate and consistent predictions  
- Generalize well on unseen data  

---

## 📊 Dataset

**Source:** Kaggle Laptop Dataset  

### 🔢 Numerical Features
- RAM (GB)  
- Storage (GB)  
- Screen Size (inches)  

### 🔤 Categorical Features
- Processor  
- GPU  
- Operating System  
- Brand  
- Warranty  

---

## 🔍 Exploratory Data Analysis (EDA)

### 📈 Key Observations
- Price distribution is **right-skewed** (presence of high-end outliers)  
- RAM has a **strong positive correlation** with price  
- Dedicated GPUs significantly increase pricing  
- Brands form clear pricing tiers  

### ⚠️ Data Issues
- Missing values in categorical features  
- Outliers in high-price range  
- Inconsistent category labels  

### 🛠️ Preprocessing Steps
- Missing value imputation  
- Outlier handling  
- Standardization of categorical variables  

---

## 🧠 Feature Engineering

Feature engineering significantly improved model performance.

### Techniques Used
- One-Hot Encoding (categorical variables)  
- Label Encoding (where necessary)  
- Feature normalization  

### Derived Features
- GPU category indicator  
- Storage type classification  
- Brand segmentation (premium vs non-premium)  

---

## 🤖 Model Selection

Models evaluated:
- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  

### 🏆 Final Model: Random Forest Regressor

**Why?**
- Handles non-linear relationships well  
- Performs strongly on tabular data  
- Resistant to overfitting  

---

### 📏 Model Evaluation

- **Train/Test Split:** 80% / 20%  
- **Metric:** R² Score

### 📊 Model Comparison

| Model               | R² Score |
|--------------------|--------|
| Linear Regression  | 0.65   |
| Decision Tree      | 0.72   |
| Random Forest      | 0.80 ✅ |

### 📊 Performance
- **R² Score:** `0.80`

### 📌 Interpretation
The model explains **~80% of the variance** in laptop prices, indicating strong predictive performance.

---

## 📉 Predicted vs Actual Analysis

### Observations
- Strong alignment in low-to-mid price ranges  
- Higher variance for expensive laptops  
- Reduced accuracy at extreme values  

### Insight
- Data imbalance in high-end laptops  
- Tree-based models struggle with extrapolation  

---

## ⭐ Feature Importance

Top features influencing price:
- RAM  
- GPU  
- Processor  
- Storage  
- Display Size  

### Insight
Hardware specifications are the dominant drivers of laptop pricing.

---

## 🌐 Application (Streamlit)

An interactive web application is included.

### Features
- 🔹 Single prediction input  
- 🔹 Batch prediction via CSV  
- 🔹 Simple and user-friendly UI

## 📸 Application Preview

### 🔹 Single Prediction
![Single Input](screenshots/single_input_page.png)

### 🔹 Prediction Result
![Result](screenshots/single_predict_result.png)

---

## 📁 Project Structure

```bash
Laptop-price-predictor/
│
├── Data/
│   └── laptops.csv
│
├── Models/
│   ├── model.pkl
│   └── columns.pkl
│
├── screenshots/
│   ├── single_input_page.png
│   ├── single_predict_result.png
│   ├── multiple_input_page.png
│   └── multiple_prediction_result.png
│
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
├── .gitignore
└── README.md
```

### ⚙️ How to Run

```bash
# Clone the repository
git clone https://github.com/Tanvirahmed-ML/Laptop-price-predictor.git

# Navigate to project directory
cd Laptop-price-predictor

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
python -m streamlit run app.py
```
### 📚 Key Learnings
Built a complete ML pipeline from scratch
Applied feature engineering to improve performance
Evaluated regression models using R² score
Understood real-world challenges like outliers and data imbalance
Developed an interactive app using Streamlit
### 💡 Insights
Tree-based models perform exceptionally well on tabular data
Feature engineering is critical for better performance
Proper handling of categorical variables is essential
### ⚠️ Limitations
Lower accuracy for high-end laptops
Limited dataset reduces generalization
Sensitive to extreme outliers
## 🔮 Future Work
Hyperparameter tuning (Grid Search / Random Search)
Try advanced models (XGBoost, Gradient Boosting)
Improve feature engineering
Deploy on cloud platforms (Streamlit Cloud, AWS, GCP)

## 💼 Real-World Impact

This system can help:
- E-commerce platforms estimate pricing
- Users compare laptop value
- Retailers optimize pricing strategies
### 👨‍💻 Author

Tanvir Ahmed Nafis
🎓 CSE Student, East Delta University
📍 Chattogram, Bangladesh

🔗 GitHub: https://github.com/Tanvirahmed-ML

### 🙏 Acknowledgment

This project demonstrates a structured approach to solving a real-world regression problem by combining machine learning techniques with practical deployment.
