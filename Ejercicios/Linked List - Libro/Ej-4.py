"""Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista."""

import sys

sys.path.append("./Clases")
from lista_enlazada import List

lista = List()


def insert_node(lista, pos, num):
    lista.insert(pos, num)

    return lista


lista.append(1)
lista.append(15)
lista.append(12)
lista.append(24)
lista.append(31)

insert_node(lista, 4, 5).show()
