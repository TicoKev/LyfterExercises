global_variable = "Probando scope"

def function():
  string = "Variable local"
  global global_variable
  global_variable = "Cambió la variable"
  
  print("Hola")
  print(string)
  print(global_variable)


print(global_variable)
function()
print(string)


