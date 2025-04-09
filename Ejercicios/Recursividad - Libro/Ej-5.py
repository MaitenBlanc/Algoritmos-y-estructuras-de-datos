"""Desarrollar una función que permita convertir un número romano en un número decimal."""

def romano_decimal(n_romano, valores=None):
    
    if valores is None:
        valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
    if not n_romano:
        return 0
    
    if len(n_romano) > 1 and valores[n_romano[0]] < valores[n_romano[1]]:
        return valores[n_romano[1]] - valores[n_romano[0]] + romano_decimal(n_romano[2:], valores)
    
    return valores[n_romano[0]] + romano_decimal(n_romano[1:], valores)

result = romano_decimal("XIV")
print(result)