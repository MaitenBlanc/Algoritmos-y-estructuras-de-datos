"""Determinar si una palabra cualquiera es un palíndromo (capicúa); por ejemplo: Neuquén."""

def palindromo(palabra):
    palabra.lower()
    
    for i in range(0, int(len(palabra) / 2)):
        if palabra[i] != palabra[-i-1]:
            return False
        return True

palabra = input("Ingrese una palabra: ")

if(palindromo(palabra)):
    print(f"La palabra {palabra} es palíndromo.")
else:
    print(f"La palabra {palabra} no es palíndromo.")