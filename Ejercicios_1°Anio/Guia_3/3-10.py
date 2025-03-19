"""Solicitar al usuario que ingrese el precio de un producto al inicio del año, y el precio del
mismo producto transcurrido un determinado tiempo. El usuario debe mostrar cuál fue el
porcentaje de aumento que tuvo ese producto en el año"""

def porcentaje_aumento(precio_inicial, precio_final):
    aumento = ((precio_final - precio_inicial) / precio_inicial) * 100
    return aumento

precio_inicial = float(input("Precio del producto al inicio del año: "))
precio_final = float(input("Precio actual del producto: "))

print(f"El producto aumentó un {porcentaje_aumento(precio_inicial, precio_final):.2f}% este año.")