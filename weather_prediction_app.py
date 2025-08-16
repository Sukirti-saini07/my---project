# weather_prediction_app.py

# 1️⃣ Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st

# 2️⃣ Load Dataset
# Kaggle ya sample weather dataset (columns: Temperature, Humidity, Wind Speed, Weather Type)
df = pd.read_csv(r"C:\My project\weather_classification_data.csv")  

# 3️⃣ Preprocessing
X = df[['Temperature', 'Humidity', 'Wind Speed']]  # Features
y = df['Weather Type']  # Target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5️⃣ Evaluate (optional)
y_pred = model.predict(X_test)
st.write("Model Accuracy:", round(accuracy_score(y_test, y_pred)*100, 2), "%")

# 6️⃣ Streamlit UI
st.title("🌤️ Next Day Weather Type Prediction")

temp = st.number_input("Temperature (°C)", min_value=-30, max_value=50, value=25)
humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=60)
wind = st.number_input("Wind Speed (km/h)", min_value=0, max_value=150, value=10)

if st.button("Predict Weather"):
    input_data = pd.DataFrame([[temp, humidity, wind]], columns=['Temperature','Humidity','Wind Speed'])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Weather Type: {prediction}")