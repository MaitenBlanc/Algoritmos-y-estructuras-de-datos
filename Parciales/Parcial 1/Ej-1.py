"""Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
a) funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
b) funcion recursiva para listar los superheroes de la lista."""

superheroes = [
    "Iron Man",
    "Thor",
    "Hulk",
    "Spider-Man",
    "Black Widow",
    "Hawkeye",
    "Doctor Strange",
    "Black Panther",
    "Ant-Man",
    "Wasp",
    "Scarlet Witch",
    "Vision",
    "Falcon",
    "Winter Soldier",
    "Capitan America",
]


# a)
def search_superhero(lista, name, index=0):
    if index >= len(lista):
        return False

    if lista[index] == name:
        return True

    return search_superhero(lista, name, index + 1)


# b)
def list_superheroes(lista, index=0):
    if index >= len(lista):
        return

    print(lista[index])
    return list_superheroes(lista, index + 1)


print("a) ")
if search_superhero(superheroes, "Capitan America"):
    print("Capitan America está en la lista.")
else:
    print("Capitan America no está en la lista.")


print("b) Lista de superheroes: ")
list_superheroes(superheroes)
