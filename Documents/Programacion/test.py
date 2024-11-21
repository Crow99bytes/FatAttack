def menuuser():
    print("Bienvenido al super programa de Manu.\nTienes diferentes opciones para escoger:\n1) Sumar números.\n2) Sumar números hasta que tu quieras.\n3) Multiplicar 2 números.\n4) Comprobador número primo.\n5) Escribir n números primos.\n6) N numeros de fibonacci.\n7) Programa saludo user.")
    menu = int(input("Opción: "))


print("Bienvenido al super programa de Manu.\nTienes diferentes opciones para escoger:\n1) Sumar números.\n2) Sumar números hasta que tu quieras.\n3) Multiplicar 2 números.\n4) Comprobador número primo.\n5) Escribir n números primos.\n6) N numeros de fibonacci.\n7) Programa saludo user.")
menu = int(input("Opción: "))

if menu == 1:
    salir = True
    while salir:
        a = int(input("Primer valor: "))
        b = int(input("Segundo valor:"))
        suma = a + b
        print(f"El resultado de sumar {a} y {b} es {suma}")

        # Módulo que pregunta al usuario si desea continuar.
        #####################################################

        continuar = input("¿Quieres seguir sumando? Y/N")
        if continuar.lower() == "s" or continuar.lower() == "y":
            salir = True
        elif continuar.lower() == "n":
            salir = False
        else:
            salir = False
menuuser()

if menu == 2:
    
    print("A")
