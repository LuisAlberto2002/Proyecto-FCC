# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 14:08:28 2021

@author: deku1
"""

def Num(lista):
    # Cambia los 0 y 1 por False y True respectivamente
    for n, i in enumerate(lista):
        if i==1:
            lista[n] = True
        elif i == 0:
            lista[n] = False
    return lista

def conjuncion(x, y):
    #Conjuncion de los valores
    return(x and y)
    
def disyuncion(x, y):
    #Disyuncion de los valores
    if x == False and y == False:
        return False
    else:
        return True

def negacion(x):
    #Negacion de los valores
  return not(x)

def condicional(x, y):
    #Condiconal de los valores
    if x == True and y == False:
        return False
    else:
        return True

def bicondicional(x, y):
    #Bicondicional de los valores
  return (condicional(x, y) and condicional(y, x))

def DisyuncionExclusiva(x,y):
    #Disyuncion Exclusiva de los valores
    if x == y:
        return False
    else:
        return True


def ConversionTabla(x,p,q,r,lista4,lista5,lista6,lista7):
    #Esta funcion recibe un numero
    if x == 1:
        for i in range(len(p)):
          lista4.append(conjuncion(p[i], q[i]))

    elif x == 2:
        for i in range(len(p)):
          lista4.append(disyuncion(p[i], q[i]))

    elif x == 3:
        for i in range(len(p)):
          lista4.append(negacion(p[i]))

    elif x == 4:
        for i in range(len(p)):
          lista4.append(negacion(q[i]))

    elif x == 5:
        for i in range(len(p)):
          lista4.append(condicional(p[i], q[i]))

    elif x == 6:
        for i in range(len(p)):
          lista4.append(condicional(q[i], p[i]))

    elif x == 7:
        for i in range(len(p)):
          lista4.append(bicondicional(p[i], q[i]))

    elif x == 8:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i], q[i]))

    elif x == 9:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(conjuncion(lista4[i],q[i]))

    elif x == 10:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(disyuncion(lista4[i],q[i]))

    elif x == 11:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(condicional(lista4[i],q[i]))

    elif x == 12:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(condicional(p[i],lista4[i]))

    elif x == 13:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(bicondicional(lista4[i],q[i]))

    elif x == 14:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(DisyuncionExclusiva(lista4[i],q[i]))

    elif x == 15:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(negacion(lista4[i]))

    elif x == 16:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(negacion(lista4[i]))

    elif x == 17:
        for i in range(len(p)):
            lista4.append(condicional(p[i],q[i]))
            lista5.append(negacion(lista4[i]))

    elif x == 18:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i],q[i]))
            lista5.append(negacion(lista4[i]))

    elif x == 19:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(negacion(lista4[i]))

    elif x == 20:
        for i in range(len(p)):
          lista4.append(conjuncion(p[i], r[i]))

    elif x == 21:
        for i in range(len(p)):
          lista4.append(disyuncion(p[i], r[i]))

    elif x == 22:
        for i in range(len(p)):
          lista4.append(negacion(r[i]))

    elif x == 23:
        for i in range(len(p)):
          lista4.append(condicional(p[i], r[i]))

    elif x == 24:
        for i in range(len(p)):
          lista4.append(condicional(r[i], p[i]))

    elif x == 25:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(bicondicional(p[i],lista4[i]))

    elif x == 31:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(disyuncion(lista4[i],lista5[i]))

    elif x == 32:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(conjuncion(lista4[i],lista5[i]))

    elif x == 33:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(condicional(lista4[i], lista5[i]))

    elif x==34:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], lista5[i]))

    elif x==35:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))

    elif x==41:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(disyuncion(lista4[i], r[i]))

    elif x== 42:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(conjuncion(lista4[i],r[i]))

    elif x == 43:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(condicional(lista4[i], r[i]))

    elif x==44:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(DisyuncionExclusiva(lista4[i], r[i]))

    elif x==45:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(bicondicional(lista4[i], r[i]))

    elif x==51:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(disyuncion(lista4[i],r[i]))

    elif x==52:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(conjuncion(lista4[i],r[i]))

    elif x==53:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(condicional(lista4[i], r[i]))

    elif x==54:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(DisyuncionExclusiva(lista4[i], r[i]))

    elif x==55:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(bicondicional(lista4[i], r[i]))

    elif x==61:
        for i in range(len(p)):
            lista4.append(condicional(p[i], q[i]))
            lista5.append(disyuncion(lista4[i], r[i]))

    elif x==62:
        for i in range(len(p)):
            lista4.append(condicional(p[i],q[i]))
            lista5.append(conjuncion(lista4[i], r[i]))

    elif x==63:
        for i in range(len(p)):
            lista4.append(condicional(p[i],q[i]))
            lista5.append(condicional(lista4[i],r[i]))

    elif x==64:
        for i in range(len(p)):
            lista4.append(condicional(p[i],q[i]))
            lista5.append(DisyuncionExclusiva(lista4, r[i]))

    elif x==65:
        for i in range(len(p)):
            lista4.append(condicional(p[i],q[i]))
            lista5.append(bicondicional(lista4[i], r[i]))

    elif x==71:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(disyuncion(lista4[i], r[i]))

    elif x==72:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(conjuncion(lista4[i],r[i]))

    elif x==73:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(condicional(lista4[i],r[i]))

    elif x==74:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(DisyuncionExclusiva(lista4[i], r[i]))

    elif x == 75:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(bicondicional(lista4, r[i]))

    elif x==81:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i],q[i]))
            lista5.append(disyuncion(lista4[i],r[i]))

    elif x==82:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i],q[i]))
            lista5.append(conjuncion(lista4[i], r[i]))

    elif x == 83:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i],q[i]))
            lista5.append(condicional(lista4[i],r[i]))

    elif x ==84:
        for i in range(len(p)):
            for i in range(len(p)):
                lista4.append(bicondicional(p[i], q[i]))
                lista5.append(DisyuncionExclusiva(lista4[i],r[i]))

    elif x==85:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i],q[i]))
            lista5.append(bicondicional(lista4[i],r[i]))

    elif x==91:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(disyuncion(lista4[i],q[i]))
            lista6.append(disyuncion(lista5[i],r[i]))

    elif x==92:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(disyuncion(lista4[i],q[i]))
            lista6.append(conjuncion(lista5[i], r[i]))

    elif x == 93:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(disyuncion(lista4[i],q[i]))
            lista6.append(condicional(lista5[i], r[i]))

    elif x==94:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(disyuncion(lista4[i],q[i]))
            lista6.append(DisyuncionExclusiva(lista5[i],r[i]))

    elif x==95:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(disyuncion(lista4[i],q[i]))
            lista6.append(bicondicional(lista5[i], r[i]))

    elif x==101:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(conjuncion(lista4[i],q[i]))
            lista6.append(disyuncion(lista5[i],r[i]))

    elif x==102:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(conjuncion(lista4[i], q[i]))
            lista6.append(conjuncion(lista5[i], r[i]))

    elif x==103:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(conjuncion(lista4[i], q[i]))
            lista6.append(condicional(lista5[i], r[i]))

    elif x==104:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(conjuncion(lista4[i], q[i]))
            lista6.append(DisyuncionExclusiva(lista5[i], r[i]))

    elif x==105:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(conjuncion(lista4[i], q[i]))
            lista6.append(bicondicional(lista5[i], r[i]))

    elif x==111:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(condicional(lista4[i],q[i]))
            lista6.append(disyuncion(lista5[i],r[i]))

    elif x ==112:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(condicional(lista4[i],q[i]))
            lista6.append(conjuncion(lista5[i], r[i]))

    elif x == 113:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(condicional(lista4[i],q[i]))
            lista6.append(condicional(lista5[i], r[i]))

    elif x == 114:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(condicional(lista4[i],q[i]))
            lista6.append(DisyuncionExclusiva(lista5[i], r[i]))

    elif x==115:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(condicional(lista4[i],q[i]))
            lista6.append(bicondicional(lista5[i], r[i]))

    elif x==121:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(DisyuncionExclusiva(lista4[i], q[i]))
            lista6.append(disyuncion(lista5[i], r[i]))

    elif x==122:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(DisyuncionExclusiva(lista4[i], q[i]))
            lista6.append(conjuncion(lista5[i], r[i]))

    elif x==123:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(DisyuncionExclusiva(lista4[i], q[i]))
            lista6.append(condicional(lista5[i], r[i]))

    elif x==124:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(DisyuncionExclusiva(lista4[i], q[i]))
            lista6.append(DisyuncionExclusiva(lista5[i], r[i]))

    elif x==125:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(DisyuncionExclusiva(lista4[i], q[i]))
            lista6.append(bicondicional(lista5[i], r[i]))

    elif x==131:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(bicondicional(lista4[i], q[i]))
            lista6.append(disyuncion(lista5[i], r[i]))

    elif x==132:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(bicondicional(lista4[i], q[i]))
            lista6.append(conjuncion(lista5[i],r[i]))

    elif x==133:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(bicondicional(lista4[i], q[i]))
            lista6.append(condicional(lista5[i], r[i]))

    elif x==134:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(bicondicional(lista4[i], q[i]))
            lista6.append(DisyuncionExclusiva(lista5[i], r[i]))

    elif x==135:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(bicondicional(lista4[i], q[i]))
            lista6.append(bicondicional(lista5[i], r[i]))

    elif x==141:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(conjuncion(p[i], lista4[i]))
            lista6.append(conjuncion(lista5[i], r[i]))

    elif x==142:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(disyuncion(p[i], lista4[i]))
            lista6.append(disyuncion(lista5[i], r[i]))

    elif x==143:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(disyuncion(p[i], lista4[i]))
            lista6.append(conjuncion(lista5[i], r[i]))

    elif x==144:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(disyuncion(p[i], lista4[i]))
            lista6.append(DisyuncionExclusiva(lista5[i], r[i]))

    elif x==145:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(disyuncion(p[i], lista4[i]))
            lista6.append(bicondicional(lista5[i], r[i]))

    elif x==151:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(conjuncion(p[i], lista4[i]))
            lista6.append(disyuncion(lista5[i], r[i]))

    elif x==152:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(conjuncion(p[i], lista4[i]))
            lista6.append(conjuncion(lista5[i], r[i]))

    elif x==153:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(conjuncion(p[i], lista4[i]))
            lista6.append(condicional(lista5[i], r[i]))

    elif x==154:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(conjuncion(p[i], lista4[i]))
            lista6.append(DisyuncionExclusiva(lista5[i], r[i]))

    elif x==155:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(conjuncion(p[i], lista4[i]))
            lista6.append(bicondicional(lista5[i], r[i]))

    elif x==161:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(condicional(p[i], lista4[i]))
            lista6.append(disyuncion(lista5[i], r[i]))

    elif x==162:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(condicional(p[i], lista4[i]))
            lista6.append(conjuncion(lista5[i],r[i]))

    elif x==163:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(condicional(p[i], lista4[i]))
            lista6.append(condicional(lista5[i], r[i]))

    elif x==164:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(condicional(p[i], lista4[i]))
            lista6.append(DisyuncionExclusiva(lista5[i], r[i]))

    elif x==165:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(condicional(p[i], lista4[i]))
            lista6.append(bicondicional(lista5[i], r[i]))

    elif x==171:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista6.append(disyuncion(lista5[i], r[i]))

    elif x==172:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista6.append(conjuncion(lista5[i], r[i]))

    elif x==173:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista6.append(condicional(lista5[i], r[i]))

    elif x==174:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista6.append(DisyuncionExclusiva(lista5[i], r[i]))

    elif x==175:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista6.append(bicondicional(lista5[i], r[i]))
    elif x==181:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(bicondicional(p[i], lista4[i]))
            lista6.append(disyuncion(lista5[i], r[i]))

    elif x==182:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(bicondicional(p[i], lista4[i]))
            lista6.append(conjuncion(lista5[i], r[i]))

    elif x==183:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(bicondicional(p[i], lista4[i]))
            lista6.append(condicional(lista5[i],r[i]))

    elif x==184:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(bicondicional(p[i], lista4[i]))
            lista6.append(DisyuncionExclusiva(lista5[i], r[i]))

    elif x==185:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(bicondicional(p[i], lista4[i]))
            lista6.append(bicondicional(lista5[i],r[i]))

    elif x==191:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(disyuncion(lista4[i], lista5[i]))

    elif x==192:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(lista4[i],lista5[i]))

    elif x==193:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(lista4[i],lista5[i]))

    elif x==194:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], lista5[i]))

    elif x==195:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))

    elif x==201:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(disyuncion(lista4[i],lista5[i]))

    elif x==202:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(lista4[i], lista5[i]))

    elif x==203:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(lista4[i],lista5[i]))

    elif x==204:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], lista5[i]))

    elif x==205:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))

    elif x==211:
        for i in range(len(p)):
            lista4.append(condicional(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(disyuncion(lista4[i], lista5[i]))

    elif x==212:
        for i in range(len(p)):
            lista4.append(condicional(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(lista4[i],lista5[i]))

    elif x==213:
        for i in range(len(p)):
            lista4.append(condicional(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(lista4[i],lista5[i]))

    elif x==214:
        for i in range(len(p)):
            lista4.append(condicional(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], lista5[i]))

    elif x==215:
        for i in range(len(p)):
            lista4.append(condicional(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))

    elif x==221:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(disyuncion(lista4[i],lista5[i]))

    elif x==222:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(lista4[i], lista5[i]))

    elif x==223:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(lista4[i], lista5[i]))

    elif x==224:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], lista5[i]))

    elif x==225:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))

    elif x==231:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(disyuncion(lista4[i], lista5[i]))

    elif x==232:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(lista4[i], lista5[i]))

    elif x==233:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(lista4[i], lista5[i]))

    elif x==234:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(lista4[i],lista5[i]))

    elif x==235:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i],q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))

    elif x==241:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(disyuncion(lista4[i], lista5[i]))
            lista7.append(disyuncion(lista6[i], r[i]))

    elif x == 242:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(disyuncion(lista4[i], lista5[i]))
            lista7.append(conjuncion(lista6[i], r[i]))

    elif x == 243:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(disyuncion(lista4[i], lista5[i]))
            lista7.append(condicional(lista6[i], r[i]))

    elif x == 244:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(disyuncion(lista4[i], lista5[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], r[i]))

    elif x == 245:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(disyuncion(lista4[i], lista5[i]))
            lista7.append(bicondicional(lista6[i], r[i]))

    elif x == 251:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(conjuncion(lista4[i], lista5[i]))
            lista7.append(disyuncion(lista6[i], r[i]))

    elif x == 252:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(conjuncion(lista4[i], lista5[i]))
            lista7.append(conjuncion(lista6[i], r[i]))

    elif x == 253:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(conjuncion(lista4[i], lista5[i]))
            lista7.append(condicional(lista6[i], r[i]))

    elif x == 254:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(conjuncion(lista4[i], lista5[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], r[i]))
            return lista4, lista5, lista6, lista7
    elif x == 255:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(conjuncion(lista4[i], lista5[i]))
            lista7.append(bicondicional(lista6[i], r[i]))
            return lista4, lista5, lista6, lista7
    elif x == 261:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(condicional(lista4[i], lista5[i]))
            lista7.append(disyuncion(lista6[i], r[i]))

    elif x == 262:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(condicional(lista4[i], lista5[i]))
            lista7.append(conjuncion(lista6[i], r[i]))

    elif x == 263:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(condicional(lista4[i], lista5[i]))
            lista7.append(condicional(lista6[i], r[i]))

    elif x == 264:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(condicional(lista4[i], lista5[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], r[i]))

    elif x == 265:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(condicional(lista4[i], lista5[i]))
            lista7.append(bicondicional(lista6[i], r[i]))

    elif x == 271:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], lista5[i]))
            lista7.append(disyuncion(lista6[i], r[i]))

    elif x == 272:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], lista5[i]))
            lista7.append(conjuncion(lista6[i], r[i]))

    elif x == 273:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], lista5[i]))
            lista7.append(condicional(lista6[i], r[i]))

    elif x == 274:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], lista5[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], r[i]))

    elif x == 275:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], lista5[i]))
            lista7.append(bicondicional(lista6[i], r[i]))

    elif x == 281:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))
            lista7.append(disyuncion(lista6[i], r[i]))

    elif x == 282:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))
            lista7.append(conjuncion(lista6[i], r[i]))

    elif x == 283:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))
            lista7.append(condicional(lista6[i], r[i]))

    elif x == 284:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], r[i]))

    elif x == 285:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(q[i]))
            lista6.append(bicondicional(lista4[i], lista5[i]))
            lista7.append(bicondicional(lista6[i], r[i]))

    elif x == 291:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i], lista5[i]))
            lista5.append(negacion(q[i]))
            lista6.append(negacion(r[i]))
            lista7.append(disyuncion(lista4[i], lista6[i]))

    elif x == 292:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i], lista5[i]))
            lista5.append(negacion(q[i]))
            lista6.append(negacion(r[i]))
            lista7.append(conjuncion(lista4[i], lista6[i]))

    elif x == 293:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i], lista5[i]))
            lista5.append(negacion(q[i]))
            lista6.append(negacion(r[i]))
            lista7.append(condicional(lista4[i], lista6[i]))

    elif x == 294:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i], lista5[i]))
            lista5.append(negacion(q[i]))
            lista6.append(negacion(r[i]))
            lista7.append(DisyuncionExclusiva(lista4[i], lista6[i]))

    elif x == 295:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i], lista5[i]))
            lista5.append(negacion(q[i]))
            lista6.append(negacion(r[i]))
            lista7.append(bicondicional(lista4[i], lista6[i]))

    elif x==301:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(p[i], lista4[i]))
            lista7.append(disyuncion(lista6[i],lista5[i]))

    elif x==302:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(p[i], lista4[i]))
            lista7.append(conjuncion(lista6[i], lista5[i]))

    elif x==303:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(p[i], lista4[i]))
            lista7.append(condicional(lista6[i], lista5[i]))

    elif x==304:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(p[i], lista4[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], lista5[i]))

    elif x==305:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(p[i], lista4[i]))
            lista7.append(bicondicional(lista6[i], lista5[i]))

    elif x==311:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(p[i], lista4[i]))
            lista7.append(disyuncion(lista6[i], lista5[i]))

    elif x==312:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(p[i], lista4[i]))
            lista7.append(conjuncion(lista6[i], lista5[i]))

    elif x==313:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(p[i], lista4[i]))
            lista7.append(condicional(lista6[i], lista5[i]))

    elif x==314:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(p[i], lista4[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], lista5[i]))

    elif x==315:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(p[i], lista4[i]))
            lista7.append(bicondicional(lista6[i], lista5[i]))

    elif x==321:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista7.append(disyuncion(lista6[i], lista5[i]))

    elif x==322:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista7.append(conjuncion(lista6[i], lista5[i]))

    elif x==323:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista7.append(condicional(lista6[i],lista5[i]))

    elif x==324:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], lista5[i]))

    elif x==325:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista7.append(bicondicional(lista6[i], lista5[i]))

    elif x==331:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(p[i], lista4[i]))
            lista7.append(disyuncion(lista6[i], lista5[i]))

    elif x==332:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(p[i], lista4[i]))
            lista7.append(conjuncion(lista6[i], lista5[i]))

    elif x==333:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(p[i], lista4[i]))
            lista7.append(condicional(lista6[i], lista5[i]))

    elif x==334:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(p[i], lista4[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], lista5[i]))

    elif x==335:
        for i in range(len(p)):
            lista4.append(negacion(q[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(p[i], lista4[i]))
            lista7.append(bicondicional(lista6[i], lista5[i]))

    elif x==341:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(disyuncion(lista4[i], q[i]))
            lista7.append(disyuncion(lista6[i], lista5[i]))

    elif x==342:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(disyuncion(lista4[i], q[i]))
            lista7.append(conjuncion(lista6[i], lista5[i]))

    elif x==343:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(disyuncion(lista4[i], q[i]))
            lista7.append(condicional(lista6[i], lista5[i]))

    elif x==344:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(disyuncion(lista4[i], q[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], lista5[i]))

    elif x==345:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(disyuncion(lista4[i], q[i]))
            lista7.append(bicondicional(lista6[i], lista5[i]))
    elif x==351:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(lista4[i], q[i]))
            lista7.append(disyuncion(lista6[i], lista5[i]))

    elif x==352:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(lista4[i], q[i]))
            lista7.append(conjuncion(lista6[i], lista5[i]))

    elif x==353:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(lista4[i], q[i]))
            lista7.append(condicional(lista6[i], lista5[i]))

    elif x==354:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(lista4[i], q[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], lista5[i]))

    elif x==355:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(conjuncion(lista4[i], q[i]))
            lista7.append(bicondicional(lista6[i], lista5[i]))

    elif x==361:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(lista4[i], q[i]))
            lista7.append(disyuncion(lista6[i], lista5[i]))

    elif x==362:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(lista4[i], q[i]))
            lista7.append(conjuncion(lista6[i], lista5[i]))

    elif x==363:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(lista4[i], q[i]))
            lista7.append(condicional(lista6[i], lista5[i]))

    elif x==364:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(lista4[i], q[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], lista5[i]))

    elif x==365:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(condicional(lista4[i], q[i]))
            lista7.append(bicondicional(lista6[i], lista5[i]))

    elif x==371:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], q[i]))
            lista7.append(disyuncion(lista6[i], lista5[i]))

    elif x==372:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(lista4[i], q[i]))
            lista7.append(conjuncion(lista6[i], lista5[i]))

    elif x==373:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista7.append(condicional(lista6[i],lista5[i]))

    elif x==374:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista7.append(DisyuncionExclusiva(lista6[i],lista5[i]))

    elif x==375:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(DisyuncionExclusiva(p[i], lista4[i]))
            lista7.append(bicondicional(lista6[i],lista5[i]))

    elif x==381:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(lista4[i], q[i]))
            lista7.append(disyuncion(lista6[i], lista5[i]))

    elif x==382:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(lista4[i], q[i]))
            lista7.append(conjuncion(lista6[i], lista5[i]))

    elif x==383:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(lista4[i], q[i]))
            lista7.append(condicional(lista6[i], lista5[i]))

    elif x==384:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(lista4[i], q[i]))
            lista7.append(DisyuncionExclusiva(lista6[i], lista5[i]))

    elif x==385:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(negacion(r[i]))
            lista6.append(bicondicional(lista4[i], q[i]))
            lista7.append(bicondicional(lista6[i], lista5[i]))

    return lista4, lista5, lista6, lista7

    
def ConversionTabla1(x,p,lista4,lista5):
    lista4 = []
    lista5 = []
    if x == 1:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
    elif x == 2:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i], p[i]))
    elif x == 3:
        for i in range(len(p)):
            lista4.append(condicional(p[i], p[i]))
    elif x == 4:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i], p[i]))
    elif x == 5:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i], p[i]))
    elif x == 6:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i], p[i]))
    elif x == 7:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(disyuncion(lista4[i], p[i]))
    elif x == 8:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(bicondicional(lista4[i], p[i]))
    elif x == 9:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(conjuncion(lista4[i], p[i]))
    elif x == 10:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(DisyuncionExclusiva(lista4[i], p[i]))
    elif x == 11:
        for i in range(len(p)):
            lista4.append(negacion(p[i]))
            lista5.append(condicional(lista4[i], p[i]))
    elif x == 12:
        for i in range(len(p)):
            lista4.append(disyuncion(p[i], p[i]))
            lista5.append(negacion(lista4[i]))
    elif x == 13:
        for i in range(len(p)):
            lista4.append(bicondicional(p[i], p[i]))
            lista5.append(negacion(lista4[i]))
    elif x == 14:
        for i in range(len(p)):
            lista4.append(conjuncion(p[i], p[i]))
            lista5.append(negacion(lista4[i]))
    elif x == 15:
        for i in range(len(p)):
            lista4.append(DisyuncionExclusiva(p[i], p[i]))
            lista5.append(negacion(lista4[i]))
    elif x == 16:
        for i in range(len(p)):
            lista4.append(condicional(p[i], p[i]))
            lista5.append(negacion(lista4[i]))
            
    return lista4,lista5
        
def preguntasUsuario():
    print("Se acaba de añadir la Proposision p")
    preQ =input("Quieres Agregar otra Proposision?(S/N) ")
    if preQ.title().strip() == "N":
        return 1
    elif preQ.title().strip() == "S":
        preR = input("Quieres Agregar otra Proposision?(S/N) ")
        if preR.title().strip() == "N":
            return 2
        elif preR == "S":
            return 3
        
def Proposiciones(X):
    if X == 1:
        p = []
        for A in range(2):
            p.append(A)
        p = Num(p)
        return p
    elif X == 2:
        p = []
        q = []
        for A in range(2):
            for B in range(2):
                p.append(A)
                q.append(B)
        p = Num(p)
        q = Num(q)
        return p, q
    elif X == 3:
        p = []
        q = []
        r = []
        for A in range(2):
            for B in range(2):
                for C in range(2):
                    p.append(A)
                    q.append(B)
                    r.append(C)
        p = Num(p)
        q = Num(q)
        r = Num(r)
        return p, q, r
    
def Print(X,columnas,p,q,r,lista4,lista5,lista6,lista7):
    # Esta funcion imprime las proposiciones ordenadas
    if X == 1:
        for i in range(len(columnas)):
            print(columnas[i],end="\t\t")
        print("\n")
        for i in range(len(p)):
            print(p[i],lista4[i],lista5[i],lista6[i],lista7[i],sep="\t")
        print("\n")
    elif X == 2:
        for i in range(len(columnas)):
            print(columnas[i],end="\t\t")
        print("\n")
        for i in range(len(p)):
            print(p[i],q[i],lista4[i],lista5[i],lista6[i],lista7[i],sep="\t")
        print("\n")
    elif X == 3:
        for i in range(len(columnas)):
            print(columnas[i],end="\t\t")
        print("\n")
        for i in range(len(p)):
            print(p[i],q[i],r[i],lista4[i],lista5[i],lista6[i],lista7[i],sep="\t")
        print("\n")
            
def Equivalencia(num1,num2,p,q,r,lista4,lista5,lista6,lista7):
    while num1 == num2 and (num1 < 0 and num2 < 0) and (num1 > 6 and num2 > 6):
        print("Estas comparando las mismas proposiciones compuestas. Intentalo de nuevo")
        num1 = eval(input("Primera proposicion a comparar (Dame el numero de la proposicion): "))
        num2 = eval(input("Segunda proposicion a comparar (Dame el numero de la proposicion): "))
    if num1 == 1 and num2 == 2:
        if p == q:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 1 and num2 == 3:
        if p == r:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 1 and num2 == 4:
        if p == lista4:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 1 and num2 == 5:
        if p == lista5:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 1 and num2 == 6:
        if p == lista6:
            print("Las proposiciones son equivalentes.")
    elif num1 == 1 and num2 == 7:
        if p == lista7:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 2 and num2 == 3:
        if q == r:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 2 and num2 == 4:
        if q == lista4:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 2 and num2 == 5:
        if q == lista5:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 2 and num2 == 6:
        if q == lista6:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 2 and num2 == 7:
        if q == lista7:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 3 and num2 == 4:
        if r == lista4:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 3 and num2 == 5:
        if r == lista5:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 3 and num2 == 6:
        if r == lista6:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 3 and num2 == 7:
        if r == lista7:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 4 and num2 == 5:
        if lista4 == lista5:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 4 and num2 == 6:
        if lista4 == lista6:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 4 and num2 == 7:
        if lista4 == lista7:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 5 and num2 == 6:
        if lista5 == lista6:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 5 and num2 == 7:
        if lista5 == lista7:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    elif num1 == 6 and num2 == 7:
        if lista6 == lista7:
            print("Las proposiciones son equivalentes.")
        else:
            print("Las proposiciones no son equivalentes.")
    
def preguntasProposiciones3():
    columnas = ["p","q","r"]
    print('Proposiciones disponibles: p, q, r')
    print('para una proposicion negativa escribe "~" antes de la letra')
    print('Conectores disponibles: ^, v, >, xor, <>')
    proposicion = input("Escribe que proposicion quieres: ")
    if proposicion.strip() == "pvq":
        columnas.append(proposicion)
        return 1,columnas
    elif proposicion.strip() == 'p^q':
        columnas.append(proposicion)
        return 2,columnas
    elif proposicion.strip() == 'p>q':
        columnas.append(proposicion)
        return 3,columnas
    elif proposicion.strip() == 'pxorq':
        columnas.append(proposicion)
        return 4,columnas
    elif proposicion.strip() == 'p<>q':
        columnas.append(proposicion)
        return 5,columnas
    if proposicion.strip() == "~pvq":
        columnas.append(proposicion)
        return 11,columnas
    elif proposicion.strip() == '~p^q':
        columnas.append(proposicion)
        return 12,columnas
    elif proposicion.strip() == '~p>q':
        columnas.append(proposicion)
        return 13,columnas
    elif proposicion.strip() == '~pxorq':
        columnas.append(proposicion)
        return 14,columnas
    elif proposicion.strip() == '~p<>q':
        columnas.append(proposicion)
        return 15,columnas
    if proposicion.strip() == "pv~q":
        columnas.append(proposicion)
        return 21,columnas
    elif proposicion.strip() == 'p^~q':
        columnas.append(proposicion)
        return 22,columnas
    elif proposicion.strip() == 'p>~q':
        columnas.append(proposicion)
        return 23,columnas
    elif proposicion.strip() == 'pxor~q':
        columnas.append(proposicion)
        return 24,columnas
    elif proposicion.strip() == 'p<>~q':
        columnas.append(proposicion)
        return 25,columnas
    if proposicion.strip() == "~pv~q":
        columnas.append(proposicion)
        return 31,columnas
    elif proposicion.strip() == '~p^~q':
        columnas.append(proposicion)
        return 32,columnas
    elif proposicion.strip() == '~p>~q':
        columnas.append(proposicion)
        return 33,columnas
    elif proposicion.strip() == '~pxor~q':
        columnas.append(proposicion)
        return 34,columnas
    elif proposicion.strip() == '~p<>~q':
        columnas.append(proposicion)
        return 35,columnas
    if proposicion.strip() == 'pvqvr':
        columnas.append(proposicion)
        return 41,columnas
    elif proposicion.strip() == 'pvq^r':
        columnas.append(proposicion)
        return 42,columnas
    elif proposicion.strip() == 'pvq>r':
        columnas.append(proposicion)
        return 43,columnas
    elif proposicion.strip() == 'pvqxorr':
        columnas.append(proposicion)
        return 44,columnas
    elif proposicion.strip() == 'pvq<>r':
        columnas.append(proposicion)
        return 45,columnas
    if proposicion.strip() == 'p^qvr':
        columnas.append(proposicion)
        return 51,columnas
    elif proposicion.strip() == 'p^q^r':
        columnas.append(proposicion)
        return 52,columnas
    elif proposicion.strip() == 'p^q>r':
        columnas.append(proposicion)
        return 53,columnas
    elif proposicion.strip() == 'p^qxorr':
        columnas.append(proposicion)
        return 54,columnas
    elif proposicion.strip() == 'p^q<>r':
        columnas.append(proposicion)
        return 55,columnas
    if proposicion.strip() == 'p>qvr':
        columnas.append(proposicion)
        return 61,columnas
    elif proposicion.strip() == 'p>q^r':
        columnas.append(proposicion)
        return 62,columnas
    elif proposicion.strip() == 'p>q>r':
        columnas.append(proposicion)
        return 63,columnas
    elif proposicion.strip() == 'p>qxorr':
        columnas.append(proposicion)
        return 64,columnas
    elif proposicion.strip() == 'p>q<>r':
        columnas.append(proposicion)
        return 65,columnas
    if proposicion.strip() == 'pxorqvr':
        columnas.append(proposicion)
        return 71,columnas
    elif proposicion.strip() == 'pxorq^r':
        columnas.append(proposicion)
        return 72,columnas
    elif proposicion.strip() == 'pxorq>r':
        columnas.append(proposicion)
        return 73,columnas
    elif proposicion.strip() == 'pxorqxorr':
        columnas.append(proposicion)
        return 74,columnas
    elif proposicion.strip() == 'pxorq<>r':
        columnas.append(proposicion)
        return 75,columnas
    if proposicion.strip() == 'p<>qvr':
        columnas.append(proposicion)
        return 81,columnas
    elif proposicion.strip() == 'p<>q^r':
        columnas.append(proposicion)
        return 82,columnas
    elif proposicion.strip() == 'p<>q>r':
        columnas.append(proposicion)
        return 83,columnas
    elif proposicion.strip() == 'p<>qxorr':
        columnas.append(proposicion)
        return 84,columnas
    elif proposicion.strip() == 'p<>q<>r':
        columnas.append(proposicion)
        return 85,columnas
    if proposicion.strip() == '~pvqvr':
        columnas.append(proposicion)
        return 91,columnas
    elif proposicion.strip() == '~pvq^r':
        columnas.append(proposicion)
        return 92,columnas
    elif proposicion.strip() == '~pvq>r':
        columnas.append(proposicion)
        return 93,columnas
    elif proposicion.strip() == '~pvqxorr':
        columnas.append(proposicion)
        return 94,columnas
    elif proposicion.strip() == '~pvq<>r':
        columnas.append(proposicion)
        return 95,columnas
    if proposicion.strip() == '~p^qvr':
        columnas.append(proposicion)
        return 101,columnas
    elif proposicion.strip() == '~p^q^r':
        columnas.append(proposicion)
        return 102,columnas
    elif proposicion.strip() == '~p^q>r':
        columnas.append(proposicion)
        return 103,columnas
    elif proposicion.strip() == '~p^qxorr':
        columnas.append(proposicion)
        return 104,columnas
    elif proposicion.strip() == '~p^q<>r':
        columnas.append(proposicion)
        return 105,columnas
    if proposicion.strip() == '~p>qvr':
        columnas.append(proposicion)
        return 111,columnas
    elif proposicion.strip() == '~p>q^r':
        columnas.append(proposicion)
        return 112,columnas
    elif proposicion.strip() == '~p>q>r':
        columnas.append(proposicion)
        return 113,columnas
    elif proposicion.strip() == '~p>qxorr':
        columnas.append(proposicion)
        return 114,columnas
    elif proposicion.strip() == '~p>q<>r':
        columnas.append(proposicion)
        return 115,columnas
    if proposicion.strip() == '~pxorqvr':
        columnas.append(proposicion)
        return 121,columnas
    elif proposicion.strip() == '~pxorq^r':
        columnas.append(proposicion)
        return 122,columnas
    elif proposicion.strip() == '~pxorq>r':
        columnas.append(proposicion)
        return 123,columnas
    elif proposicion.strip() == '~pxorqxorr':
        columnas.append(proposicion)
        return 124,columnas
    elif proposicion.strip() == '~pxorq<>r':
        columnas.append(proposicion)
        return 125,columnas
    if proposicion.strip() == '~p<>qvr':
        columnas.append(proposicion)
        return 131,columnas
    elif proposicion.strip() == '~p<>q^r':
        columnas.append(proposicion)
        return 132,columnas
    elif proposicion.strip() == '~p<>q>r':
        columnas.append(proposicion)
        return 133,columnas
    elif proposicion.strip() == '~p<>qxorr':
        columnas.append(proposicion)
        return 134,columnas
    elif proposicion.strip() == '~p<>q<>r':
        columnas.append(proposicion)
        return 135,columnas
    if proposicion.strip() == 'pv~qvr':
        columnas.append(proposicion)
        return 141,columnas
    elif proposicion.strip() == 'pv~q^r':
        columnas.append(proposicion)
        return 142,columnas
    elif proposicion.strip() == 'pv~q>r':
        columnas.append(proposicion)
        return 143,columnas
    elif proposicion.strip() == 'pv~qxorr':
        columnas.append(proposicion)
        return 144,columnas
    elif proposicion.strip() == 'pv~q<>r':
        columnas.append(proposicion)
        return 145,columnas
    if proposicion.strip() == 'p^~qvr':
        columnas.append(proposicion)
        return 151,columnas
    elif proposicion.strip() == 'p^~q^r':
        columnas.append(proposicion)
        return 152,columnas
    elif proposicion.strip() == 'p^~q>r':
        columnas.append(proposicion)
        return 153,columnas
    elif proposicion.strip() == 'p^~qxorr':
        columnas.append(proposicion)
        return 154,columnas
    elif proposicion.strip() == 'p^~q<>r':
        columnas.append(proposicion)
        return 155,columnas
    if proposicion.strip() == 'p>~qvr':
        columnas.append(proposicion)
        return 161,columnas
    elif proposicion.strip() == 'p>~q^r':
        columnas.append(proposicion)
        return 162,columnas
    elif proposicion.strip() == 'p>~q>r':
        columnas.append(proposicion)
        return 163,columnas
    elif proposicion.strip() == 'p>~qxorr':
        columnas.append(proposicion)
        return 164,columnas
    elif proposicion.strip() == 'p>~q<>r':
        columnas.append(proposicion)
        return 165,columnas
    if proposicion.strip() == 'pxor~qvr':
        columnas.append(proposicion)
        return 171,columnas
    elif proposicion.strip() == 'pxor~q^r':
        columnas.append(proposicion)
        return 172,columnas
    elif proposicion.strip() == 'pxor~q>r':
        columnas.append(proposicion)
        return 173,columnas
    elif proposicion.strip() == 'pxor~qxorr':
        columnas.append(proposicion)
        return 174,columnas
    elif proposicion.strip() == 'pxor~q<>r':
        columnas.append(proposicion)
        return 175,columnas
    if proposicion.strip() == 'p<>~qvr':
        columnas.append(proposicion)
        return 181,columnas
    elif proposicion.strip() == 'p<>~q^r':
        columnas.append(proposicion)
        return 182,columnas
    elif proposicion.strip() == 'p<>~q>r':
        columnas.append(proposicion)
        return 183,columnas
    elif proposicion.strip() == 'p<>~qxorr':
        columnas.append(proposicion)
        return 184,columnas
    elif proposicion.strip() == 'p<>~q<>r':
        columnas.append(proposicion)
        return 185,columnas
    if proposicion.strip() == 'pvqv~r':
        columnas.append(proposicion)
        return 191,columnas
    elif proposicion.strip() == 'pvq^~r':
        columnas.append(proposicion)
        return 192,columnas
    elif proposicion.strip() == 'pvq>~r':
        columnas.append(proposicion)
        return 193,columnas
    elif proposicion.strip() == 'pvqxor~r':
        columnas.append(proposicion)
        return 194,columnas
    elif proposicion.strip() == 'pvq<>~r':
        columnas.append(proposicion)
        return 195,columnas
    if proposicion.strip() == 'p^qv~r':
        columnas.append(proposicion)
        return 201,columnas
    elif proposicion.strip() == 'p^q^~r':
        columnas.append(proposicion)
        return 202,columnas
    elif proposicion.strip() == 'p^q>~r':
        columnas.append(proposicion)
        return 203,columnas
    elif proposicion.strip() == 'p^qxor~r':
        columnas.append(proposicion)
        return 204,columnas
    elif proposicion.strip() == 'p^q<>~r':
        columnas.append(proposicion)
        return 205,columnas
    if proposicion.strip() == 'p>qv~r':
        columnas.append(proposicion)
        return 211,columnas
    elif proposicion.strip() == 'p>q^~r':
        columnas.append(proposicion)
        return 212,columnas
    elif proposicion.strip() == 'p>q>~r':
        columnas.append(proposicion)
        return 213,columnas
    elif proposicion.strip() == 'p>qxor~r':
        columnas.append(proposicion)
        return 214,columnas
    elif proposicion.strip() == 'p>q<>~r':
        columnas.append(proposicion)
        return 215,columnas
    if proposicion.strip() == 'pxorqv~r':
        columnas.append(proposicion)
        return 221,columnas
    elif proposicion.strip() == 'pxorq^~r':
        columnas.append(proposicion)
        return 222,columnas
    elif proposicion.strip() == 'pxorq>~r':
        columnas.append(proposicion)
        return 223,columnas
    elif proposicion.strip() == 'pxorqxor~r':
        columnas.append(proposicion)
        return 224,columnas
    elif proposicion.strip() == 'pxorq<>~r':
        columnas.append(proposicion)
        return 225,columnas
    if proposicion.strip() == 'p<>qv~r':
        columnas.append(proposicion)
        return 231,columnas
    elif proposicion.strip() == 'p<>q^~r':
        columnas.append(proposicion)
        return 232,columnas
    elif proposicion.strip() == 'p<>q>~r':
        columnas.append(proposicion)
        return 233,columnas
    elif proposicion.strip() == 'p<>qxor~r':
        columnas.append(proposicion)
        return 234,columnas
    elif proposicion.strip() == 'p<>q<>~r':
        columnas.append(proposicion)
        return 235,columnas
    elif proposicion.strip() == '~pv~qvr':
        columnas.append(proposicion)
        return 241,columnas
    elif proposicion.strip() == '~pv~q^r':
        columnas.append(proposicion)
        return 242,columnas
    elif proposicion.strip() == '~pv~q>r':
        columnas.append(proposicion)
        return 243,columnas
    elif proposicion.strip() == '~pv~qxorr':
        columnas.append(proposicion)
        return 244,columnas
    elif proposicion.strip() == '~pv~q<>r':
        columnas.append(proposicion)
        return 245,columnas
    elif proposicion.strip() == '~p^~qvr':
        columnas.append(proposicion)
        return 251,columnas
    elif proposicion.strip() == '~p^~q^r':
        columnas.append(proposicion)
        return 252,columnas
    elif proposicion.strip() == '~p^~q>r':
        columnas.append(proposicion)
        return 253,columnas
    elif proposicion.strip() == '~p^~qxorr':
        columnas.append(proposicion)
        return 254,columnas
    elif proposicion.strip() == '~p^~q<>r':
        columnas.append(proposicion)
        return 255,columnas
    elif proposicion.strip() == '~p>~qvr':
        columnas.append(proposicion)
        return 261,columnas
    elif proposicion.strip() == '~p>~q^r':
        columnas.append(proposicion)
        return 262,columnas
    elif proposicion.strip() == '~p>~q>r':
        columnas.append(proposicion)
        return 263,columnas
    elif proposicion.strip() == '~p>~qxorr':
        columnas.append(proposicion)
        return 264,columnas
    elif proposicion.strip() == '~p>~q<>r':
        columnas.append(proposicion)
        return 265,columnas
    elif proposicion.strip() == '~pxor~qvr':
        columnas.append(proposicion)
        return 271,columnas
    elif proposicion.strip() == '~pxor~q^r':
        columnas.append(proposicion)
        return 272,columnas
    elif proposicion.strip() == '~pxorq>r':
        columnas.append(proposicion)
        return 273,columnas
    elif proposicion.strip() == '~pxor~qxorr':
        columnas.append(proposicion)
        return 274,columnas
    elif proposicion.strip() == '~pxor~q<>r':
        columnas.append(proposicion)
        return 275,columnas
    if proposicion.strip() == '~p<>~qvr':
        columnas.append(proposicion)
        return 281,columnas
    elif proposicion.strip() == '~p<>~q^r':
        columnas.append(proposicion)
        return 282,columnas
    elif proposicion.strip() == '~p<>~q>r':
        columnas.append(proposicion)
        return 283,columnas
    elif proposicion.strip() == '~p<>~qxorr':
        columnas.append(proposicion)
        return 284,columnas
    elif proposicion.strip() == '~p<>~q<>r':
        columnas.append(proposicion)
        return 285,columnas
    elif proposicion.strip() == 'pv~qv~r':
        columnas.append(proposicion)
        return 291,columnas
    elif proposicion.strip() == 'pv~q^~r':
        columnas.append(proposicion)
        return 292,columnas
    elif proposicion.strip() == 'pv~q>~r':
        columnas.append(proposicion)
        return 293,columnas
    elif proposicion.strip() == 'pv~qxor~r':
        columnas.append(proposicion)
        return 294,columnas
    elif proposicion.strip() == 'pv~q<>~r':
        columnas.append(proposicion)
        return 295,columnas
    if proposicion.strip() == 'p^~qv~r':
        columnas.append(proposicion)
        return 301,columnas
    elif proposicion.strip() == 'p^~q^~r':
        columnas.append(proposicion)
        return 302,columnas
    elif proposicion.strip() == 'p^~q>~r':
        columnas.append(proposicion)
        return 303,columnas
    elif proposicion.strip() == 'p^~qxor~r':
        columnas.append(proposicion)
        return 304,columnas
    elif proposicion.strip() == 'p^~q<>~r':
        columnas.append(proposicion)
        return 305,columnas
    elif proposicion.strip() == 'p>~qv~r':
        columnas.append(proposicion)
        return 311,columnas
    elif proposicion.strip() == 'p>~q^~r':
        columnas.append(proposicion)
        return 312,columnas
    elif proposicion.strip() == 'p>~q>~r':
        columnas.append(proposicion)
        return 313,columnas
    elif proposicion.strip() == 'p>~qxor~r':
        columnas.append(proposicion)
        return 314,columnas
    elif proposicion.strip() == 'p>~q<>~r':
        columnas.append(proposicion)
        return 315,columnas
    elif proposicion.strip() == 'pxor~qv~r':
        columnas.append(proposicion)
        return 321,columnas
    elif proposicion.strip() == 'pxor~q^~r':
        columnas.append(proposicion)
        return 322,columnas
    elif proposicion.strip() == 'pxor~q>~r':
        columnas.append(proposicion)
        return 323,columnas
    elif proposicion.strip() == 'pxor~qxor~r':
        columnas.append(proposicion)
        return 324,columnas
    elif proposicion.strip() == 'pxor~q<>~r':
        columnas.append(proposicion)
        return 325,columnas
    elif proposicion.strip() == 'p<>~qv~r':
        columnas.append(proposicion)
        return 331,columnas
    elif proposicion.strip() == 'p<>~q^~r':
        columnas.append(proposicion)
        return 332,columnas
    elif proposicion.strip() == 'p<>~q>~r':
        columnas.append(proposicion)
        return 333,columnas
    elif proposicion.strip() == 'p<>~qxor~r':
        columnas.append(proposicion)
        return 334,columnas
    elif proposicion.strip() == 'p<>~q<>~r':
        columnas.append(proposicion)
        return 335,columnas
    elif proposicion.strip() == '~pvqv~r':
        columnas.append(proposicion)
        return 341,columnas
    elif proposicion.strip() == '~pvq^~r':
        columnas.append(proposicion)
        return 342,columnas
    elif proposicion.strip() == '~pvq>~r':
        columnas.append(proposicion)
        return 343,columnas
    elif proposicion.strip() == '~pvqxor~r':
        columnas.append(proposicion)
        return 344,columnas
    elif proposicion.strip() == '~pvq<>~r':
        columnas.append(proposicion)
        return 345,columnas
    if proposicion.strip() == '~p^qv~r':
        columnas.append(proposicion)
        return 351,columnas
    elif proposicion.strip() == '~p^q^~r':
        columnas.append(proposicion)
        return 352,columnas
    elif proposicion.strip() == '~p^q>~r':
        columnas.append(proposicion)
        return 353,columnas
    elif proposicion.strip() == '~p^qxor~r':
        columnas.append(proposicion)
        return 354,columnas
    elif proposicion.strip() == '~p^q<>~r':
        columnas.append(proposicion)
        return 355,columnas
    if proposicion.strip() == '~p>qv~r':
        columnas.append(proposicion)
        return 361,columnas
    elif proposicion.strip() == '~p>q^~r':
        columnas.append(proposicion)
        return 362,columnas
    elif proposicion.strip() == '~p>q>~r':
        columnas.append(proposicion)
        return 363,columnas
    elif proposicion.strip() == '~p>qxor~r':
        columnas.append(proposicion)
        return 364,columnas
    elif proposicion.strip() == '~p>q<>~r':
        columnas.append(proposicion)
        return 365,columnas
    elif proposicion.strip() == '~pxorqv~r':
        columnas.append(proposicion)
        return 371,columnas
    elif proposicion.strip() == '~pxorq^~r':
        columnas.append(proposicion)
        return 372,columnas
    elif proposicion.strip() == '~pxorq>~r':
        columnas.append(proposicion)
        return 373,columnas
    elif proposicion.strip() == '~pxorqxor~r':
        columnas.append(proposicion)
        return 374,columnas
    elif proposicion.strip() == '~pxorq<>~r':
        columnas.append(proposicion)
        return 375,columnas
    if proposicion.strip() == '~p<>qv~r':
        columnas.append(proposicion)
        return 381,columnas
    elif proposicion.strip() == '~p<>q^~r':
        columnas.append(proposicion)
        return 382,columnas
    elif proposicion.strip() == '~p<>q>~r':
        columnas.append(proposicion)
        return 383,columnas
    elif proposicion.strip() == '~p<>qxor~r':
        columnas.append(proposicion)
        return 384,columnas
    elif proposicion.strip() == '~p<>q<>~r':
        columnas.append(proposicion)
        return 385,columnas
    
def preguntasProposiciones1():
    columnas = ["p"]
    print('Proposiciones disponibles: p')
    print('para una proposicion negativa escribe "~" antes de la letra')
    print('Conectores disponibles: ^, v, >, xor, <>')
    proposicion = input("Escribe que proposicion quieres: ")
    if proposicion.strip() == "~p":
        columnas.append(proposicion)
        return 1,columnas
    elif proposicion.strip() == 'p^p':
        columnas.append(proposicion)
        return 2,columnas
    elif proposicion.strip() == 'p>p':
        columnas.append(proposicion)
        return 3,columnas
    elif proposicion.strip() == 'pxorp':
        columnas.append(proposicion)
        return 4,columnas
    elif proposicion.strip() == 'p<>p':
        columnas.append(proposicion)
        return 5,columnas
    elif proposicion.strip() == 'pvq':
        columnas.append(proposicion)
        return 6,columnas
    elif proposicion.strip() == '~pvp':
        columnas.append(proposicion)
        return 7,columnas
    elif proposicion.strip() == '~p<>p':
        columnas.append(proposicion)
        return 8,columnas
    elif proposicion.strip() == '~p^p':
        columnas.append(proposicion)
        return 9,columnas
    elif proposicion.strip() == '~pxorp':
        columnas.append(proposicion)
        return 10,columnas
    elif proposicion.strip() == '~p>p':
        columnas.append(proposicion)
        return 11,columnas
    elif proposicion.strip() == '~(pvp)':
        columnas.append(proposicion)
        return 12,columnas
    elif proposicion.strip() == '~(p<>p)':
        columnas.append(proposicion)
        return 13,columnas
    elif proposicion.strip() == '~(p^p)':
        columnas.append(proposicion)
        return 14,columnas
    elif proposicion.strip() == '~(pxorp)':
        columnas.append(proposicion)
        return 15,columnas
    elif proposicion.strip() == '~(p>p)':
        columnas.append(proposicion)
        return 16,columnas

def preguntasProposiciones2():
    columnas = ["p","q"]
    print('Proposiciones disponibles: p, q')
    print('para una proposicion negativa escribe "~" antes de la letra')
    print('Conectores disponibles: ^, v, >, xor, <>')
    proposicion = input("Escribe que proposicion quieres: ")
    if proposicion.strip() == "pvq":
        columnas.append(proposicion)
        return 1,columnas
    elif proposicion.strip() == 'p^q':
        columnas.append(proposicion)
        return 2,columnas
    elif proposicion.strip() == 'p>q':
        columnas.append(proposicion)
        return 3,columnas
    elif proposicion.strip() == 'pxorq':
        columnas.append(proposicion)
        return 4,columnas
    elif proposicion.strip() == 'p<>q':
        columnas.append(proposicion)
        return 5,columnas
    if proposicion.strip() == "~pvq":
        columnas.append(proposicion)
        return 11,columnas
    elif proposicion.strip() == '~p^q':
        columnas.append(proposicion)
        return 12,columnas
    elif proposicion.strip() == '~p>q':
        columnas.append(proposicion)
        return 13,columnas
    elif proposicion.strip() == '~pxorq':
        columnas.append(proposicion)
        return 14,columnas
    elif proposicion.strip() == '~p<>q':
        columnas.append(proposicion)
        return 15,columnas
    if proposicion.strip() == "pv~q":
        columnas.append(proposicion)
        return 21,columnas
    elif proposicion.strip() == 'p^~q':
        columnas.append(proposicion)
        return 22,columnas
    elif proposicion.strip() == 'p>~q':
        columnas.append(proposicion)
        return 23,columnas
    elif proposicion.strip() == 'pxor~q':
        columnas.append(proposicion)
        return 24,columnas
    elif proposicion.strip() == 'p<>~q':
        columnas.append(proposicion)
        return 25,columnas
    if proposicion.strip() == "~pv~q":
        columnas.append(proposicion)
        return 31,columnas
    elif proposicion.strip() == '~p^~q':
        columnas.append(proposicion)
        return 32,columnas
    elif proposicion.strip() == '~p>~q':
        columnas.append(proposicion)
        return 33,columnas
    elif proposicion.strip() == '~pxor~q':
        columnas.append(proposicion)
        return 34,columnas
    elif proposicion.strip() == '~p<>~q':
        columnas.append(proposicion)
        return 35,columnas
    
def Tautologia(lista):
    if False in lista:
        print("No es una Tautologia.")
    else:
        print("Es una Tautologia")
            
def Contradiccion(lista):
    if True in lista:
        print("No es una Contradiccion.")
    else:
        print("Es una Contradiccion")

    


