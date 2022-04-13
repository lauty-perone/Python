import math

arch_nombres = open("nombres.txt", "r", encoding="utf-8")
nombres = arch_nombres.read().split() #Leo y me guardo ya separado en una lista los nombres  
arch_nombres.close()  

arch_notas_1= open('eval1.txt','r',encoding="utf-8")
notas_1 = map (int, arch_notas_1.read().split(","))
arch_notas_1.close()

arch_notas_2 = open('eval2.txt','r',encoding="utf-8")
notas_2 = map(int,arch_notas_2.read().split(",")) #Leo notas creando ya la lista 
arch_notas_2.close()                              #y convirtiendolos a enteros

for pos, nombre in enumerate(nombres):
    nombres[pos] = ((nombre. replace(",",''))) #Borro la , para que quede más lindo :)

total = list(map(lambda x,y: x + y, notas_1,notas_2)) #Creo una lista por comprensión con 
                                                      #la suma de los valores de las dos lista

estructura_dicci = dict(zip(nombres, total)) #Creo un diccionario con los nombres y el total
 
prom=  math.trunc(sum(total) /len(total)) #Calculo el promedio y lo trunco
print('El promedio total de alumnos es: ' ,prom)

for elem in estructura_dicci:
    if estructura_dicci[elem]> prom: #Pregunto por el valor de cada uno si es > al promedio
        print('El nombre del alumno que supera el promedio es: ',elem)
    
        
    


