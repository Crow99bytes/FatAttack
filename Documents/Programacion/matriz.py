# Función que cuente el número de elementos de una matriz que le pasamos.

def contadorMatrices(n):
    cont = 0
    for i in range(len(n)):
        for j in range(len(n[i])):
            cont += 1
    return cont

def genMatriz():
    introMatriz = []
    matriz = []
    cant = 0
    seguir = True
    while seguir == True:
        introMatriz.clear()
        cant = int(input("Introduce la cantidad de números a añadir en esta fila: "))
        while len(introMatriz)<cant:
            introMatriz.append(int(input("Introduce un elemento a añadir a la matriz: ")))
        matriz.append(introMatriz)
        
        opcion = input("Desea seguir? S|N ")
        if opcion == "n" or opcion == "N":
            break
        elif opcion == "s" or opcion == "S":
            print("Volver a añadir.")

        else: 
            break
    return introMatriz

matrizFuera = []
matrizFuera = genMatriz()

cantidad = contadorMatrices(matrizFuera)
print(cantidad)