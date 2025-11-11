# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, 
# listadas a continuación:
# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;
# d. encontrar el árbol de expansión mínima;
# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
# h. debe utilizar un grafo no dirigido.

import sys

sys.path.append("./Clases")
from graph import Graph

import math

g = Graph(is_directed=False)

# a) h)
nodes_data = [
        ("Red Hat", "Notebook"), 
        ("Debian", "Notebook"), 
        ("Arch", "Notebook"),
        ("Manjaro", "PC"), 
        ("Parrot", "PC"), 
        ("Fedora", "PC"),
        ("Ubuntu", "PC"), 
        ("Mint", "PC"),
        ("Guaraní", "Servidor"), 
        ("MongoDB", "Servidor"),
        ("Switch 1", "Switch"), 
        ("Switch 2", "Switch"),
        ("Router 1", "Router"), 
        ("Router 2", "Router"), 
        ("Router 3", "Router"),
        ("Impresora", "Impresora")
]
for node, tipo in nodes_data:
        g.insert_vertex(node)

edges_data = [
        ('Red Hat', 'Router 2', 25),
        ('Debian', 'Switch 1', 17),
        ('Ubuntu', 'Switch 1', 18),
        ('Impresora', 'Switch 1', 22),
        ('Mint', 'Switch 1', 80),
        ('Switch 1', 'Router 1', 29),
        ('Router 1', 'Router 2', 37),
        ('Router 1', 'Router 3', 43),
        ('Router 2', 'Guaraní', 9),
        ('Router 2', 'Router 3', 50),
        ('Router 3', 'Switch 2', 61),
        ('Switch 2', 'Manjaro', 40),
        ('Switch 2', 'Parrot', 12),
        ('Switch 2', 'Fedora', 3),
        ('Switch 2', 'Arch', 56),
        ('Switch 2', 'MongoDB', 5)
]
for origin, destination, weigth in edges_data:
        g.insert_edge(origin, destination, weigth)

print("a) Grafo de red cargado")
g.show()

# b)
print("b) Barrido en profundidad: ")
notebooks = ["Red Hat", "Debian", "Arch"]
for notebook in notebooks: 
    g.deep_sweep(notebook)

print("b) Barrido en amplitud: ")
for notebook in notebooks: 
    g.amplitude_sweep(notebook)
    
# c)
print("c) Camino más corto a la impresora: ")
pcs = ["Manjaro", "Red Hat", "Fedora"]
for pc in pcs:
    path = g.dijkstra(pc)
    destination = 'Impresora'
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

    if peso_total is not None and peso_total is not math.inf:
        print(f'Camino desde {pc}: {" -> ".join(camino_completo)} (Costo: {peso_total})')
    else:
        print(f'No se encontró camino desde {pc} a la Impresora.')

# d)
print("d) Árbol de expansión mínima: ")
trees = g.kruskal("Impresora")

print(trees)

# e)
print("e) Camino más corto de pc a Guarani: ")
pcs = ["Ubuntu", "Mint", "Manjaro", "Fedora", "Parrot"]
for pc in pcs:
    path = g.dijkstra(pc)
    destination = 'Guarani'
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

if peso_total is not None:
    print(f'Camino desde {pc}: {" -> ".join(camino_completo)} (Costo: {peso_total})')
else:
    print(f'No se encontró camino desde {pc} al servidor Guarani.')

# f)
print("f) Camino más corto de switch1 a MongoDB: ")
pcs = ["Ubuntu", "Mint", "Debian"]
for pc in pcs:
    path = g.dijkstra(pc)
    destination = 'MongoDB'
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

    if peso_total is not None and peso_total is not math.inf:
        print(f'Camino desde {pc}: {" -> ".join(camino_completo)} (Costo: {peso_total})')

# g)
print("g) Cambio de conexión de la impresora al router 02")
g.delete_edge('Switch 1', 'Impresora', 'value')
print("Arista 'Switch 1 <-> Impresora' eliminada.")

g.insert_edge('Router 2', 'Impresora', 22)
print(f"Arista 'Router 2 <-> Impresora' creada.")

# Repito tarea b)
print("g) Barrido en profundidad: ")
for notebook in notebooks: 
    g.deep_sweep(notebook)

print("g) Barrido en amplitud: ")
for notebook in notebooks: 
    g.amplitude_sweep(notebook)