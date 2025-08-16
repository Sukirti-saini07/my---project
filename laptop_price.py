    # laptop_price_app.py

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained pipeline
model = joblib.load("C:/My project/laptop_data/laptop_prediict.pkl")  # Window path: use / or \\


st.title("💻 Laptop Price Predictor")
st.subheader("Enter Laptop Specifications:")

# User inputs
company = st.selectbox("Company", ["Dell", "HP", "Apple", "Lenovo", "Asus", "Acer", "MSI", "Toshiba", 
                                   "Samsung", "Razer", "Mediacom", "Microsoft", "Xiaomi",
                                   "Google", "Fujisu", "LG", "Huawei", "Other"])
type_name = st.selectbox("Type", ["Ultrabook", "Gaming", "Notebook", "2 in 1 Convertible", "Workstation", "Other"])
gpu_brand = st.selectbox("GPU Brand", ["Intel", "NVIDIA", "AMD", "Other"])
os = st.selectbox("Operating System", ["Windows", "Macos", "No Os / Linux", "Other"])
cpu = st.selectbox("CPU Brand", ["Intel", "AMD", "Other"])

ram = st.number_input("RAM (GB)", min_value=2, max_value=64, step=2)
weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)
ppi = st.slider("PPI (Pixel Per Inch)", min_value=90, max_value=300)
ghz = st.number_input("CPU GHz", min_value=0.5, max_value=5.0, step=0.1)

ssd = st.selectbox("SSD (GB)", [0, 128, 256, 512, 1024, 2048, 4096])
hdd = st.selectbox("HDD (GB)", [0, 500, 750, 1000, 2000, 4000])
flash_storage = st.selectbox("Flash Storage (GB)", [0, 32, 64, 128, 256, 512])

ips = st.selectbox("IPS Display", ['No', 'Yes'])
ips_int = 1 if ips == 'Yes' else 0

touchscreen = st.selectbox("Touchscreen", ['No', 'Yes'])
touchscreen_int = 1 if touchscreen == 'Yes' else 0

full_hd = st.selectbox("Full HD Display", ['No', 'Yes'])
full_hd_int = 1 if full_hd == 'Yes' else 0

gb = st.number_input("Storage GB", min_value=0, max_value=8000, step=10)
tb = st.selectbox("TB", [0, 1, 2, 4, 8])

# Prediction
if st.button("Predict price"):
    # Construct DataFrame: use processed variables
    input_df = pd.DataFrame([{
        "Company": company,
        "TypeName": type_name,
        "Ram1": int(ram),
        "Weight1": float(weight),
        "PPi": int(ppi),
        "IPS": ips_int,
        "Touchscreen": touchscreen_int,
        "Full HD": full_hd_int,
        "GHz": float(ghz),
        "SSD": int(ssd),
        "HDD": int(hdd),
        "FlStorage": int(flash_storage),
        "GB": int(gb),
        "TB": int(tb),
        "Gpu_com": gpu_brand,
        "OpSys_ew": os,
        "CPU": cpu
    }])
 # Predict
prediction = model.predict(input_df)[0]
st.success(f"💰 Estimated Laptop Price: ₹{prediction:,.2f}")