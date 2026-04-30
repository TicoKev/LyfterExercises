list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
dictionary = {}

for index in range(len(list_a)):
  dictionary[list_a[index]] = list_b[index]

print(dictionary)