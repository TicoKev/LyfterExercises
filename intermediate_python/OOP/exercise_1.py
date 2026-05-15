class Circle:
  
  def __init__(self, radius):
    self.radius = radius

  def get_area(self):
    pi = 3.14
    return pi * self.radius **2
  

new_circle = Circle(5)

print(new_circle.get_area())