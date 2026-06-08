from utils.spacy_helper import get_doc

def detect_internships(text):

    doc = get_doc(text)

    internships = []

    for ent in doc.ents:

        if ent.label_ == "ORG":
            internships.append(ent.text)

    return list(set(internships))