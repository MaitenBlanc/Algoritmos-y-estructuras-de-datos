"""Se ingresa el nombre, edad y dirección de dos socios, se pide mostrar los datos de socio
más joven."""

directorio = {}

def cargar_datos():
    for _ in range(2):
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        direccion = input("Ingrese su dirección: ")

        directorio[nombre] = {"edad": edad, "direccion": direccion}

def socio_mas_joven():
    return min(directorio.items(), key=lambda x: x[1]["edad"])

cargar_datos()

nombre_joven, data_joven = socio_mas_joven()

print("El socio más jóven es: ")
print(f"Nombre: {nombre_joven}")
print(f"Edad: {data_joven["edad"]} ")
print(f"Direccion: {data_joven["direccion"]} ")