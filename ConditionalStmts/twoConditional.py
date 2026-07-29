#if condiftion is true, then the code inside the if block will be executed
score=80
submitted_assignment=True
if(score>=50):
    print("You have passed the exam")
else:
    print("You have failed the exam")

topgrade = "A"
grade = "B"  
if(score>70):
    print(f"You have got an {topgrade} grade")
else:
    print(f"You have got a {grade} grade")


if(score>=50):
    print("You have passed the exam")
    if(score>=70):
        if(submitted_assignment):
            print("You have submitted the assignment")
        else:
            print("You have not submitted the assignment")        
        print(f"You have got an {topgrade} grade")
    elif (score>=50):
        print(f"You have got a {grade} grade")
    elif(score<50 and score>=0):
        print("You have failed the exam")
    else:
        print("You have not attended the exam")

if(score<0 or score>100):
    print("Invalid score")
elif(score>=50 and submitted_assignment):
    print("You have passed the exam and submitted the assignment")
elif(score>=50 and not submitted_assignment):
    print("You have passed the exam but not submitted the assignment")
elif(score<50 and submitted_assignment):
    print("You have failed the exam but submitted the assignment")
elif(score<50 and not submitted_assignment):
    print("You have failed the exam and not submitted the assignment")
elif(score == 0):
    print("You have not attended the exam")


#--------------------------------------------inline if ot ternary-------------------------------------------------

# inline if statement
print("You have passed the exam") if(score>=50) else print("You have failed the exam")
print(f"You have passed the exam and got {topgrade} grade" if(score>=50) else "You have not passed the exam or not submitted the assignment")

grade = "A" if(score>=70) else "B" if(score>=50) else "C"
print(f"You have got a {grade} grade")


# we can rewrite the above code in a more readable way using parentheses and indentation bad pracrtice but it is more readable
#if in this case go to normal if else statement
grade = (
    "A" if(score>=70) 
    else "B" 
    if(score>=50) 
    else "C" 
    if(score>=0) 
    else "Invalid")
print(f"You have got a {grade} grade")

