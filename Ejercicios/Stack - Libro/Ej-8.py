"""Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
cartas de baraja española–,resolver las siguientes actividades:
a. generar las cartas del mazo de forma aleatoria;
b. separar la pila mazo en cuatro pilas una por cada palo;
c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente."""

import sys
sys.path.append("./Clases")
from stack import Stack
from random import randint, shuffle

# a) 
def generate_deck():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    palos = ["espada", "oro", "copa", "basto"]
    cards = [(num, palo) for num in nums for palo in palos]
    shuffle(cards)
    
    stack = Stack()
    for card in cards:
        stack.push(card)
    return stack

# b)
def separate_cards(cards: Stack):
    espada = Stack()
    oro = Stack()
    basto = Stack()
    copa = Stack()
    
    while cards.size() > 0:
        card = cards.pop()
        if card[1]== "espada":
            espada.push(card)
        elif card[1]== "oro":
            oro.push(card)
        elif card[1]== "basto":
            basto.push(card)
        elif card[1]== "copa":
            copa.push(card)
            
    return oro, espada, copa, basto

# c) 
def sort_stack(stack: Stack):
    aux_stack = []
    sorted_stack = Stack()
    
    while stack.size() > 0:
        aux_stack.append(stack.pop())
        
    aux_stack.sort(key=lambda card: card[0])
    
    for card in reversed(aux_stack):
        sorted_stack.push(card)
        
    return sorted_stack

carta = generate_deck()
print("Mazo: ")
carta.show()

oro, espada, copa, basto = separate_cards(carta)

print("Mazo espada sin ordenar: ")
espada.show()

espada = sort_stack(espada)

print("Mazo espada ordenado: ")
espada.show()