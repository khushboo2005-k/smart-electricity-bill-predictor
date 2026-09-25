import streamlit as st
import numpy as np
import pickle

# Agar model aur scaler files saved hain toh load karein
try:
    model = pickle.load(open('electricity_model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except:
    st.error("Pehle model aur scaler files generate karein!")

st.set_page_config(page_title="Electricity Bill Predictor", page_icon="⚡", layout="centered")

st.title("⚡ Smart Home Electricity Bill Predictor")
st.write("Apne ghar ki details neche darj karein aur apna expected monthly electricity bill maloom karein!")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    house_area = st.number_input("House Area (Square Feet)", min_value=300, max_value=6000, value=2000)
    rooms = st.number_input("Number of Rooms", min_value=1, max_value=12, value=4)
    ac_count = st.number_input("Number of ACs", min_value=0, max_value=8, value=2)

with col2:
    avg_temp = st.slider("Average Outside Temp (°C)", min_value=20.0, max_value=50.0, value=35.0)
    family_size = st.number_input("Family Members", min_value=1, max_value=15, value=4)

st.markdown("---")

if st.button("Predict Bill", type="primary"):
    input_data = np.array([[house_area, rooms, ac_count, avg_temp, family_size]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    
    st.success(f"💡 Estimated Monthly Electricity Bill: **Rs. {prediction[0]:,.2f}**")
    
    if ac_count > 2 or avg_temp > 40:
        st.warning("Tip: High temperature aur multiple ACs ki wajah se bill zyada aa raha hai!")
