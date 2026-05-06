approved = 0
failed = 0
score_for_approval = 70
counter = 0
average_overall = 0
average_approved_grades = 0
average_failed_grades = 0

total_grades = int(input("Ingrese la cantidad de notas: "))

while counter < total_grades:
    grade = int(input("Ingrese la nota: "))

    if grade < 0 or grade > 100:
        print("Nota ingresada no es correcta")
        continue

    counter += 1
    average_overall += grade

    if grade >= score_for_approval:
        approved += 1
        average_approved_grades += grade
    else:
        failed += 1
        average_failed_grades += grade

print(f"Hay {approved} notas aprobadas y {failed} notas reprobadas.")

if counter > 0:
    average_overall = average_overall / counter
    print(f"El promedio de las notas es {average_overall}.")
else:
    print("No se ingresaron notas válidas.")

if approved > 0:
    average_approved_grades = average_approved_grades / approved
    print(f"El promedio de las notas aprobadas es {average_approved_grades}.")
else:
    print("No hay notas aprobatorias")

if failed > 0:
    average_failed_grades = average_failed_grades / failed
    print(f"El promedio de las notas reprobadas es {average_failed_grades}.")
else:
    print("No hay notas reprobatorias")