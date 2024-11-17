# FILE: test.py

from openai import AzureOpenAI
from dotenv import load_dotenv
import streamlit as st
from streamlit_option_menu import option_menu

load_dotenv()

def client_openai(messages):
    client = AzureOpenAI()
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    return_response = chat_completion.choices[0].message.content
    return return_response

if __name__ == "__main__":

    st.title("Chat.IA")

    menu = option_menu(None, 
        ["Chat Geral", "Pergunte aos seus dados"], 
        icons=["chat", "data"], 
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal")

    if menu == "Chat Geral":

        # Initialize chat history with system message
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "system", "content": "Você está conversando com um assistente que mantém o contexto das conversas anteriores."}
            ]

        # Display chat messages from history on app rerun, excluding system messages
        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        # React to user input
        if prompt := st.chat_input("Escreva sua mensagem"):
            
            # Display user message in chat message container
            st.chat_message("user").markdown(prompt)

            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Obter resposta do assistente com contexto
            llm_response = client_openai(st.session_state.messages)
            with st.chat_message("assistant"):
                st.markdown(llm_response)

            # Adicionar resposta do assistente ao histórico
            st.session_state.messages.append({"role": "assistant", "content": llm_response})
