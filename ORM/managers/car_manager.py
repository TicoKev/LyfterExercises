from models.car import Car
from models.user import User
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from database import SessionLocal

class CarManager():
  def create_car(self, make, model, user=None):
    session = SessionLocal()
    try:
      car = Car(make=make, model=model, user=user)
      session.add(car)
      session.commit()
      return car
    except SQLAlchemyError as e:
      session.rollback()
      print(f'Error detected: {e}')
      return False
    finally:
      session.close()

  def update_car(self, car_id, new_make, new_model):
      session = SessionLocal()
      try:
        statement = select(Car).filter_by(id=car_id)
        car = session.scalar(statement)
        
        if not car:
          print('car not found')
          return False
        
        car.make = new_make
        car.model = new_model
        session.commit()
        print('car modified successfully!')
        return car
      
      except SQLAlchemyError as e:
        session.rollback()
        print(f'Error detected while updating the car: {e}')
        return False
      finally:
        session.close()

  def delete_car(self, car_id):
    session = SessionLocal()
    try:
      statement = select(Car).filter_by(id=car_id)
      car = session.scalar(statement)

      if not car:
        print('car not found')
        return False
      session.delete(car)
      session.commit()
      print('car deleted successfully!')
      return True
    except SQLAlchemyError as e:
      session.rollback()
      print(f'Error detected while deleting the car, rollback applied: {e}')
      return False
    finally:
      session.close()

  def assign_car_to_user(self, car_id, user_id):
    session = SessionLocal()
    try:
      statement = select(Car).filter_by(id=car_id)
      car = session.scalar(statement)
      if not car:
        print('car not found')
        return False

      if user_id is None:
        car.user_id = user_id
        session.commit()
        return car
      get_user = select(User).filter_by(id=user_id)
      user = session.scalar(get_user)
      
      if not user:
        print('User not found')
        return False
    
      car.user_id = user_id
      session.commit()
      print('car owner modified successfully!')
      return car
    except SQLAlchemyError as e:
      session.rollback()
      print(f'Error detected while updating the car owner: {e}')
      return False
    finally:
      session.close()

  def get_all_cars(self):
    session = SessionLocal()
    try:
      statement = select(Car)
      cars =session.scalars(statement)
      cars = cars.all()
      if len(cars) == 0:
        return []
      return cars
    except SQLAlchemyError as e:
      print(f'Error while getting the cars {e}')
      return False
    finally:
      session.close()

  