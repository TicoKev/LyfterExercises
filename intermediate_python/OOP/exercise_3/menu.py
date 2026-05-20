from student import Student, create_student, grades_average, get_top_3_students, print_students_info, remove_student, failed_students

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
        self.students_list = create_student(self.students_list)

      case 2:
        if self.students_list:
            average = grades_average(self.students_list)
            print(f"The students` average is: {average}")
        else:
              print("There are no students in the database yet")
      
      case 3:
        if self.students_list:
            get_top_3 = get_top_3_students(self.students_list)
            print(f"The top 3 stundents with better average are: {get_top_3}")
        else:
            print("There are no students in the database yet")
      
      case 4:
        if self.students_list:
          print_students_info(self.students_list)
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
          remove_student(self.students_list)
        else:
          print("There are no students in the database yet")
      
      case 8:
        if self.students_list:
          failed_students_list = failed_students(self.students_list)
          for failed in failed_students_list:
            print(f"Name: {failed['name']}, Section: {failed['section']}, Failed: {failed['failed_subjects']}")
        else:
          print("There are no students in the database yet")
      
      case 9:
        self.exit_program = True
      
      case _:
        print("Invalid option. Try again")
          