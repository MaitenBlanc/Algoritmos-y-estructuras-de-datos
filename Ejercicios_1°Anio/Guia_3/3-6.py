"""Diseñe un algoritmo que determine el porcentaje de: Alumnos promocionados, Alumnos
regularizados, Alumnos desaprobados y Alumnos libres, teniendo como datos cantidad de
alumnos que cumplen con cada condición."""

def calc_promocionados(cant_promocionados, cant_total):
    porc_promocionados = (cant_promocionados / cant_total) * 100
    return porc_promocionados

def calc_regularizados(cant_regularizados, cant_total):
    porc_regularizados = (cant_regularizados / cant_total) * 100
    return porc_regularizados

def calc_desaprobados(cant_desaprobados, cant_total):
    porc_desaprobados = (cant_desaprobados / cant_total) * 100
    return porc_desaprobados

def calc_libres(cant_libres, cant_total):
    porc_libres = (cant_libres / cant_total) * 100
    return porc_libres

cant_promocionados = int(input("Cantidad de promocionados: "))
cant_regularizados = int(input("Cantidad de regularizados: "))
cant_desaprobados = int(input("Cantidad de desaprobados: "))
cant_libres = int(input("Cantidad de libres: "))

cant_total = cant_promocionados + cant_regularizados + cant_desaprobados + cant_libres

print(f"Porcentaje promocionados = {calc_promocionados(cant_promocionados, cant_total):.2f}%")
print(f"Porcentaje regularizados = {calc_regularizados(cant_regularizados, cant_total):.2f}%")
print(f"Porcentaje desaprobados = {calc_desaprobados(cant_desaprobados, cant_total):.2f}%")
print(f"Porcentaje libres = {calc_libres(cant_libres, cant_total):.2f}%")