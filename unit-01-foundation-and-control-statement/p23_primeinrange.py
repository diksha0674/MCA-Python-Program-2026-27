rangestart=int(input("enter starting range : "))
rangeend=int(input("enter ending range(dont use infinite) :"))
count=0
for i in range(rangestart,rangeend+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        count=count+1
        print(i)
print("the total no. of prime nos are :",count)        