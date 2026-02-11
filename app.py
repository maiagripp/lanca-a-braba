import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage


api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    st.error("❌ Configure DEEPSEEK_API_KEY em Streamlit Secrets")
    st.stop()

os.environ["OPENAI_API_KEY"] = api_key

st.title("🤖 ChatBot Lança Braba 🔥💪")

@st.cache_resource
def get_llm():
    return ChatOpenAI(
        base_url="https://api.deepseek.com/v1",
        model="deepseek-chat",
        temperature=0.8
    )

llm = get_llm()

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content="""
        Você é o 'Lança Braba', coach carioca explosivo! Fala com gíria RJ, 
        motiva DEMAIS sobre fitness/código/viagens, usa metáforas de samba/praia. 
        SEMPRE termina com 'Lança a braba! 🔥💪' Seja ENERGÉTICO!
    """)]

for message in st.session_state.messages[1:]:  
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    else:
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Input do usuário
if prompt := st.chat_input("Fala aííí"):
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Lançando a braba..."):
            response = llm.invoke(st.session_state.messages)
            st.markdown(response.content)
    
    st.session_state.messages.append(response)
