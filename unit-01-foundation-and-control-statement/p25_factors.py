number=int(input("enter a number "))
count=0
for i in range(1,number+1):
    if number%i==0:
        count=count+1
        print ("the factors of number",number," are",i)
print("the number of factors are",count)