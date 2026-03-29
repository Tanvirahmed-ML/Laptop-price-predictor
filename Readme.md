## Laptop Price Predictor

Ever wondered how much a laptop should actually cost?

This project uses machine learning to predict laptop prices based on specifications such as RAM, processor, storage, GPU, screen size, and other features. It supports both single laptop predictions and multiple laptop predictions in one go.

# Overview

Laptop pricing is often confusing—similar specs can have very different prices. This project provides:

A machine learning model that predicts laptop prices
Support for single or multiple laptop predictions
A Streamlit web application for easy interaction

It covers the complete workflow: data preprocessing, feature engineering, model training, and deployment in a simple web app.

# Dataset

The dataset contains laptop specifications:

Brand
Processor
RAM
Storage (SSD/HDD)
GPU
Operating System
Screen Size
Warranty

Location: Data/laptops.csv

# Data Preparation

Steps taken:

Handled missing and inconsistent values
Cleaned and standardized data
Converted categorical features into formats suitable for modeling
# Feature Engineering

To improve performance, some transformations were applied:

Extracted CPU brand from processor names
Separated storage into SSD and HDD
Simplified GPU categories

These steps helped the model learn meaningful patterns.

# Model Building

Models tested:

Linear Regression
Random Forest Regressor

Random Forest Regressor was chosen for its better performance and ability to capture non-linear relationships.

# Results
Achieves an R² score around 0.8 (may vary with data split)
Key observations:
More RAM generally increases price
SSD storage adds more value than HDD
Processor type significantly affects price
Brand also impacts cost
# Web Application

Built with Streamlit, the app allows users to:

Enter laptop specifications
Get instant price predictions
Make single or multiple laptop predictions

Model and column files location:

Models/model.pkl
Models/columns.pkl

 The app uses your token if required, so no extra authentication steps are needed.

# Demo & Usage

The web app supports single laptop predictions and multiple laptop predictions via CSV upload.

1 Single Laptop Prediction
Open the app.
Fill in the specifications for one laptop:
Brand
Processor
RAM
Storage (SSD/HDD)
GPU
Operating System
Screen Size
Warranty
Click Predict.
The predicted price will appear instantly.

Screenshot Example:




2️ Multiple Laptop Prediction
Prepare a CSV file with the same columns as the model expects (see CSV tips below).
Upload the CSV in the Multiple Laptop Prediction section.
Click Predict.
The app will output predicted prices for all laptops in the file.

Screenshot Example:




# Tips for CSV Formatting (Multiple Predictions)

To make sure the multiple laptop prediction works smoothly:

Column Names Must Match Exactly

Required columns (case-sensitive):

brand, processor, ram, ram_type, rom, rom_type, gpu, os, screen_size, warranty
Order of columns can vary, but names must match exactly.
No Missing Values
Fill all cells; empty cells can cause prediction errors.
Example: If a laptop has no dedicated GPU, you can use Integrated.
Consistent Data Types
RAM and ROM should be numeric (e.g., 8, 512)
Screen size should be numeric in inches (e.g., 15.6)
Strings for categorical features (brand, processor, GPU, OS, warranty)
Save as CSV
Ensure the file is .csv
UTF-8 encoding is recommended
Example CSV Row
brand	processor	ram	ram_type	rom	rom_type	gpu	os	screen_size	warranty
Dell	Intel i5	8	DDR4	512	SSD	Integrated	Windows	15.6	1 Year
HP	AMD Ryzen 7	16	DDR4	1024	SSD	Nvidia GTX 1650	Windows	16	2 Years

# Following these tips ensures your CSV uploads work perfectly with the app’s multiple prediction feature.

# How to Run the Project
Clone the repository
git clone https://github.com/Tanvirahmed-ML/Laptop-price-predictor.git
cd Laptop-price-predictor
Install dependencies
pip install -r requirements.txt
Run the application
python -m streamlit run app.py
# Project Structure
Laptop-price-predictor/
│
├── Data/
│   └── laptops.csv
│
├── Models/
│   ├── model.pkl
│   └── columns.pkl
│
├── notebooks/
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
└── README.md
# Future Improvements
Test advanced models (e.g., XGBoost)
Hyperparameter tuning for better accuracy
Visualize feature importance
Deploy the app online
Extend into a laptop recommendation system
# About

I am a CSE student learning machine learning and building practical projects. This project demonstrates how features influence laptop pricing and provides a working prediction tool.

# Conclusion

This project goes beyond price prediction. It shows the complete machine learning workflow, helps understand feature impact on laptop pricing, and makes it accessible through a single or multiple prediction web app.
