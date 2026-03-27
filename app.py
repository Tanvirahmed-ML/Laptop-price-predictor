import streamlit as st
import pickle
import pandas as pd
import os

# -------------------------------
# Load model and columns
# -------------------------------
MODEL_PATH = os.path.join("Models", "model.pkl")
COLUMNS_PATH = os.path.join("Models", "columns.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(COLUMNS_PATH, "rb") as f:
    model_columns = pickle.load(f)

# -------------------------------
# Title
# -------------------------------
st.title("💻 Laptop Price Predictor (Multiple)")

st.write("Upload or enter multiple laptops for prediction")

# -------------------------------
# Option: Upload CSV
# -------------------------------
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

def preprocess(df):
    df_encoded = pd.get_dummies(df)
    df_encoded = df_encoded.reindex(columns=model_columns, fill_value=0)
    return df_encoded

# -------------------------------
# If CSV uploaded
# -------------------------------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("📄 Uploaded Data:")
    st.dataframe(df)

    processed = preprocess(df)
    predictions = model.predict(processed)

    df["Predicted Price"] = predictions

    st.write("✅ Predictions:")
    st.dataframe(df)

# -------------------------------
# Manual Entry (Multiple)
# -------------------------------
else:
    st.subheader("Enter Laptop Details")

    num = st.number_input("How many laptops?", min_value=1, max_value=20, step=1)

    data_list = []

    for i in range(num):
        st.write(f"### Laptop {i+1}")

        brand = st.selectbox(f"Brand {i}", ["Dell","HP","Lenovo","Asus","Acer","Apple"], key=f"brand{i}")
        processor = st.selectbox(f"Processor {i}", ["i3","i5","i7","Ryzen 5","Ryzen 7"], key=f"proc{i}")
        ram = st.selectbox(f"RAM {i}", [4,8,16,32], key=f"ram{i}")
        ram_type = st.selectbox(f"RAM Type {i}", ["DDR3","DDR4","DDR5"], key=f"ramtype{i}")
        rom = st.selectbox(f"Storage {i}", [128,256,512,1024], key=f"rom{i}")
        rom_type = st.selectbox(f"Storage Type {i}", ["HDD","SSD"], key=f"romtype{i}")
        gpu = st.selectbox(f"GPU {i}", ["Intel","NVIDIA","AMD"], key=f"gpu{i}")
        os_sys = st.selectbox(f"OS {i}", ["Windows","Mac","Linux"], key=f"os{i}")
        warranty = st.selectbox(f"Warranty {i}", [1,2,3], key=f"war{i}")
        screen_size = st.number_input(f"Screen Size {i} (inches)", 10.0, 20.0, key=f"screen{i}")

        data_list.append({
            "brand": brand,
            "processor": processor,
            "ram": ram,
            "ram_type": ram_type,
            "rom": rom,
            "rom_type": rom_type,
            "gpu": gpu,
            "os": os_sys,
            "warranty": warranty,
            "screen_size": screen_size
        })

    # -------------------------------
    # Predict Button
    # -------------------------------
    if st.button("Predict Prices"):
        df = pd.DataFrame(data_list)

        processed = preprocess(df)
        predictions = model.predict(processed)

        df["Predicted Price"] = predictions

        st.write("✅ Results:")
        st.dataframe(df)