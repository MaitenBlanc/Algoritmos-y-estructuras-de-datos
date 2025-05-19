"""Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
una que contenga los números pares y otra para los números impares."""

import sys

sys.path.append("./Clases")
from lista_enlazada import List

lista = List()

def split_list(lista):
    lista_pares = List()
    lista_impares = List()
    
    for num in lista:
        if num % 2 == 0:
            lista_pares.append(num)
        else:
            lista_impares.append(num)
    
    return lista_pares, lista_impares
    

lista.append(1)
lista.append(15)
lista.append(12)
lista.append(24)
lista.append(31)

pares, impares = split_list(lista)

print(f'Números pares: {pares}')
print(f'Números impares: {impares}')