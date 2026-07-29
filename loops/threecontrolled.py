#controlled statements 

#break
names = ["Alice", "Bob", "Charlie","", "David", "Eve"]
for name in names:
    if name == "":
        print("Empty name found, stopping the loop.")
        break
    print(f"Hello, {name}!")

#continue
for name in names:
    if name == "":
        print("Empty name found, skipping this iteration.")
        continue
    print(f"Hello, {name}!")

#pass

for name in names:
    if name == "":
        print("Empty name found, doing nothing for this iteration.")
        pass   #todo: we can add some code here to handle the empty name case in future
        #name = name.replace("", "Unknown") #this will print even for empty name, we can add some code here to handle the empty name case in future
    print(f"Hello, {name}!")


#Task for continue and break: loop list of dayes  print only the working days , skiping the weekends

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    if day == "Saturday" or day == "Sunday": #if day in ["Saturday", "Sunday"]: #if day is in the list of weekends
       # print(f"{day} is a weekend, skipping this day.")
        continue
    print(f"{day} is a working day.")

for day in days:
    if day in ["Saturday", "Sunday"]: #if day is in the list of weekends
       # print(f"{day} is a weekend, skipping this day.")
        pass
    print(f"Working day: {day} ")
print(f"Last day processed: {day}")

# Task scan emails to block unsafe data from entering your system
emails = ["srasd.asd@df.com", "" ,"test.tes@gmail.com" ,"Drop table users;","mariya@gmail.com"]
for email in emails:
    if email == "":
        print("Empty email found, skipping this iteration.")
        continue
    if "@" not in email:
        print(f"Unsafe email found: {email}, stopping the loop.")
        break
    if ";"  in email:
        print(f"Unsafe email found: {email}, stopping the loop.")
        break
    print(f"Valid email: {email}")