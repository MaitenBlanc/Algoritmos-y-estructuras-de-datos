"""De los y las estudiantes de Fundamentos de Programación se desea saber qué porcentaje
de personas menores a 20 años se encuentran cursando la materia. El programa debe
solicitar al usuario que ingrese la cantidad total de estudiantes menores a 20 años y el
total."""

def porcentaje_menores(total, menores):
    porc_menores = (menores / total) * 100
    return porc_menores

cant_total = int(input("Cantidad total de alumnos: ")) 
cant_menores = int(input("Cantidad de menores de 20 años: "))

print(f"Hay un {porcentaje_menores(cant_total, cant_menores):.2f}% de alumnos menores de 20 años.")