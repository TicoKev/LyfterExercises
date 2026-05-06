def get_prime_numbers(numbers_list):
  prime_number_list = []
  
  for number in numbers_list:
    if number > 1:
      is_prime = True
      for possible_prime_number in range(2, number):
        if number % possible_prime_number == 0:
          is_prime = False
          break
      if is_prime:
        prime_number_list.append(number)

  return prime_number_list


print(get_prime_numbers([1, 4, 6, 7, 13, 9, 67]))