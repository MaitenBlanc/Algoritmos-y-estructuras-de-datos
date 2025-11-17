# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales 
# se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma 
# gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando 
# lo siguiente:
# a. los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b. mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad,
# es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
# c. mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
# d. realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
# e. mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
# f. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
# g. determinar cuantos Pokémons tienen megaevolucion.
# h. determinar cuantos Pokémons tiene forma gigamax.

from tree import BinaryTree


# Formato: [nombre, numero, tipos, debilidades, mega, giga] 
data_pokemons = [
    ["Bulbasaur", 1, ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psiquico"], False, True],
    ["Charmander", 4, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False],
    ["Charizard", 6, ["Fuego", "Volador"], ["Roca", "Electrico", "Agua"], True, True],
    ["Squirtle", 7, ["Agua"], ["Electrico", "Planta"], False, False],
    ["Pikachu", 25, ["Electrico"], ["Tierra"], False, True],
    ["Jolteon", 135, ["Electrico"], ["Tierra"], False, False],
    ["Lycanroc", 745, ["Roca"], ["Agua", "Planta", "Tierra", "Acero", "Lucha"], False, False],
    ["Tyrantrum", 697, ["Roca", "Dragon"], ["Hielo", "Hada", "Tierra", "Acero", "Lucha", "Dragon"], False, False],
    ["Gastly", 92, ["Fantasma", "Veneno"], ["Fantasma", "Siniestro", "Psiquico", "Tierra"], False, False],
    ["Magnemite", 81, ["Electrico", "Acero"], ["Tierra", "Fuego", "Lucha"], False, False],
    ["Steelix", 208, ["Acero", "Tierra"], ["Fuego", "Agua", "Lucha", "Tierra"], True, False],
    ["Gengar", 94, ["Fantasma", "Veneno"], ["Fantasma", "Siniestro", "Psiquico", "Tierra"], True, True],
    ["Aegislash", 681, ["Acero", "Fantasma"], ["Fuego", "Tierra", "Fantasma", "Siniestro"], False, False],
    ["Rotom", 479, ["Electrico", "Fantasma"], ["Fantasma", "Siniestro"], False, False],
    ["Heatran", 485, ["Fuego", "Acero"], ["Tierra", "Lucha", "Agua"], False, False]
]

name_tree = BinaryTree()
number_tree = BinaryTree()
type_tree = BinaryTree()

# a. los índices de cada uno de los árboles deben ser nombre, número y tipo;
for pokemon in data_pokemons:
    # Índice nombre
    name_tree.insert(pokemon[0], pokemon)
    
    # Índice número
    number_tree.insert(pokemon[1], pokemon)
    
    # Índice tipo
    for tipo in pokemon[2]:
        type_tree.insert(tipo, pokemon)

# b. mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad,
# es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
def show_pokemons():
    num_searched = 135
    node = number_tree.search(num_searched)
    if node: 
        print(f"Búqueda por número {num_searched}: {node.other_values}")
        
    name = "Lycanroc"
    node = name_tree.proximity_search(name)
    for pokemon in node:
        print(f" Búsqueda por nombre: {pokemon.other_values}")    
    
print("b) Datos por número y nombre: ")
show_pokemons()

# c. mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
def show_pokemons_by_type():
    types = ["Fantasma", "Fuego", "Acero", "Electrico"]
    for type in types:
        names = []
        nodes = type_tree.proximity_search(type)
        for node in nodes:
            name = node.other_values[0]
            names.append(name)

        print(f"Tipo {type}: {names}")
    
print("c) Pokémons por tipo: ")
show_pokemons_by_type()

# d. realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
print("d) Listado ascendente por número y nombre: ")
number_tree.in_order()

print("d) Listado por nivel por nombre: ")
name_tree.by_level()

# e. mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
types_jolteon = name_tree.search("Jolteon").other_values[2]
types_lycanroc = name_tree.search("Lycanroc").other_values[2]
types_tyrantrum = name_tree.search("Tyrantrum").other_values[2]

# Agrego todos los pokemons en una lista
all_pokemons = name_tree.proximity_search("") 

weak_jolteon = []
weak_lycanroc = []
weak_tyrantrum = []

for nodo in all_pokemons:
    pokemon = nodo.other_values
    weaknesses = pokemon[3]
    name = pokemon[0]
    
    # Comparo si la debilidad coincide con los tipos del atancante
    for t in types_jolteon:
        if t in weaknesses: 
            weak_jolteon.append(name)
        
    for t in types_lycanroc:
        if t in weaknesses: 
            weak_lycanroc.append(name)
        
    for t in types_tyrantrum:
        if t in weaknesses: 
            weak_tyrantrum.append(name)

print(f"e) Débiles frente a Jolteon: {weak_jolteon}")
print(f"   Débiles frente a Lycanroc: {weak_lycanroc}")
print(f"   Débiles frente a Tyrantrum: {weak_tyrantrum}")

# f. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
print("f) Tipos de Pokémons: ")
def show_pokemons_by_type():
    types = []
    for pokemon in data_pokemons:
        for type in pokemon[2]:
            if type not in types:
                types.append(type)
                
    return types

types = show_pokemons_by_type()

for type in types:
    count = 0
    for pokemon in data_pokemons:
        if type in pokemon[2]:
            count += 1
    print(f"{type}: {count}")

# g. determinar cuantos Pokémons tienen megaevolucion.
def count_pokemons_by_mega():
    count = 0
    for pokemon in data_pokemons:
        if pokemon[4] == True:
            count += 1
    print(f"g) Megaevoluciones: {count}")
    
count_pokemons_by_mega()

# h. determinar cuantos Pokémons tiene forma gigamax.
def count_pokemons_by_giga():
    count = 0
    for pokemon in data_pokemons:
        if pokemon[5] == True:
            count += 1
    print(f"h) Gigamax: {count}")
    
count_pokemons_by_giga()