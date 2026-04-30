number = int(input("Ingrese el primer número: "))
biggest = number

for index in range(2):
  number = int(input("Ingrese el siguiente número: "))
  
  if (number > biggest):
    biggest = number

print(f"El número mayor es {biggest}")



