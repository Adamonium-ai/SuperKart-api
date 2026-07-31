import streamlit as st
import requests

st.title("SuperKart Sales Prediction")

Product_Id = st.text_input("Product Id", value="FD6114")
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.0, max_value=1.0, value=0.05, step=0.001, format="%.3f")
Product_Type = st.selectbox("Product Type", ["Baking Goods", "Breads", "Breakfast", "Canned", "Dairy", "Frozen Foods", "Fruits and Vegetables", "Hard Drinks", "Health and Hygiene", "Household", "Meat", "Others", "Seafood", "Snack Foods", "Soft Drinks", "Starchy Foods"])
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=141.0)
Store_Id = st.selectbox("Store Id", ["OUT001", "OUT002", "OUT003", "OUT004"])
Store_Establishment_Year = st.number_input("Store Establishment Year", min_value=1980, max_value=2026, value=1999, step=1)
Store_Size = st.selectbox("Store Size", ["Small", "Medium", "High"])
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
Store_Type = st.selectbox("Store Type", ["Supermarket Type1", "Supermarket Type2", "Departmental Store", "Food Mart"])

product_data = {
    "Product_Id": Product_Id,
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_Type": Product_Type,
    "Product_MRP": Product_MRP,
    "Store_Id": Store_Id,
    "Store_Establishment_Year": Store_Establishment_Year,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type
}

if st.button("Predict", type="primary"):
    try:
        response = requests.post("https://fantastic-computing-machine-96776qg6rpg53xp9p-5000.app.github.dev/v1/predict", json=product_data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            predicted_sales = result["Sales"]
            st.write(f"Predicted Product Store Sales Total: ₹{predicted_sales:.2f}")
        else:
            st.error(f"Error in API request: status {response.status_code}")
            st.write(response.text)
    except Exception as e:
        st.error(f"Request failed: {e}")
