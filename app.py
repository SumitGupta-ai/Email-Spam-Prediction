import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# For newer NLTK versions
try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    try:
        nltk.download("punkt_tab")
    except:
        pass

model = joblib.load("Email_Spam_Prediction.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


def transform_text(text):

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenize
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))

    clean_words = []

    for word in words:
        if word not in stop_words:
            clean_words.append(word)

    return " ".join(clean_words)


st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Email Spam Detection")
st.write("Enter an email and check whether it is Spam or Ham.")

email = st.text_area("Email Message", height=200)

if st.button("Predict"):

    if email.strip() == "":
        st.warning("Please enter an email.")
    else:
        # Preprocess
        processed_email = transform_text(email)

        # Vectorize
        email_vector = vectorizer.transform([processed_email])

        # Predict
        prediction = model.predict(email_vector)

        if prediction[0] == 1:
            st.error("🚨 Spam Email")
        else:
            st.success("✅ Ham (Not Spam)")

        # Show probability (if supported)
        try:
            prob = model.predict_proba(email_vector)[0]

            st.write(f"Ham Probability: **{prob[0]*100:.2f}%**")
            st.write(f"Spam Probability: **{prob[1]*100:.2f}%**")
        except:
            pass