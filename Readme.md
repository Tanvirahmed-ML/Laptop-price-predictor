## Laptop Price Predictor

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.30-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Model:** Random Forest Regressor  
**Performance:** R² ≈ 0.82  
**Description:** Predicts laptop prices based on key specifications like RAM, CPU, storage, GPU, screen size, and brand. Supports single and batch predictions via a Streamlit app.  

Ever wondered if a laptop is priced fairly? This project predicts realistic laptop prices using machine learning. You can predict **a single laptop** or **multiple laptops at once** using a CSV file.  

---

# What This Project Does

Laptop prices can be confusing—even laptops with similar specs can cost very differently. This project helps you:

- Predict laptop prices using a **trained ML model**  
- Make **single or batch predictions** with an easy-to-use web app  
- Explore the **full machine learning workflow**, from data cleaning to deployment  

---

# The Dataset

The model uses a dataset with common laptop features:

| Feature       | Type        | What it Means |
|---------------|------------|---------------|
| brand         | Categorical | Laptop brand |
| processor     | Categorical | CPU model/type |
| ram           | Numeric     | RAM in GB |
| ram_type      | Categorical | RAM type (DDR4/DDR5) |
| rom           | Numeric     | Storage size |
| rom_type      | Categorical | SSD or HDD |
| gpu           | Categorical | GPU model/type |
| os            | Categorical | Operating system |
| screen_size   | Numeric     | Screen size in inches |
| warranty      | Categorical | Warranty period |
| price         | Numeric     | Target variable (USD) |

**Dataset location:** `Data/laptops.csv`  

---

# Cleaning & Preparing Data

Before training the model, we:

- Handled missing or inconsistent values  
- Standardized categories and labels  
- Converted data into formats suitable for modeling  

---

# Feature Engineering

To help the model perform better, we:

- Extracted **CPU brand** from processor names  
- Split storage into **SSD and HDD**  
- Simplified **GPU categories**  

This helps the model capture patterns that affect laptop pricing.

---
# Model Building

Model Tested: Random Forest Regressor (best performance)
Performance Metrics:

Metric	Score
R²	~0.82
MAE	120 USD
RMSE	150 USD

📊 Model Evaluation

Predicted vs Actual Price:
Visualizes how closely predicted prices match actual prices. Closer points to the diagonal line indicate higher accuracy.

Top 10 Feature Importances:
Highlights which features influence price predictions the most.

# How the Model Works

We tested a few models:

- Linear Regression  
- Random Forest Regressor ✅ *(the winner!)*  

**Why Random Forest?**  
It handles non-linear relationships well and gave better predictions overall.

**Performance metrics:**

| Metric | Score |
|--------|-------|
| R²     | ~0.82 |
| MAE    | 120 USD |
| RMSE   | 150 USD |

**Key takeaways:**

- More RAM usually increases price  
- SSDs add more value than HDDs  
- CPU type has a big impact  
- Brand also matters  

---

# Using the Web App

The app is built with **Streamlit**, making it easy to interact with the model.

**You can:**

- Enter laptop specs manually for **single predictions**  
- Upload a CSV for **multiple laptop predictions**  

**Model files location:**  
Models/model.pkl
Models/columns.pkl


---

## Demo

# Single Laptop Prediction

1. Open the app  
2. Fill in the specs: brand, processor, RAM, storage, GPU, OS, screen size, warranty  
3. Click **Predict**  
4. The price appears instantly!  

**Example screenshot:**  
![Single Prediction](screenshots/single_predict_result.png)

---

# Multiple Laptop Prediction

1. Prepare a CSV with all required columns  
2. Upload it in the **Multiple Prediction** section  
3. Click **Predict**  
4. See prices for all laptops in your file  

**Example screenshot:**  
![Multiple Prediction](screenshots/multiple_predict_result.png)



# CSV Tips for Multiple Predictions

- Column names must match exactly (case-sensitive):  
  `brand, processor, ram, ram_type, rom, rom_type, gpu, os, screen_size, warranty`  
- No missing values  
- RAM, ROM, and screen size should be numeric  
- Others should be strings  
- Save as **UTF-8 CSV**
**Example CSV row:**

| brand | processor    | ram | ram_type | rom | rom_type | gpu            | os      | screen_size | warranty |
|-------|-------------|-----|----------|-----|----------|----------------|---------|------------|---------|
| Dell  | Intel i5    | 8   | DDR4     | 512 | SSD      | Integrated     | Windows | 15.6       | 1 Year  |
| HP    | AMD Ryzen 7 | 16  | DDR4     | 1024| SSD      | Nvidia GTX 1650| Windows | 16         | 2 Years |

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

#Project Structure

Laptop-price-predictor/
│
├── Data/
│   └── laptops.csv
├── Models/
│   ├── model.pkl
│   └── columns.pkl
├── ├── screenshots/
│   ├── single_input_page.png
│   ├── single_predict_result.png
│   ├── multiple_input_page.png
│   └── multiple_prediction_result.png
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
└── README.md
#Future Improvements
-Try advanced models like XGBoost or LightGBM
-Hyperparameter tuning for better predictions
-Visualize feature importance
-Deploy the app online
-Extend to a laptop recommendation system

# About Me

I’m a CSE student passionate about machine learning.
This project shows how laptop features affect pricing and provides a working, user-friendly tool to predict laptop prices.

#Conclusion

This project goes beyond just predicting prices. It:
-Demonstrates a full ML workflow
-Helps understand feature impact on pricing
-Provides a usable web application for single or multiple predictions
