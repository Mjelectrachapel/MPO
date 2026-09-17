limite = int(input("Introduce un límite "))
cantidad=0
suma=0
for i in range(1,limite+1):
  if i%3==0:
    print(i, end=" ")
    cantidad+=1
    suma+=i
print()
print(f"Suma: {suma}")
print(f"Cantidad: {cantidad}")

