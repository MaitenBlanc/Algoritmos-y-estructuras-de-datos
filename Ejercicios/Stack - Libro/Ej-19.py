"""Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, desarrollar
las funciones necesarias para resolver las siguientes actividades:
a. mostrar los nombre películas estrenadas en el año 2014;
b. indicar cuántas películas se estrenaron en el año 2018;
c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
"""

import sys

sys.path.append("./Clases")
from stack import Stack

movie_stack = Stack()

movie_stack.push(("Interstellar", "Paramount", 2014))
movie_stack.push(("Pulp Fiction", "Miramax Films", 1994))
movie_stack.push(("Guardians of the Galaxy", "Marvel Studios", 2014))
movie_stack.push(("The Matrix", "Warner Bros. Pictures", 1999))
movie_stack.push(("La La Land", "Lionsgate", 2016))
movie_stack.push(("The Pianist", "Babelsberg", 2002))
movie_stack.push(("The Machinist", "Filmax Group", 2004))
movie_stack.push(("Bohemian Rhapsody", "20th Century Fox", 2018))
movie_stack.push(("Doctor Strange", "Marvel Studios", 2016))

movies_2014 = Stack()
movies_2018 = Stack()
movies_2016 = Stack()
aux_stack = Stack()
count_2018 = 0

while movie_stack.size() > 0:
    movie = movie_stack.pop()
    aux_stack.push(movie)
    
    if movie[2] == 2014:
        movies_2014.push(movie)

    if movie[2] == 2018:
        count_2018 += 1

    if movie[2] == 2016 and movie[1] == "Marvel Studios":
        movies_2016.push(movie)

while aux_stack.size() > 0:
    movie_stack.push(aux_stack.pop())


print("a) Películas estrenadas en 2014: ")
while movies_2014.size() > 0:
    movie = movies_2014.pop()
    print(f"- {movie[0]}")
    
    aux_stack.push(movie)

while aux_stack.size() > 0:
    movies_2014.push(aux_stack.pop())

print(f"b) Cantidad de películas estrenadas en 2018: {count_2018}")

print("c) Películas de Marvel Studios estrenadas en 2016: ")
while movies_2016.size() > 0:
    movie = movies_2016.pop()
    print(f"- {movie[0]} / {movie[2]}")
    
    aux_stack.push(movie)

while aux_stack.size() > 0:
    movies_2016.push(aux_stack.pop())
