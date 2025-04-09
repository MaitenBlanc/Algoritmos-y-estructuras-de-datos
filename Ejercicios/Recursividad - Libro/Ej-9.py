"""Implementar una función para calcular el logaritmo entero de número n en una base b. Recuerde que:
        log b (n/b) = log b n + log b b    
"""

# log b n --> b^result = n
#             result = n // b

def logaritmo(n, b):
    if n < b:
        return 0
    else:
        return 1 + logaritmo(n // b, b)

print(logaritmo(1000, 10))