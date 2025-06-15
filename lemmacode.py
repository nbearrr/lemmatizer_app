import streamlit as st
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

def clean_and_lemmatize(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmas)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://stihi.ru/pics/2017/11/15/825.jpg");
background-size: cover;
background-position: center;
}

[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("*TEXT LEMMATIZER* :book:")

if 'show_input' not in st.session_state:
    st.session_state.show_input = False
if not st.session_state.show_input:
    st.write("Спасибо, что выбрали именно меня!")
    if st.button('Ввод текста'):
        st.session_state.show_input = True
else:
    text = st.text_area('Введи текст для лемматизации')
    if st.button('Лемматизировать'):
        result = clean_and_lemmatize(text)
        st.write('Результат лемматизации:')
        st.text_area('Лемматизированный текст', value=result, height=150, key='lemm_result', disabled=True)
