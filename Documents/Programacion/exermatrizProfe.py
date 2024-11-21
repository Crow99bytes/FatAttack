def Pedir():
    matriz = []
    for i in range(2):
        lista = []
        for _ in range(3):
            lista.append(int(input("Valor: ")))
        matriz.append(lista)

    return matriz



# Esta función recorre todos los valores de una lista y almacena el mayor de todos.
def Maior(Matriz):
    maior = Matriz[0][0]
    for fila in Matriz:
        for valor in fila:
            if valor > maior:
                maior = valor
    return maior

def maiorUnBucle(matriz):
    maior = max(matriz[0]) # Pilla el valor más alto de la primera fila
    for fila in matriz: # Pasa por todas las filas
        if maior < max(fila): # Si o maior e menor que o max de la fila actual lo actualiza
            maior = max(fila)

    return maior

n=Pedir()
print(Maior(n))


# Ejercicio de 0 y 1.

def Matriz_binaria(Matriz):
    binaria = []
    l_temp = []
    for fila in Matriz:
        for valor in fila:
            if valor % 2 == 0:
                l_temp.append(0)
            else:
                l_temp.append(1)
        binaria.append(l_temp)
                
    return maior
