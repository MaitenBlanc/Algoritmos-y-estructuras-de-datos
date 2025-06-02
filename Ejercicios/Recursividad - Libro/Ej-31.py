"""Por último, desarrollar otra función recursiva que permita calcular el método de Newton-Raphson de una función f(x)."""

# Método NR: aproximación de las raices de f
# x(n-1) = xn - (f(xn)/f'(xn))

def newton_method(f, df, x, max_iter, e=1e-10):
    if max_iter == 0 or abs(f(x)) < e:
        return x
    
    if abs(df(x)) < e:
        print(f"Error. Derivada casi nula en x={x}")
        return None
    
    next_x = x - f(x) / df(x)
    return newton_method(f, df, next_x, max_iter - 1, e)

def f(x):
    return x**2 - 2

def df(x):
    return 2*x 

result = newton_method(f, df, x=1, max_iter=10)
if result is not None:
    print(f"Método Newton-Raphson: {result:.6f}")