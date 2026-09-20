abc=int(input("enter values"))
sum=0
pro=1
while abc>0:
    rem=abc%10
    abc=abc//10
    sum=sum+rem
    pro=pro*rem
print(sum)
print(pro)    