import pytest
from exercise_1 import bubble_sort

def test_bubble_sort_algorithm_with_a_small_list():
  input_list = [3,1,7]

  result = bubble_sort(input_list)

  assert result == [1, 3, 7]


def test_bubble_sort_algorithm_with_a_big_list():
  input_list = [
  42, 7, 89, 13, 56, 91, 3, 77, 25, 64,
  18, 109, 99, 12, 110, 5, 83, 41, 68, 2, 
  34, 73, 50, 27, 8, 61, 36, 95, 14, 47, 
  22, 70, 11, 65, 9, 31, 85, 4, 28, 93, 
  16, 38, 20, 75, 6, 33, 87, 10, 45, 29, 
  97, 15, 24, 107, 108, 80, 1, 35, 90, 19, 
  53, 26, 71, 17, 39, 84, 30, 48, 96, 101,
  21, 55, 32, 72, 23, 103, 106, 40, 82, 37,
  49, 94, 44, 60, 63, 78, 46, 67, 59, 74, 52, 
  66, 104, 57, 76, 54, 62, 79, 58, 69, 81, 43, 
  88, 51, 92, 98, 100, 86, 105
]


  result = bubble_sort(input_list)

  assert result == sorted(input_list)


def test_bubble_sort_algorithm_with_an_empty_list():
  input_list = []


  result = bubble_sort(input_list)

  assert result == []


def test_bubble_sort_algorithm_with_different_parameters():

  with pytest.raises(TypeError):
    bubble_sort("this is a string")

  with pytest.raises(TypeError):
    bubble_sort(123)
  
  with pytest.raises(TypeError):
    bubble_sort(False)
  
  with pytest.raises(TypeError):
    bubble_sort(True)
  
  with pytest.raises(TypeError):
    bubble_sort(None)