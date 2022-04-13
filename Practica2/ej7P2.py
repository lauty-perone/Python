cadena = input('Ingrese una palabra o frase para indicar si es un cadena: ')
cumple= False
cont=0
while (cumple == False)& (cont <len(cadena)):
    if (cadena.count(cadena[cont])>1):
        cumple = True
    cont+=1
if cumple:
    print('La palabra o frase es un heterograma')
else:
    print('La palabra o frase no es un heterograma') 