from models.user import User
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from database import SessionLocal

class UserManager():
  def create_user(self, name, email):
    session = SessionLocal()
    try:
      user = User(name=name, email=email)
      session.add(user)
      session.commit()
      return user
    except SQLAlchemyError as e:
      session.rollback()
      print(f'Error detected: {e}')
      return False
    finally:
      session.close()

  def update_user(self, user_id, name, email):
      session = SessionLocal()
      try:
        statement = select(User).filter_by(id=user_id)
        user = session.scalar(statement)
        if not user:
          print('user not found')
          return False
        user.name = name
        user.email = email
        session.commit()
        print('User modified successfully!')
        return user
      except SQLAlchemyError as e:
        print(f'Error detected while updating the user: {e}')
        return False
      finally:
        session.close()

  def delete_user(self, user_id):
    session = SessionLocal()
    try:
      statement = select(User).filter_by(id=user_id)
      user = session.scalar(statement)

      if not user:
        print('User not found')
        return False
      session.delete(user)
      session.commit()
      print('User deleted successfully!')
      return True
    except SQLAlchemyError as e:
      session.rollback()
      print(f'Error detected while deleting the user, rollback applied: {e}')
      return False
    finally:
      session.close()

  def get_all_users(self):
    session = SessionLocal()
    try:
      statement = select(User)
      users =session.scalars(statement)
      users = users.all()
      if len(users) == 0:
        return []
      return users
    except SQLAlchemyError as e:
      print(f'Error while getting the users {e}')
      return False
    finally:
      session.close()