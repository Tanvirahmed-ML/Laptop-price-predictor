import pandas as pd
import pickle
import os

# ----------------------------
# Load model and training columns
# ----------------------------
with open(os.path.join("Models", "model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join("Models", "columns.pkl"), "rb") as f:
    training_columns = pickle.load(f)

print("Model loaded successfully!")

# ----------------------------
# Choose prediction type
# ----------------------------
choice = input("Enter 1 for single prediction or 2 for multiple (CSV): ")

# ----------------------------
# SINGLE INPUT
# ----------------------------
if choice == "1":

    # Numeric inputs
    ram = int(input("ram (GB): "))
    rom = int(input("rom (GB): "))
    display_size = float(input("display_size (inches): "))

    # Categorical inputs (NO df usage → no error)
    brand = input("brand: ")
    name = input("name: ")
    processor = input("processor: ")
    cpu = input("cpu: ")
    ram_type = input("ram_type: ")
    rom_type = input("rom_type: ")
    gpu = input("gpu: ")
    resolution = input("resolution: ")
    os_name = input("os: ")
    warranty = input("warranty: ")

    # Create dataframe
    input_df = pd.DataFrame([{
        "brand": brand,
        "name": name,
        "processor": processor,
        "cpu": cpu,
        "ram": ram,
        "rom": rom,
        "ram_type": ram_type,
        "rom_type": rom_type,
        "gpu": gpu,
        "display_size": display_size,
        "os": os_name,
        "warranty": warranty
    }])

# ----------------------------
# MULTIPLE INPUT (CSV)
# ----------------------------
elif choice == "2":
    file_path = input("Enter CSV file path: ")
    input_df = pd.read_csv(file_path)
    input_df.columns = input_df.columns.str.strip().str.lower()

else:
    print("Invalid choice")
    exit()

# ----------------------------
# PROCESS INPUT (IMPORTANT)
# ----------------------------
input_encoded = pd.get_dummies(input_df)

# Add missing columns
for col in training_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0

# Remove extra columns
input_encoded = input_encoded[training_columns]

# ----------------------------
# PREDICT
# ----------------------------
predictions = model.predict(input_encoded)

print("\nPredicted Prices:")
for i, price in enumerate(predictions, 1):
    print(f"Laptop {i}: {price:.2f}")