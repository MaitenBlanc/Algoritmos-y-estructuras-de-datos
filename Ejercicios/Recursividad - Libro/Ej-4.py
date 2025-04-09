"""Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y 
segundo el exponente."""

# potencia(b, e) = b^e

def potencia(b, e):
    if e == 1:
        return b
    else:
        return b * potencia(b, e-1)
    
print(potencia(4, 2))