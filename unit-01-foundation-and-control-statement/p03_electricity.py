unit=int(input("enter electricity bill units"))
if unit<100:
    bill=unit*1.0
    print("the electricity bill is ",bill)
elif unit>100:
    bill=unit*1.5
    print("the electricity bill is ",bill)
elif unit>200:
    bill=unit*2.5
    print("the electricity bill is ",bill)
elif unit>300:
    bill=unit*3.5
    print("the electricity bill is ",bill)
elif unit>500:
    bill=unit*2.5
    print("the electricity bill is ",bill)