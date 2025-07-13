# 🎓 Student Performance Analysis with Machine Learning

This project aims to analyze and predict student performance based on various socio-economic and academic factors. Using a linear regression model, we predict a student's average score from their test scores and background data.

---

## 📌 Objective

To build a machine learning model that helps in understanding the impact of different factors (like gender, parental education, lunch type, etc.) on student performance and predict the average score.

---

## 📁 Dataset

The dataset used in this project is [StudentsPerformance.csv](dataset/StudentsPerformance.csv), which contains:
- **Gender**
- **Race/Ethnicity**
- **Parental Level of Education**
- **Lunch Type**
- **Test Preparation Course**
- **Math Score**
- **Reading Score**
- **Writing Score**

---

## 🧠 Machine Learning Model

We use **Linear Regression** from `scikit-learn` to:
- Train on the average of `math`, `reading`, and `writing` scores
- Save the model using `joblib`
- Use the model in a web interface for predictions

---

## 📊 Technologies Used

- Python
- Pandas, NumPy
- Seaborn, Matplotlib
- scikit-learn
- Flask (for deployment)
- Jupyter Notebook (for analysis)

---

## 📓 Notebooks

The `notebook/analysis.ipynb` contains complete EDA, data visualization, and model training.

---

## 🌐 Web App

The `app.py` file runs a Flask app that:
- Takes student info as input
- Predicts their average score
- Displays the result on a web page

> Run with:  
> ```bash
> python app.py
> ```

---


---

## 🧑‍💻 Author

**Mirza Naveed Baig**  
Final Year BCA Student | Aspiring Data Scientist  
[GitHub](https://github.com/Naveed05)

