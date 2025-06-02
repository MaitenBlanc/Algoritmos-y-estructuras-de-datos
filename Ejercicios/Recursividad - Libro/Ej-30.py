"""Desarrollar también una función recursiva que permita calcular el método de la secante de
una función f(x)."""

# secante: x(n+1) = x1 - f(x1) * (x1 - x0)/(f(x1) - f(x0))
# e = epsilon (para que no considere que los valores son iguales cuando son parecidos)


def secant(f, x0, x1, max_iter, e=1e-10):
    if max_iter == 0 or abs(x1 - x0) < e:
        return x1

    f_x0 = f(x0)
    f_x1 = f(x1)

    if abs(f_x1 - f_x0) < e:
        print(f"Error. División por cero: f({x1:.6f}) - f({x0:.6f}) = 0")
        return None

    x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
    return secant(f, x1, x2, max_iter - 1, e)


def f(x):
    return x**2 - 2


result = secant(f, 1, 2, 10)
if result is not None:
    print(f"Secante de f(x): {result:.6f}")
