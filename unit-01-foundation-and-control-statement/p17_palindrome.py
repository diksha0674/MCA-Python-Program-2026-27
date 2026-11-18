palindrome=int(input("enter a number to check for palindrome"))
org=0
rev=palindrome
while palindrome>0:
    rem=palindrome%10
    org=(org*10)+rem
    palindrome=palindrome//10
if rev==org:
        print("palindrome")
else:
        print("not palindrome") 