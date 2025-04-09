"""Escribir un programa que muestre un mensaje afirmativo si el número introducido es múltiplo de 5."""

def multiplo(num):
    return num % 5 == 0

num = int(input("Ingrese un número: "))

if (multiplo(num)):
    print(f"El número {num} es múltiplo de 5.")
else: 
    print(f"El número {num} no es múltiplo de 5.")
    