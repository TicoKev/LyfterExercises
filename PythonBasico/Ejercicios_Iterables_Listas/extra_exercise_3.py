my_list = [9, 4, 7, 1, 5]
lower_number = my_list[0]

for number in my_list:
  if number < lower_number:
    lower_number = number
    
print(f"El menor valor es {lower_number}")