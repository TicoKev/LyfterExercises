import csv
from student import Student
class CSVManager:
  
  def export_students_data(self, path, students_list):
    try:
      headers = ["name", "section", "spanish", "english", "social_studies", "science"]
      with open(path, "w", encoding="utf-8", newline="") as file:
          writer = csv.DictWriter(file, fieldnames=headers)
          writer.writeheader()
          for student in students_list:
              row = {
                  "name": student.name,
                  "section": student.section,
                  "spanish": student.grades["spanish"],
                  "english": student.grades["english"],
                  "social_studies": student.grades["social_studies"],
                  "science": student.grades["science"],
              }
              writer.writerow(row)
    except (KeyError, TypeError, ValueError) as error:
          print(f"Error while exporting students data: {error}")
  
  
  def import_students_data(self, path):
    students = []
    try:
      with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
          student = Student(
              name=row["name"],
              section=row["section"],
              spanish_grade=int(row["spanish"]),
              english_grade=int(row["english"]),
              social_studies_grade=int(row["social_studies"]),
              science_grade=int(row["science"])
          )
          students.append(student)
      return students
    except FileNotFoundError:
        print("The data file does not exist.")
        return []
    except (KeyError, ValueError, TypeError) as error:
        print(f"Error while importing students data: {error}")
        return []