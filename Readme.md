Laptop Price Prediction using Machine Learning



# Overview

This project presents an end-to-end machine learning system for predicting laptop prices based on hardware specifications. It integrates data preprocessing, feature engineering, model training, evaluation, and deployment into a unified pipeline, culminating in an interactive web application built with Streamlit.

The system is designed to handle both single-instance predictions and batch predictions, making it practical for real-world use cases such as price benchmarking and market analysis.

# Problem Statement

Laptop pricing is influenced by multiple interacting factors such as processor type, RAM, storage, GPU, and display characteristics. These relationships are often non-linear and complex, making manual estimation unreliable.

The objective of this project is to develop a regression model that can effectively learn these relationships and provide accurate and consistent price predictions from structured input features.

# Dataset
Source: Kaggle Laptop Dataset
Features

Numerical:

RAM (GB)
Storage (GB)
Screen Size (inches)

Categorical:

Processor
GPU
Operating System
Brand
Warranty
# Methodology
Data Preprocessing
Handled missing values and removed outliers
Encoded categorical variables using Label Encoding and One-Hot Encoding
Normalized numerical features
Feature Engineering
Extracted structured information from raw attributes
Created derived features to improve predictive performance
Model Selection

The following models were evaluated:

Linear Regression
Decision Tree Regressor
Random Forest Regressor

Final Model: Random Forest Regressor

Captures non-linear relationships effectively
Robust to noise and feature interactions
Provides feature importance for interpretability
# Experiments and Results
Training Configuration
Train/Test Split: 80% / 20%
Evaluation Metric: R² Score
Performance
R² Score: ~0.82
# Predicted vs Actual Prices

Observations:

Strong alignment in low-to-mid price ranges
Increased variance in high-end predictions
Indicates limited extrapolation capability for extreme values
# Feature Importance

Insights:

Hardware specifications dominate predictions
RAM and display features significantly influence pricing
Feature engineering contributed notably to performance gains
# Application Demo
Single Input Prediction

Batch Prediction (CSV Upload)

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
# How to Run
# Clone the repository
git clone https://github.com/Tanvirahmed-ML/Laptop-price-predictor.git
cd Laptop-price-predictor

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run the application
python -m streamlit run app.py
 Key Learnings
Developed a complete ML pipeline from data to deployment
Applied feature engineering on structured datasets
Evaluated regression models using R² score
Understood model limitations with outliers and edge cases
Built an interactive ML application using Streamlit
# Insights
Tree-based models perform strongly on tabular data
Feature engineering is critical for performance improvement
Handling categorical variables is a key real-world challenge
# Limitations
Reduced accuracy for high-end laptops
Dataset constraints limit generalization
Model struggles with extreme outliers
# Future Work
Hyperparameter tuning (Grid Search / Random Search)
Integration of advanced models (XGBoost, Gradient Boosting)
Enhanced feature engineering
Deployment on cloud platforms (e.g., Streamlit Cloud, AWS, GCP)
# Author

Tanvir Ahmed Nafis
Student of Computer Science and Engineering
East Delta University
Chattogram,Bangladesh
GitHub: https://github.com/Tanvirahmed-ML#

# Acknowledgment

This project reflects my learning journey in machine learning and my interest in building practical, interpretable, and deployable ML systems.
