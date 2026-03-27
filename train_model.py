import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("Data/laptops.csv").dropna()

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Convert categorical to numeric
df = pd.get_dummies(df)

# Split features and target
X = df.drop("price", axis=1)
y = df["price"]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
with open("Models/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save training columns
with open("Models/columns.pkl", "wb") as f:
    pickle.dump(list(X.columns), f)

print("Model and columns saved successfully!")