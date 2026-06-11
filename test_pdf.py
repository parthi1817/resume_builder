from utils.pdf_reader import extract_text

with open("sample_resume.pdf", "rb") as f:
    text = extract_text(f)

print("TEXT LENGTH =", len(text))
print(text.encode("utf-8", errors="ignore").decode("utf-8"))