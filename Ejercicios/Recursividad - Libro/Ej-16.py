"""Implementar una función recursiva que permita obtener el valor de an en una sucesión geomé-
trica (o progresión geométrica) con un valor a1= 2 y una razón r = -3. Además desarrollar un
algoritmo que permita visualizar todos los valores de dicha sucesión desde a1 hasta an.
"""

# a, a r, a r^2, a r^3, a r^4, ..., an r^(n-1)


def sequence(n):
    a1 = 2
    r = -3

    if n == 1:
        return a1

    return r * sequence(n - 1)


def show_sequence(n):
    def print_seq(i):
        if i > n:
            return

        print(f"a{i} = {sequence(i)}")
        print_seq(i + 1)

    print_seq(1)


n = int(input("Ingrese número: "))
print(f"Sucesión geométrica hasta a{n}")
show_sequence(n)
