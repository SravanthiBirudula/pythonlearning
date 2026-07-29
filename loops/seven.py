attempts = 0
while attempts < 3:
    answer = input("Do you want to exit? (yes/no): ")
   # attempts += 1    # here we are incrementing the attempts counter by 1 each time the user enters an answer that is not "yes"
    if answer.lower() == "yes":
        print("glad we are in the same page")
        break
    attempts += 1   # here we are incrementing the attempts counter by 1 each time the user enters an answer that is not "yes"
else:
    print("3 strikes, you are out!")