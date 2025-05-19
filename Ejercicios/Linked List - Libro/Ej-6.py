"""Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar las funciones necesarias para poder
realizar las siguientes actividades:
a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic."""

import sys

sys.path.append("./Clases")
from lista_enlazada import List


class Superhero:
    def __init__(self, name, year, house, biography):
        self.name = name
        self.year = year
        self.house = house
        self.biography = biography

    def __str__(self):
        return f"Nombre: {self.name} \nAño: {self.year} \nCasa: {self.house} \nBiografía: {self.biography} \n"


superhero_list = List()
superhero_list.add_criterion("name", lambda sh: sh.name)
superhero_list.add_criterion("year", lambda sh: sh.year)
superhero_list.add_criterion("house", lambda sh: sh.house)
superhero_list.add_criterion("biography", lambda sh: sh.biography)

superhero_list.extend(
    [
        Superhero(
            "Linterna Verde",
            1940,
            "DC",
            "Posee un anillo de poder y viste un traje especial.",
        ),
        Superhero(
            "Wolverine",
            1974,
            "Marvel",
            "Tiene garras retráctiles y factor de curación.",
        ),
        Superhero("Dr. Strange", 1963, "DC", "Usa magia y viste una túnica."),
        Superhero(
            "Iron Man",
            1963,
            "Marvel",
            "Tony Stark usa una armadura de alta tecnología.",
        ),
        Superhero("Capitana Marvel", 1968, "Marvel", "Tiene poderes cósmicos."),
        Superhero(
            "Mujer Maravilla", 1941, "DC", "Princesa amazona con traje de batalla."
        ),
        Superhero("Flash", 1940, "DC", "Corre a velocidades increíbles."),
        Superhero("Star-Lord", 1976, "Marvel", "Usa una máscara y armadura espacial."),
        Superhero(
            "Batman", 1939, "DC", "Lucha contra el crimen con traje de murciélago."
        ),
        Superhero("Spider-Man", 1962, "Marvel", "Lleva un traje rojo y azul."),
        Superhero(
            "Magneto", 1963, "Marvel", "Controla el magnetismo y usa casco y armadura."
        ),
        Superhero("Superman", 1938, "DC", "Traje azul con capa roja."),
    ]
)


# a)
def delete_green_lantern(lista):
    lista.delete_value("Linterna Verde", "name")

print("a)")
delete_green_lantern(superhero_list)
superhero_list.show()


# b)
def year_wolverine(lista):
    index = lista.search("Wolverine", "name")
    if index is not None:
        print(f"Wolverine apareció en el año {lista[index].year}.")
    else:
        print("No se encontró Wolverine.")

print("b)")
year_wolverine(superhero_list)


# c)
def change_house(lista, hero, search_key):
    index = lista.search(hero, search_key)

    if index is not None:
        lista[index].house = "Marvel"

    return lista

print("c)")
change_house(superhero_list, "Dr. Strange", "name").show()


# d)
def show_suit_armor(lista):
    for hero in lista:
        bio = hero.biography.lower()
        if "traje" in bio or "armadura" in bio:
            print(hero.name)

print("d)")
show_suit_armor(superhero_list)


# e)
def show_before_1963(lista):
    for i in lista:
        if i.year < 1963:
            print(f"Nombre: {i.name} y casa: {i.house}")

print("e)")
show_before_1963(superhero_list)


# f)
def show_house(lista, superhero):
    index = lista.search(superhero, "name")

    return lista[index].house

print("f)")
print(f"Capitana Marvel - casa: {show_house(superhero_list, "Capitana Marvel")}")
print(f"Mujer Maravilla - casa: {show_house(superhero_list, "Mujer Maravilla")}")


# g)
def show_data(lista, superhero):
    index = lista.search(superhero, "name")

    if lista[index].name == superhero:
        return lista[index]

print("g)")
print(show_data(superhero_list, "Flash"))
print(show_data(superhero_list, "Star-Lord"))


# h)
def list_by_initial(lista):
    for i in lista:
        if i.name.startswith(("B", "M", "S")):
            print(i.name)

print("h)")
list_by_initial(superhero_list)


# i)
def count_by_house(lista):
    dc = 0
    marvel = 0
    for hero in lista:
        if hero.house == "DC":
            dc += 1
        if hero.house == "Marvel":
            marvel += 1
    return dc, marvel

print("i)")
dc, marvel = count_by_house(superhero_list)
print(f"Cantidad DC: {dc}")
print(f"Cantidad Marvel: {marvel}")
