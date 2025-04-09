"""El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
c. Utilizar un vector para representar la mochila."""

# i = indice de objeto en mochila

# a
def usar_la_fuerza(mochila, i=0):
    if i >= len(mochila):
        return False, i
    
    if mochila[i] == "sable de luz":
        return True, i+1
    
    return usar_la_fuerza(mochila, i + 1)

# c
mochila_1 = ["agua", "mapa", "sable de luz", "escudo", "comida"]
mochila_2 = ["agua", "mapa", "escudo", "comida"]

# b) Ejemplo si tiene sable de luz
encontrado, i = usar_la_fuerza(mochila_1)

if (encontrado):
    print("La mochila contiene un sable de luz.")
    print(f"Fue necesario sacar {i} objetos.") if i > 1 else print(f"Fue necesario sacar {i} objeto.")
else: 
    print("El sable de luz no se encuentra en la mochila.")

# b) Ejemplo si no tiene sable de luz
encontrado, i = usar_la_fuerza(mochila_2)

if (encontrado):
    print(f"\nLa mochila contiene un sable de luz.")
    print(f"Fue necesario sacar {i} objetos.") if (i > 1) else print(f"Fue necesario sacar {i} objeto.")
else: 
    print("El sable de luz no se encuentra en la mochila.")