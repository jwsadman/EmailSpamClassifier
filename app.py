import streamlit as st
import pickle
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)

  y = []
  for i in text:
    if i.isalnum():
      y.append(i)
  text = y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)
  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)

st.title("Email Spam Classifier")
input_mail = st.text_area('Enter the Email')

if st.button('Predict'):
  transformed_mail = transform_text(input_mail)

  vector_input = tfidf.transform([transformed_mail])

  result = model.predict(vector_input)[0]

  if result == 1:
    st.header('Spam')
  else:
    st.header('Not Spam')







