import string

# Funcion devolve as words do textp, en minusculas e sin puntuación para poder comparalas
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return set(words)

def compare_texts(text1, text2):
    # limpiar textos
    words1 = clean_text(text1)
    words2 = clean_text(text2)

    # Palabras comuns en ambos textos
    common_words = words1 & words2
    
    # Calcular % de coincidencia
    if len(words1) > 0:
        precision_percentage = (len(common_words) / len(words1)) * 100
    else:
        precision_percentage = 0
    
    return text1, text2, precision_percentage

# Funcion para reemplazar unha palabra por outra
def replace_word(text: str, original: str, new: str):
    new_text = text.replace(original, new)
    return new_text
