class Rectangle:
  
  def __init__(self):
    self.height = int(input("Enter the height: "))
    self.width = int(input("Enter the width: "))
  
    if self.height < 0 or self.width < 0:
      raise ValueError("There`s a negative value, both values must be a positive number")

  def get_area(self):
    return self.height * self.width
  
  def get_perimeter(self):
    
    return 2 * (self.height + self.width)
  
rectangle = Rectangle()

print(rectangle.get_area())
print(rectangle.get_perimeter())