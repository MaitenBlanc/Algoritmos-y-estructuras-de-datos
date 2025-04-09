"""Escriba un programa que permita el ingreso de un número de tres dígitos y determine si
es un número Armstrong (ej. 153, 371). Como el número que se ingresa posee 3 dígitos,
la suma de cada uno de sus dígitos elevado a 3 debe ser igual al número."""

num = int(input("Ingrese número de 3 dígitos: "))

def numArmstrong(num):
    unidad = int(num % 10)
    decena = int(num % 100 / 10)
    centena = int(num / 100)
    
    armstrong = unidad**3 + decena**3 + centena**3
    
    return armstrong

if (num == numArmstrong(num)):
    print(f"El número {num} es Armstrong.")
else:
    print(f"El número {num} no es Armstrong.")
    
