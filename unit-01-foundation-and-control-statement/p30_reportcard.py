n=int(input("enter number of students:"))
sum=0
avg=0
countfail=0
countpass=0
ctop=0
high=0
low=100
for i in range(1,n+1):
    marks=int(input("enter marks from 0 to 100:"))
    sum=sum+marks
    avg=sum/n
    if marks>high:
        high=marks
    if marks<low:
        low=marks     
    if marks>=75 and marks<=100:
        ctop=ctop+1
    elif marks>=33 and marks<75:
        countpass=countpass+1
    else:
        countfail=countfail+1    
# print("the total marks by student are",sum)
print("the class average is :",avg)
print("students passed are :",countpass+ctop)
print("the students failed are :", countfail)
print("the toppers are :",ctop)
print("the highes marks is :",high)
print("the lowest marks is :",low)

