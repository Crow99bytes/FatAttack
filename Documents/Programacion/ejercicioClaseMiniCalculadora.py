
a1 = input("Introduce el simbolo de la operación que desees: ")
a2 = int(input("Introduce el valor 1: "))
a3 = int(input("Introduce el valor 2: "))
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


resultado_final= miniCalculadora(a1, a2, a3)

print(resultado_final)
print(f"{a1}{a2}{a3}={resultado_final}")

def menuSelectoroperacion():

    print("Para dividir introduce: '/'")
    print("Para multiplicar introduce: '*'")
    print("Para restar introduce: '-'")
    print("Para sumar introduce: '+'")
    print("Para obtener el modulo introduce: ''")

