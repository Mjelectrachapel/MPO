precio_comida = float(input("Introduzca el precio de la comida: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina (%): "))

propina = precio_comida * (porcentaje_propina / 100)
total = precio_comida + propina

print(f"Propina: {propina:.2f} €")
print(f"Total: {total:.2f} €")
