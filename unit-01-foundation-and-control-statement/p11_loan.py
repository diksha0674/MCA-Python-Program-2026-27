age=int(input("enter persons age :"))
income=int(input("enter monthly income :"))
score=int(input("enter credit score between 0 to 100 :"))
if score>80 and income >50000 and age >21 and age<50 :
    print("the person is reliable ")
elif score>50 and income <50000 and age >50 and age<60 :
    print("the person can be given loan on conditions")
elif score> 10 and income <10000 and age >60 and age <70:
    print("the person may/may not be reliable to give loan ")       
else:
    print("cant be given loan")    