""" 1. Insertar un elemento na lista (pideselle o usuario)
2. Insertar un elemento nunha posición determinada (pidese elemento e posición a cal ten 
que existir)  insert(i, x): Inserta un elemento x en la posición i. posición - elemento
3. Visualizar a lista (completa)
4. Buscar un elemento e decir si está ou non na lista.
5. Eliminar un elemento da lista (ten que existir)
6. Ordear a lista en orden inverso
7. Devolver o ultimo elemento da lista e eliminalo.
8. Sair """
lista=[]
def insetNumPosConcrt():
    for i in range (5):
        lista.append(input("Introduce 5 valores"))

    print(lista)
    i = int(input("En que posición quieres meter un dato?"))
    x = input("Dato a insertar: ")
    lista.insert(i, x)
    print(lista)

insetNumPosConcrt()