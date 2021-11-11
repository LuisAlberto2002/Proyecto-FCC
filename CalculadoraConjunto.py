"""
@authors:
Luis Alberto Rendon Alonso
Jose Santiago Oseguera Garcia
Jose Luis Almendarez Gonzalez

"""

import random

def crearConjunto(conjunto,tam):
    #Le pide valores al usuario para crear sus conjuntos
    #f"{i} indica cual valor es el que esta ingresando
    for i in range(1,tam+1):
        num = int(input(f"{i} Introduce un valor para el conjunto (1,100): "))
        while num < 1 or num > 100:
            print("Valor se pasa del limite intentalo de nuevo")
            num = int(input(f"{i} Introduce un valor para el conjunto (1,100): "))
        while num in conjunto:
            print("Valor repetido intentalo de nuevo")
            num = int(input(f"{i} Introduce un valor para el conjunto (1,100): "))
        conjunto.append(num)
    return sorted(conjunto)

def crearConjuntoRan(conjunto,tam):
    #Usando la funcion sample de random, nos da una lista en el rango indicado 
    conjunto = random.sample(range(1,101), tam)
    return sorted(conjunto)
    
def union(conjunto1,conjunto2):
    #Se suman los conjuntos y la lista resulante se convierte en un diccionario
    #para quitar los numeros repetidos, despues de eso se convierte en una lista
    #de nuevo
    conjunto3 = conjunto1+conjunto2
    conjunto3 = list(dict.fromkeys(conjunto3))
    return sorted(conjunto3)

def interseccion(conjunto1,conjunto2):
    #Muestra los elementos en comun entre los dos conjuntos
    conjunto3 = []
    for i in range(0,len(conjunto1)):
        for h in range(0,len(conjunto2)):
            if conjunto1[i] == conjunto2[h]:
                add = conjunto1[i]
                if add in conjunto3:
                    continue
                else:
                    conjunto3.append(add)
    return conjunto3

def productoCartesiano(conjunto1,conjunto2):
    #Crea el producto cartesiano de los dos conjuntos señalados
    conjunto3 = []
    for i in range(0,len(conjunto1)):
        for h in range(0,len(conjunto2)):
            conjunto3.append((conjunto1[i],conjunto2[h]))
    return conjunto3

def diferencia(conjunto1,conjunto2):
    #Muestra el conjunto sin los elementos del otro conjunto
    conjunto3 = []
    for i in range(0,len(conjunto2)):
        add = conjunto2[i]
        if add not in conjunto1:
            conjunto3.append(add)
    return sorted(conjunto3)
        
def complemento(conjunto1,U):
    #Usa la diferencia para mostrar que elementos no se encuentran en el
    #conjunto señalado
    conjunto3 = diferencia(conjunto1, U)
    return sorted(conjunto3)

def diferenciaSim(conjunto1,conjunto2):
    #Calcula la diferencia simetrica usando la interseccion y la union de los conjuntos
    conjunto3 = diferencia(interseccion(conjunto1,conjunto2), union(conjunto1, conjunto2))
    return sorted(conjunto3)

def cardinalidad(conjunto):
    #Aqui hacemos que se cuenten la cantidad de elementos que se encuentran dentro de la lista
    tam = len(conjunto)
    return tam

def contencionAdentroB(conjunto1,conjunto2):
    conjunto1Tupla = tuple(conjunto1)
    conjunto2Tupla = tuple(conjunto2)
    resultadoBdentroA = conjunto1Tupla < conjunto2Tupla
    if resultadoBdentroA == True:
        print("A dentro de A")
    else:
        print("no hay contencion en este caso")
    #Mediante el operador y los conjuntos como tupla se detecta si todos los elementos de A estan dentro de B

def contencionBdentroA(conjunto1,conjunto2):
    conjunto1Tupla = tuple(conjunto1)
    conjunto2Tupla = tuple(conjunto2)
    resultadoBdentroA = conjunto2Tupla < conjunto1Tupla
    if resultadoBdentroA == True:
        print("B dentro de A")
    else:
        print("no hay contencion en este caso")
    #Mediante el operador y los conjuntos como tupla se detecta si todos los elementos de B estan dentro de A


def conjuntoPotencia(numeros):
    return subconjuntos_recursivo([], sorted(numeros))

def subconjuntos_recursivo(actual, conjunto):
    if conjunto:
        return subconjuntos_recursivo(actual, conjunto[1:]) + subconjuntos_recursivo(actual + [conjunto[0]], conjunto[1:])
    return [actual]

#Estas dos funciones son para el conjunto potencia, al hacer tener que hacer todas las combinaciones se uso una oporacion
#recursiva. Partiendo la lista y dando distintas combinaciones.








