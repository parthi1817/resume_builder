from utils.pdf_reader import extract_text
from utils.certificate_detector_v2 import detect_certificates

with open("sample_resume.pdf", "rb") as f:
    text = extract_text(f)

lines = text.split("\n")

certificates = detect_certificates(lines)

print(certificates)