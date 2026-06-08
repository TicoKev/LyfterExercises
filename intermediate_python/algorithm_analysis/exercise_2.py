def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)
		
'''
This algorithm`s time complexity is O(n).
Because the foor loop runs through all the elements on the list.
'''


def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False

'''
This algorithm has a time complexity of O(n^2).
Because in the worst case scenario, if no match is 
found, the outer loop and the inner loop both will 
run up n times.
'''


def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])
		
'''
The algorithm has a time complexity of O(1).
This is because, regardless of the size of the list,
the for loop executes at most 10 iterations.
'''


def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

'''
The algorithm has a time complexity of O(n^3).
Because in the worst case scenario, all loops will run
up to n times
'''