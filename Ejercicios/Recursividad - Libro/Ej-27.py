"""El valor 1.376.256 pertenece a una sucesión geométrica cuya razón es 4, implementar un algoritmo para mostrar todos los
valores de la sucesión hacia atrás hasta el valor de a1= 5,25"""

# r=4
# valor anterior = a(n-1) = an / r


def sequence(value, r, limit):
    print(value)

    if value <= limit:
        return

    sequence(value / r, r, limit)


an = 1376256
r = 4
limit = 5.25

sequence(an, r, limit)
