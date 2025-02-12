class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters para cada atributo
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio
class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Asegurarse de que el ID sea único
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("¡Error! Ya existe un producto con ese ID.")
            return

        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.")
                return

        print("¡Error! No se encontró ningún producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado correctamente.")
                return

        print("¡Error! No se encontró ningún producto con ese ID.")

    def buscar_producto(self, nombre):
        resultados = [
            producto
            for producto in self.productos
            if nombre.lower() in producto.get_nombre().lower()
        ]
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("Inventario:")
        for producto in self.productos:
            print(
                f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, "
                f"Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}"
            )
    def main():inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto(s)")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            elif opcion == "2":
                id = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id)

            elif opcion == "3":
                id = int(input("ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (o Enter para omitir): ")
                precio = input("Nuevo precio (o Enter para omitir): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id, cantidad, precio)

            elif opcion == "4":
                nombre = input("Nombre del producto a buscar: ")
                resultados = inventario.buscar_producto(nombre)
                if resultados:
                    print("Resultados de la búsqueda:")
                    for producto in resultados:
                        print(
                            f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, "
                            f"Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}"
                        )
                else:
                    print("No se encontraron productos con ese nombre.")

            elif opcion == "5":
                inventario.mostrar_inventario()

            elif opcion == "6":
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        except ValueError:
            print("¡Error! Debe ingresar un número entero para ID y cantidad, y un número decimal para el precio.")


if __name__ == "__main__":
    main()                