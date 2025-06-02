"""Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
obtener la siguiente información sin perder los datos:
a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
b. calcular el promedio de temperatura (o media) del total de valores;
c. determinar la cantidad de valores por encima y por debajo de la media."""

import sys

sys.path.append("./Clases")
from stack import Stack

temperature_stack = Stack()

temperatures = [
    22.5,
    21.8,
    20.0,
    19.5,
    18.3,
    20.1,
    21.0,
    22.0,
    23.2,
    24.0,
    25.1,
    26.3,
    27.0,
    23.5,
    21.2,
    20.8,
    19.9,
    18.0,
    17.5,
    19.0,
    20.5,
    22.0,
    24.5,
    26.0,
    27.5,
    25.0,
    23.3,
    21.7,
    20.4,
    19.2,
]

for t in temperatures:
    temperature_stack.push(t)


# a)
def temp_max_min(stack):
    aux_stack = Stack()
    min = 999999999
    max = -99999999

    while stack.size() > 0:
        temp = stack.pop()
        if temp < min:
            min = temp

        if temp > max:
            max = temp
        aux_stack.push(temp)

    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

    return min, max


min, max = temp_max_min(temperature_stack)
print(f"a) Temperatura mínima: {min}°")
print(f"   Temperatura máxima: {max}°")


# b)
def average_temperatures(stack):
    aux_stack = Stack()
    total = 0
    count = 0

    while stack.size() > 0:
        temp = stack.pop()
        total += temp
        count += 1
        aux_stack.push(temp)

    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

    return total / count if count > 0 else 0


avg = average_temperatures(temperature_stack)

print(f"b) Promedio de temperatura: {avg:.2f}°")


# c)
def amount_values(stack, avg):
    aux_stack = Stack()
    above = 0
    below = 0

    while stack.size() > 0:
        temp = stack.pop()
        if temp > avg:
            above += 1
        elif temp < avg:
            below += 1

        aux_stack.push(temp)

    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

    return above, below


above, below = amount_values(temperature_stack, avg)
print(f"c) Cantidad de valores por encima de la media: {above}")
print(f"   Cantidad de valores por debajo de la media: {below}")
