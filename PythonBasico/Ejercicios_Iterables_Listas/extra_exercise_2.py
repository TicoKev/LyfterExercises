my_list = [3,6,0,-2,4]
all_positive = True

for number in my_list:
  if number <= 0:
    all_positive = False
    break

if  all_positive:
   print("Todos los números son positivos")
else:

  print("Hay al menos un número negativo o cero")

