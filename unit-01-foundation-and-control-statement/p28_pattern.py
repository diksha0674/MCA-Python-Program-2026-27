n=int(input("enter n to make pattern"))
for i in range(1,n):
    for j in range(i):
        print(i+j,end="")
    print()    