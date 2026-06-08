from utils.certificate_detector import detect_certificates
from utils.internship_detector import detect_internships
from utils.project_detector import detect_projects
from utils.career_selector import select_career
from utils.roadmap_helper import get_roadmap
from utils.interview_helper import get_questions
from utils.skill_advisor import explain_missing_skills
from utils.pdf_reader import extract_text
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats
from utils.career_logic import missing_skills
from utils.career_logic import detect_domain


with open("sample_resume.pdf", "rb") as f:
    text = extract_text(f)
print(len(text))
    

skills = extract_skills(text)

projects=detect_projects(text)

internships=detect_internships(text)

certificates=detect_certificates(text)

domain = detect_domain(skills)

if domain == "Engineering":
    career = "Software Engineer"

elif domain == "Medical":
    career = "Doctor"

else:
    career = "Accountant"

score = calculate_ats(
    skills,
    career,
    projects,
    internships,
    certificates
)

missing = missing_skills(skills, career)

advice = explain_missing_skills(missing)

questions = get_questions(career)

roadmap = get_roadmap(career)

career = select_career()

print("Detected Domain:")
print(domain)

print("Career:")
print(career)

print("\nSkills Found:")
print(skills)

print("\nATS Score:")
print(score)

print("\nMissing Skills:")
print(missing)

print("\nSkill Advice:")

for skill, reason in advice.items():
    print(f"\n{skill}:")
    print(reason)

print("\nInterview Questions:")

for question in questions:
    print("-", question)

print("\nLearning Roadmap:")

for step in roadmap:
    print("-", step)

print("\nProjects Found:")

for project in projects:
    print("-", project)

print("\nInternships Found:")

for internship in internships:
    print("-", internship)

print("\nCertificates Found:")

for certificate in certificates:
    print("-", certificate)