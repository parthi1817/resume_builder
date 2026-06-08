from utils.spacy_helper import get_doc

text = """
Software Development Intern at Infosys
May 2025 - July 2025
"""

doc = get_doc(text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)