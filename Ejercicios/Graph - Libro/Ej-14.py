# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, 
# sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los 
# ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de 
# red se necesitan para conectar el router con el Smart Tv.

import sys

sys.path.append("./Clases")
from graph import Graph

import math

g = Graph(is_directed=False)

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, 
# sala de estar, terraza, patio;
environments = [
    "Cocina", 
    "Comedor", 
    "Cochera", 
    "Quincho", 
    "Baño 1", 
    "Baño 2",
    "Habitación 1", 
    "Habitación 2", 
    "Sala de estar", 
    "Terraza", 
    "Patio"
]
for environment in environments:
    g.insert_vertex(environment)

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los 
# ambientes, se debe cargar en metros;
distancias = [
    # Ambiente 1: "Sala de estar" (5 aristas)
    ("Sala de estar", "Comedor", 2),
    ("Sala de estar", "Cocina", 5),
    ("Sala de estar", "Habitación 1", 3),
    ("Sala de estar", "Habitación 2", 3),
    ("Sala de estar", "Baño 2", 2),
    # Ambiente 2: "Cocina" (5 aristas, ya tiene sala de estar)
    ("Cocina", "Comedor", 3),
    ("Cocina", "Cochera", 6),
    ("Cocina", "Quincho", 3),
    ("Cocina", "Baño 1", 4),
    #  Ambiente 3: "Comedor" (3 aristas, ya tiene sala de estar y cocina)
    ("Comedor", "Cochera", 5),
    # Ambiente 4: "Habitación 1" (3 aristas, ya tiene sala de estar)
    ("Habitación 1", "Baño 1", 3),
    ("Habitación 1", "Baño 2", 2),
    # Ambiente 5: "Habitación 2" (3 aristas, ya tiene sala de estar)
    ("Habitación 2", "Baño 2", 2),
    ("Habitación 2", "Terraza", 4),
    # Ambiente 6: "Cochera" (3 aristas, ya tiene cocina y comedor)
    ("Cochera", "Patio", 4),
    # Ambiente 7: "Quincho" (3 aristas, ya tiene cocina)
    ("Quincho", "Baño 1", 2),
    ("Quincho", "Patio", 3),
    # Ambiente 8: "Patio" (3 aristas, ya tiene cochera y quincho)
    ("Patio", "Terraza", 5),
    # Ambiente 9: "Baño 1" (3 aristas, ya tiene cocina, habitación 1 y quincho)
    # Ambiente 10: "Baño 2" (3 aristas, ya tiene sala, habitación 1 y habitación 2)
    # Ambiente 11: "Terraza" (3 aristas, ya tiene habitación 2 y patio)
    ("Terraza", "Quincho", 2)
]

for origen, destino, peso in distancias:
    g.insert_edge(origen, destino, peso)

print("a) b) Grafo de ambientes de la casa cargado")
g.show()

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
print("c) Árbol de expansión mínima: ")
trees = g.kruskal("Sala de estar")
print(trees)

peso_total = 0
for edge in trees.split(';'):
    origin, destination, weight = edge.split('-')
    peso_total += int(weight)
print(f'Metros de cable que se necesitan: {peso_total}')

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de 
# red se necesitan para conectar el router con el Smart Tv.
print("d) Camino más corto de habitación 1 a sala de estar: ")
path = g.dijkstra('Habitación 1')
destination = 'Sala de estar'
peso_total = None
camino_completo = []
    
while path.size() > 0:
    value = path.pop()
    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]
        camino_completo.append(value[0])
        destination = value[2]
camino_completo.reverse()

if peso_total is not math.inf:
    print(f'Camino desde {" -> ".join(camino_completo)} (Costo: {peso_total})')
else:
    print(f'No se encontró camino desde habitación 1 a la sala de estar.')
