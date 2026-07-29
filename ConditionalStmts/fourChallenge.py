#validate the quality and correctness of email values
#email must not be empty
#must contain . and @
# it must contain exactly one @
# must end with .com , .org, .net, .edu, .gov
#must not be longer that 50 characters
# it must start or end with a letter or number

email = "sravanthi.birudula@gmail.com"
valid_email = True
if email is None or len(email) == 0 or email=="":
    print("Invalid email address length is zero")
else:
    #email = email.strip() # remove leading and trailing spaces
    if len(email) == 0:
        print("Invalid email address length is zero")
    elif "@" not in email or "." not in email:
        print("Invalid email address, must contain @ and .")
    elif not("@" in email and "." in email):
        print("Invalid email address, must contain @ and . another way to check")
    elif email.count("@") != 1:
        print("Invalid email address")
    elif not(email.endswith(('.com', '.org', '.net', '.edu', '.gov'))):# alternative way to check if email ends with any of the specified suffixes
        print("Invalid email address must end with .com, .org, .net, .edu, or .gov") 
    elif not (email.endswith(".com") or email.endswith(".org") or email.endswith(".net") or email.endswith(".edu") or email.endswith(".gov")):
        print("Invalid email address")
    elif len(email) > 50:
        print("Invalid email address")
    elif not (email[0].isalnum() and email[-1].isalnum()):
        print("Invalid email address not starting or ending with a letter or number")
    elif(email.count(".") == 0):
        print("Invalid email address")
    else:
        print("Valid email address")
    # The following block is redundant and should be removed


    #want to check with independent if statements instead of elif statements
    if len(email) == 0:
        print("Invalid email address length is zero")
        valid_email = False
    if "@" not in email or "." not in email:
        print("Invalid email address, must contain @ and .")
        valid_email = False
    if not("@" in email and "." in email):
        print("Invalid email address, must contain @ and . another way to check")
        valid_email = False
    if email.count("@") != 1:
        print("Invalid email address")
        valid_email = False
    if not(email.endswith(('.com', '.org', '.net', '.edu', '.gov'))):# alternative way to check if email ends with any of the specified suffixes
        print("Invalid email address must end with .com, .org, .net, .edu, or .gov")
        valid_email = False
    if not (email.endswith(".com") or email.endswith(".org") or email.endswith(".net") or email.endswith(".edu") or email.endswith(".gov")):
        print("Invalid email address")
        valid_email = False
    if len(email) > 50: 
        print("Invalid email address")
        valid_email = False
    if not (email[0].isalnum() and email[-1].isalnum()):
        print("Invalid email address not starting or ending with a letter or number")
        valid_email = False
    if(email.count(".") == 0):
        print("Invalid email address")
        valid_email = False
    if valid_email:
        print("Valid email address individual if statements")


#-----------------------------------------------------------------------------------------------------------------------
#validate the qulity and correctness of password
#must not be empty
#must be at least 8 characters long
#must contain at least one uppercase letter, one lowercase letter
#must not be same as email
#must not contain spaces
#must start with and end with a letter or number

email ="birudula.sravanthi@gmail.com"
password = "Sraavnthi@123"
valid_password = True


if password is None or len(password) == 0 or password=="":
    print("Invalid password length is zero")
    valid_password = False
# elif password == password[::-1]: #password is a palindrome example: "racecar", "madam", "level", "deified"
#     print("Invalid password must not be a palindrome")
#     valid_password = False
elif password == "".join(reversed(password)): #password is a palindrome example: "racecar", "madam", "level", "deified"
    print("Invalid password must not be a palindrome")
    valid_password = False
elif len(password) < 8:
    print("Invalid password length is less than 8 characters")
    valid_password = False
elif password.upper() == password or password.lower() == password:
    print("Invalid password must contain at least one uppercase and one lowercase letter")
    print(password.capitalize())
    print(password.upper())
    print(password.lower())
    valid_password = False
elif password == email:
    print("Invalid password must not be same as email")
    valid_password = False
elif " " in password:
    print("Invalid password must not contain spaces")
    valid_password = False
elif not (password[0].isalnum() and password[-1].isalnum()):
    print("Invalid password must start and end with a letter or number")
    valid_password = False
print("Valid password" if valid_password else "Invalid password")


