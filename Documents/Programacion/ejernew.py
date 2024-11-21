""" 
suma1. Pasaremoslle dous valores enteiros e DEVOLVERÁ o resultado da suma.
suma2. Pasaremoslle dous valores enteiros e VISUALIZARÁ o resultado da suma.
suma3. Pedirá dous valores enteiros e DEVOLVERÁ o resultado da suma.
suma4. Pedirá dous valores enteiros e VISUALIZARÁ o resultado da suma.

"""

def suma1(valor1,valor2):
    print("[SUMA ·1·] esta función retorna un valor. [SUMA ·1·]")
    resultadoSuma1 = valor1 + valor2
    return resultadoSuma1

def suma2(valor1,valor2):
    print("[SUMA 2]Esta función muestra los datos en pantalla que le han sido enviados [SUMA 2]")
    total = valor1+valor2
    print(f"[SUMA 2]la suma(2) DENTRO FUNCIÓN de {valor1} y {valor2} es {total}")

def suma3():
    print("[SUMA ·3·] esta función retorna un valor. [SUMA ·3·]")
    valor1=int(input("[SUMA 3]Introduce el valor 1 : "))
    valor2=int(input("[SUMA 3]Introduce el valor 2: "))
    resultadoSuma3 = valor1 + valor2

    return resultadoSuma3

def suma4():
    print("Esta función muestra los datos en pantalla que ha solicitado [SUMA 4]")
    valor1=int(input("[SUMA 4]Introduce el valor 1: "))
    valor2=int(input("[SUMA 4]Introduce el valor 2: "))
    total = valor1+valor2
    print(f"la suma(4) DENTRO FUNCIÓN de {valor1} y {valor2} es {total}")
    print(valor1 + valor2)

# Hay que darle datos:
num1 = int(input("[SUMA 1/2]Introduce el primer valor: "))
num2 = int(input("[SUMA 1/2]Introduce el segundo valor: "))
resultadosuma1 = suma1(num1, num2)
resultadosuma3 = suma3()

print(f" [SUMA 1]El resultado de la SUMA 1 es:  {resultadosuma1}")
print(f"[SUMA 3]El resultado de la SUMA  3 es: {resultadosuma3}")

# Pide los datos:

suma3()
suma4()
