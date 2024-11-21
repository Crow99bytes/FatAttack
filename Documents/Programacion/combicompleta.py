def generar_combinaciones(palabra):
    def generar_permutaciones(prefix, resto):
        if len(resto) == 0:
            # Si no queda nada más por combinar, se añade el prefijo a las combinaciones
            combinaciones.append(prefix)
        else:
            for i in range(len(resto)):
                # Llamada recursiva eliminando el caracter en la posición i y agregándolo al prefijo
                generar_permutaciones(prefix + resto[i], resto[:i] + resto[i+1:])
    
    combinaciones = []
    # Llamamos a la función recursiva para generar las permutaciones de todas las longitudes
    for i in range(1, len(palabra) + 1):
        generar_permutaciones("", palabra)
    
    return combinaciones

# Ejemplo de uso
palabra =input("A")
combinaciones = generar_combinaciones(palabra)

# Imprimir todas las combinaciones posibles
for combinacion in combinaciones:
    print(combinacion)