import streamlit as st
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Streamlit UI
st.title("🌸 Iris Flower Prediction App")
st.write("Enter flower measurements and get prediction")

# User inputs
sepal_length = st.number_input("Sepal length (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input("Sepal width (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Petal length (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input("Petal width (cm)", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Predict"):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.success(f"Predicted flower: {iris.target_names[prediction[0]]}")