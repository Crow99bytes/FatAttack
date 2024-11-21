lista = [2,3,4,5,54,45,61,78]
lista_pares = []

""" Función normal. """
for num in lista:
    if num%2==0:
        lista_pares.append(num)

print(lista_pares)

""" Funciones generadoras. """
lista_pares2=[num for num in lista if num % 2 == 0]

# el primer num es como un 'return' y luego hace el bucle.

