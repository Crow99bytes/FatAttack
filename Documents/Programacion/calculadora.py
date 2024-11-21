
msg_salida=("\nGracias por usar nuestros servicios.\nFinalizando programa.")
salir=True
# Sumas
def Suma2Valores():
    salir = False
    # Es el módulo que realiza la suma de dos números
    while salir:
        a = int(input("Primer valor: "))
        b = int(input("Segundo valor: "))
        suma = a + b
        print(f"El resultado de sumar {a} y {b} es {suma}")

        # Este es un módulo que pregunta al user si quiere seguir o no y realiza la acción.
        continuar = input("Quieres seguir sumando? Y/N: ")
        if continuar.lower() == "n":
            salir = False
        elif continuar.lower() == "y":
            salir = True
        else:
            print("No sé como has llegado a este error.\nEnhorabuena por liarla, volviendo al menú principal.")

def SumaContinua():
    salir=True
    suma = 0
    # Este módulo suma cifras hasta que el usuario introduzca el número 0.
    while salir: # while salir = mientras salir sea Verdader, hace el bucle.
        num = int(input("Introduce valores a sumar: (introduce un 0 para salir)"))
        if num == 0:
            salir = False
        else:
            suma = suma + num
            print(f"La suma va en {suma}")
    print(f"La suma se ha quedado en {suma}{msg_salida}")

# Multiplicas 2 valores
def MultiplicacionDosNumeros():
    salir=True
    while salir:
        a = int(input("Primer valor: "))
        b = int(input("Segundo valor: "))
        multipl = a * b
        print(f"El resultado de sumar {a} y {b} es {multipl}")

        # Modulo pregunta salida.
        continuar = input("Quieres seguir sumando? Y/N: ")
        if continuar.lower() == "n":
            salir = False
        elif continuar.lower() == "y":
            salir = True
        else:
            print("No sé como has llegado a este error.\nEnhorabuena por liarla, volviendo al menú principal.")
    print(f"{msg_salida}")


# Números primos
def ComprobarNumerosPrimos():
    salir = True
    print("Bienvenido a nuestra calculadora de números primos.")
    
    while salir:
        primo = int(input("Introduce un número: "))

        if primo < 2:
            print(f"El número {primo} no es primo.")
        else:
            es_primo = True
            for i in range(2, primo):
                if primo % i == 0:
                    es_primo = False
                    break

        if es_primo:
            print(f"El número {primo} es primo.")
        else:
            print(f"El número {primo} NO es primo.")

        # Módulo para salir.
        continuar = input("Quieres seguir sumando? Y/N: ")
        if continuar.lower() == "n":
            salir = False
        elif continuar.lower() == "y":
            salir = True
        else:
            print("No sé como has llegado a este error.\nEnhorabuena por liarla, volviendo al menú principal.")
    print(f"{msg_salida}")

# Función para ver si es primo (para el printer de primo, solo sirve para se llamado por PrinterPrimos())
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def PrinterPrimos():
    cantidad = int(input("¿Cuantos números primos quieres solicitar? (se generan de menor a mayor)"))
    primos = []  # Lista para almacenar los números primos encontrados
    num = 2  # Empezamos comprobando desde el número 2
    while len(primos) < cantidad:  # Continuar hasta que tengamos 'n' primos
        if es_primo(num):  # Comprobamos si el número actual es primo
            primos.append(num)  # Si es primo, lo añadimos a la lista, al final de todo.
        num += 1  # Pasamos al siguiente número
    print(f"Los primeros {cantidad} números son: {primos}")

# Da N números de la serie fibonacci
def NcantFibo():
    cantidad = int(input("¿Cuantos números de la serie quieres? (se generan de menor a mayor)"))
    fibo = [0, 1]
    
    while len(fibo) < cantidad:
        siguiente_numero = fibo[-1] + fibo[-2]
        fibo.append(siguiente_numero)
    return fibo



PrinterPrimos()
