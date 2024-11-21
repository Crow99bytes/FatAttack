def media(temp):
    media=sum(temp)/len(temp)
    return media

def temps_maior_media(temps):
    med=media(temps)
    lista = []
    cont=0
    for temp in temps:
        if temp>med:
            lista.append(temp)

    return lista,cont
temps = (23,31,23,13,12,31,20,414,12,31,21,24,14)

li,co = temps_maior_media(temps)
print(li)
print(co)