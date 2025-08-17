Productos = {}

class producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        print(f"[{self.codigo}] {self.nombre} - {self.categoria} - ${self.precio: .2f} - Stock: {self.stock}")

class buscador:
    def Buscar_Por_Codigo(self, codigo, productos):
        if codigo in productos:
            return productos[codigo]
        return None

    def Buscar_Por_Nombre(self, productos, nombre):
        resultado = []
        nombre = nombre.lower()
        for prod in productos.values():
            if nombre in prod.nombre.lower():
                resultado.append(prod)
        return resultado

    def Buscar_Por_Categoria(self, productos, categoria):
        resultado = []
        categoria = categoria.lower()
        for prod in productos.values():
            if categoria in prod.categoria.lower():
                resultado.append(prod)
        return resultado

def Registrar(productos, codigo, nombre, categoria, precio, stock):
    if codigo.strip() == "" or nombre.strip() == "" or categoria.strip() == "":
        return "Error: se requieren llenar todos los campos"

    if codigo in productos:
        return "Error: el código ya existe"

    try:
        precio = float(precio)
        stock = int(stock)
    except:
        return "Error: precio o stock inválido"

    if precio < 0 or stock < 0:
        return "Error: precio o stock no pueden ser negativos"

    nuevo = producto(codigo, nombre, categoria, precio, stock)
    productos[codigo] = nuevo
    return "Producto agregado correctamente."

def mostrar():
    print("\n--- MENÚ DE PRODUCTOS ---")
    print("1. Registrar productos")
    print("2. Buscar por código")
    print("3. Buscar por nombre")
    print("4. Salir")

def main():
    Buscardor = buscador()
    while True:
        mostrar()
        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            codigo = input("Ingrese el código del producto: ").strip()
            nombre = input("Ingrese el nombre del producto: ").strip()
            categoria = input("Ingrese la categoría del producto: ").strip()
            precio = input("Ingrese el precio del producto: ").strip()
            stock = input("Ingrese el stock del producto: ").strip()
            mensaje = Registrar(Productos, codigo, nombre, categoria, precio, stock)
            print(mensaje)

        elif opcion == "2":
            Codigo = input("Ingrese el código del producto: ").strip()
            resultado = Buscardor.Buscar_Por_Codigo(Codigo, Productos)
            if resultado:
                resultado.mostrar()
            else:
                print("Error: el código no existe")

        elif opcion == "3":
            Nombre = input("Ingrese el nombre del producto: ").strip()
            resultado = Buscardor.Buscar_Por_Nombre(Productos, Nombre)
            if len(resultado) > 0:
                for Produc in resultado:
                    Produc.mostrar()
            else:
                print("Error: el nombre no existe")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

main()