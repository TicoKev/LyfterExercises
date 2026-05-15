from student import  Student

from csv_manager import CSVManager


PATH = "students_data.csv"

class Menu():

  def __init__(self):
     self.students_list =[]
     self.exit_program = False
     self.csv_manager = CSVManager()

  def menu(self):
    while not self.exit_program:
      try:
          print("Select an option")
          self.option = int(input(
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
          self.options(self.option)
      except ValueError:
        print("You must select a valid number")
      except Exception as error:
        print(f"Unexpected error ocurred {error}")

    
  def options(self, option):
    match option:
      case 1:
        student_creator = Student(0, "", "", 0, 0, 0, 0)
        self.students_list = student_creator.create_student(self.students_list)
      case 2:
        if self.students_list:
            print(Student(0, "", "", 0, 0, 0, 0).grades_average(self.students_list))
        else:
              print("There are no students in the database yet")
      case 3:
        if self.students_list:
            print(Student(0, "", "", 0, 0, 0, 0).get_top_3_students(self.students_list))
        else:
            print("There are no students in the database yet")
      case 4:
        if self.students_list:
            Student(0, "", "", 0, 0, 0, 0).print_students_info(self.students_list)
        else:
            print("There are no students in the database yet")
      case 5:
        if self.students_list:
            self.csv_manager.export_students_data(PATH, self.students_list)
        else:
            print("There are no students in the database yet")
      case 6:
        self.students_list = self.csv_manager.import_students_data(PATH)
        
      case 7:
        if self.students_list:
          Student(0, "", "", 0, 0, 0, 0).remove_student(self.students_list)
        else:
          print("There are no students in the database yet")
      case 8:
        if self.students_list:
          print(Student(0, "", "", 0, 0, 0, 0).failed_students(self.students_list))
        else:
          print("There are no students in the database yet")
      case 9:
        self.exit_program = True
      case _:
        print("Invalid option. Try again")
          