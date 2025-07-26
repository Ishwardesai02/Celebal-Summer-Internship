# app.py
import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Load model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.set_page_config(page_title="California Housing Price Prediction", layout="centered")
st.title("🏡 California House Price Prediction")
st.write("Adjust sliders to predict the **median house price** in $100,000s.")

# User input
med_inc = st.slider("Median Income (10k$)", 0.5, 15.0, 3.0, step=0.1)
avg_rooms = st.slider("Average Rooms per Household", 1.0, 15.0, 5.0, step=0.1)
house_age = st.slider("House Age (years)", 1, 50, 20)

# Prepare data
input_data = np.array([[med_inc, avg_rooms, house_age]])
input_scaled = scaler.transform(input_data)
prediction = model.predict(input_scaled)[0]

# Display result
st.success(f"Predicted Median House Price: ${prediction * 100000:,.2f}")

# Visualization
st.subheader("📈 Income vs Price Trend")
sample_incomes = np.linspace(0.5, 15, 100)
preds = model.predict(scaler.transform(np.column_stack((sample_incomes, [avg_rooms]*100, [house_age]*100))))

fig, ax = plt.subplots()
ax.plot(sample_incomes, preds * 100000, label="Predicted Price", color="blue")
ax.scatter(med_inc, prediction * 100000, color="red", label="Your Input")
ax.set_xlabel("Median Income (10k$)")
ax.set_ylabel("Predicted Price ($)")
ax.legend()
st.pyplot(fig)
