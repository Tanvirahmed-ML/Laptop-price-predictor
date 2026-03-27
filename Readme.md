# Laptop Price Prediction Pipeline

## 1. Project Overview
This repository contains an end-to-end machine learning pipeline for predicting laptop prices based on hardware specifications. The project demonstrates a standard engineering workflow for tabular data, encompassing data preprocessing, feature engineering, model training, persistence, and inference.

The objective is to establish a robust regression model that evaluates historical specification data to estimate pricing for unseen configurations. The codebase is modular and designed for reproducibility.

## 2. Methodology and System Architecture

### 2.1 Data Preprocessing and Feature Engineering
*   **Categorical Encoding:** Categorical variables are transformed using One-Hot Encoding to ensure compatibility with numerical algorithms.
*   **Feature State Preservation:** Column mappings are persisted during training to ensure feature space alignment during inference.

### 2.2 Model Selection
The pipeline utilizes a **Random Forest Regressor** as the primary estimator. This selection is justified by its capacity to model non-linear relationships, its robustness against overfitting in tabular datasets, and its ability to handle unscaled features.

### 2.3 Artifact Persistence
The trained pipeline components are serialized using the Python standard library `pickle` and stored in the `Models` directory:
*   `model.pkl`: The serialized regression model.
*   `columns.pkl`: The exact feature vector mapping required for inference.

## 3. Repository Structure

```text
Laptop-price-predictor/
├── Data/
│   └── laptops.csv           # Raw dataset
├── Models/
│   ├── model.pkl             # Serialized trained model
│   └── columns.pkl           # Serialized feature indices
├── .gitignore                # Version control exclusions
├── predict.py                # CLI script for model inference
├── requirements.txt           # Python environment specifications
├── README.md                 # System documentation
└── train_model.py            # Script for model training and serialization
```

## 4. Environment Setup and Installation

Follow these steps to deploy the project environment locally.

### Step 1: Clone the Repository
```bash
git clone https://github.com/Tanvirahmed-ML/laptop-price-predictor.git
cd laptop-price-predictor
```

### Step 2: Configure Virtual Environment
It is recommended to use Python virtual environments to prevent dependency conflicts.
```bash
# For Unix/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Required Packages
```bash
pip install -r requirements.txt
```

## 5. Usage Guidelines

The workflow is divided into discrete training and inference stages.

### 5.1 Model Training
To execute the data preprocessing and training pipeline, run:
```bash
python train_model.py
```
This script loads the raw dataset, fits the Random Forest estimator, and exports the serialized artifacts to the `/Models` directory.

### 5.2 Model Inference
To generate a prediction for a custom laptop configuration, run the CLI interface:
```bash
python predict.py
```
The script will prompt for inputs, align features with the training schema, and output the predicted market price.

## 6. Model Evaluation
Model performance is evaluated using standard continuous metrics:
*   Root Mean Squared Error (RMSE)
*   Mean Absolute Error (MAE)
*   Coefficient of Determination (R-squared score)

Quantitative metric tracking will be integrated into automated test modules in subsequent releases.

## 7. Known Limitations
*   **Feature Complexity:** The current release utilizes standard feature extraction. Advanced engineering (e.g., screen pixel-density metrics) is not yet implemented.
*   **Hyperparameter State:** The model runs on baseline parameters without Bayesian or grid optimization.

## 8. Future Roadmap
Proposed system improvements include:
*   **Automated Hyperparameter Tuning:** Grid search integration for performance optimization.
*   **Explainable AI (XAI):** Integration of SHAP or LIME for model interpretability.
*   **User Interface (UI):** Deployment via Streamlit for a web-based graphical interface.
*   **Cross-Validation:** Integration of K-Fold cross-validation for rigorous evaluation.

## 9. Authorship and Affiliations
**Tanvir Ahmed Nafis**
Computer Science and Engineering Undergraduate
East Delta University
Chattogram, Bangladesh

## 10. License and Usage
Users are encouraged to fork this repository for non-commercial research, academic, or portfolio development. Contributions and issue reporting can be conducted through standard GitHub pull request procedures.
