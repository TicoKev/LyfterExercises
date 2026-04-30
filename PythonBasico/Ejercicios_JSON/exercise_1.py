import json

def read_JSON(path):
  try:
    with open(path, "r") as file:
      data = json.load(file)
  
    return data
  except FileNotFoundError:
    print("No se encontró el archivo JSON.")
    return []
  except json.JSONDecodeError:
    print("El archivo JSON está corrupto.")
    return []
  except PermissionError:
    print("No tienes permisos para leer el archivo.")
    return []

def write_JSON(path, data, new_pokemon): 
  try:
    data.append(new_pokemon) 
    with open(path, "w") as file:
      json.dump(data, file, indent=4)
  except TypeError:
    print("Los datos no son serializables o no tienen un formato correcto")
  except PermissionError:
    print("No tienes permisos para escribir el archivo.")

def get_pokemon_stats():
  try:

    name = input("Ingrese el nombre del pokémon ")
    level = int(input("Ingrese el nivel: "))
    pokemon_type = input("Ingrese el tipo: ")
    hp = int(input("Ingrese los puntos de vida: "))
    attack = int(input("Ingrese la cantidad del ataque: "))
    defense = int(input("Ingrese la cantidad de defensa: "))
    sp_attack = int(input("Ingrese la cantidad del ataque especial: "))
    sp_defense = int(input("Ingrese la cantidad de defensa especial: "))
    speed = int(input("Ingrese la cantidad de velociad: "))
    template = {
      "name": {
        "english": name
      },
      "level": level,
      "type": [
        pokemon_type
      ],
      "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
      }
    }
    return template
  except ValueError:
    print("Error debes ingresar números correctos en los campos númericos")
    return None
  except TypeError:
    print("Se ingresó un tipo de dato incorrecto")
    return None


def main():
  try:
    data = read_JSON("pokemon.json")
    new_pokemon = get_pokemon_stats()
    write_JSON("pokemon.json", data, new_pokemon)
  except Exception as error:
    print("Error inesperado: ", error)

if __name__ == "__main__":
  main()
