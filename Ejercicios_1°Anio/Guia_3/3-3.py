"""Dadas las horas trabajadas por un operario y el valor de las mismas, determinar que
sueldo percibe dicho operario. Se solicita indicar cuanto cobraría si se aplican descuentos
del 20%"""

def sueldo(horas, valor_hora):
    sueldo = horas * valor_hora
    descuento = sueldo * 0.2
    return sueldo - descuento

horas = float(input("Horas trabajadas: "))
valor_hora = float(input("Valor por hora: "))

print(f"Sueldo con descuento del 20% del operario: ${sueldo(horas, valor_hora)}")