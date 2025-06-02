"""Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita
calcular el valor de un determinado número en dicha sucesión."""

# f(n) { 2, n=1 y (n+(1/f(n-1))), n>=2}

def sequence(n):
    if n == 1:
        return 2

    return n + (1 / sequence(n - 1))


def show_sequence(n):
    def print_seq(i):
        if i > n:
            return

        print(f"f({i}) = {sequence(i)}")
        print_seq(i + 1)

    print_seq(1)

n = int(input("Ingrese un número: "))
show_sequence(n)

