import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import joblib

# Load the saved model
finalized_xgboost_model = joblib.load('finalized_xgboost_models.pkl')

# Define feature names for prediction
categorical_columns = ['Product', 'Market Location', 'County']
# Excluding 'Supply Volume' from prediction model input
numerical_columns = ['usd_rate']

# List of counties in Kenya and market options
counties = ["Busia", "Embu", "Kitale", "Garissa", "Nairobi", "Kajiado", "Kiambu", "Kilifi", "Kirinyaga", "Kisii", "Kisumu", "Migori", "Mombasa", "Nairobi", "Nakuru", "Nandi", "Narok", "Nyandarua", "Siaya", "TharakaNithi", "Vihiga"]
markets = ['Akala', 'Aram', 'Bondo', 'Nakuru Wakulima', "Gikomba", 'Eldoret Main', 'Kibuye', 'Kongowea', 'Malindi Old Market', 'Kitale Municipality Market', 'Daraja Mbili', 'Ngurubani Market', 'Cheptulu', 'Chuka', 'Diani Market', 'Rongo', 'Busia Market', 'Soko Mpya', 'Garissa Soko Mugdi', 'Kagio', 'Embu Town']

def predict_wholesale_price(user_input):
    """Performs prediction using the XGBoost model."""
    df = pd.DataFrame([user_input])
    
    # Encode categorical features
    encoder = OneHotEncoder()
    encoder.fit(df[categorical_columns])  # Fitting the encoder dynamically, not recommended for production
    encoded_categories = encoder.transform(df[categorical_columns]).toarray()
    feature_labels = encoder.get_feature_names_out()
    encoded_df = pd.DataFrame(encoded_categories, columns=feature_labels)
    
    # Include numerical features (excluding Supply Volume) and date-related features
    for col in numerical_columns + ['Year', 'Month', 'Day']:
        encoded_df[col] = df[col]
    
    # Fill missing model features with zeros
    missing_cols = set(finalized_xgboost_model.get_booster().feature_names) - set(encoded_df.columns)
    for col in missing_cols:
        encoded_df[col] = 0

    encoded_df = encoded_df[finalized_xgboost_model.get_booster().feature_names]
    prediction = finalized_xgboost_model.predict(encoded_df)
    return prediction[0]

# Streamlit app layout
st.title("Wholesale Price Prediction")
selected_date = st.date_input("Date", value=pd.to_datetime('today'))
user_input = {
    'Year': selected_date.year,
    'Month': selected_date.month,
    'Day': selected_date.day
}

# Collecting user input for categorical and numerical features
for col in categorical_columns:
    options = counties if col == 'County' else (['Bean', 'Dry Maize', 'Onion', 'Rice'] if col == 'Product' else markets)
    user_input[col] = st.selectbox(f"{col}", ['...'] + options)

# Collecting usd_rate as it's used in the model
user_input['usd_rate'] = st.number_input('Enter USD Rate')

# Collecting Supply Volume for logging or reporting, but not for prediction
supply_volume = st.number_input('Enter Supply Volume', value=0.0, format="%.2f")

if st.button("Predict Wholesale Price"):
    try:
        predicted_price = predict_wholesale_price(user_input)
        st.success(f"Predicted Wholesale Price: Ksh {predicted_price:.2f} per KG")
        st.write(f"Supply Volume collected for records: {supply_volume} units")  # Optionally display supply volume
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.write("**Note:** This application provides an estimate of wholesale prices based on input data.")
