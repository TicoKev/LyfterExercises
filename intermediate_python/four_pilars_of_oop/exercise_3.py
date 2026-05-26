class Cleaner:
  def __init__(self, name):
     self.name = name

  def clean(self):
    return f"{self.name} cleaning the floor"

class Cook:
  def cook(self):
    return f"{self.name} cooking dinner"

class Robot(Cleaner, Cook):
  def __init__(self, robot_model):
    super().__init__(robot_model)
    

robot = Robot("T-800")
print(robot.clean())  
print(robot.cook())  