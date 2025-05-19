"""Dada una lista de números enteros eliminar de estas los números primos."""

import sys

sys.path.append("./Clases")
from lista_enlazada import List

lista = List()

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def delete_prime(lista):
    lista_aux = List()
    for num in lista:
        if not is_prime(num):
            lista_aux.append(num)
    lista.clear()
    lista.extend(lista_aux)
    
    return lista

lista.append(1)
lista.append(15)
lista.append(13)
lista.append(24)
lista.append(31)

delete_prime(lista).show()