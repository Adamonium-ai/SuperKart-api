# Import necessary libraries
import numpy as np
import joblib  # For loading the serialized model
import pandas as pd  # For data manipulation
from flask import Flask, request, jsonify  # For creating the Flask API
from flask_cors import CORS

# Initialize Flask app with a name
superkart_api = Flask("Prediction_Model")
CORS(superkart_api)

# Load the trained model
model = joblib.load("xgb_final.joblib")

# Define a route for the home page
@superkart_api.get('/')
def home():
    return "SuperKart Model API is running."

# Define an endpoint to predict sales
@superkart_api.post('/v1/predict')
def predict_sales():
    data = request.get_json()

    # Match exactly what model.feature_names_in_ expects
    sample = {
        'Product_Id': data['Product_Id'],
        'Product_Weight': data['Product_Weight'],
        'Product_Sugar_Content': data['Product_Sugar_Content'],
        'Product_Allocated_Area': data['Product_Allocated_Area'],
        'Product_Type': data['Product_Type'],
        'Product_MRP': data['Product_MRP'],
        'Store_Id': data['Store_Id'],
        'Store_Establishment_Year': data['Store_Establishment_Year'],
        'Store_Size': data['Store_Size'],
        'Store_Location_City_Type': data['Store_Location_City_Type'],
        'Store_Type': data['Store_Type']
    }

    input_data = pd.DataFrame([sample])
    prediction = model.predict(input_data).tolist()[0]

    return jsonify({'Sales': prediction})
