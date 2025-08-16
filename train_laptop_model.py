# train_laptop_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# -----------------------------
# 1️⃣ Load dataset
# -----------------------------
data_path = r"C:\My project\laptop_data\laptop_data.csv"
df = pd.read_csv(data_path)

# -----------------------------
# 2️⃣ Rename columns to match Streamlit app
# -----------------------------
df = df.rename(columns={
    "Brand": "Company",
    "Type": "TypeName",
    "GPU_Brand": "Gpu_com",
    "Operating_System": "OpSys_ew",
    "RAM": "Ram1",
    "Weight": "Weight1",
    "PPI": "PPi",
    "CPU_GHZ": "GHz",
    "Flash_Storage": "FlStorage",
    "Full_HD": "Full HD"
})

# -----------------------------
# 3️⃣ Define features and target
# -----------------------------
x = df.drop("Price", axis=1)
y = df["Price"]

# Match columns as per Streamlit input
cat_features = ["Company", "TypeName", "Gpu_com", "OpSys_ew", "CPU", "IPS", "Touchscreen", "Full HD"]
num_features = ["Ram1", "Weight1", "PPi", "GHz", "SSD", "HDD", "FlStorage"]

# -----------------------------
# 4️⃣ Preprocessing pipeline
# -----------------------------
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features),
    ("num", StandardScaler(), num_features)
])
# -----------------------------
# 5️⃣ Model pipeline
# -----------------------------
pipe = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(n_estimators=100, random_state=42))
])

# -----------------------------
# 6️⃣ Train model
# -----------------------------
pipe.fit(x, y)
print("✅ Model trained successfully!")

# -----------------------------
# 7️⃣ Save trained model
# -----------------------------
save_path = r"C:\My project\laptop_data\laptop_prediict.pkl"
joblib.dump(pipe, save_path)
print(f"💾 Model saved at: {save_path}")                                                                              
