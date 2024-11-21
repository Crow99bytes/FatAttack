def menuOperaciones():

    print("Para dividir introduce: '/'\nPara multiplicar introduce: '*'\nPara restar introduce: '-'\nPara sumar introduce: '+'\nPara obtener el modulo introduce: '%'")
    operacion = input("Introduce el simbolo de la operación que desees: ")
    n1 = int(input("Introduce el valor 1: "))
    n2 = int(input("Introduce el valor 2: "))
    resultado_final = miniCalculadora(operacion, n1, n2)
    print(resultado_final)
    print(f"La operación {n1}{operacion}{n2} es igual a {resultado_final}")

def miniCalculadora(operacion, num1, num2):
    
    match operacion:

        case "/":
            if num2 != 0:
                resultado = num1/num2
            else:
                print("No se puede dividir entre 0")
        case "*":
            resultado = num1*num2
        case "-":
            resultado = num1-num2
        case "+":
            resultado = num1+num2
        case "%":
            resultado = num1%num2
        case _:
            print("error")
    return resultado

lista_divisores = ["/","*","+","-","%"]
operacion = input("Introduce el simbolo de la operación que desees: ")
i=1
while i<2:
    operacion = input("Introduce el simbolo de la operación que desees: ")
    if operacion in lista_divisores:
        print("Si.") 
# La lista de los valores que solo puede introducir funciona