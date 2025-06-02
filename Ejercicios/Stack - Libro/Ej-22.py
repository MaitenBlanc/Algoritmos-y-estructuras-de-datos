"""Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The Mandalorian), las
cuales se almacenaban en una pila (en su correspondiente nave) en cada misión de caza que emprendió, con la
siguiente información: planeta visitado, a quien capturó, costo de la recompensa. Resolver las siguientes
actividades:
a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno de los cazzarrecompensas;
b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos quien obtuvo mayor
fortuna;
c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la que Boba Fett capturo
a Han Solo, suponga que dicha misión está cargada;
d. indicar la cantidad de capturas realizadas por cada cazarrecompensas."""

import sys

sys.path.append("./Clases")
from stack import Stack

boba_fett_stack = Stack()
din_djarin_stack = Stack()

# Misiones de Boba Fett
boba_fett_stack.push(("Tatooine", "Han Solo", 5000))
boba_fett_stack.push(("Kamino", "Cad Bane", 3000))
boba_fett_stack.push(("Bespin", "Lando Calrissian", 3500))

# Misiones de Din Djarin
din_djarin_stack.push(("Nevarro", "Mythrol", 2000))
din_djarin_stack.push(("Sorgan", "Raider", 1500))
din_djarin_stack.push(("Tatooine", "Fennec Shand", 4000))

# Función para no repetir código al clonar una pila sin modificar la original
def clone_stack(stack):
    aux_stack = Stack()
    clon_stack = Stack()
    
    while stack.size() > 0:
        element = stack.pop()
        aux_stack.push(element)
        
    while aux_stack.size() > 0: 
        element = aux_stack.pop()
        stack.push(element)
        clon_stack.push(element)
        
    return clon_stack

# a)
def show_planets(stack, name):
    print(f"{name} visitó los siguientes planetas: ")
    aux_stack = clone_stack(stack)
    temp = []
    
    while aux_stack.size() > 0:
        mission = aux_stack.pop()
        temp.append(mission[0])
    
    temp.reverse()
    for i, planet in enumerate(temp, start=1):
        print(f"Misión {i}: {planet}")

print("a) ")
show_planets(boba_fett_stack, "Boba Fett")
show_planets(din_djarin_stack, "Din Djarin")

# b)
def calc_total_reward(stack):
    aux = clone_stack(stack)
    total = 0

    while aux.size() > 0:
        mission = aux.pop()
        total += mission[2]

    return total

total_boba = calc_total_reward(boba_fett_stack)
total_din = calc_total_reward(din_djarin_stack)

print(f"b) Total recaudado por Boba Fett: {total_boba} créditos.")
print(f"   Total recaudado por Din Djarin: {total_din} créditos.")

if total_boba > total_din:
    print(f"   Boba Fett recaudó mayor fortuna.")
else:
    print(f"   Din Djarin recaudó mayor fortuna.")

# c)
def mission_han_solo(stack):
    aux = clone_stack(stack)
    missions = []

    while aux.size() > 0:
        missions.append(aux.pop())

    missions.reverse()
    for i, mission in enumerate(missions):
        if mission[1] == "Han Solo":
            return i + 1

    return None

print(f"c) Número de misión en la que Boba Fett capturó a Han Solo: {mission_han_solo(boba_fett_stack)}")

# d)
def count_captures(stack):
    return stack.size()

print(f"d) Cantidad de capturas de Boba Fett: {count_captures(boba_fett_stack)}")
print(f"d) Cantidad de capturas de Din Djarin: {count_captures(din_djarin_stack)}")
