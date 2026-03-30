# Laptop Price Prediction using Machine Learning

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.30-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Model:** Random Forest Regressor  
**Performance:** R² ≈ 0.82  
**Description:** Predicts laptop prices based on key specifications like RAM, CPU, storage, GPU, screen size, and brand. Supports single and batch predictions via a Streamlit app.  

Ever wondered if a laptop is priced fairly? This project predicts realistic laptop prices using machine learning. You can predict **a single laptop** or **multiple laptops at once** using a CSV file.  



## Overview

This project presents an end-to-end machine learning pipeline for predicting laptop prices based on hardware specifications. It integrates data preprocessing, feature engineering, model training, evaluation, and deployment into a practical application using Streamlit.

The project emphasizes both predictive performance and interpretability, providing insights into how different features influence laptop pricing.

---

## Problem Statement

Laptop prices depend on multiple interacting factors such as processor type, RAM, storage, GPU, and display characteristics. These relationships are complex and often non-linear.

The objective of this project is to build a regression model capable of learning these relationships and accurately predicting laptop prices from structured input features.

---

## Dataset

* Source: Kaggle Laptop Dataset

### Feature Types:

**Numerical Features:**

* RAM (GB)
* Storage (GB)
* Screen Size (inches)

**Categorical Features:**

* Processor
* GPU
* Operating System
* Brand
* Warranty

---

## Methodology

### Data Preprocessing

* Handled missing values and removed outliers
* Encoded categorical variables using Label Encoding and One-Hot Encoding
* Normalized numerical features

### Feature Engineering

* Extracted meaningful attributes from raw features
* Created derived features to improve model performance

### Model Selection

Models evaluated:

* Linear Regression
* Decision Tree Regression
* Random Forest Regression

**Final Model: Random Forest Regressor**

* Captures non-linear relationships effectively
* Provides feature importance insights

---

## Experiments and Results

### Training Setup

* Train/Test Split: 80% / 20%
* Evaluation Metric: R² Score

### Performance

* **R² Score: ~0.80**

---

### Predicted vs Actual Prices

```
![Predicted vs Actual](screenshots/pred_vs_actual.png)
```

**Observation:**

* Strong alignment for low-to-mid price ranges
* Increased error for high-end laptops
* Indicates limited extrapolation capability

---

### Feature Importance

```
![Feature Importance](screenshots/feature_importance.png)
```

**Insights:**

* Specification-related features dominate predictions
* RAM and display characteristics strongly influence price
* Feature engineering significantly improved performance

---

## Application Demo

### Single Input Page

```md id="img3"
![Single Input](screenshots/single_input_page.png)
```

### Single Prediction Result

```md id="img4"
![Single Prediction](screenshots/single_predict_result.png)
```

### Multiple Input Page

```
![Multiple Input](screenshots/multiple_input_page.png)
```

### Multiple Prediction Result

```
![Multiple Prediction](screenshots/multiple_prediction_result.png)
```
# Project Structure
Laptop-price-predictor/
│
├── Data/
│   └── laptops.csv
├── Models/
│   ├── model.pkl
│   └── columns.pkl
├── screenshots/
│   ├── single_input_page.png
│   ├── single_predict_result.png
│   ├── multiple_input_page.png
│   └── multiple_prediction_result.png
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
└── README.md
---

# 🚀 How to Run

```bash
# Clone the repository
  git clone https://github.com/Tanvirahmed-ML/Laptop-price-predictor.git
  cd Laptop-price-predictor

# Install dependencies
   pip install -r requirements.txt

# Run the app
   python -m streamlit run app.py


### 4. Install dependencies

```bash id="run5"
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the application

```bash id="run6"
python -m streamlit run app.py
```

---

## Key Learnings

* Built a complete end-to-end machine learning pipeline
* Applied feature engineering on structured data
* Evaluated regression models using R² score
* Understood limitations of models with outliers
* Developed an interactive ML application using Streamlit

---

## Insights

* Tree-based models perform well on structured/tabular data
* Feature engineering plays a crucial role in improving performance
* Handling categorical variables is a key challenge in real-world datasets

---

## Limitations

* Reduced accuracy for high-end laptops
* Dataset limitations affect generalization
* Model struggles with extreme outliers

---

## Future Improvements

* Hyperparameter tuning
* Use advanced models (XGBoost, Gradient Boosting)
* Improve feature engineering
* Deploy application on cloud platforms

---

## Author

Tanvir Ahmed Nafis
GitHub: https://github.com/Tanvirahmed-ML

---

## Acknowledgment

This project reflects my learning journey in machine learning and my interest in building practical, interpretable ML systems.

---


