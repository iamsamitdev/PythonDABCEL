# import libraries
import streamlit as st
from joblib import load
import numpy as np

# load the model from disk
model = load('iris_model.joblib')

# Create Streamlit Web App
st.title('Iris Flower Prediction App')

# Create input fields for user to enter data
sepal_length = st.slider("Sepal Length", 4.3, 7.9, 5.4)
sepal_width = st.slider("Sepal Width", 2.0, 4.4, 3.4)
petal_length = st.slider("Petal Length", 1.0, 6.9, 1.3)
petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2)

features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Create a button to predict the species
if st.button('Predict'):
    prediction = model.predict(features)
    st.write(f"Predicted Species: {prediction[0]}")
