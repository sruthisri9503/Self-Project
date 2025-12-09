import streamlit as st

st.set_page_config(page_title="AI Career Mentor", layout="centered")

st.markdown("""
    <style>
        .big-title {
            font-size: 48px !important;   /* Increase size */
            font-weight: 800 !important;
            text-align: center;
            padding-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="big-title">🤖 AI Career Mentor</h1>', unsafe_allow_html=True)

# ---------- PAGE TITLE ----------
st.markdown(
    """
    <p style='text-align:center; font-size:18px; color:#555;'>
        Choose a feature to get started
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------- CUSTOM CSS FOR CARDS ----------
st.markdown("""
    <style>
        .feature-btn {
            border: 1px solid #e6e6e6;
            padding: 20px;
            border-radius: 14px;
            text-align: center;
            background-color: #ffffff;
            width: 100%;
            font-size: 18px;
            cursor: pointer;
        }
        .feature-btn:hover {
            border-color: #4b8bff;
            background: #f3f7ff;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- FEATURE CARDS ----------
col1, col2 = st.columns(2)

with col1:
    if st.button("💬 Chat With Mentor", use_container_width=True):
        st.switch_page("pages/Chat_with_Mentor.py")

    if st.button("🎯 Career Roadmap", use_container_width=True):
        st.switch_page("pages/Career_Roadmap.py")

with col2:
    if st.button("📄 Resume / Marksheet Evaluation", use_container_width=True):
        st.switch_page("pages/Resume_Evaluation.py")

    if st.button("🏫 College Finder", use_container_width=True):
        st.switch_page("pages/College_Finder.py")

st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background: rgba(255,255,255,0.8);
            color: #555;
            font-size: 16px;
        }
    </style>

    <div class="footer">© 2025 AI Career Mentor</div>
""", unsafe_allow_html=True)
