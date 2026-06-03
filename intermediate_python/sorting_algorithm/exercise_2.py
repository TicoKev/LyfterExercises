def inverse_bubble_sort(list_to_sort):
  length = len(list_to_sort)
  start = 0
  
  while True:
    swapped = False
    for i in range(length - 1, start, -1):
      if list_to_sort[i] < list_to_sort[i - 1]:
        list_to_sort[i], list_to_sort[i - 1] = list_to_sort[i - 1], list_to_sort[i]
        swapped = True
    start +=1

    if not swapped:
      break

  return list_to_sort




list_to_sort = [20, 5, 8, 2, 1, 17, 4]

print(inverse_bubble_sort(list_to_sort))