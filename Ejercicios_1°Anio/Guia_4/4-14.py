"""Desarrollar un algoritmo que una vez leída una Fecha en formato dd/mm/aaaa, indique cual
será la fecha un día después."""

from datetime import datetime, timedelta

fecha_dada = input("Ingrese una fecha (formato: dd/mm/aaaa): ")

def fechaSiguiente(fecha_dada):
    # Convertir el string en datetime
    fecha = datetime.strptime(fecha_dada, "%d/%m/%Y").date()
    fecha_siguiente = fecha + timedelta(days=1)
    
    return fecha_siguiente.strftime("%d/%m/%Y")

print(f"La fecha del día siguiente es: {fechaSiguiente(fecha_dada)}")