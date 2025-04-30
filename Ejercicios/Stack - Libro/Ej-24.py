""" 
    Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que 
    participó, implementar las funciones necesarias para resolver las siguientes actividades:
    a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
    b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
    c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
    d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
"""
import sys
sys.path.append("./Clases")
from stack import Stack

stack_characters = Stack()

stack_characters.push({'name': 'Iron Man', 'movies': 10})
stack_characters.push({'name': 'Captain America', 'movies': 9})
stack_characters.push({'name': 'Thor', 'movies': 8})
stack_characters.push({'name': 'Black Widow', 'movies': 7})
stack_characters.push({'name': 'Hulk', 'movies': 6})
stack_characters.push({'name': 'Hawkeye', 'movies': 5})
stack_characters.push({'name': 'Groot', 'movies': 4})
stack_characters.push({'name': 'Doctor Strange', 'movies': 5})
stack_characters.push({'name': 'Gamora', 'movies': 4})
stack_characters.push({'name': 'Rocket Raccoon', 'movies': 4})
stack_characters.push({'name': 'Drax', 'movies': 4})
stack_characters.push({'name': 'Captain Marvel', 'movies': 3})

# a) 
def pos_rocket_groot(stack, characters):
    aux_stack = Stack()
    position_stack = {}
    pos = 1
    
    while stack.size() > 0:
        character = stack.pop()
        
        if character['name'] in characters:
            position_stack[character['name']] = pos
        aux_stack.push(character)
        pos += 1
    
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())
        
    return position_stack

# b)
def more_than_5(stack, n):
    aux_stack = Stack()
    result = Stack()
    
    while stack.size() > 0:
        char = stack.pop()
        
        if char['movies'] > n:
            result.push(char)
        aux_stack.push(char)
        
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())
        
    return result

# c)
def count_movies(stack, character):
    aux_stack = Stack()
    counter = 0
    
    while stack.size() > 0:
        char = stack.pop()
        
        if char['name'] == character:
            counter = char['movies']
        
        aux_stack.push(char)
    
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

    return counter

# d) 
def show_by_initial(stack, initials):
    aux_stack = Stack()
    characters = Stack()
    
    while stack.size() > 0:
        character = stack.pop()
        
        if character['name'][0] in initials:
            characters.push(character['name'])
        
        aux_stack.push(character)

    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())
        
    return characters

print("a) Posición de Rocket Raccoon y Groot: ")
print(pos_rocket_groot(stack_characters, ["Rocket Raccoon", "Groot"]))

print("b) Personajes que participaron en más de 5 películas: ")
more_than_5(stack_characters, 5).show()

print(f"c) Películas donde participó la 'Viuda Negra': {count_movies(stack_characters, "Black Widow")}")

print("d) Personajes cuyos nombre empiezan con C, D y G")
show_by_initial(stack_characters, ["C", "D", "G"]).show()