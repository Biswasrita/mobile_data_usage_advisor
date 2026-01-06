#  Smart Mobile Data Usage Advisor

🔗 **Live Application**  
https://mobiledatausageadvisor-eoufcvjtpktabmhfn4nltn.streamlit.app/

---

##  Overview

Smart Mobile Data Usage Advisor is a **machine learning–based web application** that predicts the risk of mobile data exhaustion based on daily usage patterns.  
The app helps users understand whether their mobile data usage is **Safe**, **Warning**, or **High Risk**, enabling better data management.

The project is built using **Python, Scikit-learn, and Streamlit**, and is deployed on **Streamlit Cloud**.

---

##  Problem Statement

Many mobile users face sudden data exhaustion because:
- They do not monitor daily data usage
- They spend excessive time on high data-consuming apps
- Existing tools show usage but do not provide predictive insights

This project addresses the problem by **predicting data usage risk in advance**.

---

##  Solution

The application:
- Takes daily mobile usage inputs
- Uses a trained ML model to analyze patterns
- Predicts the **data usage risk level**
- Provides clear and actionable feedback to users

---

##  Machine Learning Details

- **ML Algorithm:** Random Forest Classifier
- **Problem Type:** Classification
- **Features Used:**
  - Screen-on time (hours/day)
  - App usage time (minutes/day)
  - Mobile data usage (MB/day)
- **Target Output:**
  - Safe
  - Warning
  - High Risk

---

##  Tech Stack

- **Language:** Python
- **Machine Learning:** Scikit-learn
- **Frontend:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Model Saving:** Joblib
- **Deployment:** Streamlit Cloud
- **Version Control:** Git & GitHub

---



