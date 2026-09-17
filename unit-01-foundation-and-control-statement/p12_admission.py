math=int(input("enter marks of maths subject :"))
physics=int(input("enter marks of physics :"))
chem=int(input("enter marks of chemistry :"))
total=math+physics+chem
percentage=total/300*100
if math>50 and physics>50 and chem>50 and percentage>50:
    total=math+physics+chem
    percentage=total/300*100
    print("the person is eligible for admission beacuse percentage is :", percentage)
elif math>33 and physics>33 and chem>33 and percentage>33:
    total=math+physics+chem
    percentage=total/300*100
    print("the person can be admitted by giving entrance exam cause percentage is  ",percentage)
else:
    total=math+physics+chem
    percentage=total/300*100
    print("the person is not eligible for admission cause percentage is",percentage)    