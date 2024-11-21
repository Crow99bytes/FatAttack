def numplusnum():
    keepgoing = True
    while keepgoing:

        num1 = int(input("Introduce el primer valor: \n"))
        num2 = int(input("Introduce el segundo valor: \n"))

        suma = num1 + num2

        print(f"El resultado de sumar {num1} y {num2} es {suma}")

        seguir = input("Quieres seguir? Y/N")

        if seguir == "y" or seguir == "Y" or seguir == "s" or seguir == "S":
            keepgoing = True
        elif seguir == "n" or seguir == "N":
            keepgoing = False
        else:
            print("Claro que sí, escribe lo que tu quieras.")
            keepgoing = False


def plusinfinitesum():

    while 