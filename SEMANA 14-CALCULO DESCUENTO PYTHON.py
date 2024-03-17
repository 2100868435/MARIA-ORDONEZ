#Pizarra (whiteboard)


def calcular_descuento(subtotal, descuento = 10):
    monto_descuento = (subtotal * descuento) / 100
    return monto_descuento

valor_subtotal = 100
porcentaje_descuento = 20

valor_descuento= calcular_descuento(valor_subtotal)
valor_total = valor_subtotal - valor_descuento
print(f'Total = {valor_total}. luego de un descuento de {valor_descuento}. Aplicando el 10% al subtotal de {valor_subtotal}')

valor_subtotal = float(input('ingrese el subtotal:'))
porcentaje_descuento = int(input('ingreso el porcentaje de descuento: '))

valor_descuento= calcular_descuento(valor_subtotal, porcentaje_descuento)
valor_total = valor_subtotal - valor_descuento
print(f'Total = {valor_total}. luego de un descuento de {valor_descuento}. Aplicando el {porcentaje_descuento}% al subtotal de {valor_subtotal}')

