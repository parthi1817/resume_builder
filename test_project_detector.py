from utils.pdf_reader import extract_text
from utils.project_detector_v2 import detect_projects

with open("sample_resume.pdf", "rb") as f:
    text = extract_text(f)

lines = text.split("\n")

projects = detect_projects(lines)

print(projects)