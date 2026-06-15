# basically it is the local web server of medical assistance bot
import ollama
import streamlit as st
st.title("MEDICAL ASSISTANCE BOT")
question=st.text_input("Ask your question related to medical field")
def medicalassistance_bot(question):
    response= ollama.chat(
        model='tinyllama',
        messages=[
            {
                'role':'system',
                'content':"""you are a medical assistance bot:
                rules:
                -greate the user with a precise beautiful context
                -be polite and friendly
                -give a accurate analysis of the disease or report but precise
                -check the blood pressure and pulse rate if asked
                -suggest the general medication by seeing the symptoms of patient
                -suggest the test and do and don't"""
            },
            {
                'role':'user',
                'content':question
            }
        ]
    )
    return response['message']['content']
if st.button("send"):
    if question:
        with st.spinner("THINKING AND ANALYZING"):
            answer=medicalassistance_bot(question)
            st.write(answer)
else:
    st.warning("PLEASE TYPE A QUESTION FIRST")
