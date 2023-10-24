import random

letras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("ingrese el largo de contraseña"))
clave = ""
for i in range(longitud):
    temp = random.choice(letras)
    clave = clave + temp
print(clave)