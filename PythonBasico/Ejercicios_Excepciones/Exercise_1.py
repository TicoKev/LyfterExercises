def numbers_sum(number_1, number_2):
  try:
    return number_1 + number_2
  except TypeError as error:
    print("No se ingreso un número", error)


def substraction(number_1, number_2):
  try:
    return number_1 - number_2
  except TypeError as error:
    print("No se ingreso un número", error)

def multiplication(number_1, number_2):
  try:
    return number_1 * number_2
  except TypeError as error:
    print("No se ingreso un número", error)


def division(number_1, number_2):
  try:
    return number_1 / number_2
  except TypeError as error:
    print("No se ingreso un número", error)
  except ZeroDivisionError as error:
    print("No se puede realizar una división entre 0", error)
    return number_1


def calculator():
  actual_number = 10
  exit =  True
  
  while exit:
    try:
      option = int(input("\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n5.Borrar Resultado\n6.Salir\nElija una opción "))
      match option:
        case 1 | 2 | 3 | 4:
          number = int(input("Ingrese un número: "))
          if option == 1:
            actual_number = numbers_sum(actual_number, number)
          elif option == 2:
            actual_number = substraction(actual_number, number)
          elif option == 3:
            actual_number = multiplication(actual_number, number)
          elif option == 4:
            actual_number = division(actual_number, number)
          print(f"El resultado es: {actual_number}")
        case 5:
          actual_number = 10
        case 6:
          exit = False
          
        case _:
          print("Opción no valida")
          
    except ValueError as error:
      print("Opción ingresada no es valida, deber ser un número de la lista", error)


def main():
  try:
    calculator()
  except Exception:
    print("Error desconocido ocurrió")

if __name__ == "__main__":
  main()