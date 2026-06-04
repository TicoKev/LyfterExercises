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




list_to_sort = [20, 5, 8, 2, 1, 17, 4]

print(bubble_sort(list_to_sort))

'''
The bubble sort algorithm`s time complexity is O(n^2). 
This is because in the worst case scenario if the list is
unordered, the outer loop and the inner loop run up to n times
resulting in n x n 
'''