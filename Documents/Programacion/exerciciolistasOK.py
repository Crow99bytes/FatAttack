listaUsuario = []

# Esta función permite al usuario añadir valores numéricos a la lista.
def RETORNA_L():
    i = 0
    cant = int(input("¿Cuántos valores desea añadir a la lista? "))  # Pregunta al usuario la cantidad de números que quiere añadir.
    for i in range(cant):
        listaUsuario.append(int(input("Introduce un valor a añadir a la lista: ")))
    return listaUsuario

# Esta función muestra el contenido de la lista en pantalla.
def VER_L():
    print(f"La lista es:\n{listaUsuario}")

# Esta función coge los elementos de la lista y aumenta su valor en 10.
def INC_10(lista):
    for i in range(len(lista)):
        lista[i] += 10
    print(f"La lista añadiéndole 10 a cada valor es: {lista}")
    return lista

# Suma todos los elementos de la lista y devuelve el resultado.
def SUMAR_L():
    num = 0
    suma = 0
    print(f"Estos son los valores que se van a sumar:\n{listaUsuario}")
    for num in listaUsuario:
        suma += num
    return suma

# Esta función clona la lista y devuelve el orden inverso.
def CLONA_L(lista):
    listaNova = []
    i = 0
    valor = 0
    n = (len(listaUsuario))
    for i, valor in enumerate(listaUsuario):
        listaNova.insert(n-n, valor)
        n -= 1
    print(f"La lista ordenada es:\n{listaUsuario}")
    print(f"La lista ordenada al revés es:\n{listaNova}")
    return listaNova

# Función del menú principal que permite al usuario interactuar con el programa.
def Menu(N):
    continuar = True
    contador = 0
    while continuar:
        contador = len(N)
        if contador == 0:
            listaUsuario = RETORNA_L()
        
        print("\nBienvenido al programa.\n\nEstas son las opciones disponibles:\n\n1) Añadir números a la lista.\n2) Ver la lista completa.\n3) Aumentar en 10 el valor de los valores numéricos.\n4) Sumar el valor de todos los elementos de la lista.\n5) Devolver la lista del revés.\n6) Salir del programa.")
        select = int(input("Introduce el número de la función que desees:\n"))
        
        match select:
            case 1:
                listaUsuario = RETORNA_L()
                print(f"La lista completa es:\n{listaUsuario}")
            case 2:
                VER_L()
            case 3:
                INC_10(listaUsuario)
            case 4:
                totalSuma = SUMAR_L()
                print(f"\nLa suma de todos los elementos de la lista es:\n{totalSuma}")
            case 5:
                listaReversa = []
                listaReversa = CLONA_L(listaUsuario)
            case 6:
                continuar = False
                print("Muchas gracias por usar nuestro programa.")
                break
            case _:
                print("Te dije que introdujeses el número. Vuelve a intentarlo.")
                continue

Menu(listaUsuario)
