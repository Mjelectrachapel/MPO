edad = int(input("Edad: "))

if edad >=18:
    print("ACCESO PERMITIDO")
elif edad>=16:
    control = input("¿Autorización parental? (s/n): ").lower()
    if control == "s":
        print("ACCESO PERMITIDO")
    else: 
        print("ACCESO DENEGADO")
else:
    print("ACCESO DENEGADO")