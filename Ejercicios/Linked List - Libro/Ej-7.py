"""Implementar los algoritmos necesarios para resolver las siguientes tareas:
a. concatenar dos listas, una atrás de la otra;
b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
"""

import sys

sys.path.append("./Clases")
from lista_enlazada import List

lista_1 = List()
lista_2 = List()
lista_3 = List()

# a)
lista_1.extend([1, 2, 3, 4, 5])
lista_2.extend(["a", "b", "c", "d"])


def concat_lists(l1, l2):
    lista = List()

    for i in l1:
        lista.append(i)
    for i in l2:
        lista.append(i)

    return lista


print(concat_lists(lista_1, lista_2))


# b)
lista_3.extend([1, "b", 3, "d"])


def concat_without_duplicates(l1, l3):
    lista = List()
    for i in l1 + l3:
        if i not in lista:
            lista.append(i)
    return lista


print(concat_without_duplicates(lista_1, lista_3))


# c)
def count_repeated_elements(l1, l3):
    elements = 0
    for i in l1:
        if i in l3:
            elements += 1
    return elements


print(count_repeated_elements(lista_1, lista_3))


# d)
def delete_nodes(lista):
    while lista:
        value = lista[0]
        deleted = lista.delete_value(value)
        print(f"Elemento eliminado: {deleted}")


delete_nodes(lista_1)
