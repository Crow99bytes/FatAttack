# Definimos las funciones que actuarán como operadores matemáticos básicos

# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar el segundo número del primero
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir el primer número por el segundo, si es posible
def dividir(a, b):
    # Comprobamos que no estamos dividiendo entre cero y que la división no tiene residuo (división exacta)
    if b != 0 and a % b == 0:
        return a // b  # Devolvemos el resultado entero de la división
    return None  # Si la división no es posible, devolvemos None

# Función para elevar el primer número al valor del segundo
def elevar(a, b):
    return a ** b

# Lista que contiene todas las funciones anteriores para usarlas fácilmente
operadores = [sumar, restar, multiplicar, dividir, elevar]

# Lista que contiene los nombres de los operadores en forma de símbolos
nombres_operadores = ['+', '-', '*', '/', '^']

# Lista de números disponibles para usar en nuestras operaciones
numeros_disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]

# Pedimos al usuario que ingrese el número objetivo que desea obtener mediante operaciones
objetivo = int(input("Ingresa el número objetivo: "))

# Función que busca una combinación de operaciones y números que nos lleve al número objetivo
def encontrar_combinacion():
    # Primero calculamos la cantidad de números disponibles para usarlos en los bucles
    n = len(numeros_disponibles)
    
    # Generamos todas las permutaciones posibles de tres números diferentes
    for i in range(n):  # Primer número
        for j in range(n):  # Segundo número
            for k in range(n):  # Tercer número
                
                
                # Asignamos los valores seleccionados a, b y c
                a, b, c = numeros_disponibles[i], numeros_disponibles[j], numeros_disponibles[k]
                
                # Probamos todas las combinaciones posibles de dos operadores
                for op1 in range(len(operadores)):  # Primer operador
                    for op2 in range(len(operadores)):  # Segundo operador
                        
                        # Aplicamos el primer operador a los dos primeros números
                        resultado_1 = operadores[op1](a, b)
                        
                        # Verificamos si el resultado de la primera operación es válido (no None)
                        if resultado_1 is not None:
                            # Aplicamos el segundo operador al resultado de la primera operación y al tercer número
                            resultado_2 = operadores[op2](resultado_1, c)
                            
                            # Si el resultado de la segunda operación es igual al objetivo, devolvemos la combinación
                            if resultado_2 is not None and resultado_2 == objetivo:
                                # Devolvemos la combinación encontrada en forma de una cadena para mostrar al usuario
                                return f"({a} {nombres_operadores[op1]} {b}) {nombres_operadores[op2]} {c} = {objetivo}"

    # Si no encontramos ninguna combinación, devolvemos un mensaje indicándolo
    return "No se encontró ninguna combinación"

# Llamamos a la función para encontrar una combinación y almacenamos el resultado
resultado = encontrar_combinacion()

# Mostramos el resultado al usuario
print(resultado)
