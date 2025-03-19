"""Un millonario excéntrico tenía tres hijos: Carlos, José y Marta. Al morir dejó el siguiente
legado: A José le dejó 4/3 de lo que le dejó a Carlos. A Carlos le dejó 1/3 de su fortuna. A
Marta le dejo la mitad de lo que le dejó a José. Preparar un algoritmo para darle la suma
a repartir e imprima cuanto le tocó a cada uno."""

fortuna = float(input("Total de la fortuna: "))

carlos = 1/3 * fortuna
jose = 4/3 * carlos
maria = jose / 2

print(f"Herencia de Carlos: ${carlos:.2f}")
print(f"Herencia de José: ${jose:.2f}")
print(f"Herencia de María: ${maria:.2f}")