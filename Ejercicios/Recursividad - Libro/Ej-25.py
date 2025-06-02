"""Desarrollar una función recursiva que permita calcular y mostrar por pantalla el triángulo de
Pascal, para n filas utilizando una matriz auxiliar para guardar los resultados parciales
"""

# triangulo de pascal: (a+b)^n = a^n + a^(n-1)*b + a^(n-2)*b^2 + ... + b^n
# fila i y columna j = suma de (i-1, j-1) e (i-1, j)
# extremos siempre 1

def pascal_triangle(triangle, n, row=0, col=0):
    # base
    if row == n:
        return

    if col == 0 or col == row:
        triangle[row][col] = 1
    else:
        triangle[row][col] = triangle[row-1][col-1] + triangle[row-1][col]

    if col < row:
        pascal_triangle(triangle, n, row, col + 1)
    else:
        pascal_triangle(triangle, n, row + 1, 0)


def print_pascal(triangle, n):
    for i in range(n):
        for j in range(i + 1):
            print(triangle[i][j], end=" ")
        print()


def generate_triangle(n):
    triangle = [[0] * n for _ in range(n)]

    pascal_triangle(triangle, n)
    print_pascal(triangle, n)

generate_triangle(5)