# digit=int(input("enter no. of digits"))
count=0
num=int(input("enter number :"))
temp=num
org=num
sum=0
while temp>0:
    d=temp%10
    count=count+1
    temp=temp//10
while num>0:
        rem=num%10
        sum=sum+rem**count
        num=num//10    
if sum==org:
    print("the number is armstrong number")
else:
    print("the number is not armstrong")        
