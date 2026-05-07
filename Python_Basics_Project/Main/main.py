from Menu.menu import menu

def main():
  try:
    menu()
  except Exception as error:
    print(f"Unexpected error ocurred", error)

if __name__ == "__main__":
  main()
