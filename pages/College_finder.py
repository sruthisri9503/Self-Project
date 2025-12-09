import streamlit as st
from college_agent import find_colleges

st.title("🏫 College Finder")

loc = st.text_input("Enter city / state / college name")

if st.button("Search"):
    if not loc:
        st.warning("Enter a location!")
    else:
        with st.spinner("Searching..."):
            results = find_colleges(loc)

        st.success("Done!")
        st.write(results)
