ten_minutes_in_seconds = 600
remaining_time = 0
time_in_seconds = int(input("Ingrese el tiempo en segundos: "))

if time_in_seconds < ten_minutes_in_seconds:
  remaining_time = ten_minutes_in_seconds - time_in_seconds
  print(f"Faltan {remaining_time} segundos para diez minutos")
elif time_in_seconds == ten_minutes_in_seconds:
  print("El tiempo es igual a diez minutos")
else:
  print("El tiempo es mayor a diez minutos")
