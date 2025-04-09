"""Leer tres letras, encontrar y visualizar cuál viene primero en el alfabeto."""

def primera_letra(l1, l2, l3):
    if (l1 < l2 and l1 < l3):
        return l1
    elif (l2 < l1 and l2 < l3):
        return l2
    else:
        return l3

l1 = input("Ingrese letra 1: ")
l2 = input("Ingrese letra 2: ")
l3 = input("Ingrese letra 3: ")

print(f"La letra que viene primero en el alfabeto es {primera_letra(l1,l2,l3)}")