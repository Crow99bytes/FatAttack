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
