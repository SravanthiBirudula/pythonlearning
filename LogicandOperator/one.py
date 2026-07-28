print(True and False) # False
print(True or False) # True
print(not True) # False 
print(not False) # True
print(False or True) # True
print(True)
print(False)
print(type(True))
print (bool())
print (bool(0))
print(bool(123))
print (bool(""))
print (bool("Hello"))
print(bool(None))
print(bool([]))
print(bool([1, 2, 3])) # True


#all & any
print(all([True, True, True])) # True
print(all([True, False, True])) # False
print(any([False, False, False])) # False
print(any([True, False, True])) # True


email = ""
phone = "1234567890"
username = "username"
print (any([email, phone, username])) # True
print (all([email, phone, username])) # False

#isinstance() function is used to check if an object is an instance of a particular class or type. It takes two arguments: the object to be checked and the class or type to check against. It returns True if the object is an instance of the specified class or type, and False otherwise.

print(isinstance(5, int)) # True
print(isinstance(5.0, float)) # True
print(isinstance(True, str)) # False
print(isinstance("Hello", str)) # True
print(username.endswith("name")) # True
print(username.startswith("name")) # False


#------------------------------------comparision operator-----------------------------------------

print(5 == 5) # True
print(5 != 5) # False
print(5 > 3) # True
print(5 < 3) # False
print(5 >= 5) # True
print(5 <= 5) # True
print("a" < "b") # True
print("a" > "b") # False
print("a" == "A") # False
x = 50
print(x >= 50) # True
print(x < 100) # True
print(x <= 50) # True

#chain comparison operator
print(5 < 10 < 15) # True
print(5 < 10 > 15) # False

# age between 18 and 30
age = 25
print(18 <= age <= 30) # True


#-------------------------------------logical operators----------------------------------------

print((3>2) and (2<3)) # True
print((3>2) or (2>3)) # True
print(not (3>2)) # False

#check if the system is under pressure
cpu_usage = 70
memory_usage = 95
if cpu_usage > 80 and memory_usage > 90:
    print("System is under pressure")
else:
    print("System is running smoothly")

if cpu_usage > 80 or memory_usage > 90:
    print("System is under pressure")
else:
    print("System is running smoothly")


#check if the user credentials are valid
is_logged_in = True
is_password = False

print(is_logged_in and is_password) # False

print(not not is_logged_in) # True


#-------------------------------------execution order of logical operators----------------------------------------

print(True or False and False) # True, 'and' has higher precedence than 'or' 

#allow access only if the user is logged in
#or they are a guest
#but they they must not be banned
is_logged_in= True
is_guest = False
is_banned = False

print(is_logged_in or is_guest and not is_banned) # wrong output, 'and' has higher precedence than 'or'

print((is_logged_in or is_guest) and not is_banned)
if (is_logged_in or is_guest) and not is_banned:
    print("Access granted")

#--------------------------------membership operators(in)--------------------------------------------------------

print("a" in "apple") # True string membership operator
print("b" in "apple") # False string membership operator
print("c" not in "apple") # True string membership operator
print("apple" in ["apple", "banana", "cherry"]) # True list membership operator
print("grape" not in ["apple", "banana", "cherry"]) # True list membership operator
print("apple" in ("apple", "banana", "cherry")) # True tuple membership operator
print("grape" not in ("apple", "banana", "cherry")) # True tuple membership operator

domain = "spam.com"
banned_domains = ["spam.com", "junk.com", "trash.com"]
if domain in banned_domains:
    print("Access denied")


    #---------------------------------identity operators(is)--------------------------------------------------------

    x=['a', 'b', 'c']
    y=['a', 'b', 'c']

    print(x is y) # False, x and y are different objects in memory
    print(x == y) # True, x and y have the same values
    a=10
    b= 10
    print(a is b) # True, a and b refer to the same object in memory
    print(a == b) # True, a and b have the same values

    m=['a', 'b', 'c']
    n=m
    print(m is n) # True, m and n refer to the same object in memory
    print(m == n) # True, m and n have the same values


    #validate the email address , it must be filled in and no t be empty
    email="birudula.sravanthi@gmail.com"
    print(email)
    print(email is not None and email != "") # False, email is None and empty string
    print(email != "")
    print(email is not None and email != "") # False, email is None and empty string
    email=None
    print(email)
    print(email is not None and email != "") # False, email is None and empty string
    print(email != "")
    print(email is not None and email != "") # False, email is None and empty string
    email=""
    print(email)
    print(email is not None and email != "") # False, email is None and empty string
    print(email != "")
    print(email is not None and email != "") # False, email is None and empty string

