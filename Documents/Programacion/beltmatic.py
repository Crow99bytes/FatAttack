listaNumeros = [1,2,3,4,5,6,7,8,9,11,12,13,14]


def laGranMultiplicadora(n):
    seguir = True
    while seguir:
        for i in range(n):
            for j in range(n):
                multi = i * j
                if multiplicacionMasAlta<multi and multi<laCifra:
                    multiplicacionMasAlta = multi
                    imas = i
                    jmas = j

        print(f"la multiplicación más alta para llegar a {laCifra} es {imas} * {jmas} es igual a {multiplicacionMasAlta}")
        laCifra = laCifra - multiplicacionMasAlta
        print(laCifra)
        break
    return laCifra

def laGranElevadora(n):
    seguir = True
    multiplicacionMasAlta = 0
    multi = 0
    while seguir:
        for i in range(n):
            for j in range(n):
                multi = i ** j
                if multiplicacionMasAlta<multi and multi<laCifra:
                    multiplicacionMasAlta = multi
                    imas = i
                    jmas = j

        print(f"la elevación más alta para llegar a {laCifra} es {imas} ** {jmas} es igual a {multiplicacionMasAlta}")
        laCifra = laCifra - multiplicacionMasAlta
        print(laCifra)
        break
    return laCifra


n = (len(listaNumeros))
laCifra = int(input("Introduce el valor a alcanzar."))
multiplicacionMasAlta = 0
imas = 0
jmas = 0


if laCifra > 195:
    print(laGranElevadora(laCifra))
elif laCifra <= 196:
    print(laGranMultiplicadora(laCifra))


