import csv

def export_students_data(path, students_data):
  try:
    headers = ["name", "section", "spanish", "english", "social_studies", "science"]

    with open(path, "w", encoding="utf-8", newline="") as file:
      writer = csv.DictWriter(file, fieldnames=headers)
      writer.writeheader()
      for student in students_data:
        row = {
            "name": student["name"],
            "section": student["section"],
            "spanish": student["grades"]["spanish"],
            "english": student["grades"]["english"],
            "social_studies": student["grades"]["social_studies"],
            "science": student["grades"]["science"],
          }
        writer.writerow(row)
  except(KeyError, TypeError, ValueError) as error:
    print(f"Error while exporting students data: {error}")


def import_students_data(path):
  students = []
  try:
    with open(path, "r", encoding="utf-8") as file:
      reader = csv.DictReader(file)

      for row in reader:
        student = {
          "name" : row["name"],
          "section": row["section"],
          "grades" : {
            "spanish" : int(row["spanish"]),
            "english" : int(row["english"]),
            "social_studies" : int(row["social_studies"]),
            "science" : int(row["science"])
          } 
        }
        students.append(student)
      return students

  except FileNotFoundError:
    print("The data file does not exist.")
    return []
  except (KeyError, ValueError, TypeError) as error:
    print(f"Error while importing students data: {error}")
    return []