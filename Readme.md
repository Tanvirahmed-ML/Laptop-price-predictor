Laptop Price Prediction Using Machine Learning
1. Project Overview

This project implements a machine learning pipeline to predict laptop prices based on their technical specifications. It demonstrates a full workflow from data preprocessing and feature engineering to model training and inference, providing a practical example of applied ML on tabular data.

The model learns patterns from historical laptop specifications and predicts prices for unseen configurations.

2. Objectives
Build a robust regression model for laptop price prediction.
Apply proper data preprocessing and feature encoding.
Demonstrate a reproducible and modular ML workflow.
Provide an extensible codebase suitable for research or portfolio projects.
3. Dataset

The dataset contains laptop specifications, including:

Brand / Manufacturer
Processor type
RAM size
Storage type and capacity
GPU
Screen size and resolution
Operating System

The dataset is stored at:
data/laptops.csv

4. Methodology
4.1 Data Preprocessing
Handle categorical variables with one-hot encoding.
Clean and structure tabular data for modeling.
Ensure feature alignment for training and inference using saved column mappings.
4.2 Feature Engineering
Convert categorical features into numerical representations.
Maintain a consistent feature space for predictions.
4.3 Model Selection

The project uses a Random Forest Regressor because:

It performs well on tabular datasets.
It models non-linear relationships effectively.
It is robust to overfitting with proper tuning.
4.4 Model Persistence
Model is saved using Pickle.
Feature columns are stored separately to ensure consistent predictions.
5. Project Structure
Laptop-price-predictor/
│
├── Data/
│   └── laptops.csv
├── Models/
│   ├── model.pkl
│   └── columns.pkl
├
├── train_model.py
├── predict.py
├── requirements.txt
├── README.md
└── .gitignore
6. Installation & Setup
Clone the repository:
git clone https://github.com/Tanvirahmed-ML/laptop-price-predictor.git
cd laptop-price-predictor
Install dependencies:
pip install -r requirements.txt
7. Model Training

Run the training script:

python train_model.py

This will:

Load and preprocess the dataset.
Train the Random Forest Regressor.
Save the trained model and feature columns to /models.
8. Prediction / Inference

Run the prediction script:

python predict.py
Accepts user input for laptop specifications.
Outputs the predicted price.
9. Model Evaluation

 To measure reliability, the model can be evaluated with standard regression metrics:

 Mean Absolute Error (MAE)
 Root Mean Squared Error (RMSE)
 R² Score

 Evaluation metrics can be implemented in future versions for a more rigorous assessment.

10. Reproducibility
  All dependencies are listed in requirements.txt.
  Model artifacts are stored in /models.
  Code is modular: training and inference stages are separated.
11. Limitations
  Model performance depends on dataset quality and size.
  Minimal feature engineering is applied in the current version.
  No hyperparameter tuning has been applied yet.
12. Future Work
  Hyperparameter optimization (Grid Search / Random Search).
  Advanced feature engineering for improved accuracy.
  Cross-validation for robust evaluation.
  Deployment via Streamlit web app.
  Model explainability using SHAP values or other techniques.
13. Author

Tanvir Ahmed Nafis
CSE Undergraduate
East Delta University
Chattogram,Bangladesh

14. Acknowledgment

  If you find this project useful:

  Star the repository.
  Provide feedback or suggestions.
  Fork to explore improvements.
15. Optional Enhancements 
  Add evaluation metrics (MAE, RMSE, R²) in the training notebook.
  Include an EDA notebook with insights and plots.
  Create a Streamlit demo for interactive predictions.
  Add screenshots or GIFs to showcase model predictions.

