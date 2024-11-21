dia = int(input("Introduce de manera numérica el día de la semana (1-7):"))


match dia: # abre el coso de match en la VARIABLE 'dia'
    case 1:
        print(f"El día {dia} de la semana es Lunes.")
    case 2:
        print(f"El día {dia} de la semana es Martes.")
    case 3: 
        print(f"El día {dia} de la semana es Miércoles.")
    case 4:
        print(f"El día {dia} de la semana es Jueves.")
    case 5:
        print(f"El día {dia} de la semana es Viernes.")
    case 6:
        print(f"El día {dia} de la semana es Sábado.")
    case 7:
        print(f"El día {dia} de la semana es Domingo.")
    case _:
        print(f"You have only one task, and you did it wrong.")
print("Fin.")


#versión profe.
