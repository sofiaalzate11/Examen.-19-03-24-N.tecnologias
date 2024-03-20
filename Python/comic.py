import random

class Comic:
    def __init__(self, nombre, precio, ubicacion, descripcion, casa, referencia, pais, unidades, garantia):
        self.id = generar_id_aleatorio()
        self.nombre = nombre
        self.precio = precio
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.casa = casa
        self.referencia = referencia
        self.pais = pais
        self.unidades = unidades
        self.garantia = garantia

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: ${self.precio}, Descripción: {self.descripcion}, Referencia: {self.referencia}, pais: {self.pais}, ubicacion: {self.ubicacion}, pertenece: {self.casa} "

def generar_id_aleatorio():
    return random.randint(1, 100)

def registrar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario del producto: "))
    ubicacion = input("Ubicación en la tienda (Zona A, B, C o D): ").upper()
    descripcion = input("Descripción del producto: ")
    casa = input("Casa a la que pertenece el producto (Marvel, DC, One Piece, Dragon Ball Z, Los Supercampeones): ")
    referencia = generar_alfanumerico(6)
    pais = input("País de origen del producto: ")
    unidades = int(input("Número de unidades compradas del producto: "))
    garantia = input("¿Producto con garantía extendida? (True/False): ").lower() == "True" or "False"
    
    return Comic(nombre, precio, ubicacion, descripcion, casa, referencia, pais, unidades, garantia)

def mostrar_inventario(inventario):
    print("*** Inventario de la Tienda de Cómics ***")
    for comic in inventario:
        print(comic)

def buscar_producto_por_nombre(inventario, nombre):
    for comic in inventario:
        if comic.nombre == nombre:
            print("Información del producto:")
            print(f"ID: {comic.id}, Nombre: {comic.nombre}, Precio: ${comic.precio}, Descripción: {comic.descripcion}")
            return
    print("Producto no encontrado en el inventario.")

def modificar_unidades_compradas(inventario, nombre, nuevas_unidades):
    for comic in inventario:
        if comic.nombre == nombre:
            if nuevas_unidades <= comic.unidades:
                comic.unidades = nuevas_unidades
                print(f"Unidades compradas del producto '{nombre}' modificadas exitosamente.")
                return
            else:
                print("El número de unidades modificadas no puede ser mayor al número inicial.")
                return
    print("Producto no encontrado en el inventario.")

def eliminar_producto(inventario, nombre):
    for comic in inventario:
        if comic.nombre == nombre:
            confirmacion = input(f"¿Estás seguro de eliminar el producto '{nombre}'? (Sí/No): ").lower()
            if confirmacion == "si":
                inventario.remove(comic)
                print("Producto eliminado del inventario.")
            return
    print("Producto no encontrado en el inventario.")

def generar_alfanumerico(longitud):
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def main():
    inventario = []
    opcion = 0

    while opcion != 6:
        print("\n*** Menú de Opciones ***")
        print("1. Registrar un producto")
        print("2. Mostrar todos los productos en bodega")
        print("3. Buscar producto por nombre")
        print("4. Modificar número de unidades compradas de un producto")
        print("5. Eliminar un producto del inventario")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nuevo_producto = registrar_producto()
            inventario.append(nuevo_producto)
            print("Producto registrado exitosamente.")

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto_por_nombre(inventario, nombre_producto)

        elif opcion == 4:
            nombre_producto = input("Ingrese el nombre del producto: ")
            nuevas_unidades = int(input("Ingrese el nuevo número de unidades compradas: "))
            modificar_unidades_compradas(inventario, nombre_producto, nuevas_unidades)

        elif opcion == 5:
            nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(inventario, nombre_producto)

if __name__ == "__main__":
    main()
    