def Anagrama(str1, str2):
    if len(str1) != len(str2):
        print(f"{str1} y {str2} no son anagramas.")
    else:
        if sorted(str1) == sorted(str2):
            print(f"{str1} y {str2} son anagramas.")

palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

Anagrama(palabra1, palabra2)