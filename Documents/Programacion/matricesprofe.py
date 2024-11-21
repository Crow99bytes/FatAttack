def contar_items(taboa):
    cont = 0
    for filas in range(len(taboa)):
        for columnas in range(len(taboa[filas])):
            cont+=1
    
    return cont



lista = []
lista.append([1,2,3])
lista.append([4,5,6,20])
lista.append([7,8,9])

cont = contar_items(lista)
print(f"total elementos {cont}")