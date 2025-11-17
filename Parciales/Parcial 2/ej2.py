# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que  aparecieron juntos ambos personajes 
# que se relacionan;
# b. hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# c. determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
# e. calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# f. indicar qué personajes aparecieron en los nueve episodios de la saga.

from graph import Graph

g = Graph(is_directed=False)

# # a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que 
# aparecieron juntos ambos personajes que se relacionan;
# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
characters = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
    "C-3PO", "Leia", "Rey", "Kylo Ren", 
    "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]
# Carga vértices
for character in characters:
    g.insert_vertex(character)

# Carga aristas
g.insert_edge("Luke Skywalker", "Leia", 5)
g.insert_edge("Luke Skywalker", "Han Solo", 4)
g.insert_edge("Luke Skywalker", "Yoda", 3)
g.insert_edge("Luke Skywalker", "Darth Vader", 4)
g.insert_edge("Luke Skywalker", "R2-D2", 6)
g.insert_edge("Luke Skywalker", "C-3PO", 6)

g.insert_edge("Leia", "Han Solo", 5)
g.insert_edge("Leia", "C-3PO", 8)
g.insert_edge("Leia", "R2-D2", 8)
g.insert_edge("Leia", "Chewbacca", 5)
g.insert_edge("Leia", "Rey", 2)

g.insert_edge("Han Solo", "Chewbacca", 6)
g.insert_edge("Han Solo", "R2-D2", 4)
g.insert_edge("Han Solo", "Kylo Ren", 1)

g.insert_edge("Chewbacca", "Yoda", 1)
g.insert_edge("Chewbacca", "Rey", 3)

g.insert_edge("C-3PO", "R2-D2", 9)
g.insert_edge("C-3PO", "Rey", 3)
g.insert_edge("C-3PO", "Chewbacca", 6)

g.insert_edge("Darth Vader", "Boba Fett", 2)
g.insert_edge("Darth Vader", "Yoda", 0)

g.insert_edge("Rey", "Kylo Ren", 3)
g.insert_edge("Rey", "BB-8", 3)
g.insert_edge("BB-8", "R2-D2", 2)

# b. hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
print("b) Árbol de expansión mínimo: ")
print("Desde C-3PO: ")
print(g.kruskal("C-3PO"))

print("Desde Yoda: ")
print(g.kruskal("Yoda"))

print("Desde Leia: ")
print(g.kruskal("Leia"))

# c. determinar cuál es el número máximo de episodio que comparten dos  personajes, e indicar todos los pares de personajes que coinciden con dicho  número;
max_episodes = 0
pairs = []

for vertex in g:
    for edge in vertex.edges:
        if edge.weight > max_episodes:
            max_episodes = edge.weight
            pairs = [(vertex, edge)]
        elif edge.weight == max_episodes:
            pairs.append((vertex, edge))

print(f"c) Número máximo de episodios compartidos: {max_episodes}")
print(f"   Pares de personajes que comparten el número máximo de episodios: ")
for p1, p2 in pairs: 
    print(f"- {p1.value} y {p2.value}")

# e. calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
def show_path(g, origin, destination):
    path = g.dijkstra(origin)
    total_weight = None
    full_path = []
    current_destination = destination
    
    while path.size() > 0:
        value = path.pop()
        if value[0] == current_destination:
            if total_weight is None:
                total_weight = value[1]
            full_path.append(value[0])
            current_destination = value[2]
    
    full_path.reverse()
    print(f'{" - ".join(full_path)} con un costo de {total_weight}')

print(f"e) Caminos mas cortos: ")
show_path(g, "C-3PO", "R2-D2")
show_path(g, "Yoda", "Darth Vader")

# f. indicar qué personajes aparecieron en los nueve episodios de la saga.
found = []
for vertex in g:
    for edge in vertex.edges:
        if edge.weight == 9:
            found.append(vertex.value)
print(f"f) Personajes que aparecieron en los nueve episodios de la saga: {found}")