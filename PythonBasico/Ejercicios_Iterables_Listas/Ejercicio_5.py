my_number_list = []
user_number = int(input("Ingrese un número: "))
biggest_number = user_number
my_number_list.append(user_number)

for _ in range(1, 10):
  user_number = int(input("Ingrese el siguiente número número: "))
  my_number_list.append(user_number)
  if user_number > biggest_number:
    biggest_number = user_number

print(my_number_list, f"El más alto fue {biggest_number}")