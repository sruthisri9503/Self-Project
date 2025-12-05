import streamlit as st
from chat_agent import get_reply
from roadmap_agent import getting_reply
from college_agent import find_colleges
import os




#lets start with the UI
# we have imported the streamlit so lets set the title

st.set_page_config(page_title='AI Career Mentor',layout='centered')
st.title('AI Career Mentor')


if "feature" not in st.session_state:
    st.session_state["feature"] = "Dashboard"
# ---------------------------
# Sidebar (Project Info + Developer Info)
# ---------------------------
with st.sidebar:

    # Project Title
    st.markdown("## 🤖 AI Career Mentor")
    st.write(
        "Your personal AI-powered assistant that helps with resume analysis, "
        "career roadmap generation, college search, and interactive chat guidance."
    )

    st.markdown("---")

    # Project Features
    st.markdown("### 📌 Features")
    st.write("""
    - 📄 Resume / Marksheet Evaluation  
    - 🎯 Personalized Career Roadmaps  
    - 💬 AI Mentor Chat  
    - 🏫 College Finder  
    - 📊 ATS Score Analysis  
    """)

    st.markdown("---")

    # Developer Info
    st.markdown("## 👩‍💻 Developer")
    st.markdown("### **Sruthi Sri Chayapathi**")
    
    
    st.markdown("### 📬 Contact")
    st.write("sruthisrichayapathi@gmail.com")
    

    st.markdown("### 🔗 Social Links")
    st.write("[LinkedIn](https://www.linkedin.com/in/sruthichayapathi09)")
    st.write("[GitHub](https://github.com/)")

    st.markdown("---")

# create a side bar
options = ["Dashboard", "Chat with Mentor", "Resume/Marksheet Evaluation", "Career Roadmap", "College Finder"]

# Notice: NO session_state assignment here
feature = st.sidebar.selectbox(
    "Choose a feature",
    options,
    index=options.index(st.session_state["feature"])
)



if feature == "Dashboard":
    st.subheader("Welcome to AI Career Mentor 👋")
st.write("Choose a section to get started:")

# ===== Card 1 =====
st.markdown("### 📄 Resume/Marksheet Evaluation")
st.write("Analyze your resume or marksheet and get skill insights.")
if st.button("Open Resume Evaluation"):
    st.session_state["feature"] = "Resume/Marksheet Evaluation"
    st.rerun()

st.markdown("---")

# ===== Card 2 =====
st.markdown("### 🎯 Career Roadmap")
st.write("Generate a 3-year personalized roadmap for your target role.")
if st.button("Open Career Roadmap"):
    st.session_state["feature"] = "Career Roadmap"
    st.rerun()

st.markdown("---")

# ===== Card 3 =====
st.markdown("### 💬 Chat with Mentor")
st.write("Ask any career, interview, or skill-related questions.")
if st.button("Chat with Mentor"):
    st.session_state["feature"] = "Chat with Mentor"
    st.rerun()

st.markdown("---")

# ===== Card 4 =====
st.markdown("### 🏫 College Finder")
st.write("Find the best colleges in any city or state.")
if st.button("Open College Finder"):
    st.session_state["feature"] = "College Finder"
    st.rerun()



if feature == "Chat with Mentor":
    # show chat UI  
    # we want to save the chat so
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

# Show chat history
    for message in st.session_state["messages"]:
        st.chat_message(message["role"]).write(message["content"])

# Chat input
    user_input = st.chat_input("Hi, how can I help you?")

    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        reply = get_reply(user_input)
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)

elif feature == "Resume/Marksheet Evaluation":
    st.subheader("Upload your Resume or Marksheet (PDF)")

    pdf_type = st.radio(
        "Select PDF Type:",
        ["Resume", "Marksheet"]
    )

    target_role = None
    if pdf_type =="Resume":
        job_roles=[
            "Data Analyst",
            "Data Scientist",
            "Python Developer",
            "Software Engineer",
            "Machine Learning Engineer",
            "AI/ML Engineer",
            "Full Stack Developer",
            "Frontend Developer",
            "Backend Developer",
            "Cloud Engineer",
            "Cybersecurity Analyst",
            "DevOps Engineer",
            "Business Analyst",
            "UI/UX Designer",
        ]
        target_role = st.selectbox("Select your Job role:", job_roles)

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file:

        # Import inside this block
        from evaluation_agent import (
            extract_text_from_pdf,
            analyze_resume,
            analyze_marksheet,
            getting_reply,
            generate_pdf_report      # ⭐ ADDED HERE
        )

        text = extract_text_from_pdf(uploaded_file)

        if pdf_type == "Resume":
            analysis = analyze_resume(text, target_role)
            st.success("Resume Analysis Complete!")
        else:
            analysis = analyze_marksheet(text)
            st.success("Marksheet Analysis Complete!")

        st.write(analysis)

        from evaluation_agent import extract_ats_score

        ats_score = extract_ats_score(analysis)

        if ats_score is not None:
            st.subheader("ATS Score")
            st.progress(ats_score / 100)
            st.write(f"Your ATS Score: **{ats_score}/100**")

        # ⭐ PDF download option — INSIDE uploaded_file block
        pdf_file = generate_pdf_report(analysis, target_role)

        with open(pdf_file, "rb") as f:
            st.download_button(
                label="📄 Download Resume Evaluation as PDF",
                data=f,
                file_name="Resume_Evaluation_Report.pdf",
                mime="application/pdf"
            )

        # ⭐ Chat AFTER PDF
        chat_user = st.chat_input("Any questions about your evaluation?")

        if chat_user:
            st.session_state.setdefault("messages", [])
            st.session_state["messages"].append({"role": "user", "content": chat_user})
            st.chat_message("user").write(chat_user)

            reply = getting_reply(chat_user, analysis, target_role)

            st.session_state["messages"].append({"role": "assistant", "content": reply})
            st.chat_message("assistant").write(reply)


elif feature == "Career Roadmap":
    st.subheader("Get Your Personalized Career Roadmap")

    # Input box for career
    career_input = st.text_input("Enter your dream career (e.g., Data Scientist)")

    # Button to generate roadmap
    if st.button("Generate Roadmap"):
        if career_input:
            from roadmap_agent import generate_roadmap

            roadmap = generate_roadmap(career_input)

            # Store roadmap in session_state (IMPORTANT)
            st.session_state["roadmap"] = roadmap

        else:
            st.warning("Please enter a career!")

    # ---------------------------------------------
    # SHOW GENERATED ROADMAP (if exists)
    # ---------------------------------------------
    if "roadmap" in st.session_state:
        st.write(st.session_state["roadmap"])

        # Follow-up chat
        follow_up_q = st.chat_input("Ask anything about your roadmap")

        if follow_up_q:
            from roadmap_agent import getting_reply

            reply = getting_reply(follow_up_q, st.session_state["roadmap"])
            st.chat_message("assistant").write(reply)



elif feature == "College Finder":

    st.subheader("🏫 Search Colleges")

    location = st.text_input("Enter College name or City or State")

    if st.button("Search Colleges"):
        if not location:
            st.warning("Please enter a location.")
        else:
            from college_agent import find_colleges

            with st.spinner("Searching colleges..."):
                results = find_colleges(location)

            st.success("Search Complete!")

            # If model returns text → show as text
            if isinstance(results, str):
                st.write(results)

            # If model returns list/dict → try showing nicely
            else:
                st.write("### Results:")
                st.json(results)



