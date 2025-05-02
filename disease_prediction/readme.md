
---

# 🧠 Disease Prediction using Machine Learning

A web-based application built with **Streamlit** that predicts the likelihood of three major health conditions — **Heart Disease**, **Diabetes**, and **Parkinson’s Disease** — using multiple machine learning models. This project leverages the predictive power of **SVM**, **Logistic Regression**, and **Random Forest** classifiers to deliver fast and accurate results. All models are pre-trained and stored separately for easy loading and scalability.

---

## 📁 Project Structure

```
├── app3.py                       # Streamlit app main file
├── saved_model/                 # Directory containing pre-trained model .pkl files
│   ├── logistic_regression.pkl
│   ├── logistic_regression.pkl
│   ├── Parkinson_disease.pkl
│   ├── random_forest.pkl
│   ├── random_forest1.pkl
│   ├── svm.pkl
│   ├── svm1.pkl
```

---

## 🧪 Models Used

### 🔹 Heart Disease Prediction
- Support Vector Machine (SVM)
- Logistic Regression
- Random Forest

### 🔹 Diabetes Prediction
- Support Vector Machine (SVM)
- Logistic Regression
- Random Forest

### 🔹 Parkinson’s Disease Prediction
- Random Forest

---

## 🚀 Features

- 🖥️ Interactive and user-friendly Streamlit interface
- 🧠 Multiple models for increased prediction reliability
- 📊 Clean output with immediate diagnosis suggestions
- 💾 Pre-trained models for rapid inference
- 🔄 Easy to extend for future diseases or models

---

## ⚙️ Installation & Running the App

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/disease-prediction-ml.git
   cd disease-prediction-ml
   ```

2. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app3.py
   ```

---

## 📦 Requirements

- Python 3.7+
- streamlit
- pandas
- numpy
- scikit-learn
- joblib

All dependencies are listed in the `requirements.txt` file.

---

## 💡 Use Case & Impact

Early detection is key to treating chronic diseases. This project is designed to provide a quick, accessible prediction platform that helps individuals and medical professionals get instant results and take preventive measures in a timely manner.

---

## 👩‍💻 Author

**Dwiti Thaker**  
B.Tech – Information Technology  
5th Semester | 10 SGPA  
GitHub: [DwitiThaker](https://github.com/DwitiThaker)  
LinkedIn: [Dwiti Thaker](https://www.linkedin.com/in/dwiti-thaker-a36358236/)

---

## 📌 Future Improvements

- Add more diseases (e.g., liver, kidney)
- Deploy using Streamlit Cloud / Render / Hugging Face Spaces
- Include a login and user history feature
- Add visualization of health metrics and risk scores

---

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
