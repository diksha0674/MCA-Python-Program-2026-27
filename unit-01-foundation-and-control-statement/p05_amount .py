price=int(input("enter price :"))
quantity =int(input("enter quantity "))
discount=int(input("enter discount = "))
subtotal=price+quantity
print("the subtotal is ",subtotal)
grand=subtotal*discount/100
gst= grand*5/100
grandtotal=subtotal -discount + gst 
print("the grand total is ",grandtotal)

