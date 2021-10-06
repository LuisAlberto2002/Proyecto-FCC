# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:06:32 2021

@author: deku1
"""

import CalculadoraVerdad as CV

def main():
    p = []
    q = []
    r = []
    lista4 = []
    lista5 = []
    lista6 = []
    lista7 = []
    opc_menu = 0
    num = 0
    while opc_menu != 4:
        print("Menú de Calculadora de Tabla de Verdades")
        print("1. Imprimir Tabla de Verdad")
        print("2. Comprobar Equivalencias")
        print("3. Determinar si es tautologia o contradiccion")
        print("4. Salir")
        opc_menu = eval(input("Selecciona una opcion: "))
        if opc_menu == 1:
            num = CV.preguntasUsuario()
            if num == 1:
                p = CV.Proposiciones(num)
                num2, columnas = CV.preguntasProposiciones1()
                lista4,lista5 = CV.ConversionTabla1(num2, p,lista4,lista5)
                if lista5 == []:
                    lista5 = ["","","",""]
                if lista6 == []:
                    lista6 = ["","","",""]
                if lista7 == []:
                    lista7 = ["","","",""]
                CV.Print(num,columnas,p,q,r,lista4,lista5,lista6,lista7)
            elif num == 2:
                p, q = CV.Proposiciones(num)
                num2, columnas = CV.preguntasProposiciones2()
                lista4,lista5,lista6,lista7 = CV.ConversionTabla(num2,p,q,r,lista4,lista5,lista6,lista7)
                if lista5 == []:
                    lista5 = ["","","",""]
                if lista6 == []:
                    lista6 = ["","","",""]
                if lista7 == []:
                    lista7 = ["","","","","","","",""]
                CV.Print(num,columnas,p,q,r,lista4,lista5,lista6,lista7)
            elif num == 3:
                p, q, r = CV.Proposiciones(num)
                num2, columnas = CV.preguntasProposiciones3()
                lista4,lista5,lista6,lista7 = CV.ConversionTabla(num2,p,q,r,lista4,lista5,lista6,lista7)
                if lista5 == []:
                    lista5 = ["","","","","","","",""]
                if lista6 == []:
                    lista6 = ["","","","","","","",""]
                if lista7 == []:
                    lista7 = ["","","","","","","",""]
                CV.Print(num,columnas,p,q,r,lista4,lista5,lista6,lista7)
        elif opc_menu == 2:
            if num == 0:
                print("No has creado una proposicion compuesta. Intentalo de nuevo después.")
            else:
                x = eval(input("Primera proposicion a comparar (Dame el numero de la proposicion): "))
                y = eval(input("Segunda proposicion a comparar (Dame el numero de la proposicion): "))
                CV.Equivalencia(x,y,p,q,r,lista4,lista5,lista6,lista7)
        elif opc_menu == 3:
            z = input("Quieres checar Tautologia o Contradiccion? (T/C): ").strip().title()
            if z == "T":
                a = eval(input("Cual proposicion compuesta quieres verificar? (1,2,3) "))
                if a == 1:
                    CV.Tautologia(lista4)
                elif a == 2:
                    CV.Tautologia(lista5)
                elif a == 3:
                    CV.Tautologia(lista6)
                elif a == 4:
                    CV.Tautologia(lista7)
                    print("Proposicion no valida.")
            elif z == "C":
                a = eval(input("Cual proposicion compuesta quieres verificar? (1,2,3,4) "))
                if a == 1:
                    CV.Contradiccion(lista4)
                elif a == 2:
                    CV.Contradiccion(lista5)
                elif a == 3:
                    CV.Contradiccion(lista6)
                elif a == 4:
                    CV.Contradiccion(lista7)
                else:
                    print("Proposicion no valida.")
        elif opc_menu == 4:
            print("Adios")
        else:
            print("Opcion no valida. Intentalo de nuevo\n")
if __name__ == "__main__":
    main()