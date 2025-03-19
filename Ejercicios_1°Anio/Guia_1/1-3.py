"""Dadas las horas trabajadas por un operario y el valor de las mismas, determinar que
sueldo percibe dicho operario."""

def sueldo(horas, valor_hora):
    sueldo = horas * valor_hora
    return sueldo

horas = float(input("Horas trabajadas: "))
valor_hora = float(input("Valor por hora: "))

print(f"Sueldo del operario: ${sueldo(horas, valor_hora)}")