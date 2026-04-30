multiplier = int(input("Ingrese la tabla de multiplicar entre 1 y 10: "))

if  1 <= multiplier <= 10:
  for number in range(1, 13):
    print(f"{multiplier} x {number} = {multiplier * number}")
else:
  print("El número esta fuera del rango")