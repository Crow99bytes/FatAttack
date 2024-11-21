""" Función que lle pida ó usuario os datos (números) para gardalos nunha matriz de 2 filas e
tres columnas. Dita función devolverá a matriz creada.
• Función que pasandolle unha matriz, devolva a suma de todos os elementos da matriz.
• Función que pasandolle unha matriz a visualice en formato matriz.
• Función que devolva o valor maior de todos os elementos da matriz.
• Función que devolva unha lista con todos os elementos <0 que conteña a matriz.
• Función que pasandolle unha matriz, devolva outra matriz onde os valores pares da orixinal
se sustituiran por un 0 e os impares por un 1. """

def AskUser():
    matriz = []
    lista = []
    ncol = 3
    nfil = 2
    for j in range(nfil):
        lista.clear()
        i=0
        for i in range(ncol):
            lista.append(int(input("Introduce valores: ")))
        matriz.append(lista.copy())
       
    return matriz

def sumAllNumbersMatriz(coso):
    totalSuma = 0
    for i in range(len(coso)):
        for j in coso[i]:
            totalSuma += j

    return totalSuma

def ImpresoraTOWapadeMAtrices(matriz):
    lista1= []
    for k in range(len(matriz)):
        lista1.clear()
        for l in matriz[k]:
            lista1.append(l)
        print(lista1)

def CalEoMaIor(os_cartinhos):
    maxi = 0
    for k in range(len(os_cartinhos)):
        for l in os_cartinhos[k]:
            if maxi < l:
                maxi = l
    
    return maxi

def listaBajoSero(contratos):
    LasQueLeGustanADAllas = []
    for k in range(len(contratos)):
        for l in contratos[k]:
            if l < 0:
                LasQueLeGustanADAllas.append(l)  


    return LasQueLeGustanADAllas    


def BinarioTypeTHing(lereles):
    matrizSecundaria = []
    matrizfinal=[]
    for k in range(len(lereles)):
        matrizSecundaria.clear()
        for l in lereles[k]:
            if l % 2 == 0:
                matrizSecundaria.append(0)
            else:
                matrizSecundaria.append(1)
        matrizfinal.append(matrizSecundaria.copy())
    return matrizfinal
               




matrizOutside = AskUser()
# print(f"Esta es la matriz!{matrizOutside}")
# totalOutside = sumAllNumbersMatriz(matrizOutside)
# ImpresoraTOWapadeMAtrices(matrizOutside)
# maximoAugustoRomero = CalEoMaIor(matrizOutside)
# print(f"El valor más alto es: {maximoAugustoRomero}")
# Pambis = []
# Pambis = listaBajoSero(matrizOutside)
# print(Pambis)
binance = BinarioTypeTHing(matrizOutside)
print(f"La matriz original es: {matrizOutside}")
print(f"La matriz modificada a 0 y 1 es: {binance}")