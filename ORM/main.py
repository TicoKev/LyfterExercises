from sqlalchemy import select
from database import engine
from models.base import Base
from models.user import User
from models.car import Car
from models.address import Address
from managers.user_manager import UserManager
from managers.car_manager import CarManager
from managers.address_manager import AddressManager


def main():
  Base.metadata.create_all(engine)
  
  user = UserManager()
  user.create_user('Peter Weyland', 'weyland@gmail.com')
  user.create_user('David Findlay', 'da_find@outlook.com')
  user.create_user('Ashley Graham', 'ash@yahoo.com')
  users = user.get_all_users()
  
  if users is False:
    print('An error ocurred')
  elif not users:
    print('There are no users in the database')
  else:
    for u in users:
      print(f'id: {u.id}, name: {u.name}, email: {u.email}')

  car = CarManager() 

  car.create_car('Toyota', 'Land Cruiser')
  car.create_car('Chevrolet', 'Camaro')
  car.create_car('BMW', 'M4')
  car.create_car('Mercedes Benz', 'G-wagon')

  car.assign_car_to_user(1, 1)
  car.assign_car_to_user(2, 2)
  car.assign_car_to_user(3, None)

  car.delete_car(4)

  cars = car.get_all_cars()

  if cars is False:
    print('An error ocurred')
  elif not cars:
        print('There are no cars in the database')
  else:
    for c in cars:
      print(f'id: {c.id}, make: {c.make}, model: {c.model}, user: {c.user_id}')

  address = AddressManager()
  address.create_address('123 Main Street, New York, NY', 1)
  address.create_address('45 Park Avenue, Brooklyn, NY', 2)
  address.create_address('789 Oak Street, Los Angeles, CA', 3)

  addresses = address.get_all_addresses()

  if addresses is False:
    print('An error ocurred')
  elif not addresses:
        print('There are no addresses in the database')
  else:
    for a in addresses:
      print(f'id: {a.id}, address: {a.address}, user: {a.user_id}')

if __name__ == '__main__':
  main()