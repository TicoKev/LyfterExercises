discount = 0
two_percent_discount = 0.02
ten_percent_discount = 0.1
base_price = 100
final_price = 0
product_price = int(input("Ingrese el precio del producto: "))

if product_price < base_price:
  discount = product_price * two_percent_discount
else:
  discount = product_price * ten_percent_discount

final_price = product_price - discount

print (f"El precio con descuento es {final_price}")