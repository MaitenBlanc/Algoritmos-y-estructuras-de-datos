"""Dada una lista de valores ordenadas, desarrollar un algoritmo que modifique el método de
búsqueda binaria para que funcione de forma recursiva, y permita determinar si un valor dado
está o no en dicha lista."""


def binary_search(v, value, start=0, end=None):
    if end is None: 
        end = len(v) - 1
        
    if start > end:
        return False
    else:
        middle = (start + end) // 2

        if v[middle] == value:
            return True
        elif value < v[middle]:
            return binary_search(v, value, start, middle - 1)
        else:
            return binary_search(v, value, middle + 1, end)

def show(v, value):
    if binary_search(v, value):
        print(f"El valor {value} se encuentra en la lista.")
    else:
        print(f"El valor {value} no se encuentra en la lista.")

v = [1, 2, 3, 4, 5]
search_value = int(input("Ingrese el valor a buscar: "))
show(v, search_value)
