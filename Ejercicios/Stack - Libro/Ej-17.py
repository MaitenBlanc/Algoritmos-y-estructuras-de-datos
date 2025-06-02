"""Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales, consonantes y otros
caracteres que no sean letras (signos de puntuación números, espacios, etc.). Luego utilizando las operaciones
de pila resolver las siguientes consignas:
a. cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);
b. cantidad de espacios en blanco;
c. porcentaje que representan las vocales respecto de las consonantes sobre el total de caracteres del párrafo;
d. cantidad de números;
e. determinar si la cantidad de vocales y otros caracteres son iguales;
f. determinar si existe al menos una z en la pila de consonantes."""

import sys

sys.path.append("./Clases")
from stack import Stack

vowels = Stack()
consonants = Stack()
others = Stack()


def separate_stack(paragraph):
    for char in paragraph:
        char = char.lower()

        if char in "aeiou":
            vowels.push(char)
        elif char.isalpha():
            consonants.push(char)
        else:
            others.push(char)


paragraph = "Luke Skywalker nació en Tatooine, un planeta desértico, y fue entrenado por Yoda como Jedi durante 2 semanas."

separate_stack(paragraph)

# a)
print(f"a) Cantidad de vocales: {vowels.size()}")
print(f"   Cantidad de consonantes: {consonants.size()}")
print(f"   Cantidad de caracteres que no son letras: {others.size()}")

# b)
blank = 0
aux_stack = Stack()

while others.size() > 0:
    element = others.pop()
    if element == " ":
        blank += 1

    aux_stack.push(element)

while aux_stack.size() > 0:
    others.push(aux_stack.pop())

print(f"b) Cantidad de espacios en blanco: {blank}")

# c)
if consonants.size() > 0:
    vowel_percentage = (vowels.size() / consonants.size()) * 100
else:
    vowel_percentage = 0

print(f"c) Porcentaje de vocales respecto a consonantes: {vowel_percentage:.2f}%.")

# d)
number_count = 0
while others.size() > 0:
    e = others.pop()

    if e.isdigit():
        number_count += 1
    aux_stack.push(e)

while aux_stack.size() > 0:
    others.push(aux_stack.pop())

print(f"d) Cantidad de números: {number_count}")

# e)
if vowels.size() == others.size():
    print(
        f"e) La cantidad de vocales ({vowels.size()}) y otros caracteres ({others.size()}) son iguales."
    )
else:
    print(
        f"e) La cantidad de vocales ({vowels.size()}) y otros caracteres ({others.size()}) no son iguales."
    )

# f)
while consonants.size() > 0: 
    c = consonants.pop()
    found = False
    
    if c.lower() == 'z':
        found = True
        
    aux_stack.push(c)
    
while aux_stack.size() > 0:
    consonants.push(aux_stack.pop())
    
if found: 
    print(f"f) Existe al menos una z en la pila de consonantes.")
else:
    print(f"f) No existe ninguna z en la pila de consonantes.")
    