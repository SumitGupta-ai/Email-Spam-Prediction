# 📧 Email Spam Detection using Machine Learning

A Machine Learning web application that classifies emails as **Spam** or **Ham (Not Spam)** using **TF-IDF Vectorization** and **Logistic Regression**. The application is built with **Python**, **Scikit-learn**, and **Streamlit**.

---

## 🚀 Live Demo

🌐 **Streamlit App:**  
https://email-spam-prediction-pbt5ukd3qrbgs5g4dx2hda.streamlit.app/

---

## 📌 Features

- Detects whether an email is **Spam** or **Ham**
- Text preprocessing
- TF-IDF Vectorization
- Logistic Regression Classifier
- Real-time prediction using Streamlit
- Prediction confidence (Spam/Ham Probability)
- Responsive and user-friendly interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Joblib

---

## 📂 Project Structure

```
Email-Spam-Prediction/
│
├── app.py
├── Email_Spam_Prediction.pkl
├── tfidf_vectorizer.pkl
├── spam.csv
├── requirements.txt
├── README.md
├── .gitignore
└── email_spam_pred.ipynb
```

---

## 📊 Dataset

- SMS Spam Collection Dataset
- Total Samples: **5572**
- After removing duplicates: **5157**

Target Labels:

- **0 → Ham**
- **1 → Spam**

---

## 🧹 Text Preprocessing

- Convert text to lowercase
- Remove punctuation
- Remove stopwords
- Tokenization using NLTK

---

## 🤖 Machine Learning Pipeline

```
Raw Email
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorizer
      │
      ▼
Logistic Regression Model
      │
      ▼
Spam / Ham Prediction
```

---

## 📈 Model Performance

| Metric | Score |
|---------|-------|
| Training Accuracy | **99.03%** |
| Testing Accuracy | **97.09%** |

Classification Report

| Class | Precision | Recall | F1-score |
|---------|-----------|--------|----------|
| Ham | 0.98 | 0.98 | 0.98 |
| Spam | 0.89 | 0.88 | 0.88 |

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SumitGupta-ai/Email-Spam-Prediction.git
```

Move into the project directory

```bash
cd Email-Spam-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 💡 Example

**Input**

```
Congratulations!

You have won a FREE iPhone.

Click the link below to claim your prize.
```

**Prediction**

```
🚨 Spam
```

---

## 📸 Application Screenshot

> Add a screenshot of your Streamlit app here.

Example:

```
screenshots/app.png
```

---

## 📌 Future Improvements

- Support for real email datasets
- Deep Learning Models (LSTM/BERT)
- Email attachment analysis
- Phishing detection
- Email URL analysis

---

## 👨‍💻 Author

**Sumit Gupta**

GitHub:
https://github.com/SumitGupta-ai

LinkedIn:
(Add your LinkedIn Profile)

---

## ⭐ Support

If you like this project, don't forget to ⭐ the repository.
