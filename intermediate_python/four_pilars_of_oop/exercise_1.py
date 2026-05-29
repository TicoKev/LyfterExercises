class BankAccount():
  
  def __init__(self, balance):
    self.balance = balance


  def deposit(self, amount):
    self.balance +=amount
    return self.balance


  def withdraw(self, amount):
    self.balance -=amount
    return self.balance
class SavingAccount(BankAccount):

  def __init__(self, balance, min_balance):
    super().__init__(balance)
    self.min_balance = min_balance
  

  def deposit(self, amount):
    if amount < 0:
      raise ValueError("The deposit must be a positive number")
    return super().deposit(amount)
  

  def withdraw(self, amount):
    if amount < 0:
      raise ValueError("The withdraw must be a positive number")

    remaining = self.balance - amount

    if remaining < self.min_balance:
      raise ValueError("The withdraw cannot be completed because the balance would be less than the minimum required in the account.")
    
    self.balance = remaining
    return self.balance
    

savings_account = SavingAccount(100, 100)
print(savings_account.deposit(400))
print(savings_account.withdraw(100))
print(savings_account.withdraw(100))
print(savings_account.withdraw(100))
print(savings_account.withdraw(100))
print(savings_account.withdraw(100))