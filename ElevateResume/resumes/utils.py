import spacy
nlp = spacy.load('en_core_web_sm')

def analyze_resume(content):
    doc = nlp(content)
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return keywords
