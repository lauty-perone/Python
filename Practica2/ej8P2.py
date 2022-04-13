palabra = input ('Ingrese una palabra: ').upper()
dicci= {'AEIOULNRST': 1,'DG': 2,'BCMP': 3, 'FHVWY': 4,'K': 5,'JX': 8,'QZ':10} 
total=0
for letra in palabra: #agarro una letra
    for clave in dicci:  #recorro las claves para ver a que letra le corresponde
        if (clave.count(letra)): #si la letra esta en esa clave
            total+=dicci[clave]  #sumo el valor
            print(f'El puntaje por la letra es: {dicci[clave]}')

print(f'El puntaje total por la palabra es: {total}')

