import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #f8fafc,
        #dbeafe
    );
}

/* Title */
h1 {
    color: #1E88E5;
    text-align: center;
}

/* Subheaders */
h2, h3 {
    color: #1565C0;
}

/* Buttons */
.stButton > button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #1E3A8A,
        #2563EB
    );
}
         section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# Navigation Sidebar
st.sidebar.title("📌 Navigation")
st.sidebar.info("AI Resume Analyzer Dashboard")
page = st.sidebar.selectbox(
    "📌 Navigation",
    [
        "🏠 Home",
        "📤 Upload Resume",
        "📊 Results",
        "ℹ️ About"
    ]
)

# Home Page
if page == "🏠 Home":

    st.markdown("""
    <div style="
        padding:30px;
        border-radius:20px;
        background:linear-gradient(90deg,#4F46E5,#06B6D4);
        color:white;
        text-align:center;
        margin-bottom:20px;
    ">
        <h1>🚀 AI Resume Analyzer</h1>
        <h4>Transform Your Resume Into Career Opportunities</h4>
        <p>
        Upload your resume and receive ATS insights,
        skills analysis, project recommendations,
        and career guidance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Statistics
    st.markdown("### 📊 Platform Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Resumes Analyzed", "100+")

    with col2:
        st.metric("🎯 Accuracy", "95%")

    with col3:
        st.metric("👨‍💻 Users", "50+")

    st.markdown("---")

    # Features
    st.markdown("### ✨ Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("📈 ATS Score Analysis")

    with col2:
        st.success("💻 Skills Detection")

    with col3:
        st.success("🎯 Career Guidance")

    st.markdown("---")

    # Resume Tips
    st.subheader("💡 Resume Tips")

    st.write("""
    ✅ Keep your resume to 1–2 pages

    ✅ Highlight technical skills

    ✅ Include projects and internships

    ✅ Use action verbs

    ✅ Use clean and professional formatting
    """)

    st.markdown("---")
    st.caption("AI Resume Analyzer | Developed by Team")

# Upload Resume Page
elif page == "📤 Upload Resume":

    st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:20px;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
text-align:center;
">
<h1>📤 Upload Resume</h1>
<p>Upload your resume and receive instant career insights.</p>
</div>
""", unsafe_allow_html=True)

    st.info("Upload your resume in PDF format for analysis.")

    st.info("""
📋 Upload Guidelines

• PDF format only

• Maximum size 200 MB

• Use a professional resume format
""")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    col1, col2 = st.columns(2)

    with col1:
        domain = st.selectbox(
            "Select Domain",
            ["Engineering", "Medical", "Commerce"]
        )

    with col2:

        if domain == "Engineering":
            career_options = [
                "Software Engineer",
                "Web Developer",
                "Data Analyst",
                "AI Engineer"
            ]

        elif domain == "Medical":
            career_options = [
                "Doctor",
                "Surgeon",
                "Dentist",
                "Nurse"
            ]

        else:
            career_options = [
                "Accountant",
                "Financial Analyst",
                "Auditor",
                "Bank Manager"
            ]

        career = st.selectbox(
            "Select Career",
            career_options
        )

    if uploaded_file:
        st.success("Resume Uploaded Successfully ✅")

    if st.button("🚀 Analyze Resume", use_container_width=True):
        st.success("Analysis Started Successfully")

# Results Page
elif page == "📊 Results":

    st.title("📊 Resume Analysis Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📈 ATS Score", "84%")

    with col2:
        st.metric("💻 Skills Found", "4")

    with col3:
        st.metric("📁 Projects", "2")

    st.subheader("ATS Performance")
    st.progress(84)
    st.success("""
📋 Resume Summary

Strong technical profile with good projects and skills.
""")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["💻 Skills", "📁 Projects", "🏆 Certificates", "🏢 Internships"]
    )

    with tab1:
        st.write("✅ Python")
        st.write("✅ Java")
        st.write("✅ SQL")
        st.write("✅ Machine Learning")

    with tab2:
        st.write("AI Resume Analyzer")
        st.write("E-Commerce Website")

    with tab3:
        st.write("AWS Cloud Practitioner")
        st.write("Python Programming Certificate")

    with tab4:
        st.write("Software Development Intern")

    st.warning("""
    Missing Skills Detected:

    • DSA

    • DBMS
    """)

    st.markdown("---")
    st.caption("AI Resume Analyzer | Developed by Team")
    # About Page
elif page == "ℹ️ About":

    st.title("ℹ️ About Project")

    st.write("""
    This project is an AI Resume Analyzer.

    It helps users upload resumes and view analysis results.

    Features:
    • Resume Upload
    • ATS Score Display
    • Skills Analysis
    • Missing Skills Detection
    • Career Suggestions
    """)
   
    st.subheader("🛠 Technologies Used")


    st.subheader("👨‍💻 Team")

    col1, col2 = st.columns(2)

    with col1:
        st.info("👩‍💻 Pragna\n\nWebsite UI Developer")

    with col2:
        st.info("🤖 Backend Team\n\nAI & Resume Analysis")

    st.subheader("👨‍💻 Team Members")

    st.write("""
    • Pragna - Website UI

    • Team Member 2 - Resume Processing

    • Team Member 3 - AI Analysis

    • Team Member 4 - Testing & Documentation
    """)

    st.markdown("---")

    st.caption("AI Resume Analyzer | Developed by Team")