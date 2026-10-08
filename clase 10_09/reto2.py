segundos = int(input("Ingresa una cantidad de segundos: "))

horas = segundos // 3600
segundos = segundos %3600
minutos = segundos//60
segundos = segundos % 60

if horas < 10:
    h = "0" + str(horas)
else:
    h = str(horas)

if minutos < 10:
    m = "0" + str(minutos)
else:
    m = str(minutos)

if segundos < 10:
    s = "0" + str(segundos)
else:
    s = str(segundos)

print(f"{h}:{m}:{s}")
