evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python.
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""
lista= [0,0,0,0]

titulo = evaluar.split("\n")[0].split() #Me quedo con el titulo
titulo.remove(titulo[0])                #Saco la primer palabra

if(len(titulo)<=10):
    print('Titulo esta ok')
else: 
    print('Titulo NO ok')

oraciones = evaluar.split(".")
oraciones.remove(oraciones[0])

for elem in oraciones: 
    if (len((elem).split()) <=12):
       lista[0]+=1
    elif((len((elem).split()) >= 13) & (len((elem).split()) <=17) ):
        lista[1]+=1
    elif((len((elem).split()) >= 18) & (len((elem).split()) <=25) ):
        lista[2]+=1
    elif (len((elem).split())>25):
        lista[3]+=1
print('Facil de leer: ',lista[0],'aceptable de leer: ', lista[1], 'dificil de leer: ',lista[2], 'muy dificil: ', lista[3])

