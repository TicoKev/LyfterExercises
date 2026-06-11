from exercise_2 import sum_all_numbers_in_a_list, invert_string, number_of_lower_case_letters, number_of_upper_case_letters, sort_string, get_prime_numbers

def test_sums_all_numbers_correctly():
  input_list = [1, 3, 7, 5, 10, 20]

  result = sum_all_numbers_in_a_list(input_list)

  assert result == 46


def test_returns_zero_if_list_is_empty():
  input_list = []

  result = sum_all_numbers_in_a_list(input_list)

  assert result == 0


def test_sums_negative_and_positive_numbers_correctly():
  input_list = [-5, 10, -3, 8]

  result = sum_all_numbers_in_a_list(input_list)

  assert result == 10


def test_invert_string_correctly():
  input_test = "Hello"

  result = invert_string(input_test)

  assert result == "olleH"

def test_returns_an_empty_string_if_empty_string_is_passed_as_parameter():
  input_test = ""

  result = invert_string(input_test)

  assert result == ""


def test_invert_a_string_with_spaces_correctly():
  input_test = "string  with   spaces"

  result = invert_string(input_test)

  assert result == "secaps   htiw  gnirts"


def test_returns_the_number_of_upper_case_letters_correctly():

  input_test = "Hello My Name is Kevin"

  result = number_of_upper_case_letters(input_test)

  assert result == 4 


def test_returns_zero_if_an_empty_string_is_passed_as_parameter():

  input_test = ""

  result = number_of_upper_case_letters(input_test)

  assert result == 0



def test_returns_zero_if_the_string_passed_is_all_in_lower_case():
  input_test = "lower case string"

  result = number_of_upper_case_letters(input_test)

  assert result == 0


def test_returns_the_number_of_lower_case_letters_correctly():

  input_test = "aspqdver"

  result = number_of_lower_case_letters(input_test)

  assert result == 8


def test_returns_zero_if_an_empty_string_is_passed_as_parameter():

  input_test = ""

  result = number_of_lower_case_letters(input_test)

  assert result == 0



def test_returns_zero_if_the_string_passed_is_all_in_lower_case():
  input_test = "UPPER CASE STRING"

  result = number_of_lower_case_letters(input_test)

  assert result == 0


def test_returns_the_string_sorted_correctly():
  input_test = "this-is-a-test"

  result = sort_string(input_test)

  assert result == "a-is-test-this"

def test_if_the_input_string_is_sorted_returns_the_same_string():
  input_test = "a-b-c"

  result = sort_string(input_test)

  assert result == "a-b-c"

def test_returns_empty_string_if_the_input_is_an_empty_string():
  input_test = ""

  result = sort_string(input_test)

  assert result == ""


def test_returns_the_prime_numbers_of_a_list_correctly():
  input_test = [1, 4, 6, 7, 13, 9, 67]

  result = get_prime_numbers(input_test)

  assert result == [7, 13, 67]


def test_returns_an_empty_array_if_there_are_not_prime_numbers():
  input_test = []

  result = get_prime_numbers(input_test)

  assert result == []

def test_returns_an_empty_list_if_the_numbers_are_equals_or_lower_than_1():
  input_test = [-10, -2, 0, 1]

  result = get_prime_numbers(input_test)

  assert result == []
