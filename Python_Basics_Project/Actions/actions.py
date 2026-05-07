import re

def add_students():
    students_quantity = int(input("Enter the number of students: "))
    if students_quantity < 0:
        raise ValueError("The students quantity must be higher than 0.")
    
    if not isinstance(students_quantity, int):
        raise TypeError("The quantity must be a number.")

    students = []

    for student in range(students_quantity):
        
        name = input(f"Enter full name for student #{student + 1}: ").strip()
        is_valid_name(name)
        section = input(f"Enter {name}`s class: ").strip()
        is_valid_section(section)
        
        duplicate_student(students, name, section)
        
        spanish_grade = ask_for_grade("Enter the spanish grade: ")
        english_grade = ask_for_grade("Enter the english grade: ")
        social_studies_grade = ask_for_grade("Enter the social studies grade: ")
        science_grade = ask_for_grade("Enter the science grade: ")

        students.append({
            "name": name,
            "section": section,
            "grades": {
              "spanish": spanish_grade,
              "english": english_grade,
              "social_studies": social_studies_grade,
              "science": science_grade
            }
            
        })

    return students


def is_valid_name(name):
  if name == "":
    raise ValueError ("The name cannot be in blank")
  elif any(char.isdigit() for char in name):
    raise ValueError ("The name cannot contain numbers")
  return True


def is_valid_section(section):
    pattern = r"^\d{1,2}[A-Z]$"
    if section == "":
        raise ValueError("The section cannot be blank")
    if not re.match(pattern, section):
        raise ValueError("The section must be 1 - 2 digits followed by a capital letter")
    return True


def student_exists(students, name):
  if not isinstance(students, list):
     raise TypeError("Students must be a list")
  
  if not isinstance(name, str):
     raise TypeError("Name must be a string")

  for student in students:
    if student["name"] == name:
      print("The student is in the list.")
      return True
  print("The student does not exist.")
  return False


def duplicate_student(students, name, section):
  if not isinstance(students, list):
     raise TypeError("Students must be a list")
  
  if not isinstance(name, str) or not isinstance(section, str):
     raise TypeError("Name and section must be a string")

  for student in students:
    if student["name"] == name and student["section"] == section:
      raise ValueError("The student is already in the list, and it cannot be added again.")
      
   
def ask_for_grade(prompt):

    while True:
        try:
            grade = int(input(prompt))
            is_valid_grade(grade)
            return grade
        except ValueError as error:
            print("Error:", error)
        except TypeError as error:
            print("Error:",error)


def is_valid_grade(grade):
    if not isinstance(grade, int):
        raise TypeError("The grade must be a number.")
    if grade <= 0:
        raise ValueError("The grade must be higher than 0")
    return True


def print_students_info(students):
    for student in students:
        print(student)


def grades_average(students):
    try:
      students_grades_sum = 0
      students_grades_average = 0
      grades_quantity = 0
      for student in students:
          for grade in student["grades"].values():
            students_grades_sum += grade
            grades_quantity +=1
    
      students_grades_average = students_grades_sum / grades_quantity

      return students_grades_average
    except KeyError as error:
        print("Error: falta la clave en el diccionario: ", error)
    except TypeError as error:
        print("Error: tipo de dato inválido: ", error)
    except ZeroDivisionError as error:
        print("Error:", error)


def get_top_3_students(students):
  results = []
  for student in students:
    try:
      all_grades = list(student["grades"].values())
      if not all_grades:
        continue
      average = sum(all_grades) / len(all_grades)
      results.append({
        "name": student["name"],
        "average": round(average, 2)
      })
    except KeyError as e:
      print(f"Falta la clave {e} en el estudiante: {student}")
    except TypeError:
      print(f"Las notas deben ser números: {student}")

  return sorted(results, key=lambda x: x["average"], reverse=True)[:3]


def remove_student(students):
  try:
    name_to_delete = input("Enter the student`s name you want to remove: ").strip()
    section_to_delete = input("Enter the student`s section: ").strip()

    found_index = None
    for index, student in enumerate(students):
      if student["name"] == name_to_delete and student["section"] == section_to_delete:
        found_index = index
        break

    if found_index is None:
        print("Student not found or section does not match.")
        return

      
    while True:
        option = input("Are you sure you want to remove this student? (yes/no): ").strip().lower()
        if option == "yes":
            students.pop(found_index)
            print("Student removed successfully.")
            return
        elif option == "no":
            print("Going back to main menu.")
            return
        else:
            print("Invalid option. Please type 'yes' or 'no'.")
  except (ValueError, IndexError, KeyError, TypeError) as error:
    print(f"Error while removing student, {error}")
  

def failed_students(students):
  try:
    failed_students_list = []
    
    for student in students:
      failed_subjects = {}
      for subject, grade in student["grades"].items():
          if grade <= 60:
            failed_subjects[subject] = grade
      
      if len(failed_subjects) > 0:
        failed_students_list.append({
                "name": student["name"],
                "section": student["section"],
                "failed_subjects": failed_subjects
            })
  except (TypeError, KeyError, ValueError) as error:
        print(f"Error while executing failed students option: {error}")
  
  return failed_students_list