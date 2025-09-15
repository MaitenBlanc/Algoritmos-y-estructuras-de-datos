# Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

import sys

sys.path.append("./Clases")
from lista_enlazada import List


class Jedi:
    def __init__(self, name, master, saber_colors, specie):
        self.name = name
        self.master = master
        self.saber_colors = saber_colors
        self.specie = specie

    def __str__(self):
        return f"{self.name} ({self.specie}) - Maestros: {self.master}, Sables: {self.saber_colors}"


def order_by_name(self):
    return self.name


def order_by_specie(self):
    return self.specie


jedis = List()
list_jedi = [
    Jedi(
        name="Ahsoka Tano",
        master=["Anakin Skywalker"],
        saber_colors=["verde", "azul"],
        specie="Togruta",
    ),
    Jedi(name="Kit Fisto", master=["Yoda"], saber_colors=["verde"], specie="Nautolano"),
    Jedi(
        name="Luke Skywalker",
        master=["Obi-Wan Kenobi", "Yoda"],
        saber_colors=["verde"],
        specie="Humano",
    ),
    Jedi(
        name="Qui-Gon Jin",
        master=["Conde Dooku"],
        saber_colors=["verde"],
        specie="Humano",
    ),
    Jedi(
        name="Mace Windu",
        master=["Cyslin Myr"],
        saber_colors=["violeta"],
        specie="Humano",
    ),
    Jedi(name="Plo Koon", master=["Tyvokka"], saber_colors=["azul"], specie="Kel Dor"),
    Jedi(
        name="Aayla Secura",
        master=["Quinlan Vos", "Qui-Gon Jin"],
        saber_colors=["azul"],
        specie="Twi'lek",
    ),
    Jedi(
        name="Rey",
        master=["Leia Organa", "Luke Skywalker"],
        saber_colors=["azul", "amarillo"],
        specie="Humano",
    ),
]

jedis.add_criterion("name", order_by_name)
jedis.add_criterion("species", order_by_specie)

for jedi in list_jedi:
    jedis.append(jedi)


# a. listado ordenado por nombre y por especie;
print("A) Listado ordenado por nombre:")
jedis.sort_by_criterion("name")
jedis.show()
print()

print("\nListado ordenado por especie:")
jedis.sort_by_criterion("species")
jedis.show()


# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
def show_info(name):
    for jedi in jedis:
        if jedi.name == name:
            print(jedi)


print("b) ")
show_info("Ahsoka Tano")
show_info("Kit Fisto")


# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
def show_padawans(master):
    for jedi in jedis:
        if master in jedi.master:
            print(jedi.name)


print("c) Padawans de Yoda:")
show_padawans("Yoda")
print("Padawans de Luke Skywalker:")
show_padawans("Luke Skywalker")


# d. mostrar los Jedi de especie humana y twi'lek;
def show_by_specie(specie):
    for jedi in jedis:
        if jedi.specie.lower() == specie.lower():
            print(jedi.name)


print("d) Jedi de especie Humana:")
show_by_specie("Humano")
print("Jedi de especie Twi'lek:")
show_by_specie("Twi'lek")


# e. listar todos los Jedi que comienzan con A;
def show_starting_with(letter):
    for jedi in jedis:
        if jedi.name.startswith(letter):
            print(jedi.name)


print("e) Jedi que comienzan con A:")
show_starting_with("A")


# f. mostrar los Jedi que usaron sable de luz de más de un color;
def show_multiple_sabers():
    for jedi in jedis:
        if len(jedi.saber_colors) > 1:
            print(jedi.name, jedi.saber_colors)


print("f) Jedi con más de un color de sable:")
show_multiple_sabers()


# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
def show_color_saber(colors):
    for jedi in jedis:
        for color in jedi.saber_colors:
            if color in colors:
                print(jedi.name, jedi.saber_colors)


print("g) Jedi con sable amarillo o violeta:")
show_color_saber(["amarillo", "violeta"])


# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
def show_padawans(name):
    padawans = []
    for jedi in jedis:
        if name in jedi.master:
            padawans.append(jedi.name)
    return padawans


padawans_qui_gon = show_padawans("Qui-Gon Jin")
padawans_mace_windu = show_padawans("Mace Windu")

if padawans_qui_gon or padawans_mace_windu:
    print("h) Padawans de Qui-Gon Jin:")
    if padawans_qui_gon:
        for p in padawans_qui_gon:
            print(p)
    else:
        print("Qui-Gon Jin no tuvo padawans registrados.")

    print("Padawans de Mace Windu:")
    if padawans_mace_windu:
        for p in padawans_mace_windu:
            print(p)
    else:
        print("Mace Windu no tuvo padawans registrados.")
else:
    print("h) Qui-Gon Jin y Mace Windu no tuvieron padawans.")
