#build a counter using while loop
i=0
while i<4:
    print("Round :",i)
    i+=1

answer = ""
while answer.lower() != "yes":
    answer = input("Do you want to exit? (yes/no): ")
print("thank you")


#while true

while True:
    answer = input("Do you want to exit? (yes/no): ")
    if answer.lower() == "yes":
        break
print("thank you")

#ctrl+ c to stop the infinite loop
# while True:
#    print("This is an infinite loop. Press Ctrl+C to stop it.")

#condition vs

while True:
    answer = input("Do you want to exit? (yes/no): ")
    if answer.lower() == "yes":
        break
    elif answer.lower() == "no":
        print("You chose not to exit. Continuing the loop.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

