"""Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero.
Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro
el número a calcular su raíz."""


def raiz_cuadrada(n):
    def raiz_cuadrada_aux(n, i):
        if i * i > n:
            return i - 1
        return raiz_cuadrada_aux(n, i + 1)

    if n < 0:
        return "El número debe ser entero no negativo."
    return raiz_cuadrada_aux(n, 0)


n = int(input("Ingrese número: "))
print(raiz_cuadrada(n))
