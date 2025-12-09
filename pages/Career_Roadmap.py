import streamlit as st
from roadmap_agent import generate_roadmap, getting_reply

st.title("🎯 Career Roadmap")

career = st.text_input("Enter your dream career")

if st.button("Generate Roadmap"):
    if career:
        st.session_state["roadmap"] = generate_roadmap(career)
    else:
        st.warning("Please enter a career!")

if "roadmap" in st.session_state:
    st.write(st.session_state["roadmap"])

    q = st.chat_input("Ask anything about your roadmap")
    if q:
        st.chat_message("assistant").write(getting_reply(q, st.session_state["roadmap"]))
