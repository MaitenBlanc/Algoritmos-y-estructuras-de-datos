"""Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena."""

def invertir_numero(numero, invertido = 0):
    if numero == 0:
        return invertido
    else: 
        ultimo_digito = numero % 10
        invertido = invertido * 10 + ultimo_digito
        return invertir_numero(numero // 10, invertido)
    
    
num = int(input("Ingresa un número: "))
print(f"Número {num} invertido: {invertir_numero(num)}")