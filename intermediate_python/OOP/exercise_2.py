class Bus:
  passengers = []

  def __init__(self, max_passengers):
    self.max_passengers = max_passengers
    self.passengers = []
    
  def board(self, person):
    if len(self.passengers) < self.max_passengers:
      self.passengers.append(person)
    else:
      print("The bus is full and can`t accept more passengers")
      
  def unboard(self, person):
    if person in self.passengers:
      self.passengers.remove(person)
    else:
      raise  ValueError("The person is not in bus")

class Person():
	def __init__(self, name):
		self.name = name

person_1 = Person("John")
person_2 = Person("Sofia")
person_3 = Person("Thomas")
person_4 = Person("Vanessa")
person_5 = Person("Andres")
person_6 = Person("Kevin")
person_7 = Person("Pedro")

bus = Bus(5)

bus.board(person_1)
bus.board(person_2)
bus.board(person_3)
bus.board(person_4)
bus.board(person_5)
bus.board(person_6)
bus.board(person_7)

bus.unboard(person_2)
bus.unboard(person_7)