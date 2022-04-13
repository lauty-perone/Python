from collections import Counter

f=open("Readme.txt", "r")
texto = f.read()
contador=Counter ()
texto=texto.lower().replace('/', ' ').replace(':', ' ').replace('.', ' ').replace(';', ' ').replace('"', ' ').replace('-', ' ')
texto=texto.replace('(', ' ').replace(')', ' ').replace(',', ' ').replace('!', ' ').replace('@', ' ').replace('\'', ' ')
palabras=texto.split()


for palabra in palabras:
    contador[palabra] += 1
print (contador.most_common())
print ()