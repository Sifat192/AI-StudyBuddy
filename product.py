import streamlit as st
from google import genai
client = genai.Client(api_key='')
st.title('AI - STUDY BUDDY')
st.markdown('Welcome to your AI powered study sessions')
st.sidebar.title('Study Buddy Menu')
st.sidebar.subheader('Select Study Mode')
mode = st.sidebar.selectbox('Enter the mode',['Explain concept','Summarise in Essay','Exam Minutes'])
st.subheader('Enter the topic you want to study')
topic = st.text_input('Enter your input here')
if st.button("Generate"):

    if mode == "Explain concept":
        prompt = f"Explain {topic} in simple language for a college student."

    elif mode == "Summarise in Essay":
        prompt = f"Write a concise essay on {topic} in about 300 words."

    elif mode == "Exam Minutes":
        prompt = f"Create exam-ready notes on {topic} with key points and bullet points."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    st.subheader("Generated Output")
    st.markdown(response.text)





