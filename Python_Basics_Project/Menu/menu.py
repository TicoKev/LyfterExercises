from Actions.actions import (
    add_students, grades_average, get_top_3_students, print_students_info, remove_student, failed_students
)
from Data.data import (
    export_students_data, import_students_data
)

PATH = "students_data.csv"

def menu():
  exit_program = False
  students_list = []  
  while not exit_program:
    try:
        print("Select an option")
        option = int(input(
            "1. Add students\n"
            "2. Students average\n"
            "3. Top 3 best averages\n"
            "4. Show all students information\n"
            "5. Export students data\n"
            "6. Import students data\n"
            "7. Remove student from the list\n"
            "8. Show failed students\n"
            "9. Exit program\n"
        ))
        match option:
          case 1:
            students_list = add_students(students_list)
          case 2:
            if students_list:
                print(grades_average(students_list))
            else:
                  print("There are no students in the database yet")
          case 3:
            if students_list:
                print(get_top_3_students(students_list))
            else:
                print("There are no students in the database yet")
          case 4:
            if students_list:
                print_students_info(students_list)
            else:
                print("There are no students in the database yet")
          case 5:
            if students_list:
                export_students_data(PATH, students_list)
            else:
                print("There are no students in the database yet")
          case 6:
            students_list = import_students_data(PATH)
          case 7:
            if students_list:
              remove_student(students_list)
            else:
              print("There are no students in the database yet")
          case 8:
            if students_list:
              print(failed_students(students_list))
            else:
              print("There are no students in the database yet")
          case 9:
            exit_program = True
          case _:
            print("Invalid option. Try again" )
    except ValueError:
        print("You must select a valid number")
    except Exception as error:
        print(f"Unexpected error ocurred {error}")
          