""" 
Facede un programa que faga o seguinte cunha lista de enteiros (3 números):

    1. Mediante unha función RETORNA_L: a función pedirá os valores ó usuario, os gardará
    nunha lista e retornará a lista.

    2. Mediante a función VER_L: a cal lle pasamos unha lista de enteiros e os visualizara por
    pantalla.

    3. Mediante a función INC_10: Pasaremoslle unha lista e a función incrementará en 10
    unidades cada unha das posicións da lista.

    4. Mediante a función SUMAR_L: a función sumará todas os elementos da lista e devolverá a
    suma de todo (sin empregar a función sum).

    5. Mediante a función CLONA_L: Pasaremoslle unha lista e retornará unha copia desa mesma
    lista en orde inverso.

    Para comprobar si funcionan ben as funcións anteriores sempre despois de cada opción
    amosaremos o contido da lista.

"""

listaExercicioPredeterminada = [71, 427, 3371]
def RETORNA_L():
    listaUsuario1 = []

    i=0
    cant = int(input("Cuantos valores quieres añadir a la lista?????????? "))
    for i in range(cant):
        listaUsuario1.append(int(input("Introduce un valor a añadir a la lista: ")))
    
    return listaUsuario1

def VER_L(num):
    print(num)

def INC_10(A):
    listaPredeterminadaMas10=[]
    num = 0
    print(f"La lista original es:\n{listaExercicioPredeterminada}")
    for num in A:
        num10 = num
        num10 = num10 + 10
        listaPredeterminadaMas10.append(num10)
    print(f"La lista añadiendole 10 a cada valor es de\n{listaPredeterminadaMas10}")

def SUMAR_L():
    num = 0
    suma = 0
    print(f"Se va a realizar toda la suma de los valores en esta lista:\n{listaExercicioPredeterminada}")
    for num in listaExercicioPredeterminada:
        suma = suma + num

    return suma

def CLONA_L(B):
   # Esta es la manera usando las funciones de Python.
    """print(f"La lista es:\n{listaExercicioPredeterminada}")
    listaExercicioPredeterminada.reverse()
    print(f"La lista del revés es:\n{listaExercicioPredeterminada}")"""


    # Esta es la manera sin usar las funciones de Python (para ordenarlo del revés, si se usará len(lista))
    listaNova = []
    i=0
    valor = 0
    n = (len(listaExercicioPredeterminada)) # Recogemos el valor máximo de la lista.
    for i, valor in enumerate(listaExercicioPredeterminada): # Esto va dando 
        
        listaNova.insert(n-n, valor) #insertamos los datos con números negativos, siendo -1 el equivalente al 0 (primera posición) y siendo -n(cantidad de números de la lista en negativo la última posición.)
        n-=1

    print(f"La lista ordenada es:\n{listaExercicioPredeterminada}") # imprimimos la lista original para visualizarla
    print(f"La lista ordenada al revés es:\n{listaNova}") # imprimimos la lista nueva.
    return listaNova

""" returnL = RETORNA_L()
print(f"La lista de RETORNA_L es:\n{returnL}") """
""" 
INC_10(listaExercicioPredeterminada) """

""" VER_L(listaExercicioPredeterminada)

returnSumarL = SUMAR_L()
print(f"El retorno de SUMAR_L es:\n{returnSumarL}") """

listaNovaFora = []
listaNovaFora = CLONA_L(listaExercicioPredeterminada)

print(listaNovaFora)