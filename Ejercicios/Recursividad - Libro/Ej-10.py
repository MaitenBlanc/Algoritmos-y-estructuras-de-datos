"""Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero."""

def contar_digitos(num):
    num = abs(num)
    
    if (num < 10):
        return 1
    else:
        return 1 + contar_digitos(num // 10)

numero = int(input("Ingrese un número: "))
print(f"Cantidad de dígitos del número {numero}: {contar_digitos(numero)}")