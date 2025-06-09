"""Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
b. indicar el plantea natal de Luke Skywalker y Han Solo
c. insertar un nuevo personaje antes del maestro Yoda
d. eliminar el personaje ubicado después de Jar Jar Binks"""

import sys

sys.path.append("./Clases")
from cola import Queue
from lista_enlazada import List


class Char:
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def __str__(self):
        return f"{self.name} - Planeta: {self.planet}"


characters = [
    {"name": "Luke Skywalker", "planet": "Tatooine"},
    {"name": "Leia Organa", "planet": "Alderaan"},
    {"name": "Han Solo", "planet": "Corellia"},
    {"name": "Chewbacca", "planet": "Kashyyyk"},
    {"name": "Yoda", "planet": "Dagobah"},
    {"name": "Jar Jar Binks", "planet": "Naboo"},
    {"name": "Wicket W. Warrick", "planet": "Endor"},
    {"name": "Darth Vader", "planet": "Tatooine"},
    {"name": "Obi-Wan Kenobi", "planet": "Stewjon"},
    {"name": "Ewok", "planet": "Endor"},
]

queue_star_wars = Queue()
for char in characters:
    queue_star_wars.arrive(char)


# a)
def show_by_planets(queue, planets: List):
    aux_queue = Queue()
    planet_stacks = {planet: [] for planet in planets}

    while queue.size() > 0:
        char = queue.attention()

        if char["planet"] in planets:
            planet_stacks[char["planet"]].append(char["name"])
        aux_queue.arrive(char)

    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())

    for planet in planets:
        print(f"Personajes de {planet}:")
        if planet_stacks[planet]:
            for name in planet_stacks[planet]:
                print(f"- {name}")
        else:
            print(f"No hay personajes en {planet}.")


print("a) ")
show_by_planets(queue_star_wars, ["Alderaan", "Endor", "Tatooine"])


# b)
def show_home_planet(queue, char_list: List):
    aux_queue = Queue()

    while queue.size() > 0:
        char = queue.attention()

        if char["name"] in char_list:
            print(f"{char["name"]} es del planeta {char["planet"]}.")
        aux_queue.arrive(char)

    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())


print("b) ")
show_home_planet(queue_star_wars, ["Luke Skywalker", "Han Solo"])

# c)
def insert_before_yoda(queue, new_char):
    aux_queue = Queue()
    
    while queue.size() > 0:
        char = queue.attention()
        
        if char["name"] == "Yoda":
            aux_queue.arrive(new_char)
        aux_queue.arrive(char)
        
    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())
    
    return queue

print("c) ")
new_char = {"name": "Ahsoka Tano", "planet": "Shili"}
insert_before_yoda(queue_star_wars, new_char).show()

# d)
def delete_after_char(queue: Queue, name):
    aux = Queue()
    delete_next = False
    
    while queue.size() > 0:
        character = queue.attention()
        if delete_next:
            delete_next = False
            continue
        if character["name"] == name:
            delete_next = True
        aux.arrive(character)
        
    while aux.size() > 0:
        queue.arrive(aux.attention())
        
    return queue

print("d) ")
delete_after_char(queue_star_wars, "Jar Jar Binks").show()