"""Dada una lista de 3 números determinar si el Nº 3 se encuentra en dicha lista."""

def estaTres(lista):
    for i in range(len(lista)):
        if (lista[i] == 3):
            return True

n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Tercer número: "))

lista = []
lista.append(n1)
lista.append(n2)
lista.append(n3)

if (estaTres(lista)):
    print(f"El número 3 se encuentra en la lista.")
else:
    print(f"El número 3 no se encuentra en la lista.")