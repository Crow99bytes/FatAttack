tareas = []
def menu():
   seguir = True
   while seguir:
        print("Bienvenido al Task-Master.\n_________________________________________________________________________________________\nTienes las siguientes opciones:\n1) Añadir tarea.\n2) Ver la lista de tareas\n3) Eliminar una tarea.\n4) Salir.")
        opcion = int(input("Introduce el valor correspondiente a la opción que desees:\n"))

        match opcion:
            case 1:
                AddTarea()
            case 2:
                VerTareas()
            case 3:
                deleteTask()
            case 4:
                break
            case _:
                print("Te pedí el número de la función, no la cura del Cancer.")
        print("\n\n\n")

    
def AddTarea():
    tarea = input("Introduce la tarea a añadir:\n")
    tareas.append(tarea)

def VerTareas():
    contador = 1
    print("La lista de tareas es:")
    for i in tareas:
        print(contador, i)
        contador+=1

def deleteTask():
    VerTareas()
    deleteado = input("Introduce la tarea que desees eliminar:\n")
    tareas.remove(deleteado)
    print(f"{deleteado} ha sido eliminada de la lista de tareas.")


menu()
print("Muchas gracias por usar nuestro programa.\nHasta pronto.")