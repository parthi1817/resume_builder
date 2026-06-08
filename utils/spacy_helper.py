import spacy

nlp = spacy.load("en_core_web_sm")

def get_doc(text):

    # Remove problematic unicode characters
    text = text.encode("utf-8", "ignore").decode("utf-8")

    return nlp(text)