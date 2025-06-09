"""Suponga que se escapa hacia el planeta tierra en un Caza TIE robado –huyendo de un Destructor Estelar y
necesita localizar la base rebelde más cercana– y se tiene una cola con información de las bases rebeldes
en la tierra de las cuales conoce su nombre, número de flota aérea, coordenadas de latitud y longitud.
Desarrolle un algoritmo que permita resolver las siguientes tareas una vez que aterrice:
a. determinar cuál es la base rebelde más cercana desde su posición actual.
b. para el cálculo de la distancia deberá utilizar la fórmula de Haversine: donde r es el radio medio de
la tierra en metros (6371000), φ1 y φ2 las latitudes de los dos puntos –por ejemplo coordenadas actual–,
λ1 y λ2 las longitudes de los dos puntos –coordenadas de la base– ambos expresadas en radianes; para
convertir de grados a radianes utilice la función math.radians(ángulo coordenada).
c. mostrar el nombre y la distancia a la que se encuentran las tres bases más cercanas y determinar cual
tiene mayor flota aérea.
d. determinar la distancia hasta la base rebelde con mayor flota aérea.
"""

import sys

sys.path.append("./Clases")

import math

from cola import Queue
from lista_enlazada import List

bases_queue = Queue()
bases_queue.arrive(
    {"name": "Base D'Qar", "fleet": 20, "lat": -33.4569, "lon": -70.6483}
)
bases_queue.arrive({"name": "Base Hoth", "fleet": 35, "lat": -38.0055, "lon": -57.5426})
bases_queue.arrive(
    {"name": "Base Dantooine", "fleet": 15, "lat": -45.8667, "lon": -67.4833}
)
bases_queue.arrive(
    {"name": "Base Chopper", "fleet": 50, "lat": -24.7821, "lon": -65.4232}
)


# b)
def haversine(lat1, lon1, lat2, lon2):
    """Función para calcular la distancia por fórmula de Haversine
    Args:
        lat1: latitud de posición actual
        lon1: longitu de posición actual
        lat2: latitud de la base
        lon2: longitud de la base
    """
    r = 6371000
    φ1 = math.radians(lat1)
    φ2 = math.radians(lat2)
    dφ = math.radians(lat2 - lat1)
    dλ = math.radians(lon2 - lon1)

    dist = (
        2
        * r
        * math.asin(
            math.sqrt(
                math.sin(dφ / 2) ** 2
                + math.cos(φ1) * math.cos(φ2) * math.sin(dλ / 2) ** 2
            )
        )
    )

    return dist


# a)
my_lat = -32.4833
my_lon = -58.2283


def distance_to_bases(queue):
    aux_queue = Queue()
    distances_queue = Queue()

    while queue.size() > 0:
        base = queue.attention()
        dist = haversine(my_lat, my_lon, base["lat"], base["lon"])

        base_with_distances = {
            "name": base["name"],
            "fleet": base["fleet"],
            "lat": base["lat"],
            "lon": base["lon"],
            "distance": dist,
        }

        distances_queue.arrive(base_with_distances)
        aux_queue.arrive(base)

    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())

    return distances_queue


# a)
def nearest_base(queue):
    aux_queue = Queue()
    distances = distance_to_bases(queue)
    min_base = None
    min_distance = float("inf")

    while distances.size() > 0:
        base = distances.attention()

        if base["distance"] < min_distance:
            min_distance = base["distance"]
            min_base = base

        aux_queue.arrive(base)

    while aux_queue.size() > 0:
        distances.arrive(aux_queue.attention())

    return min_base


min_base = nearest_base(bases_queue)
name = min_base["name"]
distance = min_base["distance"]
print(
    f"a) La base rebelde más cercana a la posición actual es {name} con un distancia de {distance:.2f}."
)


# c)
def three_neareast_bases(queue):
    distances = distance_to_bases(queue)
    bases_list = []

    while distances.size() > 0:
        bases_list.append(distances.attention())

    bases_list.sort(key=lambda x: x["distance"])

    top_3 = bases_list[:3]

    print("Las tres bases más cercanas: ")
    for base in top_3:
        print(f"- {base['name']} a {base['distance']:.2f} metros")

    max_fleet_base = max(top_3, key=lambda x: x["fleet"])
    print(
        f"La base con mayor flota entre las tres más cercanas es {max_fleet_base['name']} con {max_fleet_base['fleet']} naves."
    )


print("c) ")
three_neareast_bases(bases_queue)


# d)
def distance_max_fleet(queue):
    distances = distance_to_bases(queue)
    max_fleet = -1
    base_max_fleet = None
    aux_queue = Queue()

    while distances.size() > 0:
        base = distances.attention()

        if base["fleet"] > max_fleet:
            max_fleet = base["fleet"]
            base_max_fleet = base

        aux_queue.arrive(base)

    while aux_queue.size() > 0:
        distances.arrive(aux_queue.attention())

    print(
        f"La base con mayor flota se encuentra a una distancia de {base_max_fleet['distance']:.2f} de tu posición actual."
    )


print("d)")
distance_max_fleet(bases_queue)
