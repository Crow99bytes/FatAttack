
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