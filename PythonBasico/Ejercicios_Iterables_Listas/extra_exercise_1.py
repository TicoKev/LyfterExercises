my_list = []
number_to_find = int(input("Ingrese el número a encontrar: "))
number = int(input("Ingrese un número: "))
my_list.append(number)
number_to_find_counter = 0

if number == number_to_find:
  number_to_find_counter +=1

for _ in range (1, 10):
  number = int(input("Ingrese el siguiente número: "))
  my_list.append(number)
  if number == number_to_find:
    number_to_find_counter +=1

print(f"El número {number_to_find} aparece {number_to_find_counter} veces")