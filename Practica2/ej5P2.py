frase = input ('Ingrese una frase: ').split(" ")

palabra = input('Ingrese una palabra para indicar cuantas veces se repite en la frase: ')
cant=frase.count(palabra)
print(f'La cantidad de veces que se repite la palabra es: {cant}')
