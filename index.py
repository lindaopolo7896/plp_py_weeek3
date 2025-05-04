original_price=float(input("Enter the price of the item: "))
discount=float(input("Enter the discount percentage: "))



def calculate_discount(price,discount_percent):
  discount_percent=float(discount)/100
  if discount_percent >= 0.2:
    return price -(price * discount_percent)
  else:
    return price
  
final_price=calculate_discount(original_price,discount)
print(f"Final price after discount is: {final_price}")