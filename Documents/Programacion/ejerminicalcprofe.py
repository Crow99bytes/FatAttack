def calculadora(operacion, oper1, oper2):
    
    # Aquí ya se tiene que haber introducido desde otra parte el operante y los 2 numeros.

    match operacion:

        case '+':
            resultado = oper1 + oper2
        case '-':
            resultado = oper1 - oper2
        case '*':
            resultado = oper1 * oper2
        case '/':
            if oper2!=0:                                # <---| Si el número no es 0 deja pasara a la división. NO SE PUEDE DIVIDIR ENTRE 0. |-------------------------->
                resultado= oper1 / oper2
            else:
                resultado = "El divisor no puede ser 0" #<----| Envía la cadena de texto como resultado. |------------------------>

    return resultado


def menu():
    operacions = ["+","-","*","/"]
    opcion='€'
    while opcion not in operacions: # <-----------------------| Mientras lo que mete el usuario no es uno de los valores validos (lista) repite la pregunta.
        print("Sumar +\nRestar -\nMultiplicar\nDividir /")
        opcion = input("escolla unha opción")

    return opcion

operacion = menu()
num1 = int(input("Introduce el primer valor: "))
num2 = int(input("Introduce el segundo valor: "))

result=calculadora(operacion,num1,num2) # <-------------------| Recogemos el resultado de calculadora() en el 'result' |------------------------->

if type(result)==str: # Si el tipo del resultado es la cadena de texto que le pusimos al caso de dividir entre 0, imprime la cadena. Si no 'operaría' con la cadena 7/0={cadena str}
    print(result)
else:
    print(f"O resultado de {num1}{operacion}{num2}={result}")