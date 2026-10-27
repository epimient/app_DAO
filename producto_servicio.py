#aplicar las reglas del negocio
from modelo import Producto


class ProductoServicio:

    def __init__(self, dao):
        self.dao = dao

    # 1. REGISTRAR PRODUCTO
    def registrar(self, nombre, precio, stock):

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        producto = Producto(None, nombre.strip(), precio, stock)

        return self.dao.crear(producto)
