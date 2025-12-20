#Ejercicio2_S4.py
name = input("Digite su nombre: ")
surname = input("Digite su apellido: ")
age = int(input("Digite su edad: "))

if age < 3:
    stage = "bebé"
elif age < 10:
    stage = "niño"
elif age < 13:
    stage = "preadolescente"
elif age < 18:
    stage = "adolescente"
elif age < 30:
    stage = "joven adulto"
elif age < 65:
    stage = "adulto"
else:
    stage = "adulto mayor"

print(f"{name} {surname}, usted está clasificado como {stage}.")