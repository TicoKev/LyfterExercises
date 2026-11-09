from models.address import Address
from models.user import User
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from database import SessionLocal

class AddressManager():
  def create_address(self, address, user_id):
    session = SessionLocal()
    try:
      if user_id is None:
        print('User must not be None (null)')
        return False
      
      if isinstance(user_id, bool):
        print('user_id cannot be a boolean value')
        return False

      if not isinstance(user_id, int) or user_id <= 0:
        print('User id must be a positive number')
        return False

      get_user = select(User).filter_by(id=user_id)
      user = session.scalar(get_user)
      if user is None:
        print('User not found')
        return False
      
      address = Address(address=address, user_id=user_id)
      session.add(address)
      session.commit()
      return address
    except SQLAlchemyError as e:
      session.rollback()
      print(f'Error detected: {e}')
      return False
    finally:
      session.close()

  def update_address(self, address_id, new_address):
      session = SessionLocal()
      try:
        statement = select(Address).filter_by(id=address_id)
        address = session.scalar(statement)
        
        if not address:
          print('address not found')
          return False
        
        address.address = new_address
        session.commit()
        print('Address modified successfully!')
        return address
      
      except SQLAlchemyError as e:
        session.rollback()
        print(f'Error detected while updating the address: {e}')
        return False
      finally:
        session.close()

  def delete_address(self, address_id):
    session = SessionLocal()
    try:
      statement = select(Address).filter_by(id=address_id)
      address = session.scalar(statement)

      if not address:
        print('address not found')
        return False
      
      session.delete(address)
      session.commit()
      print('Address deleted successfully!')
      return True
    except SQLAlchemyError as e:
      session.rollback()
      print(f'Error detected while deleting the address, rollback applied: {e}')
      return False
    finally:
      session.close()

  def assign_address_to_user(self, address_id, user_id):
    session = SessionLocal()
    try:
      statement = select(Address).filter_by(id=address_id)
      address = session.scalar(statement)
      if not address:
        print('address not found')
        return False

      if user_id is None:
        print('User must not be None (null)')
        return False
      
      if not isinstance(user_id, int) or user_id <= 0:
        print('User id must be a positive number')
        return False
      
      get_user = select(User).filter_by(id=user_id)
      user = session.scalar(get_user)
      
      if not user:
        print('User not found')
        return False
    
      address.user_id = user_id
      session.commit()
      print('Address owner modified successfully!')
      return address
    except SQLAlchemyError as e:
      session.rollback()
      print(f'Error detected while updating the address owner: {e}')
      return False
    finally:
      session.close()

  def get_all_addresses(self):
    session = SessionLocal()
    try:
      statement = select(Address)
      addresses = session.scalars(statement)
      all_addresses = addresses.all()
      
      if len(all_addresses) == 0:
        return []
      return all_addresses
    except SQLAlchemyError as e:
      print(f'Error while getting the address {e}')
      return False
    finally:
      session.close()

  