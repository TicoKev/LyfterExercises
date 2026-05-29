from datetime import date


class User():
  date_of_birth : date

  def __init__(self, date_of_birth):
    self.date_of_birth = date_of_birth


  @property
  def age(self):
    today = date.today()
    get_age = today.year - self.date_of_birth.year

    if(today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
      get_age -=1
    return get_age
 
def check_user_age(func):
  def wrapper(user):
    user
    result = func(user)
    if result < 18:
      raise ValueError("You`re not an adult")
    
    return result
  return wrapper
    


user = User(date(2015, 6, 15))

@check_user_age
def user_age(user):
  return user.age

print(user_age(user))