#1
string_1 = "Hi"
string_2 = "Kevin"
print(string_1 + string_2) #HiKevin

#2
number = 23
print(string_1 + number) #TypeError: can only concatenate str (not "int") to str

#3 
print(number + string_1) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#4
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
print(list_1 + list_2) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#5
print(string_2 + list_1) #TypeError: can only concatenate str (not "list") to str

#6
float_number = 2.95
print(float_number + number) #25.95

#7
boolean_1 = True
boolean_2 = False
print(boolean_1 + boolean_2) #1