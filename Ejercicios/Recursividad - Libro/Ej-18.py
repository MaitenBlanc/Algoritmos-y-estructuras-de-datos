"""Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores."""


def show_matrix(m, i=0, j=0):
    if i >= len(m):
        return

    if j >= len(m[i]):
        print()
        show_matrix(m, i + 1, 0)
        return

    print(m[i][j], end=" ")
    show_matrix(m, i, j + 1)

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

show_matrix(m)