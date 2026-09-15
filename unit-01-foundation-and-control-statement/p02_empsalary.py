salary=int(input("enter salary"))
other=int(input("enter other allowances"))
pf=int(input("enter provident fund"))
da=int(input("enter da percentage"))
d=salary*(da/100)
hra=salary+d/50*100
gross=salary+other+d+hra
it=gross*10/100
net=gross-(pf+it)
print(salary)
print("daily allowance is",d)
print("house rent allowance is", hra)
print("the gros salary is ",gross)
print("the net salary is ",net)

