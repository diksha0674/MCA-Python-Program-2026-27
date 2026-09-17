marks=int(input("enter marks of a student"))
if (marks<0 or marks>100):{
    print("invalid marks")
}
elif (marks>=90):{
    print ("topper")
}
elif(marks>=50):{
    print (" average marks")
}
elif(marks>=33):{
    print("below average")
}
else:{
    print("failure")
}        
