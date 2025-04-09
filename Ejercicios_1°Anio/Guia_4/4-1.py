"""Determinar si un número leído es positivo."""

def esPositivo(num):
    if(num > 0):
        print(f"El número {num} es positivo.")
    elif (num < 0):
        print(f"El número {num} es negativo.")
    else:
        print(f"El número es {num:.0f}.")
        
num = float(input("Ingrese un número: "))

print(esPositivo(num))