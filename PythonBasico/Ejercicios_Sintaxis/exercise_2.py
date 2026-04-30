name = input("Ingrese su nombre ")
last_name = input("Ingrese su apellido ")
age = int(input("Ingrese su edad K"))

if (age < 0):
  print("La edad ingresada no es correcta")
elif (age < 3):
  print("Eres un bebé")
elif(age < 11):
  print("Eres un niño")
elif (age < 13):
  print("Eres un preadolescente")
elif (age < 18):
  print("Eres un adolescente")
elif (age < 35):
  print("Eres un adulto joven")
elif (age < 65):
  print("Eres un adulto")
else:
  print("Eres un adulto mayor")
