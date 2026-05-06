my_list = [10, 20, 30, 40, 50]
my_new_list = []
my_list_quantity = len(my_list)
total_sum = 0
average = 0

for number in my_list:
  total_sum += number

average = total_sum / my_list_quantity

for number in my_list:
  if number > average:
    my_new_list.append(number)

print(f"Promedio: {average}\nNueva lista: {my_new_list}")