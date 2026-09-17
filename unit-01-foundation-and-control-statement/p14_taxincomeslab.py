income=int(input("enter a person income :"))
if income>120000:
    taxpay=income*10/100
    print("the tax payable is ", taxpay)
elif income>200000:
    taxpay=income*15/100
    print("the tax payable is ",taxpay)
else:
    taxpay=income*20/100
    print("tax payable is ",taxpay)        