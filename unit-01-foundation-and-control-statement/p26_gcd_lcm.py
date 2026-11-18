num1=int(input("enter first number"))
num2=int(input("enter second number"))
pro=1
if num1>num2:
    for i in range(1,num1):
        if num1%i==0 and num2%i==0:
            pro=i
else:
     for i in range(1,num2):
            if num1%i==0 and num2%i==0:
                pro=i 
if num1>num2:
    for j in range(num1,num1*num2+1):
        if j%num1==0 and j%num2==0:
            print("the lcm is ", i)
else:
     for j in range(num2,num1*num2+1):
            if j%num1==0 and j%num2==0:
                 break
print("the gcd is",pro)                
print("the lcm is",j)
                
           

