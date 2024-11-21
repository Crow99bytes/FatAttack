
#añadir muchos valores a una lista de variables desde un solo input. el '.split()' divide los valores introducidos separacdos según lo que esté entre parentesis.

num1, num2, num3 = input("Introduce 3 valores: ").split()

""" num1=int(input("Escribe un número: "))
num2=int(input("Escribe un número: "))
num3=int(input("Escribe un número: ")) """

#versión 1.0 (alumno)
""" if num1==num2 and num1==num3:#<------------Caso de que los 3 números indicados por el usuario sean iguales.
    print("Los números son iguales")
elif num1>num2 and num1>num3:#<------------Caso de que el 1 sea el mayor.
    print(f"El numero {num1} é o mayor.")
elif num2>num3:#<--------------------------Caso de que el número 2 sea el mayor.
    print(f"El número {num2} é o mayor")
else:#<------------------------------------Caso de que el tercer valor sea el mayor
    print(f"El número {num3} é o mayor.")

 """

#versión 2.0 (corrección) 
#python permite comparar entre si varios numeros

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1>=num2 and num1>=num3:             # if (0>num<34) para que solo muestre lo del medio

    print(f"El numero {num1} é o mayor.")
elif num2>=num3:
    print(f"El número {num2} é o mayor")
else:
    print(f"El número {num3} é o mayor.")

    