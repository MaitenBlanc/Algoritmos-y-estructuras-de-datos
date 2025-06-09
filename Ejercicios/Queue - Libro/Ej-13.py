"""Dada una cola de 50000 caracteres generados aleatoriamente realizar las siguientes actividades:
a. separarla en dos colas una con dígitos y otra con el resto de los caracteres.
b. determinar cuántas letras hay en la segunda cola.
c. determinar además si existen los caracteres “?” y “#”."""

import sys

sys.path.append("./Clases")

from cola import Queue
from lista_enlazada import List
from string import ascii_letters, digits, punctuation
from random import choice


queue = Queue()
all_chars = ascii_letters + digits + punctuation

for i in range(50):
    queue.arrive(choice(all_chars))

# a)
def separate_queue(queue):
    digits_queue = Queue()
    others_queue = Queue()
    aux_queue = Queue()
    
    while queue.size() > 0:
        char = queue.attention()
        
        if char in digits:
            digits_queue.arrive(char)
        else:
            others_queue.arrive(char)

        aux_queue.arrive(char)
        
    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())
    
    return digits_queue, others_queue

digits_queue, others_queue = separate_queue(queue)
print("a) Cola de dígitos: ")
digits_queue.show()
print("Cola con resto de caracteres: ")
others_queue.show()

# b)
def count_letters(queue):
    aux_queue = Queue()
    count = 0
    
    while queue.size() > 0:
        char = queue.attention()
        
        if char in ascii_letters:
            count += 1

        aux_queue.arrive(char)
        
    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())
        
    return count

print(f"b) Cantidad de letras: {count_letters(others_queue)}")

# c)
def there_are_chars(queue, char_list: List):
    aux_queue = Queue()
    found = [False] * len(char_list)

    while queue.size() > 0:
        char = queue.attention()

        for i in range(len(char_list)):
            if char == char_list[i] and not found[i]:
                print(f"Existe el caracter '{char_list[i]}'.")
                found[i] = True
                
        aux_queue.arrive(char)        

    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())

print("c) ")
there_are_chars(queue, ["?", "#"])
