pin=int(input("enter a 4 digit pin"))
balance=int(input("enter balance amount"))
withdraw=int(input("enter a withdraw amount"))
if balance<100 and withdraw>100:
    print("the balance is insufficient and cant withdraw")
elif balance<withdraw:
    print("the withdrawing amount is more than balance")    
else:
    print("the amount ",withdraw,"is withdrawn")  
    print("the final balance is ", (balance-withdraw))  
