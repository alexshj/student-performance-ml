# 🎓 Student Performance Predictor

## 🚀 Live Demo
[Click here to try the app](https://student-performance-ml-alxshaju.streamlit.app/)

---

## 📊 Project Overview
This project predicts student performance using Machine Learning based on study habits such as study hours, attendance, and class participation.

---

## ⚙️ Features
- Predict student scores using:
  - Weekly study hours
  - Attendance percentage
  - Class participation
- Real-time prediction through an interactive web app
- Fast predictions using a pre-trained model

---

## 🤖 Model Details
- Algorithm: Random Forest Regressor
- R² Score: ~0.72
- Model optimized for fast inference using joblib (pre-trained model loading)

---

## 💡 Key Insight
Weekly self-study hours have the strongest impact on student performance.

---

## 🛠 Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

---

## 📂 Project Structure

student-performance-ml/
│── app/
│ └── app.py
│── data/
│ └── student_performance.csv
│── model.pkl
│── requirements.txt
│── README.md


---

## ▶️ How to Run Locally


pip install -r requirements.txt
python -m streamlit run app/app.py
📌 Future Improvements
Add more features (sleep, study environment, etc.)
Improve model accuracy
Enhance UI/UX of the web app


👨‍💻 Author

Alex Shaju

B.Tech Artificial Intelligence & Data Science
