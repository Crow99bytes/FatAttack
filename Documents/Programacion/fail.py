def menuOperaciones():

    print("Para dividir introduce: '/'\nPara multiplicar introduce: '*'\nPara restar introduce: '-'\nPara sumar introduce: '+'\nPara obtener el modulo introduce: '%'")
    operacion = input("Introduce el simbolo de la operación que desees: ")
    n1 = int(input("Introduce un valor: "))
    n2 = int(input("Introduce otro valor:"))
    resultado_final = miniCalculadora(operacion, n1, n2)
    print(resultado_final)
    print(f"La operación {n1}{operacion}{n2} es igual a {resultado_final}")

def miniCalculadora(operacion, num1, num2):
    
    match operacion:

        case "/":
            resultado = num1/num2
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

menuOperaciones()