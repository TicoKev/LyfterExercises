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

print(f"There`s {number_of_upper_case_letters("I love Nación Sushi")} upper case letters and {number_of_lower_case_letters("I love Nación Sushi")} lower cases")