import random
number=random.randint(1,100)
while True:
    guess=int(input("enter number to guess"))
    if guess==number:
        print("you guessed it coorrectly")
        break
    elif  guess>number:
                print("too high") 
    else:
                print("too low")       
