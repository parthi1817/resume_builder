# Keep your existing imports
from utils.pdf_reader import extract_text
with open("sample_resume.pdf", "rb") as f:
    text = extract_text(f)

lines = text.split("\n")

for i, line in enumerate(lines):
    if "INTERNSHIP" in line.upper():
        print("FOUND AT:", i)

        for j in range(i, min(i + 15, len(lines))):
            print(j, ":", repr(lines[j]))