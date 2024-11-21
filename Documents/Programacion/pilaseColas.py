lista = [1,4,5,4,6,41,5,54,4,4,654,11,1,61,11,414,44]

def VER_COLA_FILA():
    print(f"La cola actualmente es:\n{lista}")

def INSERTAR_FILA():
    insertado = int(input("Introduce un valor a añadir -----> "))
    lista.append(insertado)
    print(f"La lista actualmente consta de:\n{lista}")

def EXTRAER_FILA():
    lista.pop(0)
    print(f"La lista ahora mismo es:\n{lista}")

def menu_FILA():
    seguir = True
    while seguir:
        print(f"Bienvenido al programa extraño este.\n1) Ver cola.\n2) Insertar.\n3) Extraer.\n4) Salir al menú principal.")
        opcion = int(input("Selecciona una opción."))

        match opcion:

            case 1:
                VER_COLA_FILA()
            case 2:
                INSERTAR_FILA()
            case 3:
                EXTRAER_FILA()
            case 4:
                seguir = False
            case _:
                continue

def VER_COLA_PILA():
    print(f"La cola actualmente es:\n{lista}")

def INSERTAR_PILA():
    prox = int(input("Introduce el valor a añadir: "))
    lista.append(prox)
    print(f"La lista tras añadir ese valor es:\n{lista}")

def EXTRAER_PILA():
    n = (len(lista)-1)
    lista.pop(n)
    print(f"La lista tras extraer el último valor añadido es:\n{lista}")

def menu_PILA():
    seguir = True
    while seguir:
        print(f"Bienvenido al programa extraño este.\n1) Ver cola.\n2) Insertar.\n3) Extraer.\n4) Salir al menú principal.")
        opcion = int(input("Selecciona una opción."))

        match opcion:

            case 1:
                VER_COLA_PILA()
            case 2:
                INSERTAR_PILA()
            case 3:
                EXTRAER_PILA()
            case 4:
                seguir = False
            case _:
                continue

def menuPrincipal():
    seguir = True
    while seguir:
        print("Estas son las opciones a escoger:\n1) Ejercicio Fila.\n2) Ejercicio Pila.\n3) Finalizar programa.")
        opcionprincipal = int(input("Escoge la función: "))

        match opcionprincipal:
            case 1:
                menu_FILA()
            case 2:
                menu_PILA()
            case 3:
                seguir = False
            case _:
                seguir = False
menuPrincipal() 