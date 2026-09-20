prime=int(input("enter number whther to decide :"))
count=0
for i in range(1,prime+1):
    if prime%i==0:
        count=count+1
if count==2:
         print("the number is prime")
else:
         print("the number is not prime")            