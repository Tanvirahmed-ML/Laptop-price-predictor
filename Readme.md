# Laptop Price Prediction using Machine Learning

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.30-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

# 1. Overview

This project presents an end-to-end machine learning pipeline for predicting laptop prices based on hardware specifications. It integrates data preprocessing, feature engineering, model training, evaluation, and deployment into a unified workflow.

The system supports:
- Single-instance prediction  
- Batch prediction via CSV upload  

The final model is deployed using Streamlit, providing an interactive interface for real-world usage.

---

# 2. Problem Statement

Laptop pricing depends on multiple interacting features such as processor type, RAM, storage, GPU, and display characteristics. These relationships are non-linear and complex, making manual estimation unreliable.

The objective is to develop a regression model that:
- Learns complex feature interactions  
- Produces consistent and accurate predictions  
- Generalizes well to unseen data  

---

# 3. Dataset

Source: Kaggle Laptop Dataset  

## Features

### Numerical
- RAM (GB)  
- Storage (GB)  
- Screen Size (inches)  

### Categorical
- Processor  
- GPU  
- Operating System  
- Brand  
- Warranty  

---

# 4. Exploratory Data Analysis (EDA)

Exploratory analysis was conducted to understand feature distributions, relationships, and anomalies.

## Key Observations

- Price distribution is right-skewed, indicating high-end outliers  
- RAM shows strong positive correlation with price  
- Dedicated GPUs significantly increase price  
- Brand segmentation reveals clear pricing tiers  

## Data Issues Identified

- Missing values in categorical variables  
- Outliers in high-price range  
- Inconsistent categorical labels  

## Actions Taken

- Missing value imputation  
- Outlier handling using statistical methods  
- Standardization of categorical variables  

---

# 5. Feature Engineering

Feature engineering played a key role in improving model performance.

## Techniques Applied

- One-Hot Encoding for categorical variables  
- Label Encoding where applicable  
- Normalization of numerical features  

## Derived Features

- GPU category indicator  
- Storage type differentiation  
- Brand grouping for premium segmentation  

---

# 6. Model Selection

The following models were evaluated:

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  

## Final Model: Random Forest Regressor

Selected due to:
- Strong performance on tabular data  
- Ability to capture non-linear relationships  
- Robustness against overfitting  

---

# 7. Model Evaluation

## Training Configuration

- Train/Test Split: 80% / 20%  
- Evaluation Metric: R² Score  

## Performance

- R² Score: 0.80  

## Interpretation

The model explains approximately 80% of the variance in laptop prices, indicating strong predictive performance across most data ranges.

---

# 8. Predicted vs Actual Analysis

## Observations

- Strong alignment in low-to-mid price ranges  
- Increased variance in high-end predictions  
- Reduced accuracy for extreme values  

## Insight

This behavior indicates limited extrapolation capability due to:
- Data imbalance in high-price segments  
- Tree-based model limitations on unseen extremes  

---

# 9. Feature Importance

## Key Influencing Features

- RAM  
- GPU  
- Processor  
- Storage  
- Display size  

## Insight

Hardware specifications dominate pricing decisions, and feature engineering significantly improved predictive performance.

---

# 10. Application

The project includes an interactive web application built using Streamlit.

## Features

- Single laptop price prediction  
- Batch prediction via CSV upload  
- Simple and user-friendly interface  

---

# 11. Project Structure
Laptop-price-predictor/
│
├── Data/
│ └── laptops.csv
├── Models/
│   ├── model.pkl
│   └── columns.pkl
├── Screenshots/
│.   ├── single_input_page.png
│    ├── single_predict_result.png
│.   ├── multiple_input_page.png
│    └── multiple_prediction_result.png
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
└── README.md


---

# 12. How to Run

```bash
# Clone the repository
git clone https://github.com/Tanvirahmed-ML/Laptop-price-predictor.git
cd Laptop-price-predictor

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m streamlit run app.py

13. Key Learnings
Built an end-to-end machine learning pipeline
Applied feature engineering to improve model performance
Evaluated regression models using R² score
Identified real-world limitations such as outliers and data imbalance
Developed an interactive application using Streamlit
14. Insights
Tree-based models are highly effective for tabular data
Feature engineering plays a critical role in performance improvement
Proper handling of categorical variables is essential
15. Limitations
Reduced accuracy for high-end laptops
Dataset constraints limit generalization
Sensitivity to extreme outliers
16. Future Work
Hyperparameter tuning (Grid Search / Random Search)
Integration of advanced models (XGBoost, Gradient Boosting)
Enhanced feature engineering techniques
Deployment on cloud platforms (Streamlit Cloud, AWS, GCP)
17. Author
Tanvir Ahmed Nafis
Student of Computer Science and Engineering
East Delta University
Chattogram, Bangladesh
GitHub: https://github.com/Tanvirahmed-ML
18. Acknowledgment
This project reflects a structured approach to solving a real-world regression problem and demonstrates the integration of machine learning concepts with practical deployment.
