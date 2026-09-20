terms=int(input("enter no of terms. to generate fibonnaci series :"))
a=0
b=1
for i in range(terms):
    print(a)
    c=a+b
    a=b
    b=c
   
