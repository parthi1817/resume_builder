from utils.pdf_reader import extract_text
from utils.spacy_helper import get_doc

with open("sample_resume.pdf", "rb") as f:
    text = extract_text(f)

doc = get_doc(text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)