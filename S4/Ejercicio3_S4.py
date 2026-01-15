#Ejercicio3_S4.py
import random

secret_number = random.randint(1, 10)
guessed = False

while not guessed:
    user_guess = int(input("Adivina el número (1-10): "))
    
    if user_guess == secret_number:
        print("¡Lo adivinaste!")
        guessed = True
    else:
        print("Número incorrecto, intenta de nuevo.")
