import os
db = {}

def cargar_usuarios():
    try:
        with open("./recursos/dataUsuarios.txt") as file:
            for data in file.readlines():
                data = data.strip().split("|")
                email = data[0]
                pwd = data[1]
                db.update({email : pwd})
    except FileNotFoundError:
        pass

cargar_usuarios()

def guardar_usuario(email, pwd):
    if email not in db:
        db[email] = pwd
        try:
            with open("./recursos/dataUsuarios.txt", "a") as file:
                file.write(f"{email}|{pwd}\n")
                print("Registro exitoso. ¡Bienvenido!")
        except FileNotFoundError:
            with open("./recursos/dataUsuarios.txt", "w") as file:
                file.write(f"{email}|{pwd}\n")
                print("Registro exitoso. ¡Bienvenido!")
    else:
        print("El usuario ya existe.")


def iniciar_sesion(email,pwd):
    with open("./recursos/dataUsuarios.txt") as file:
        for data in file.readlines():
            data = data.strip().split("|")
            if data[0] == email and data[1] == pwd:
                print("Bienvenido")
                return True
    print("Correo o contraseña incorrecta")
    return False


def ciclo_de_intentos(max_intentos):
    intentos = max_intentos

    while intentos > 0:
        email = input("Correo: ")
        pwd = input("Contraseña: ")

        if iniciar_sesion(email,pwd):
            print("Sesión iniciada exitosamente.")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Correo o contraseña incorrecta. Te quedan {intentos} intentos.")
            else:
                print("Usuario bloqueado.")

def registarse():
    email = input("Correo: ")
    pwd = input("Contraseña: ")
    if len(pwd) < 8:
        print("La contraseña debe tener al menos 8 caracteres. Registro no completado.")
        return
    os.system("cls")
    try:
        guardar_usuario(email, pwd)
    except Exception as e:
        print(f"Hubo un error al intentar registrar: {type(e).__name__}")
        print("Inténtalo nuevamente.")

def mostrar_usuarios(database):
    for usuario, pwd in database.items():
        print(f"Usuario: {usuario} Contraseña: {pwd}")


opcion = input("Digite 1 para iniciar sesion o 2 para registrarse ")

try:
    opcion = int(opcion)
    if opcion == 1:
        print("Iniciar Sesion\n")
        email = input("Correo: ")
        pwd = input("Contraseña: ")
        os.system("cls")
        if not iniciar_sesion(email,pwd):
            ciclo_de_intentos(3)
    elif (opcion == 2):
        print("Registrate\n")
        registarse()
    else:
        print("Opción Incorrecta")
except ValueError:
    print("Ingresaste un caracter inválido")

mostrar_usuarios(db)



