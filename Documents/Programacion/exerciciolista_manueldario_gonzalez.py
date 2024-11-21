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


        

seguir = True

while seguir:

        selector = menuPrincipal()

        match selector:
                case 1:
                        """ numToAdd = int(input("¿Cuantos valores quieres añadir?\n"))

                        for i in range(numToAdd): 
                                lista_completa.append(input("Introduce un valor: "))""" # Si quieres que el usuario pueda añadir la cantidad de números que desee a la lista hay que sacar esto del comentario y eliminar la siguiente linea.
                        lista_completa.append(input("Introduce un valor: "))
                case 2:
                        InsertValoresPosConcr()
                case 3:
                        print(f"La lista actualmente tiene los siguientes valores:\n{lista_completa}")
                case 4:
                        ComprobarSiUnValorExisteEnLista()
                case 5:
                        BorrarValorLista_SoloSI_Existe()
                case 6:
                        DarLaListOrdenInverso()
                case 7:
                        DevolverUltimoValor_borrar()
                case 8:
                        lista_nueva = []
                        print(f"La lista actualmente consta de:\n{lista_completa}")
                        valor_aBuscar = input("Introduce un valor que buscar y cambiar(también sus duplicados): ")
                        valor_sustituir = input(f"Introduce el valor que quieres que sustituya a {valor_aBuscar}: ")
                        for valor in lista_completa:
                                if valor == valor_aBuscar:
                                        lista_nueva.append(valor_sustituir)
                                else:
                                        lista_nueva.append(valor)
                        lista_completa.clear()
                        lista_completa = lista_nueva
                        lista_nueva.clear()
                        print(f"La lista ha quedado del siguiente modo:\n{lista_completa}")
                case 9:
                        seguir = False
                        break
                case _:
                        print("No te voy a mentir, no se que has tocado.\nTe mando al menú principal.\nIntentalo de nuevo.\n")

        compseguir = input("\n\n\n¿Quiere continuar? S/N")
        if compseguir.lower() == "n":
                break
        else:
                seguir = True

print("Muchas gracias por usar nuestro programa,\nHasta pronto!")