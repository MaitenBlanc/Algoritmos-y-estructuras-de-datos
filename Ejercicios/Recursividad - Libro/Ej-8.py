"""Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario."""

def decimal_binario(decimal):
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        return decimal_binario(decimal // 2) + str(decimal % 2)
    
print(decimal_binario(81))