gb=int(input("enter total gb of data used :"))
if gb>10:
    bill=gb*21
    print("the bill is ",bill)
elif gb>30:
    bill= gb*33
    print("the monthly bill is :",bill)
elif gb>100:
    bill=gb*35
    print("the monthly bill is :",bill)
else:
    bill=gb*20
    print("the monhtly bill is ",bill)            