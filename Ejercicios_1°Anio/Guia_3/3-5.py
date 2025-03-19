"""Dadas las calificaciones de 4 exámenes finales de un estudiante determinar el promedio."""

def promedio(n1, n2, n3, n4):
    prom = (n1 + n2 + n3 + n4) / 4
    return prom

nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))
nota_4 = float(input("Nota 4: "))

print(f"Promedio = {promedio(nota_1, nota_2, nota_3, nota_4)}")