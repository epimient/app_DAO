# Sistema de inventario de videojuegos

Aplicación educativa para organizar una solución de inventario usando Python,
programación orientada a objetos (POO), el patrón DAO y SQLite. El propósito es
separar las responsabilidades del programa; no introducir SQL nuevo.

## Estado actual

Por ahora, la aplicación inicializa la base de datos y registra un videojuego de
ejemplo. El inventario, la búsqueda por ID, la actualización, la eliminación y
la venta de unidades todavía están pendientes de implementar.

Al ejecutar el programa más de una vez se vuelve a registrar el ejemplo
«Resident Evil 4». No se limpia la base de datos automáticamente.

## Cómo funciona

El recorrido actual es:

1. `main.py` llama a `inicializar_bd()` para crear la tabla si todavía no existe.
2. Crea un objeto `ProductoDAO`.
3. Construye un `Producto` de ejemplo y lo envía al DAO para guardarlo.
4. El DAO ejecuta un `INSERT` parametrizado en SQLite, confirma la transacción
   y asigna al objeto el ID generado.
5. `main.py` imprime el ID del producto registrado.

### Responsabilidad de cada archivo

- `main.py`: punto de entrada; actualmente inicializa la base de datos y registra
  un producto de prueba directamente.
- `modelo.py`: define `Producto`, el objeto que representa un videojuego con
  `id`, `nombre`, `precio` y `stock`.
- `base_datos.py`: abre la conexión SQLite y crea la tabla `productos`.
- `producto_dao.py`: contiene `ProductoDAO`, responsable de persistir un producto.
  DAO significa *Data Access Object*: concentra el acceso a los datos y evita
  mezclar las consultas SQL con el resto de la aplicación.
- `producto_servicio.py`: contiene `ProductoServicio` y las reglas actuales de
  validación para registrar un producto. Este servicio existe, pero `main.py`
  todavía no lo utiliza.

La tabla tiene un ID autoincremental y requiere nombre, precio y stock. La base
se llama `tienda.db` y SQLite la crea en el directorio desde el que se ejecuta
el programa.

## Ejecutar

Requiere Python 3; SQLite forma parte de la biblioteca estándar de Python.

Desde la carpeta del proyecto:

```bash
python3 main.py
```

La salida actual muestra el ID generado, por ejemplo:

```text
Producto registrado con ID: 1
```

El ID exacto puede cambiar según los registros previos de `tienda.db`.

## Funcionalidades previstas

La meta del ejercicio es completar estas operaciones:

| Operación | Estado | Descripción |
|---|---|---|
| Registrar videojuego | Parcial | El DAO puede insertar un producto y el servicio valida nombre, precio y stock. |
| Mostrar inventario | Pendiente | Consultar y mostrar todos los productos guardados. |
| Buscar por ID | Pendiente | Consultar un producto y manejar el caso en que el ID no exista. |
| Actualizar datos | Pendiente | Modificar los datos de un producto existente. |
| Eliminar videojuego | Pendiente | Eliminar un producto existente. |
| Vender unidades | Pendiente | Descontar unidades y rechazar la venta si supera el stock disponible. |

Para respetar la separación de responsabilidades, las consultas y escrituras
SQL corresponden al DAO; las reglas de negocio, al servicio; y la interacción
con la persona usuaria, a `main.py` (o a una interfaz que se agregue después).

## Información necesaria para completar las pruebas

Antes de cerrar los casos de prueba, hace falta acordar los datos y resultados
esperados. Se puede complementar esta sección con:

1. **Datos iniciales de videojuegos**: nombre, precio y stock de cada registro.
   El ID lo asignará SQLite, salvo que se quiera probar expresamente algún caso
   con un ID conocido.
2. **Moneda y formato de precio**: por ejemplo, pesos colombianos como número
   entero. Actualmente el programa guarda `precio` como entero, pero no define
   una moneda.
3. **Caso de venta correcta**: ID del videojuego, cantidad a vender y stock que
   se espera después de la operación.
4. **Caso de venta rechazada**: ID, stock disponible y cantidad solicitada mayor
   que ese stock; indicar el mensaje o resultado esperado.
5. **Casos de IDs inexistentes**: qué debe informar cada operación cuando el
   producto no existe.
6. **Reglas adicionales**: si se permiten nombres repetidos, si se puede
   actualizar el stock directamente y qué comportamiento se espera al eliminar
   un producto.
7. **Repetición de pruebas**: indicar si se probará con una base vacía o con
   datos que permanezcan entre ejecuciones. La aplicación actual conserva los
   datos y vuelve a insertar el videojuego de ejemplo cada vez.

### Plantilla para compartir los datos de prueba

| Caso | Nombre | Precio | Stock inicial | Operación / cantidad | Resultado esperado |
|---|---|---:|---:|---|---|
| Ejemplo | Resident Evil 4 | 180000 | 10 | Vender 3 | Venta aceptada; stock final 7 |
| Completar |  |  |  |  |  |
| Completar |  |  |  |  |  |

También se necesitan, como mínimo, un caso de venta por encima del stock y un
caso con un ID que no exista, con el mensaje o comportamiento esperado en ambos.
