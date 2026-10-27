#ejecutar las operaciones sql
from base_datos import obtener_conexion
from modelo import Producto

class ProductoDAO:
    
    #1. crear un producto
    def crear(self, producto):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        
        
        sql = """ 
            INSERT INTO productos (nombre, precio, stock)
            VALUES (?, ?, ?)
        """
        
        cursor.execute(sql,(producto.nombre, producto.precio, producto.stock))
        producto.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        
        return producto
        