"""Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM)
de dos número entero."""

def mcm(num1, num2):
    def mcd(num1, num2):
        if num2 == 0:
            return abs(num1)
        else:
            return mcd(num2, num1 % num2)
    
    if num1 == 0 or num2 == 0:
        return 0
    
    return abs(num1 * num2) // mcd(num1, num2)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print(f"MCM de {num1} y {num2} = {mcm(num1, num2)}")