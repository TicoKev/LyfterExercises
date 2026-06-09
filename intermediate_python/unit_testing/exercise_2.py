#Exercise 3
def sum_all_numbers_in_a_list(numbers_list):
  total_sum = 0
  for number in numbers_list:
    total_sum += number
  return total_sum

#Exercise 4
def invert_string(string):
  return string[::-1]

#Exercise 5
def number_of_upper_case_letters(string):
  upper_case_counter = 0
  for letter in string:
    if letter.isupper():
      upper_case_counter +=1

  return upper_case_counter

def number_of_lower_case_letters(string):
  lower_case_counter = 0
  for letter in string:
    if letter.islower():
      lower_case_counter +=1

  return lower_case_counter


#Exercise 6
def sort_string(string):
  string_list = string.split("-")
  string_list.sort()
  result = "-".join(string_list)

  return result


#Exercise 7
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



print(get_prime_numbers([4,4,4]))