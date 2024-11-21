num = int(input("Cuantas veces quieres que diga Hola?"))

i=0
while i < num:
    print(f"{i+1}:Hola Mundo")
    i+=1

for i  in range(num): # range [0,1,2,3] // ----> range(1,5) va desde 1 hasta 4, el ultimo de la lista, no inlcuido.
     print(f"{i+1}:Hola Mundo/////buclefor")