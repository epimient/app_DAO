# mostrar el menu y recibir datos
from base_datos import inicializar_bd
from modelo import Producto
from producto_dao import ProductoDAO

# Preparar la base de datos
inicializar_bd()

# Crear objeto DAO
dao = ProductoDAO()

# Crear un producto
nuevo = Producto(None, "Resident Evil 4", 180000, 10)

dao.crear(nuevo)

print("Producto registrado con ID:", nuevo.id)