import streamlit as st
import joblib

# Page config
st.set_page_config(page_title="Student Performance Predictor")

st.title("🎓 Student Performance Predictor")
st.write("Predict student scores using Machine Learning.")

# Load trained model (FAST)
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# Inputs
st.subheader("Enter Student Details")

study_hours = st.slider("Study Hours (per week)", 0.0, 40.0, 10.0)
attendance = st.slider("Attendance (%)", 0.0, 100.0, 75.0)
participation = st.slider("Class Participation", 0.0, 10.0, 5.0)

# Prediction
if st.button("Predict Score"):
    prediction = model.predict([[study_hours, attendance, participation]])[0]
    st.success(f"Predicted Score: {prediction:.2f}")

st.info("💡 Insight: Weekly self-study hours have the strongest impact on performance.")