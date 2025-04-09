"""Deducir si un número leído (distinto de cero) es positivo o negativo."""

def esPositivo(num):
    return num > 0

num = int(input("Ingrese un número: "))

if (esPositivo(num)):
    print(f"El número {num} es positivo.")
elif (esPositivo(num) == False and num != 0):
    print(f"El número {num} es negativo.")
else:
    print(f"El número es {num}.")