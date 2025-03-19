"""Calcular el valor a cancelar de un producto de un monto ingresado, el programa debe
mostrar cómo se presenta en una factura, subtotal (cantidad por precio), IVA (del subtotal)
y total a pagar (la suma del subtotal + el IVA). IVA=21%."""

def calculo_subtotal(cantidad, monto):
    subt = cantidad * monto
    return subt

def calculo_iva():
    iva = calculo_subtotal(cantidad, monto) * 0.21
    return iva

def calculo_total():
    total = calculo_subtotal(cantidad, monto) + calculo_iva()
    return total


cantidad = int(input("Cantidad: "))
monto = float(input("Precio del producto: "))

print(f"Subtotal: ${calculo_subtotal(cantidad, monto)}")
print(f"Iva: ${calculo_iva()}")
print(f"Total: ${calculo_total()}")