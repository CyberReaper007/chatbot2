import streamlit as st
import ollama


st.title("chatbot")
prompt = st.chat_input("ask ur query")

if prompt:

    st.chat_message("user")

    st.write(prompt)

    with st.spinner("thinking"):
        result = ollama.chat(model="codellama",messages=[{
            "role":"user",
            "content":prompt
        }])
        response = result["message"]["content"]
        st.write(response)