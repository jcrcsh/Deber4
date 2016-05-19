from textblob import TextBlob

archivo = open("texto.txt", 'r')
lineas = archivo.readlines()
archivo.close()
blob = TextBlob(lineas)
blob.tags
blob.noun_phrases
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
blob.translate(to = "en")


##oye que nomas hace el ejercicio  aparte contar las palabras y traducir?