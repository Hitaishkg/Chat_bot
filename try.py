import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define a text to be processed
text = "SpaCy is a powerful NLP library."

# Process the text using spaCy
doc = nlp(text)

# Accessing token information
for token in doc:
    print(f"Token: {token.text}, POS: {token.pos_}, Dependency: {token.dep_}")

# Extracting named entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
