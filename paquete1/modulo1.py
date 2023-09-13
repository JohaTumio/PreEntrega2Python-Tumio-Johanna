class Cliente:
    db2 = {}

    def __init__(self, nombre, edad, telefono, email):
        self.nombre = nombre
        self.edad = edad
        self.__telefono = telefono
        self.email = email

        # Agregar el cliente a la base de datos
        if self.nombre in self.db2:
            print(f"El cliente {self.nombre} ya existe en la base de datos.")
        else:
            self.db2[self.nombre] = {
                "nombre": self.nombre,
                "edad": self.edad,
                "telefono": self.__telefono,
                "email": self.email
            }

    def __str__(self):
        return f"Cliente: {self.nombre} \nEdad: {self.edad}\nEmail: {self.email}"

    def obtener_tel(self):
        return self.__telefono

    def comprar(self, articulo, tienda):
        print(f"El cliente {self.nombre} compró el artículo {articulo} en la tienda {tienda}\nLe llegará un mensaje con todos los datos a: {self.obtener_tel()}")

    def actualizar_informacion(self, nuevo_telefono, nuevo_email):
        self.__telefono = nuevo_telefono
        self.email = nuevo_email

        self.db2[self.nombre]['telefono'] = nuevo_telefono
        self.db2[self.nombre]['email'] = nuevo_email
        

class Vendedor(Cliente):
    def __init__(self, nombre, edad, telefono, email, acciones):
        super().__init__(nombre, edad, telefono, email)
        self.acciones = acciones

    def saludar(self):
        return f"Hola soy {self.nombre}, mi correo es {self.email}, y puedo ayudarlo a {', '.join(self.acciones)} un producto."
