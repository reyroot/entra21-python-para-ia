#Challenge Class 01

print("===CASH FLOW AND CLIENT REGISTER===")

client_name = input("Whats your name ?")

print("Register the  product 1")
item1_quantity =  int(input("How many items?"))
item1_price = float(input("How much is it?"))
item1_subtotal = item1_quantity * item1_price

print("Register the  product 2")
item2_quantity =  int(input("How many items?"))
item2_price = float(input("How much is it?"))
item2_subtotal = item2_quantity * item2_price

print("Register the  product 3")
item3_quantity =  int(input("How many items?"))
item3_price = float(input("How much is it?"))
item3_subtotal = item3_quantity * item3_price

total = item1_subtotal + item2_subtotal + item3_subtotal

discount = 0.0

#If total is more than 50 then apply 10% discount
if(total > 50):
   discount = total * 0.1

final_total = total - discount

#Print the fiscal cupon

print("=" * 60)
print(f"{' ' * 30} FISCAL CUPON {' ' * 30}")

print(f"\nName: {client_name}\n")

print("ITEMS LIST")
print(f"Item 1  Qnt: {item1_quantity} Price: {item1_price:.2f} Sub Total: R$ {item1_subtotal:.2f} ")
print(f"Item 2  Qnt: {item2_quantity} Price: {item2_price:.2f} Sub Total: R$ {item2_subtotal:.2f} ")
print(f"Item 3  Qnt: {item3_quantity} Price: {item3_price:.2f} Sub Total: R$ {item3_subtotal:.2f} ")
print(f"Final Total: $R {final_total:.2f}")

if(discount > 0.0):
  print(f"You get $R {discount:.2f} of discount")
print("=" * 60)



