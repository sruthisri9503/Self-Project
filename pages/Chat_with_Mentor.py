import streamlit as st
from chat_agent import get_reply

st.title("💬 Chat with Mentor")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for m in st.session_state["messages"]:
    st.chat_message(m["role"]).write(m["content"])

msg = st.chat_input("Ask anything...")
if msg:
    st.session_state["messages"].append({"role": "user", "content": msg})
    st.chat_message("user").write(msg)

    reply = get_reply(msg)
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
