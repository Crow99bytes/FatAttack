listaAutomaticaPrimos=[]
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

for i in range(1,(cantidad)*(100**cantidad)):
    if primo(i):
        if len(listaAutomaticaPrimos)<cantidad:
            listaAutomaticaPrimos.append(i)
        else:
            break

print(listaAutomaticaPrimos)