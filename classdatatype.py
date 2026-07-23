#Data Types

a= 10 #int
b= 10.5 #float
c= "Python" #string
d='Python' #string
e="131" #string
f= True #boolean , case senstitive
g= False #boolean , case senstitive
h= None #NoneType
i = "" #string , we called it as as blank 
j=" " #string , we called it as empty space

#h= 10

print(type(h))

length = len(c)
print(length)
print(d.upper())
print(a.bit_length())
print(a.bit_count())

#are you a student? , yes or no
is_student = input("Are you a student? (yes or no): ")  
print("You answered:", is_student)
print("Type of is_student:", type(is_student))

#take input as boolean value
is_student_bool = is_student.lower() == "yes"
print("Boolean value of is_student:", is_student_bool)
print("Type of is_student_bool:", type(is_student_bool))

#accept input as integer value
age = int(input("Enter your age: "))
print("You entered:", age)
print("Type of age:", type(age))

#accept input as boolean value
is_employed = input("Are you employed? (yes or no): ")
is_employed_bool = is_employed.lower() == "yes"
print("Boolean value of is_employed:", is_employed_bool)
print("Type of is_employed_bool:", type(is_employed_bool))
