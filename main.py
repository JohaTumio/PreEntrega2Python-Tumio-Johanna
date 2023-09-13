from paquete1.modulo1 import Cliente, Vendedor
#from paquete1.modulo2 import *

cliente1 = Cliente("Ana",33,22242056,"ana@gmail.com")
print(cliente1)
cliente1.comprar("Celular", "Frávega")

cliente2 = Cliente("Juan", 30, 33345678, "juan@gmail.com")
print(cliente2)
cliente2.comprar("Televisor", "Musimundo")

# Intentar agregar un cliente con el mismo nombre
cliente3 = Cliente("Juan", 28, 1112223333, "nuevojuan@example.com")

# Acceder a la base de datos de clientes
print(Cliente.db2)

#actualizar datos
cliente1.actualizar_informacion(123, "abc@hotmail.com")

#verificando si los datos fueron cambiados correctamente al comprar de nuevo
cliente1.comprar("Celular", "Frávega")

vendedor1 = Vendedor("Leo", 25, 4585695, "leo@gmail.com", ["Comprar", "Buscar", "Elegir"])
print(vendedor1.saludar())