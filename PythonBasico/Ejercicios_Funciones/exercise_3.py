def sum_all_numbers_in_a_list(numbers_list):
  total_sum = 0
  for number in numbers_list:
    total_sum += number
  return total_sum
  
print(sum_all_numbers_in_a_list([4, 6, 2, 29]))