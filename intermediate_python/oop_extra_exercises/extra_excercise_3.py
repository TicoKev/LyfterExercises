class Product:
  
  def __init__(self, product_name, price, quantity):
    self.product_name = product_name
    self.price = price
    self.quantity = quantity

  def __str__(self):
    return f"{self.product_name} - Precio: {self.price}, Cantidad: {self.quantity}"

class Inventory:

  def __init__(self):
    self.products_list = []


  def add_product(self, product):
    self.products_list.append(product)


  def show_products(self):
    for product in self.products_list:
      print(product)


  def calculate_total_value(self):
    total = 0
    for product in self.products_list:
      total += product.price * product.quantity
    print(total)

product_1 = Product("Mouse", 5000, 3)
product_2 = Product("Keyboard", 8000, 2)

inventory = Inventory()

inventory.add_product(product_1)
inventory.add_product(product_2)

inventory.show_products()

inventory.calculate_total_value()