"""Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante."""

# v = [1,2,3,4,5]
# v = 5
# v = 4
# v = 3
# v = 2
# v = 1


def show_vector(v, index):
    if index < 0:
        return

    print(v[index], end=" ")
    show_vector(v, index - 1)


v = [1, 2, 3, 4, 5]
show_vector(v, len(v)-1)
