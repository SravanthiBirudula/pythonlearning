
text = """ A Cat is a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws.
 Cat is widely kept as a pet or for catching mice, and many breeds have been developed. Cats are known for their agility, playfulness, and ability to purr. 
 cats are also independent animals that can be both affectionate and aloof. """

print(text.count("cat")) #case sensitive
print(text.lower().count("cat")) #case insensitive

#Replace function
phone_number = "+49 (176) 123-4567"
phone_number = phone_number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("+","00")
print(phone_number)  # Output: +491761234567


#Transformations---------------------------------------------------
#concatination
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

folder_path = "C:\\Users\\John\\Documents"
file_name = "example.txt"
folder_path1 = "C:/Users/John/Documents"
file_name1 = "example.txt"
full_path = folder_path + "\\" + file_name
print(full_path)  # Output: C:\Users\John\Documents\example.txt
full_path1 = folder_path1 + "/" + file_name1
print(full_path1)  # Output: C:/Users/John/Documents/example.txt

#fstring ---------------------------------------------------------

name = "Alice"
age = 30
is_student = True
print("My name is "+name+", I am "+str(age)+" years old, and I am a student: "+str(is_student)+".")# concatenation
print("My name is {}, I am {} years old, and I am a student: {}.".format(name, age, is_student))#
print(f"My name is {name}, I am {age} years old, and I am a student: {is_student}.")#fstring
print("My name is {0}, I am {1} years old, and I am a student: {2}.".format(name, age, is_student))#fstring

#{} expression

print(f"2+3 = {2+3}")
print(f"10/3= {10/3:.2f}") #formatting to 2 decimal places
print(f"10/3= {10/3}") #formatting to 2 decimal places

#print(f"{this is my print statement}") #this will give error because of the space in the expression

print(f"{{this is my print statement}}") #this will print the string as it is because of the double curly braces

# need to print {this is my print statement} with out {} as this is my print statement using fstring
print(f"{{this is my print statement}}") #this will print the string as it is because of the double curly braces
print(f"this is my print statement") #this will print the string as it is because of the double curly braces


#split------------------------------------------------------------

sentence = "The quick brown fox jumps over the lazy dog"
sentence_list = sentence.split(" ")
print(sentence_list)  # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

date = "2023-06-15"
print(date.split("-"))  # Output: ['2023', '06', '15']

csv_data = "John,Doe,30,New York,2026-06-15"
print(csv_data.split(","))  # Output: ['John', 'Doe', '30', 'New York', '2026-06-15']

# repeat with * -----------------------------------------------------

print("Hello " * 3)  # Output: Hello Hello Hello
print("#" * 50)

# Indexes and Slicing-----------------------------------------------------

#Extract first  character of the string
text = "Hello, World!" 
print(text)
print(len(text))  # Output: 13
print(text.count(text))  # Output: 1
print(text[0])  # Output: H
print(text[-13])  # Output: H

#Extract last character of the string
print(text[-1])  # Output: !
print(text[12])  # Output: !

#Extract W from the string
print(text[7])  # Output: W

#Extract World from the string
print(text[7:12])  # Output: World

#Extract hel from the string
print(text[0:3].lower())  # Output: hel

#Extract sub string with skip by 2 
print(text[0:13:2])  # Output: Hlo ol!
print(text[0::2])  # Output: Hlo ol!
print(text[::2])  # Output: Hlo ol!
print(text[-13::2])  # Output: (empty string because the step is positive and the start is before the stop)
print(text[-13::2])  # Output: 'Hl'


