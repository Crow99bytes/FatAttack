""" EXERCICIO DICCIONARIOS
• Pretendese manexar mediante dous diccionarios os datos de dous alumnos (un para cada
un).
• Os datos dos alumnos serán: nome, idade , nota.
• Teremos unha función PedirDatos a cal pedirá os datos dos alumnos e devolveraos en
formato diccionario.
• Teremos unha función VerDatos a cal lle pasamos un diccionario de alumnos e o visualiza
por pantalla.
• Teremos unha función CambiaDatos a cal lle pasamos o diccionario a modificar e dita
función preguntaralle o usuario que campo quere modificar, si ese campo existe pediralle o
usuario o novo valor para ese campo e modificarao. A función devolverá o diccionario
modificado.
• Toda a aplicación se manexará mediante un menu de opcións que o usuario escollerá.
Teremos que establecer un sistema para que o usuario escolla con cal dos alumnos
(diccionarios) quere traballar. """

# diccionario[key]=value

alumno1 = {
    "nome" : "",
    "idade" : "",
    "nota" : "",
}

alumno2 = {
    "nome" : "",
    "idade" : "",
    "nota" : "",
}

def Interrogatorio_FBI():
    print("¿A qué diccionario quieres añadir datos? 1 o 2?")
    elec = int(input("Introduce el valor que deseas actualizar: "))

    if elec == 1:
        print("Ha seleccionado el primer alumno")
        for i in alumno1.keys():
            valor = input(f"Introduce el valor a añadir a {i}:")
            alumno1[i]=valor
            print(alumno1)

            return alumno1
    else:
        print("Ha seleccionado el primer alumno")
        for i in alumno2.keys():
            valor = input(f"Introduce el valor a añadir a {i}:")
            alumno2[i]=valor
            print(alumno2)

            return alumno2


def VerDic_cionarios(n):
    if n == 1:
        print(alumno1)
    elif n == 2:
        print(alumno2)
    else:
        print("Incorrecto.")

def CambiaDatos(n):
    if n == 1:
        print(alumno1)

    elif n ==2:
        print(alumno2)


    
decision = int(input("¿Qué número de diccionario deseas visualizar? "))

CambiaDatos(decision)
Interrogatorio_FBI()

