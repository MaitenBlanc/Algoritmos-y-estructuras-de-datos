"""Leer el nombre y sueldo de una persona mostrar si este gana más de 30.000 pesos."""

def gana_mas(sueldo):
    if (sueldo > 30000):
        return True
    else:
        return False

nombre = input("Ingrese su nombre: ")
sueldo = float(input("Ingrese su sueldo: "))

if (gana_mas(sueldo)):
    print(f"{nombre} gana más de $30000.")
else:
    print(f"{nombre} gana menos de $30000.")