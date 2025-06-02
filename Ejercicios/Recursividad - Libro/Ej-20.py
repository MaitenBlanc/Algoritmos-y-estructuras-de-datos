"""Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de
manera recursiva, y permita determinar si un valor dado está o no en dicha lista."""


def sentinel_search(v, value, i=0):
    if i == 0:
        v = v + [value]

    if v[i] == value:
        if i < len(v) - 1:
            return True
        else:
            return False

    return sentinel_search(v, value, i + 1)

def show(v, value):
    found = sentinel_search(v, value)
    
    if found:
        print(f"El elemento {value} se encuentra en la lista.")
    else:
        print(f"El elemento {value} no se encuentra en la lista.")


v = [3, 8, 1, 9, 5]
show(v, 9)
show(v, 2)



