"""Dadas las horas trabajadas por un operario y el valor de las mismas, determinar que
sueldo percibe dicho operario, considerando que se le debe aplicar los descuentos correspondientes
por ley, los mismos son del 20%. Mostrar el sueldo a cobrar"""

def sueldo(horas, valor_hora):
    sueldo = horas * valor_hora
    descuento = sueldo * 0.2
    return sueldo - descuento

horas = float(input("Horas trabajadas: "))
valor_hora = float(input("Valor por hora: "))

print(f"Sueldo con descuento del 20% del operario: ${sueldo(horas, valor_hora)}")