"""Desarrollar una función recursiva que permita calcular el método de la bisección de una función f(x)."""

# Objetivo: encontrar las raíces de f en [a,b]
# medio: m = (a+b) / 2
# Verificar f(a) * f(b) < 0 (si hay cambio de signo, la raíz está en ese intervalo)
# f(a) * f(m) < 0 --> raíz entre a y m
# f(b) * f(m) < 0 --> raíz entre m y b
# Tolerancia: máximo de pasos. Ej: 20


def bisection(f, a, b, max_iter):
    if max_iter == 0:
        return (a + b) / 2

    m = (a + b) / 2
    fm = f(m)

    if fm == 0:
        return m

    # base
    if f(a) * fm < 0:
        return bisection(f, a, m, max_iter - 1)
    else:
        return bisection(f, m, b, max_iter - 1)


def f(x):
    return x**2 - 2


print(f"Bisección de f(x): {round(bisection(f, 1, 2, 20),2)}")
print(f"Bisección de f(x): {round(bisection(f, 4, 5, 20),2)}")
