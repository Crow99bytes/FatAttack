RegistroUsuarios = {}

n = 1
while True:
    Valor_User = input("Introduce el usuario: ")
    Clave_User = f"Usuario_{n}"

    RegistroUsuarios[Clave_User] = Valor_User
    
    if Valor_User.lower()=="salir":
        break

    Valor_Password = input("Introduce la contraseña: ")
    Clave_Password = f"Contraseña_{n}"
    RegistroUsuarios[Clave_Password] = Valor_Password
    n += 1

for i in len(RegistroUsuarios)+1:
    print(i)