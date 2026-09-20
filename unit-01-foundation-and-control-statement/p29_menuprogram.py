while True:
    choice=int(input("enter choice \n 1.prime no \n 2.palindrome \n 3.armstrong \n 4. factorial \n 5. fibonnaci series \n 6.exit \n"))       
    if choice==6:
            print("exit")
            break 
    num=int(input("enter value :"))
    if choice==1:
                count=0
                for i in range(1,num+1):
                    if num%i==0:
                        count=count+1
                if count==2:
                    print("the number",num,"entered is prime number") 
                    break
                else:
                    print("the number is not prime number")
                    break
    if choice==2:
                org=num
                rev=0
                while num>0:
                    rem=num%10
                    rev=rev*10+rem 
                    num=num//10
                if rev==org:
                        print("the number is palindrome")
                else:
                        print("the number is not palindrome ")                      
    if choice==3:
                org=num
                arm=0
                while num>0:
                    rem=num%10
                    arm=rem**3+arm     
                    num=num//10
                if arm==org:
                        print("the number is armstrong number")
                else:
                        print("the number is not armstrong")
                # break        
    if choice==4:
                fact=1
                for i in range(1,num+1):
                    fact=fact*i
                    print("the factorials are",fact)   
                                
    if choice==5:
                a=0
                b=1
                for i in range(num):
                    print("the fibonnaci series is ",a)
                    c=a+b
                    a=b
                    b=c
                          