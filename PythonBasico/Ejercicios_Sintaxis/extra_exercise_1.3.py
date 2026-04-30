total_sum = 0
counter = 1
number = int(input("Ingrese un número "))

while counter <= number:
  total_sum = counter + total_sum
  counter +=1
print(f"La suma es {total_sum}")