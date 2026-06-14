import streamlit as st
from utils.pdf_reader import extract_text
from utils.skill_extractor import extract_skills
from utils.missing_skills import get_missing_skills
from ai.final_report import generate_final_report
from data.career_data import career_db
from utils.ats_score import calculate_ats
from utils.project_detector_v2 import detect_projects
from utils.internship_detector_v2 import detect_internships
from utils.certificate_detector_v2 import detect_certificates
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

/* Normal Text */
.stMarkdown,
.stText,
p,
span,
label,
li {
    color: #111111 !important;
}

/* Streamlit text visibility */
[data-testid="stMarkdownContainer"] {
    color: #111111 !important;
}

[data-testid="stMetricValue"] {
    color: #111111 !important;
}

[data-testid="stMetricLabel"] {
    color: #111111 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #1E3A8A,
        #2563EB
    );
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Domain & Career dropdowns */
.stSelectbox div[data-baseweb="select"] {
    background-color: white !important;
    color: black !important;
}

/* Dropdown selected text */
.stSelectbox * {
    color: black !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background-color: white !important;
    color: black !important;
    border-radius: 10px;
}

/* Browse Files button */
[data-testid="stFileUploader"] button {
    background-color: #2563EB !important;
    color: white !important;
    border: none !important;
}

/* Analyze Resume button */
.stButton > button {
    background-color: #4CAF50 !important;
    color: white !important;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
}

/* JSON/List outputs */
[data-testid="stJson"] {
    background-color: white !important;
}

[data-testid="stJson"] * {
    color: black !important;
}

/* Success / Info / Warning boxes */
[data-testid="stAlert"] {
    color: black !important;
}
/* JSON output text */
[data-testid="stJson"] {
    background-color: #1E1E1E !important;
}

[data-testid="stJson"] * {
    color: #FFD700 !important;   /* Yellow text */
}
/* Data/List output */
pre {
    color: #FFD700 !important;
}

code {
    color: #FFD700 !important;
}

/* Titles */
h1 {
    color: #1E88E5;
    text-align: center;
}

/* Headings */
h2, h3, h4, h5, h6 {
    color: #1565C0;
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
color:black;
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

        if uploaded_file is not None:

            text = extract_text(uploaded_file)

            skills = extract_skills(text)
            
            lines = text.split("\n")
            
            projects = detect_projects(lines)

            internships = detect_internships(lines)

            certificates = detect_certificates(lines)

            required_skills = career_db.get(
                career,
                {}
            ).get(
                "skills",
                []
            )

            missing_skills = get_missing_skills(
            skills,
            required_skills
            )

            ats_score = calculate_ats(
                skills,
                career,
                projects,
                internships,
                certificates
                
            )

            st.success("Analysis Completed ✅")
            st.subheader("ATS Score")
            st.metric("ATS Score", f"{ats_score}%")

            st.subheader("Extracted Skills")
            st.json(skills)

            st.subheader("Missing Skills")
            st.json(missing_skills)

            st.subheader("Projects")
            st.json(projects)

            st.subheader("Internships")
            st.json(internships)

            st.subheader("Certificates")
            st.json(certificates)
            report = generate_final_report(
                 skills,
                 missing_skills,
                 ats_score,
                 career
)

            st.subheader("AI Report")

            st.subheader("Feedback:")
            st.write(report["feedback"])
            st.subheader("Readiness:")
            st.write(report["readiness"])

            st.subheader("Strengths:")
            st.json(report["strengths"])

            st.subheader("Weaknesses:")
            st.json(report["weaknesses"])

            st.subheader("Recommendations:")
            st.json(report["recommendations"])

        else:
            st.error("Please upload a resume first.")

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

    • Parthiban S - AI & ATS Analysis Developer

    • Pooja:- Resume processing and data extraction

    • Prathviraj - Testing & Documentation
    """)

    st.markdown("---")

    st.caption("AI Resume Analyzer | Developed by Team")