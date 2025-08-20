class CodigoDuplicadoError(Exception):
    pass
class ProductoNoExisteError(Exception):
    pass
class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        if not codigo or not nombre or not categoria:
            raise ValueError("Código, nombre y categoría no pueden estar vacíos.")
        if precio < 0 or stock < 0:
            raise ValueError("Precio y stock no pueden ser negativos.")
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
    def actualizar(self, nuevo_precio, nuevo_stock):
        if nuevo_precio < 0 or nuevo_stock < 0:
            raise ValueError("Precio y stock no pueden ser negativos.")
        self.precio = nuevo_precio
        self.stock = nuevo_stock
    def __str__(self):
        return f"[{self.codigo}] {self.nombre} | {self.categoria} | ${self.precio:.2f} | Stock: {self.stock}"
class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            raise CodigoDuplicadoError("El código ya existe.")
        self.productos[producto.codigo] = producto
    def actualizar_producto(self, codigo, nuevo_precio, nuevo_stock):
        if codigo not in self.productos:
            raise ProductoNoExisteError("No se encontró el producto.")
        self.productos[codigo].actualizar(nuevo_precio, nuevo_stock)
    def eliminar_producto(self, codigo):
        if codigo not in self.productos:
            raise ProductoNoExisteError("No se encontró el producto.")
        del self.productos[codigo]
    def obtener_lista(self):
        return list(self.productos.values())
class Ordenador:
    def ordenar(self, lista_productos, criterio):
        if criterio not in ["nombre", "precio", "stock"]:
            raise ValueError("Criterio de orden inválido. Usa 'nombre', 'precio' o 'stock'.")
        return self._quick_sort(lista_productos, criterio)
    def _quick_sort(self, lista, criterio):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [p for p in lista[1:] if getattr(p, criterio) <= getattr(pivote, criterio)]
        mayores = [p for p in lista[1:] if getattr(p, criterio) > getattr(pivote, criterio)]
        return self._quick_sort(menores, criterio) + [pivote] + self._quick_sort(mayores, criterio)
    def actualizar_producto(inventario):
        codigo = input("Código del producto a actualizar: ").strip()
        try:
            nuevo_precio = float(input("Nuevo precio: "))
            nuevo_stock = int(input("Nuevo stock: "))
            inventario.actualizar_producto(codigo, nuevo_precio, nuevo_stock)
            print("Producto actualizado correctamente.")
        except ProductoNoExisteError:
            print("No se encontró el producto.")
        except ValueError:
            print("Precio y stock deben ser válidos y no negativos.")
    def eliminar_producto(inventario):
        codigo = input("Código del producto a eliminar: ").strip()
        try:
            inventario.eliminar_producto(codigo)
            print("Producto eliminado correctamente.")
        except ProductoNoExisteError:
            print("No se encontró el producto.")
def listar_productos(inventario, ordenador):
    productos = inventario.obtener_lista()
    if not productos:
        print("No hay productos registrados.")
        return
    criterio = input("Ordenar por (nombre/precio/stock): ").strip().lower()
    try:
        ordenados = ordenador.ordenar(productos, criterio)
        print(f"\nProductos ordenados por {criterio}:")
        for p in ordenados:
            print("-", p)
    except ValueError as j:
        print(f"Error: {j}")