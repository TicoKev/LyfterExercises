import random

random_number = random.randint(1, 10)
print(random_number)

guess = None

while guess != random_number:
    guess = int(input("Adivine el número secreto. Ingrese un número entre 1 y 10: "))
    if guess != random_number:
        print("Número equivocado, intente de nuevo")

print("¡Ha adivinado el número secreto!")