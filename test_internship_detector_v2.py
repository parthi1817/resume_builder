from utils.pdf_reader import extract_text
from utils.internship_detector_v2 import detect_internships

with open("sample_resume.pdf", "rb") as f:
    text = extract_text(f)

lines = text.split("\n")

print(detect_internships(lines))