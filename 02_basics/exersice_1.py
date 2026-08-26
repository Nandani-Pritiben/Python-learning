# classify person's group in age wise child(<13),teenager(13-19),adult(19-59),Senior(>60)
age=int(input("Enter your age:"))

if age in range(13):
    print("child")
elif (age>=13) and (age<19):
    print("teenager")
elif (age>=19) and (age<=60):
    print("Adult")
elif(age>60):
    print("Senior")
else:
    print("Invalid Input")