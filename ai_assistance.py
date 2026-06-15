# basically this is for web app for local host server
import ollama
import streamlit as st #temp variable for streamlit

st.title("Your Personal Gym assistant") #set up the web page title

question=st.text_input("Ask  question regarding gym...") #create a text box taking input from user

def gym_trainer(question):
    response= ollama.chat(
          model='tinyllama',
          messages=[
               {
                    'role':'system',
                    'content':"""you area gym trainer.
                    rules:
                    - Be polite and friendly
                    - keep answers short and to the point
                    - give exersise plan for weight loss
                    """
               },
               {
             'role':'user',
             'content':question
          }
          ]
     )
    return response['message']['content']

if st.button("send"): #button to start AI agent
    if question:
        with st.spinner("Thinking..."):
            answer=gym_trainer(question)
            st.write(answer)
    else:
        st.warning("Please type a question first...!")        


