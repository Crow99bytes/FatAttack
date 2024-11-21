listaN = []
def sumar(n,m):
    return n + m

def multiplicar(n,m):
    return n*m

def dividir(n,m):
    if n == 0 or m == 0:
        print("No se puede dividir el 0 o dividir entre 0.")
    else:
        return n / m
    
def elevar(n,m):
    return n ** m

def Anagrama(str1, str2):
    if len(str1) != len(str2):
        print(f"{str1} y {str2} no son anagramas.")
    else:
        if sorted(str1) == sorted(str2):
            print(f"{str1} y {str2} son anagramas.")

def juego2048(a,b):
    
    listaN.append(a)
    m = a
    while len(listaN)<b:
        m*=a
        listaN.append(m)
    
def 