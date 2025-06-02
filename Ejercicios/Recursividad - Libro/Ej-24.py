"""En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una
plataforma de bronce sobre la cual había tres agujas de diamante. En la primera aguja estaban
apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que estaba debajo.
A los sacerdotes se les encomendó la tarea de pasarlos todos desde la primera aguja a la tercera,
con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá ponerse encima de otro más pequeño.
Se dijo a los sacerdotes que, cuando hubieran terminado de mover los discos, llegaría el fin del mundo.
Resolver este problema de la Torre de Hanói."""


def hanoi_tower(n, origin, destiny, aux):
    if n == 1:
        print(f"Mover disco 1 de {origin} a {destiny}")
        return

    hanoi_tower(n - 1, origin, aux, destiny)
    print(f"Mover disco {n} de {origin} a {destiny}")
    hanoi_tower(n - 1, aux, destiny, origin)


hanoi_tower(5, 1, 3, 2)
