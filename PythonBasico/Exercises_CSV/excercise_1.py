import csv



def csv_videogames_data(path, headers, data):
  try:
    with open(path, "w", encoding="utf-8") as file:
      writer = csv.DictWriter(file, headers)
      writer.writeheader()
      writer.writerows(data)
  except FileNotFoundError as error:
        print("La ruta no existe.", error)
  except PermissionError as error:
        print("No tienes permisos para escribir en este archivo.", error)
  except OSError as error:
        print("Error del sistema de archivos.", error)
  except (ValueError, TypeError) as error:
        print("Los datos no son válido.", error)


def add_games(quantity, games_data):
  for index in range(quantity):
      print(f"\nVideojuego {index + 1}")
      name = input("Nombre del juego: ")
      genre = input("Género: ")
      company = input("Nombre de la compañia: ")
      calification = input("Calificación ESRB: ")
      register = {
        "name": name,
        "genre": genre,
        "company":  company,
        "calification" : calification
      }
      games_data.append(register)
  return games_data


def main():
  try:
    games_headers =  (
      "name",
      "genre",
      "company",
      "calification"
    )
    games_data = []
    quantity = int(input("¿Cuántos juegos desea ingresar? "))
    games = add_games(quantity, games_data)
    csv_videogames_data("videogames_data.csv", games_headers, games)
  except ValueError as error:
     print("Debe ingresar un número válido para la cantidad de juegos")
  except Exception:
    print("Unexpected error ocurred")
if __name__ == "__main__":
  main()