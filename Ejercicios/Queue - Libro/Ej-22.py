""" 
    Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género 
    (Masculino M y FemeninoF), por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., 
    desarrollar un algoritmo que resuelva las siguientes actividades:
    a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
    b. mostrar los nombre de los superhéroes femeninos;
    c. mostrar los nombres de los personajes masculinos;
    d. determinar el nombre del superhéroe del personaje Scott Lang;
    e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
    f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
"""

import sys
sys.path.append("./Clases")
from cola import Queue

queue = Queue()

queue.arrive({"name": "Tony Stark", "superhero": "Iron Man", "gender": "M"})
queue.arrive({"name": "Steve Rogers", "superhero": "Capitán América", "gender": "M"})
queue.arrive({"name": "Natasha Romanoff", "superhero": "Black Widow", "gender": "F"})
queue.arrive({"name": "Carol Danvers", "superhero": "Capitana Marvel", "gender": "F"})
queue.arrive({"name": "Scott Lang", "superhero": "Ant-Man", "gender": "M"})
queue.arrive({"name": "Bruce Banner", "superhero": "Hulk", "gender": "M"})
queue.arrive({"name": "Clint Barton", "superhero": "Hawkeye", "gender": "M"})
queue.arrive({"name": "Wanda Maximoff", "superhero": "Scarlet Witch", "gender": "F"})

# a) 
def show_name_captain_marvel(queue: Queue, name):
    for i in range(queue.size()):
        character = queue.attention()
        
        if character['superhero'] == name:
            char = character['name']
        
        queue.arrive(character)  
    return char

# b) 
def show_superheros_F(queue: Queue):
    for i in range(queue.size()):
        character = queue.attention()
        
        if character['gender'] == "F":
            print(f"- {character['superhero']}")
        
        queue.arrive(character)

# c) 
def show_superheros_M(queue: Queue):
    for i in range(queue.size()):
        character = queue.attention()
        
        if character['gender'] == "M":
            print(f"- {character['superhero']}")
        
        queue.arrive(character)
        
# d) 
def show_name_scott_lang(queue: Queue, superhero):
    for i in range(queue.size()):
        character = queue.attention()
        
        if character['name'] == superhero:
            char = character['superhero']
        
        queue.arrive(character)
    return char

# e)
def show_initial_s(queue: Queue):
    new_queue = Queue()
    for i in range(queue.size()):
        character = queue.attention()
        
        if character['name'][0] == "S" or character['superhero'][0] == "S":
            new_queue.arrive(character)
        
        queue.arrive(character)
    
    return new_queue

# f) determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
def search_carol(queue: Queue):
    for i in range(queue.size()):
        character = queue.attention()
        
        if character['name'] == "Carol Danvers":
            print(f"Carol Denvers se encuentra en la cola, su nombre de superhéroe es {character['superhero']}.")
        
        queue.arrive(character)


print(f"a) Nombre de Capitana Marvel: {show_name_captain_marvel(queue, 'Capitana Marvel')}")

print("b) Superhéroes femeninos:")
show_superheros_F(queue)

print("c) Superhéroes masculinos:")
show_superheros_M(queue)

print(f"d) Nombre de superhéroe de Scott Lang: {show_name_scott_lang(queue, 'Scott Lang')}")

print("e) Datos con letra 'S':")
show_initial_s(queue).show()

print("f) ")
search_carol(queue)