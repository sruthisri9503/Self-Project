import streamlit as st
from evaluation_agent import (
    extract_text_from_pdf,
    analyze_resume,
    analyze_marksheet,
    generate_pdf_report,
    extract_ats_score,
    getting_reply
)

st.title("📄 Resume / Marksheet Evaluation")

# Select PDF Type
pdf_type = st.radio(
    "Select PDF Type:",
    ["Resume", "Marksheet"]
)

# Select Target Role (only for Resume)
target_role = None
if pdf_type == "Resume":
    job_roles = [
        "Data Analyst", "Data Scientist", "Python Developer", "Software Engineer",
        "Machine Learning Engineer", "AI/ML Engineer", "Full Stack Developer",
        "Frontend Developer", "Backend Developer", "Cloud Engineer",
        "Cybersecurity Analyst", "DevOps Engineer", "Business Analyst", "UI/UX Designer",
    ]
    target_role = st.selectbox("Select your target job role:", job_roles)

# Upload PDF
uploaded_file = st.file_uploader("Upload your Resume/Marksheet (PDF only)", type=["pdf"])

if uploaded_file:

    # Extract text from PDF
    text = extract_text_from_pdf(uploaded_file)

    # Analyze based on type
    if pdf_type == "Resume":
        analysis = analyze_resume(text, target_role)
        st.success("Resume Analysis Completed!")
    else:
        analysis = analyze_marksheet(text)
        st.success("Marksheet Analysis Completed!")


    # ---------------------
    # Show ATS Score
    # ---------------------
    ats_score = extract_ats_score(analysis)

    if ats_score is not None:
        st.subheader("📊 ATS Score")
        st.progress(ats_score / 100)
        st.write(f"Your ATS Score: **{ats_score}/100**")

    # ---------------------
    # Download PDF Report
    # ---------------------
    pdf_file = generate_pdf_report(analysis, target_role)

    with open(pdf_file, "rb") as f:
        st.download_button(
            label="📄 Download Evaluation as PDF",
            data=f,
            file_name="Resume_Evaluation_Report.pdf",
            mime="application/pdf"
        )
    st.write(analysis)
    
    # ---------------------
    # Follow-up Chat
    # ---------------------
    q = st.chat_input("Ask anything about your evaluation...")

    if q:
        reply = getting_reply(q, analysis, target_role)
        st.chat_message("assistant").write(reply)
