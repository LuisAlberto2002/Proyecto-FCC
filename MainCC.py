"""
@authors:
Luis Alberto Rendon Alonso
Jose Santiago Oseguera Garcia
Jose Luis Almendarez Gonzalez

"""

import CalculadoraConjunto as CC

def main():
    A = []
    B = []
    U = []
    for i in range(1,101):
        U.append(i)
    C = []
    opc_menu = 0
    print("Calculadora Conjuntos")
    opc = int(input("Quieres crear tus propios conjuntos o los quieres aleatorios? 1(crear)/2(aleatorios)"))
    while opc != 1 and opc != 2:
        print("Opcion no valida intentalo de nuevo")
        opc = int(input("Quieres crear tus propios conjuntos o los quieres aleatorios? 1(crear)/2(aleatorios)"))
    tam1 = int(input("De que tamaño quieres el primer conjunto? "))
    tam2 = int(input("De que tamaño quieres el segundo conjunto? "))
    if opc == 1:
        print("Primer conjunto:")
        A = CC.crearConjunto(A, tam1)
        print("Segundo conjunto")
        B = CC.crearConjunto(B, tam2)
    elif opc == 2:
        A = CC.crearConjuntoRan(A, tam1)
        B = CC.crearConjuntoRan(B, tam2)
    while opc_menu != 18:
        print("Menú de Calculadora de Conjuntos")
        print("1. Intersección A∩B")
        print("2. Unión A∪B")
        print("3. Diferencia A-B")
        print("4. Diferencia B-A")
        print("5. Diferencia simétrica")
        print("6. Complemento de A")
        print("7. Complemento de B")
        print("8. Producto cartesiano AxB")
        print("9. Producto cartesiano BxA")
        print("10. Producto cartesiano AxA")
        print("11. Producto cartesiano BxB")
        print("12. Conjunto potencia A")
        print("13. Conjunto potencia B")
        print("14. Cardinalidad de A")
        print("15. Cardinalidad de B")
        print("16. Contención A⊆B (Verdadero o falso)")
        print("17. Contención B⊆A (Verdadero o falso)")
        print("18. Salir")
        opc_menu = eval(input("Selecciona una opcion: "))
        if opc_menu == 1:
            C = CC.interseccion(A, B)
            print("Conjunto A: ",A)
            print("Conjunto B: ",B)
            print("Interseccion: ",C)
        elif opc_menu == 2:
            C = CC.union(A, B)
            print("Conjunto A: ",A)
            print("Conjunto B: ",B)
            print("Union: ",C)
        elif opc_menu == 3:
            C = CC.diferencia(A, B)
            print("Conjunto A: ",A)
            print("Conjunto B: ",B)
            print("Diferencia A-B: ",C)
        elif opc_menu == 4:
            C = CC.diferencia(B, A)
            print("Conjunto A: ",A)
            print("Conjunto B: ",B)
            print("Diferencia B-A: ",C)
        elif opc_menu == 5:
            C = CC.diferenciaSim(A, B)
            print("Conjunto A: ",A)
            print("Conjunto B: ",B)
            print("Diferencia Simetrica: ",C)
        elif opc_menu == 6:
            C = CC.complemento(A, U)
            print("Conjunto A: ",A)
            print("Complemento A: ",C)
        elif opc_menu == 7:
            C = CC.complemento(B, U)
            print("Conjunto B: ",B)
            print("Complemento B: ",C)
        elif opc_menu == 8:
            C = CC.productoCartesiano(A, B)
            print("Conjunto A: ",A)
            print("Conjunto B: ",B)
            print("Producto cartesiano AxB: ",C)
        elif opc_menu == 9:
            C = CC.productoCartesiano(B, A)
            print("Conjunto A: ",A)
            print("Conjunto B: ",B)
            print("Producto cartesiano BxA: ",C)
        elif opc_menu == 10:
            C = CC.productoCartesiano(A, A)
            print("Conjunto A: ",A)
            print("Producto cartesiano AxA: ",C)
        elif opc_menu == 11:
            C = CC.productoCartesiano(B, B)
            print("Conjunto B: ",B)
            print("Producto cartesiano BxB: ",C)
        elif opc_menu == 12:
            print("Conjunto A:", A)
            print("Cardinalidad de conjunto Potencia: ",len(CC.conjuntoPotencia(A)))
            print(CC.conjuntoPotencia(A))
        elif opc_menu == 13:
            print("Conjunto B:", B)
            print("Cardinalidad de conjunto Potencia: ",len(CC.conjuntoPotencia(B)))
            print(CC.conjuntoPotencia(B))
        elif opc_menu == 14:
            print("Conjunto A:", A)
            tam = CC.cardinalidad(A)
            print("La tamaño del conjunto A es de", tam, "elementos")
        elif opc_menu == 15:
            print("Conjunto B:", B)
            tam = CC.cardinalidad(B)
            print("La tamaño del conjunto B es de", tam, "elementos")
        elif opc_menu == 16:
            print("Conjunto A: ", A)
            print("Conjunto B: ", B)
            CC.contencionAdentroB(A,B)
        elif opc_menu == 17:
            print("Conjunto A: ", A)
            print("Conjunto B: ", B)
            CC.contencionBdentroA(A,B)
        elif opc_menu == 18:
            print("Gracias por usar este programa!")
        else:
            print("Opcion no valida, intentalo de nuevo")
        print("\n")
            
            
main()