def bubble_sort(list_to_sort):
  length = len(list_to_sort)

  while True:
    swapped = False
    for i in range(1, length):
      if list_to_sort[i - 1] > list_to_sort[i]:
        list_to_sort[i - 1], list_to_sort[i] = list_to_sort[i], list_to_sort[i - 1]
        swapped = True
    length -=1

    if not swapped:
      break

  return list_to_sort