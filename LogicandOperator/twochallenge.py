#check if the username is not empty and age is greater tha or equal to 18 ----------------------------------1
user_name="" 
age=15
print((user_name !="" and user_name is not None) and age>=18)

#check if the password is atleast 8 charecters long and does not contain spaces ----------------------------2

password="srabirudula"
print(password)
print((len(password)>=8)and (" " not in password))
print((len(password)>=8 and (password.isspace()==False))) #isspace() method returns True if the string contains only whitespace characters, otherwise it returns False
print((len(password)>=8 and len(password) == len(password.replace(" ","")))) #
# trim the password and check if it is atleast 8 charecters long and does not contain spaces
password="sra     birudula      "
print(password)
print(len(password))
print(len(password.strip())) # print the length of the password after trimming the spaces from the start and end of the string
print(len(password.replace(" ",""))) # print the length of the password after removing all the spaces from the string
print((len(password.strip())>=8)and (" " not in password.strip()))

print((len(password.strip())>=8 and len(password) == len(password.replace(" ",""))) and  (password.strip().isspace()==False))

password="   "
print((len(password.strip())>=8 and (password.strip().isspace()==False))) 

#check if users email is not empty and contains "@" and ends with ".com"  ----------------------------------3

email="example@example.com"
print(email)
print((email !="" and email is not None) and ("@" in email) and email.endswith(".com"))


#check if a username is string , is not none and os longer than 5 charecters----------------------------------4
username="sravanthi"
print(username)
print((isinstance(username, str) and username is not None) and len(username) > 5)
print((type(username) is str and username is not None) and len(username) > 5)

#check if the user is either an admin or a moderator, and either they're not banned or they have verified their email. ------------------------------------------------5
is_admin=True
is_moderator =False
is_banned=False 
is_email_verified=True
print((is_admin or is_moderator) and (not is_banned or is_email_verified))
