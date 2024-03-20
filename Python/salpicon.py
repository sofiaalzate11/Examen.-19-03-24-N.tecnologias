"""def recibir_frutas(n):
    frutas = []
    for i in range(n):
        id_fruta = i + 1
        nombre = input("Nombre de la fruta: ")
        precio_unitario = float(input("Precio unitario de la fruta: "))
        cantidad = int(input("Cantidad de la fruta: "))
        frutas.append({"id": id_fruta, "nombre": nombre, "precio_unitario": precio_unitario, "cantidad": cantidad})
    return frutas

def costo_total(frutas):
    total = sum(fruta["precio_unitario"] * fruta["cantidad"] for fruta in frutas)
    return total

def mostrar_frutas_ordenadas(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x["precio_unitario"], reverse=True)
    for fruta in frutas_ordenadas:
        print(f"{fruta['nombre']}: {fruta['precio_unitario']}")

def fruta_mas_barata(frutas):
    fruta_barata = min(frutas, key=lambda x: x["precio_unitario"])
    return fruta_barata["nombre"]

cantidad_frutas = int(input("Ingrese la cantidad de frutas: "))
lista_frutas = recibir_frutas(cantidad_frutas)

print("\nCosto total del salpicón:", costo_total(lista_frutas))

print("\nFrutas ordenadas por costo:")
mostrar_frutas_ordenadas(lista_frutas)

print("\nLa fruta más barata es:", fruta_mas_barata(lista_frutas))
"""