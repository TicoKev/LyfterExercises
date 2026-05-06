my_list = []
long_words_list = []

for counter in range(5): 
 word = input(f"Ingrese la palabra {counter+1}: ")
 my_list.append(word)
 
 if len(word) > 4:
  long_words_list.append(word)

print (long_words_list)