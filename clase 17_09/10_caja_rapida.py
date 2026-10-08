lista_prod = []
lista_precios = []

num_prod = int(input("¿Cuantos productos?"))
for i in range (1,num_prod+1):
  producto = input("Producto: ")
  precio = float(input("Precio : "))
  lista_prod.append(producto)
  lista_precios.append(precio)

subtotal = sum(lista_precios)
descuento = 0
print("Productos: ", end="")
for producto in lista_prod:
  print(f"{producto}, ", end="")
print()
print(f"Subtotal: {subtotal}€")
if subtotal >= 50:
  descuento = subtotal*0.1
  print(f"Descuento: {descuento}€")
print(f"Total: {subtotal-descuento}€")
indice_mas_caro = lista_precios.index(max(lista_precios))
print(f"Más caro: {lista_prod[indice_mas_caro]}({lista_precios[indice_mas_caro]}€) ")
