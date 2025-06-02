"""Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita
calcular el valor de un determinado número en dicha sucesión."""

# f(n)= {3, n=1 y f(n-1)+2n, n >= 2}


def f(n):
    if n == 1:
        return 3
    else:
        return f(n - 1) + 2 * n


n = int(input("Ingrese un número: "))

print(f"Resultado de f({n}) = {f(n)}")
