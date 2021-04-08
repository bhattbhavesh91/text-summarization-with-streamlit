import streamlit as st
from transformers import pipeline

@st.cache(allow_output_mutation=True)
def load_summarizer():
    model = pipeline("summarization")
    return model

summarizer = load_summarizer()
st.title("Summarize Text")
sentence = st.text_area('Please paste your article :', height=30)
button = st.button("Summarize")

max = st.sidebar.slider('Select max', 50, 500, step=10, value=150)
min = st.sidebar.slider('Select min', 10, 450, step=10, value=50)
do_sample = st.sidebar.checkbox("Do sample", value=False)
with st.spinner("Generating Summary.."):
    if button and sentence:
        result = summarizer(sentence, max_length=max, min_length=min, do_sample=do_sample)
        st.write(result[0]['summary_text'])