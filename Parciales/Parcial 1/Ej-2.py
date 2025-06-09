"""
Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
a) Listado ordenado de manera ascendente por nombre de los personajes.
b) Determinar en que posicion esta The Thing y Rocket Raccoon.
c) Listar todos los villanos de la lista.
d) Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
e) Listar los superheores que comienzan con  Bl, G, My, y W.
f) Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
g) Listado de superheroes ordenados por fecha de aparación.
h) Modificar el nombre real de Ant Man a Scott Lang.
i) Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
j) Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
"""

from super_heroes_data import superheroes
from cola import Queue
from lista_enlazada import List


class Superheroes:

    def __init__(
        self, name, real_name, first_appearance, short_bio=None, is_villain=False
    ):
        self.name = name
        self.real_name = real_name
        self.first_appearance = first_appearance
        self.short_bio = short_bio
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name} ({self.real_name}) - {self.first_appearance}"


def order_by_name(item):
    return item.name


def order_by_real_name(item):
    return item.real_name if item.real_name is not None else ""


def order_by_first_appearance(item):
    return item.first_appearance


list_superheroes = List(
    [
        Superheroes(
            name=hero["name"],
            real_name=hero["real_name"],
            first_appearance=hero["first_appearance"],
            short_bio=hero["short_bio"],
            is_villain=hero["is_villain"],
        )
        for hero in superheroes
    ]
)

list_superheroes.add_criterion("name", order_by_name)
list_superheroes.add_criterion("real_name", order_by_real_name)
list_superheroes.add_criterion("first_appearance", order_by_first_appearance)

# a)
print("a) Listado ordenado por nombre: ")
list_superheroes.sort_by_criterion("name")
list_superheroes.show()

# b)
pos_thing = list_superheroes.search("The Thing", "name")
pos_rocket = list_superheroes.search("Rocket Raccoon", "name")
print("\nb) ")
print(f"La posición de The Thing es: {pos_thing}")
print(f"La posición de Rocket Raccoon es: {pos_rocket}")

# c)
villains = List()

for s in list_superheroes:
    if s.is_villain:
        villains.append(s)

print("\nc) Villanos en la lista: ")
villains.show()

# d)
queue_villains = Queue()

for v in villains:
    queue_villains.arrive(v)

print("\nd) Villanos que aparecieron antes de 1980")
while queue_villains.size() > 0:
    villain = queue_villains.attention()

    if villain.first_appearance < 1980:
        print(f"{villain.name} ({villain.first_appearance})")

# e)
prefixes = ("Bl", "G", "My", "W")

filtered_superheroes = List()
for s in list_superheroes:
    if s.name.startswith(prefixes):
        filtered_superheroes.append(s)
print("\ne) Superheores que comienzan con  Bl, G, My, y W")
filtered_superheroes.show()

# f)
print("\nf) Listado ordenado por nombre real : ")
list_superheroes.sort_by_criterion("real_name")
list_superheroes.show()

# g)
print("\ng) Listado ordenado por fecha de aparición : ")
list_superheroes.sort_by_criterion("first_appearance")
list_superheroes.show()

# h)
pos_antman = list_superheroes.search("Ant Man", "name")
if pos_antman is not None:
    list_superheroes[pos_antman].real_name = "Scott Lang"

print("\nh) Modificación del nombre real de Ant Man")
print(f"{list_superheroes[pos_antman]}")

# i)
print("\ni) Personajes que en su biografia incluyen la palabra time-traveling o suit")
for s in list_superheroes:
    bio = s.short_bio.lower()
    if "time-traveling" in bio or "suit" in bio:
        print(f"- {s.name}")

# j) Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
eliminated_list = List()
names = ["Electro", "Baron Zemo"]
for name in names:
    pos = list_superheroes.search(name, "name")

    if pos is not None:
        eliminated = list_superheroes.pop(pos)
        eliminated_list.append(eliminated)

print("\nj)")
for e in eliminated_list:
    print(f"Eliminado: {e}")
