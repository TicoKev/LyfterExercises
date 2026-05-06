import random
secret_number = random.randint(1, 10)
print(secret_number)
print("Adivine el número secreto")
guess = int(input("Ingrese el número: "))

while guess != secret_number:
  guess = int(input("El número ingresado no es correcto. Ingrese el número: "))

print(f"Adivinó el número secreto, que era {secret_number}")