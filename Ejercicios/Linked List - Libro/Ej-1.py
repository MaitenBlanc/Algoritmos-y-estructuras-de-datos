"""Diseñar un algoritmo que permita contar la cantidad de nodos de una lista."""

import sys

sys.path.append("./Clases")
from lista_enlazada import List

list = List()


def count_nodes(list):
    count = 0
    for i in list:
        count += 1
    return count


list = [1, 2, 3, 4, 5]

print(count_nodes(list))
