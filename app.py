import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import joblib
import warnings

# Load the saved model
finalized_xgboost_model = joblib.load('finalized_xgboost_model .pkl')

# Define feature names
categorical_columns = ['Product', 'Market Location', 'County']
numerical_columns = ['Supply Volume', 'usd_rate', 'Year', 'Month', 'Day']

# List of counties in Kenya
counties = [
    "Baringo", "Bomet", "Bungoma", "Busia", "Elgeyo Marakwet", "Embu", 
    "Garissa", "Homa Bay", "Isiolo", "Kajiado", "Kakamega", "Kericho", 
    "Kiambu", "Kilifi", "Kirinyaga", "Kisii", "Kisumu", "Kitui", 
    "Kwale", "Laikipia", "Lamu", "Machakos", "Makueni", "Mandera", 
    "Marsabit", "Meru", "Migori", "Mombasa", "Murang'a", "Nairobi", 
    "Nakuru", "Nandi", "Narok", "Nyamira", "Nyandarua", "Nyeri", 
    "Samburu", "Siaya", "Taita Taveta", "Tana River", "Tharaka Nithi", 
    "Trans Nzoia", "Turkana", "Uasin Gishu", "Vihiga", "Wajir", "West Pokot"
]

markets = [
    'Akala', 'Aram', 'Bondo', 'Nakuru Wakulima', 'Eldoret Main', 'Kibuye', 'Kongowea',
    'Malindi Old Market', 'Kitale Municipality Market', 'Daraja Mbili', 'Ngurubani Market',
    'Cheptulu', 'Chuka', 'Diani Market', 'Rongo', 'Busia Market', 'Soko Mpya',
    'Garissa Soko Mugdi', 'Kagio', 'Embu Town'
]

def predict_wholesale_price(user_input):
    """Performs prediction using the XGBoost model."""
    # Convert user input to DataFrame
    df = pd.DataFrame([user_input])

    # One-hot encode categorical features
    encoder = OneHotEncoder()
    encoded_categories = encoder.fit_transform(df[categorical_columns]).toarray()
    feature_labels = encoder.get_feature_names_out(categorical_columns)
    encoded_df = pd.DataFrame(encoded_categories, columns=feature_labels)

    # Combine with numerical features
    df_encoded = pd.concat([encoded_df, df[numerical_columns]], axis=1)

    # Ensure all expected features are present (the model's training features)
    expected_features = np.array(finalized_xgboost_model.get_booster().feature_names)
    missing_cols = set(expected_features) - set(df_encoded.columns)
    for col in missing_cols:
        df_encoded[col] = 0  # Assuming zero-filling for missing features

    df_encoded = df_encoded[expected_features]

    # Make prediction
    prediction = finalized_xgboost_model.predict(df_encoded)
    return prediction[0]

# Streamlit app layout
st.title("Wholesale Price Prediction")

user_input = {}
for col in categorical_columns:
    if col == 'County':
        options = counties  # Use the list of counties for the 'County' selection
    elif col == 'Product':
        options = ['Bean', 'Dry Maize', 'Onion','Rice']  # Add all relevant options for 'Product'
    elif col == 'Market Location':
        options = markets  # Example market locations
    user_input[col] = st.selectbox(f" {col}", ['..'] + options)

for col in numerical_columns:
    user_input[col] = st.number_input(col)

if st.button("Predict Wholesale Price"):
    try:
        predicted_price = predict_wholesale_price(user_input)
        st.success(f"Predicted Wholesale Price: ksh{predicted_price:.2f} per KG")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.write("**Note:** This application provides an estimate of wholesale prices based on input data.")