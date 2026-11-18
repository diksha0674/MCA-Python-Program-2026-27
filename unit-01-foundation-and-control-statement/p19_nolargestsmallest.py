num=int(input("enter number "))
count=0
a=num%10
big=a
small=a
while num>0:
    rem=num%10
    count=count+1
    if rem>big:
            big=rem
    if rem<small:
            small=rem
    num=num//10
print("the digits are: " ,count)
print("the smallest digit is :",small)
print("the biggest digit is :",big)
