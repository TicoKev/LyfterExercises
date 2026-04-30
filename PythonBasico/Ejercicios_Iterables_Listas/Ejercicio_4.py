my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

index = len(my_list) -1
print(index)

for _ in my_list[::-1]:
  if my_list[index] % 2 != 0:
    my_list.pop(index)
  index -= 1

print(my_list)