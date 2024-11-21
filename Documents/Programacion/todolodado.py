
# ¿Qué hace este código?

# Suma de números desde 1 hasta N

# Versión alumno
def sumadesde1hastaNnumero():
    num = int(input("Introduce un número:\n"))

    i = 1
    suma = 0
    while i <= num:
        suma = suma + i
        i+=1
    print(f"El resultado es {suma}")

# Versión profe
def suma1aNprofe(): # Suma de números desde 1 hasta N

    num = int(input("Introduce un número: "))

    suma = 0
    for i in range(1,num+1):
        suma+=i             # suma = suma + i

    print(f"A suma dende 1 ata {num} e: {suma}")


""" #********************************************************************************************************** """
# ¿Qué hace este código?
# Ver si es positivo o negativo y acumular cuantos hay de positivos y negativos

def intronumposiynega(): 

    num = int(input("introduce un número: (0 para saír)\n"))
    cont_negativos = 0
    cont_positivos = 0
    while num != 0:
        
        if num < 0:
            cont_negativos+=1
            print(f"El número {num} é negativo")
        else:
            cont_positivos+=1
            print(f"El número {num} é positivo.")

        num = int(input("introduce un número: (0 para saír)\n")) # Sin esto sería un bucle infinito.
    
    print(f"Hai {cont_negativos} negativos e {cont_positivos} positivos.")

""" #*********************************************************************************************************** """
# ¿Qué hace este código?

# Este código comprueba si un número es o no primo.

# Versión alumno
def testprimo():
    num = int(input("introduce un número:\n"))

    if num < 2:
        print(f"El número no es primo")

    else:
        primo = True
        for i in range(2, num-1):
            if num % i == 0:
                primo = False
                break

        if primo:
            print(f"El número {num} es primo.")
        else:
            print(f"El número {num} NO es primo.")

# Versión profesor.
def testprimotutor():

    num = int(input("Introduce un número: "))

    primo = True
    for divisor in range(2,num-1):
        if num % divisor == 0:
            primo = False
            break

    if primo:
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} NO es primo.")


# Versión profesor preguntando en bucle números hasta que quiera el usuario.
def testprimotutorvariosnumeros():

    resp = 'S'
    while resp == 'S' or resp == 's':
        num = int(input("Introduce un número: (0 para salir)"))
        primo = True
        for divisor in range(2,num-1):
            if num % divisor == 0:
                primo = False
                break

        if primo:
            print(f"El número {num} es primo.")
        else:
            print(f"El número {num} NO es primo.")

        resp = input("Que si quiere bolsa? (s/n)")

    print("Fin del programa.")

""" #*********************************************************************************** """

# Explicación del "comando" 'continue'.

def continueExplicacion():

    i = 0
    while i <= 5:
        i += 1
        if i == 3:
            """ break # en este caso para por completo el bucle al llegar al 3. """
            continue # Esto hace que sólo se salte este supuesto, no muestra la vuelta
                     # vuelta del bucle, y se va directamente a comenzar el bucle.
                     # se salta todo lo de debajo en esta vuelta, ojo con poner el aumento
                     # de 'i' debajo, por que haría un bucle infinito, por que no llegaría al
                     # incremento.
        print(f"o número é {i}")


""" #************************************************************************************ """

# Listas de Python

# ejemplo 1:
def listaPythonEjemplosElementoAElemento():

    empty_list = []

    for valor in range(100,105): # Añade valores de 100 a 104 a la lista y los imprime en el print 'lista completa:'
        empty_list.append(valor)

    for valor_individual in empty_list: # mostrar cada uno de los valores de la lista uno por uno.
        print(f"o valor da lista é {valor_individual}")


    for clave, valor in enumerate(empty_list): # Enumera los numeros de la lista 'enumerate(lista que quieras)'
        print(f"En la posición {clave} o valor da lista é {valor}")

    print(f"Lista completa: {empty_list}")

    print(f"A suma de todos los valores de la lista es {sum(empty_list)}") #suma de valores de la lista


""" #************************************************************************************ """

# Ejercicio 1: Almacena n valores en una lísta, busca en la lista si hay algo concreto, y si está devuelve ese algo y su posición.

# Solución alumno:

def ejerUnoAlumno():
    lista_de_cosas = []

    i=0
    while i < 5:
        word = input("Introduce una palabra:")
        lista_de_cosas.append(word)
        i+=1
    
    print("La lista es:\n")
    for i in lista_de_cosas:
        print(i)

    comprobar = input("Que elemento quiere comprobar si está en la lista?\n")

    # Comprobar si está en la lista.
    itis = False
    for posicion, i in enumerate(lista_de_cosas):
        if i == comprobar:
            itis = True
            break

    if itis:
        print(f"El elemento {i} está en la lista en la posición {posicion}")
    else:
        print(f"El elemento {i} NO está en la lista")


ejerUnoAlumno()






# Versión profe.
def ejerUnoV1Profe():

    lista = []
    for cont in range (3):

        lista.append(input("Introduce un valor: \n"))
    
    for valor in lista:

        print(f"Na posición {lista.index(valor)} da lista temos: {valor}")


  
    num_buscar = input("Introduce el valor a buscar: ")


    if  num_buscar in lista:
        print(f"O {num_buscar} atopase na posición {lista.index(num_buscar)}")
    
"""   print(type.lista) # esto muestra el tipo de elemento que es 'lista' """

# Versión profesor ejercicio 1 V2.

def ejerUnoTutorV2(): 


    lista = []
    for cont in range (3):

        lista.append(input("Introduce un valor: \n"))
    
    for valor in lista:

        print(f"Na posición {lista.index(valor)} da lista temos: {valor}")


  
    num_buscar = input("Introduce el valor a buscar: ")


    pos=-1
    for valor in lista:
        if valor == num_buscar:
            pos = lista.index(valor)
            break

    if pos >=0:
        print(f"o {num_buscar} atopase na posición {pos}")
    else:
        print("no está na lista.")



def solucionProfesorEjeruno():
    lista = []
    for cont in range (5):

        lista.append(input("Introduce un valor: \n"))
    
    for valor in lista:

        print(f"Na posición {lista.index(valor)} da lista temos: {valor}")


  
    num_buscar = input("Introduce el valor a buscar: ")
    
    # nueva explicación lista indices. Lista dentro de una lista.
    lista_indices = []
   
    for clave, valor in enumerate(lista): # aqui tambien hay cambio. clave= 0 valor= 'Hola'
        if valor == num_buscar:
            lista_indices.append(clave) # Aquí está el cambio guarda las posiciones de lo que buscamos con el num_buscar.
            

    if len(lista_indices) > 0: # otra opción es len(lista_indices) > 0
        print(f"os índices son: {lista_indices}")
    else:
        print("no está na lista.")




""" *************************************************************************************** """

# ejercicio 2: 
# pedirle 5 números al usuario.
# Hacer la suma de todo
# ver que número es el mayor
# ver que número es el menor.


def valores5sumaminmax():
    lista = []
    for i in range(5):
        lista.append(int(input("Introduce un número: ")))

    suma = 0
    max = lista[0] # hace que el valor de max sea el del primer número metido.
    min = lista[len(lista)-1]  # len de la lista - 1 da el último posición de valores

    for valor in lista: #saca uno a uno los valores de la lista
        if valor > max:
            max = valor
        if valor < min:
            min = valor
        suma+=valor

    print(f"A suma é {suma} o nim é {min} e o max é {max}")


""" Trabajo 1 de programación. Funciones. """
lista_completa = []
def menuPrincipal():
        
        print("\nMenú de opciones: ")
        print("         1) Insertar valores en la lista.")
        print("         2) Insertar valores en posiciones concretas de la lista.")
        print("         3) Visualizar la lista.")
        print("         4) Buscar un elemento en la lista y comprobar si está o no.")
        print("         5) Eliminar un elemento existente de la lista.")
        print("         6) Ordena al revés la lista.")
        print("         7) Devolver el último valor de la lista y borrarlo.")
        print("         8) Modificar valores repetidos por el valor que el usuario quiera.")
        print("         9) Salir.")

        selector = int(input("\nIntroduce el número de la opción que desees: "))
        return selector

def TestIfTheresNumberInListAndAddIFnot():

        if len(lista_completa) < 1:
                lista_completa.append(input("Introduce los números o valores que desees añadir a la lista: "))

        elif len(lista_completa) > 0:
                print(f"Ya existen datos en la lista.")
                print(lista_completa)
                datoBorrarONo = input("¿Desea eliminar los datos almacenados? S|N")
                if datoBorrarONo.lower() == "s" or datoBorrarONo.lower() == "y":
                        lista_completa.clear()
                
def InsertValoresPosConcr():
        print(f"La lista es:")
        for clave, valor in enumerate(lista_completa):
                print(f"En la posición {clave} está el valor {valor}")
        posinterchng = int(input("En que posición quieres colocar un nuevo valor?\n"))
        valoradd = input("Que valor quieres añadir?")
        lista_completa.insert(posinterchng, valoradd)
        print(f"La lista actualizada es:\n{lista_completa}")
def ComprobarSiUnValorExisteEnLista():
        print(f"La lista es:\n{lista_completa}")
        valor_Comprobar = input("Introduce el valor que quieres comprobar si está en la lista: ")

        if valor_Comprobar in lista_completa:
                print(f"El valor {valor_Comprobar} está en la lista")
        else:
                print(f"El valor {valor_Comprobar} NO está en la lista")
def BorrarValorLista_SoloSI_Existe():
        print(lista_completa)
        valor_Borrar = input("Introduce el valor que quieres borrar de la lista: ")

        if valor_Borrar in lista_completa:
                lista_completa.remove(valor_Borrar)
                print(f"La lista ahora es:\n{lista_completa}")
        else:
                print(f"El valor {valor_Borrar} no existe en la lista, por lo cual no puede ser eliminado.")
def DarLaListOrdenInverso():
        
        lista_completa.reverse()
        print(lista_completa)

        lista_completa.reverse() # Volvemos a poner la lista al derecho tras imprimirlo por si el usuario quiere seguir operando con la lsita en el orden original.

def DevolverUltimoValor_borrar():

        valor_eliminado = lista_completa.pop()
        print(f"El valor que se ha eliminado es {valor_eliminado}")




""" --------------------------------------------------------------------------------------------------------------------------------------------------------------- """

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

""" ---------------------------------------------------------------------------------------------------------- """

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


""" ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- """

# Calculadora con las operaciones en diferentes funciones:

def suma(valor1,valor2):
    resultado = valor1+valor2
    return resultado

def resta(valor1,valor2):
    resultado = valor1-valor2
    return resultado

def multiplicacion(valor1,valor2):
    resultado = valor1*valor2
    return resultado

def division(valor1,valor2):
    if valor2 !=0:
        resultado = valor1/valor2
    else:
        resultado = "No se puede dividir entre 0."
    return resultado


def menu():
    operacions = ["+","-","*","/"]
    opcion='€'
    while opcion not in operacions: # <-----------------------| Mientras lo que mete el usuario no es uno de los valores validos (lista) repite la pregunta.
        print("Sumar +\nRestar -\nMultiplicar\nDividir /")
        opcion = input("escolla unha opción")

    return opcion

def calculadora():
    match operacion:
    
        case '+':
            result = suma(num1,num2) 
        case '-':
            result = resta(num1,num2)
        case '*':
            result = multiplicacion(num1,num2)
        case '/':
            result = division(num1,num2)
    return result

operacion = menu()
num1 = int(input("Introduce el primer valor: "))
num2 = int(input("Introduce el segundo valor: "))


result=calculadora()
print(f"El resultado de {num1}{operacion}{num2}={result}")





#________________________________________________________________________________________________________________________

"""
ejercicio varios tipos de funciones de suma. 


----> La suma1() recibe 2 valores y devuelve el resultado de la suma para ser impreso fuera de la función

----> La suma2() recibe 2 valores y imprime en pantalla directamente la suma.

----> La suma3() pide 2 valores y devuelve el resultado de la suma para ser impreso fuera de la función

----> La suma4() pide 2 valores y imprime la suma en pantalla.

"""

def suma1(valor1,valor2):
    print("[SUMA ·1·]Recibe un dato y devuelve el valor (return)")
    resultadoSuma1 = valor1 + valor2
    return resultadoSuma1

def suma2(valor1,valor2):
    print("[SUMA 2]Esta función recibe los datos y imprime el resultado")
    total = valor1+valor2
    print(f"[SUMA 2]-----------------------------------------------------{valor1} + {valor2} es {total}")

def suma3():
    print("[SUMA ·3·] esta función pide un dato y devuelve otro")
    valor1=int(input("[SUMA 3]Introduce el valor 1 : "))
    valor2=int(input("[SUMA 3]Introduce el valor 2: "))
    resultadoSuma3 = valor1 + valor2

    return resultadoSuma3

def suma4():
    print("[SUMA 4] Esta función pide 2 números y imprime el resultado")
    valor1=int(input("[SUMA 4]Introduce el valor 1: "))
    valor2=int(input("[SUMA 4]Introduce el valor 2: "))
    total = valor1+valor2
    print(f"[SUMA 4]-----------------------------------------------------{valor1} + {valor2} es {total}")
    print(valor1 + valor2)

n1 = int(input("Introduce el primer dato destinado a SUMA 1 y Suma 2: "))
n2 = int(input("Introduce el segundo dato destinado a SUMA 1 y Suma 2: "))

print("----------------------Suma1()-----------------------")

# esta variable da los valores a suma1() y los almacena en 'Rsuma1'
Rsuma1 = suma1(n1,n2)
print(f"El resultado de la SUMA 1 que ha sido 'retornado' es {Rsuma1}")

print("-----------------Llamamos a Suma2()------------------")

suma2(n1,n2)

print("----------------------Suma3()-----------------------")

# esta variable almacena el resultado de suma 3 (que ha pedido los datos por si misma)
Rsuma3 = suma3()
print(f"El resultado de la SUMA 3 que ha sido 'retornado' es {Rsuma3}")

print("-----------------Llamamos a Suma4()------------------")

suma4()

""" ____________________________________________________________________________ """

listaDePrimos = []
listaAutomaticaPrimos = []
listaFibo = [0,1]
# Función que recibe un valor y comprueba que es o no primo.
def primo(valor):
    i=1
    esprimo = True
    for i in range(2, valor):
        if valor % 2 == 0:
            esprimo = False
            break
    
    return esprimo

def almacenadorprimos(num):
    if primo(num)==True:
        listaDePrimos.append(num)


def generadorNumerosFibo():
    penultimo = 0
    ultimo = 1
    cantidad = int(input("Introduce la cantidad de números de la serie de fibonnacci que desees: "))

    while len(listaFibo) < cantidad:
        ultimo = ultimo + penultimo
        penultimo = ultimo - penultimo
        listaFibo.append(ultimo)


def generadorAutomaticoPrimos():
    num = 1
    cantidad = int(input("Introduce la cantidad de números primos que desees: "))
    while len(listaAutomaticaPrimos) < cantidad:
        if primo(num):
            listaAutomaticaPrimos.append(num)
        num+=1
    
    return cantidad

""" i=1
while i<10:
    num = int(input("Introduce un valor: "))

    esONoPrimo = primo(num)

    print(f"el número {num} ha dado {esONoPrimo} como resultado de ser primo.")

    if esONoPrimo==True:
        almacenadorprimos(num)
        print(f"La lista ahora consta de:\n{listaDePrimos}")

    i+=1  """


""" cantidad = generadorAutomaticoPrimos()
print(f"Aquí tienes {cantidad} números primos:\n{listaAutomaticaPrimos}") """

generadorNumerosFibo()
print(listaFibo)

""" _______________________________________________________________________ """
# Versión del profesor del generador automático de números primos:

# Función que comprueba si un número es primo o no.
def primo(num):
    primo = True

    for divisor in range(2, num):
        if num % divisor == 0:
            primo = False

    return primo

primeirosPrimos = int(input("Introduce cuantos números primos deseas: "))

# En vez de meterlos en una lista y medir el largo de la lista, hace un +1 en un contador.

cont_primos = 0
num_probar = 1
lista = []

while cont_primos < primeirosPrimos:
    if primo(num_probar):
        lista.append(num_probar)
        cont_primos+=1
    num_probar+=1

print(f"La lista es:\n{lista}")

""" ------------------------------------------------------------- """










def primo(valor):
    i=1
    esprimo = True
    for i in range(2, valor):
        if valor % 2 == 0:
            esprimo = False
            break
    
    return esprimo


def generadorAutomaticoPrimos():
    num = 1
    cantidad = int(input("Introduce la cantidad de números primos que desees: "))
    while len(listaAutomaticaPrimos) < cantidad:
        if primo(num):
            listaAutomaticaPrimos.append(num)
        num+=1
    
    return cantidad

i=1
cantidad = int(input("Introduce Cantidad: "))

for i in range((cantidad)*(10**cantidad)):
    print(i)


""" _________________________________________________________________________ """

# ejercicio 1 tuplas (alumno)

temperaturas = (24,56,12,35,21,-7,26,18)
lista = temperaturas
lista = list
def mediaTemp():
    total = 0
    div = len(temperaturas)
    for i in temperaturas:
        total+=i
    mediaTemp = total / div

    return mediaTemp

def CalcTempSupMedia(n):
    
    media = n
    cont = 0
    for valor in temperaturas:
        if valor > media:
            cont+=1
            print(valor)
    print(f"Un total de {cont} temperaturas que superan la media.")


mediaTemperatura = mediaTemp()
print(f"La temperatura media es de {mediaTemperatura}")

CalcTempSupMedia(mediaTemperatura)


# NOTAS:

# Se puede retornar dos valores en un solo 'return'

""" _____________________________________________________________________________________ """

""" Ejercicio de listas bidimensionales: """

""" Función que lle pida ó usuario os datos (números) para gardalos nunha matriz de 2 filas e
tres columnas. Dita función devolverá a matriz creada.
• Función que pasandolle unha matriz, devolva a suma de todos os elementos da matriz.
• Función que pasandolle unha matriz a visualice en formato matriz.
• Función que devolva o valor maior de todos os elementos da matriz.
• Función que devolva unha lista con todos os elementos <0 que conteña a matriz.
• Función que pasandolle unha matriz, devolva outra matriz onde os valores pares da orixinal
se sustituiran por un 0 e os impares por un 1. """

def AskUser():
    matriz = []
    lista = []
    ncol = 3
    nfil = 2
    for j in range(nfil):
        lista.clear()
        i=0
        for i in range(ncol):
            lista.append(int(input("Introduce valores: ")))
        matriz.append(lista.copy())
       
    return matriz

""" Versión profe de AskUser() """
def Pedir():
    matriz = []
    for i in range(2):
        lista = []
        for _ in range(3):

            lista.append(int(input("Valor: ")))
        matriz.append(lista)

    return matriz
""" ___________________________________________ """
def sumAllNumbersMatriz(coso):
    totalSuma = 0
    for i in range(len(coso)):
        for j in coso[i]:
            totalSuma += j

    return totalSuma

def ImpresoraTOWapadeMAtrices(matriz):
    lista1= []
    for k in range(len(matriz)):
        lista1.clear()
        for l in matriz[k]:
            lista1.append(l)
        print(lista1)

def CalEoMaIor(os_cartinhos):
    maxi = 0
    for k in range(len(os_cartinhos)):
        for l in os_cartinhos[k]:
            if maxi < l:
                maxi = l
    
    return maxi

def listaBajoSero(contratos):
    LasQueLeGustanADAllas = []
    for k in range(len(contratos)):
        for l in contratos[k]:
            if l < 0:
                LasQueLeGustanADAllas.append(l)  


    return LasQueLeGustanADAllas    


def BinarioTypeTHing(lereles):
    matrizSecundaria = []
    matrizfinal=[]
    for k in range(len(lereles)):
        matrizSecundaria.clear()
        for l in lereles[k]:
            if l % 2 == 0:
                matrizSecundaria.append(0)
            else:
                matrizSecundaria.append(1)
        matrizfinal.append(matrizSecundaria.copy()) 
    return matrizfinal
""" OJO, necesitas el .copy para que al resetear la lista que actúa de placeholder no se borre de la lista a donde se envían los datos. """              

BinarioTypeTHing()


matrizOutside = AskUser()
# print(f"Esta es la matriz!{matrizOutside}")
# totalOutside = sumAllNumbersMatriz(matrizOutside)
# ImpresoraTOWapadeMAtrices(matrizOutside)
# maximoAugustoRomero = CalEoMaIor(matrizOutside)
# print(f"El valor más alto es: {maximoAugustoRomero}")
# Pambis = []
# Pambis = listaBajoSero(matrizOutside)
# print(Pambis)
binance = BinarioTypeTHing(matrizOutside)
print(f"La matriz original es: {matrizOutside}")
print(f"La matriz modificada a 0 y 1 es: {binance}")

# Este comentario viene directamente de Github. GIT me puedes comer los huevos

