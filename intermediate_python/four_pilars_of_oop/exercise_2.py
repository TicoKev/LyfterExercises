from abc import ABC, abstractmethod

class Shape(ABC):

  @abstractmethod
  def calculate_perimeter(self):
    pass


  @abstractmethod
  def calculate_area(self):
    pass


class Circle(Shape):

  def __init__(self, radius):
    self.radius = radius

  
  def calculate_perimeter(self):
    perimeter = 2 * 3.14 * self.radius
    return perimeter
  

  def calculate_area(self):
    area = 3.14 * (self.radius**2)
    return area
  
class Square(Shape):

  def __init__(self, side):
    self.side = side


  def calculate_perimeter(self):
    perimeter = self.side * 4
    return perimeter
  

  def calculate_area(self):
    area = self.side**2
    return area
  


class Rectangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height

  
  def calculate_perimeter(self):
    perimeter = 2*(self.base + self.height)
    return perimeter

  def calculate_area(self):
    area = self.base *  self.height
    return area
  


circle = Circle(10)
print(circle.calculate_area())
print(circle.calculate_perimeter())

square = Square(5)
print(square.calculate_area())
print(square.calculate_perimeter())

rectangle = Rectangle(10, 5)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())