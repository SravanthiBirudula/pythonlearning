# strip , lstrip , rstrip , split , join , replace , find , index , count , upper , lower , title , capitalize , isalpha , isdigit , isspace

text = "     The cat sat on the mat. The cat is very cute.     "

print(text.strip()) #strip
#print(text.strip(".")) #strip
print(text.lstrip()) #lstrip
print(text.rstrip()) #rstrip

data = ";;;;;####;;;;;Hello World!;;;;;####;;;;;"

print(data.strip("#")) #strip
print(data.strip(";")) #strip # doesnt work 

name = "     John Doe     "
print(len(name)) #length of the string with spaces
print(len(name.strip())) #strip

print(len(name)-len(name.strip())) #length of the string with spaces - length of the string without spaces = number of spaces
print(len(name)==len(name.strip()))

no_of_spaces = len(name)-len(name.strip())
is_clean=no_of_spaces==0
is_clean_name = len(name)==len(name.strip())
print("Is the string clean? ", is_clean)
print("no of spaces in the string: ", no_of_spaces)
print("Is the name clean? ", is_clean_name)

#--------------------------------clean cases--------------------------

#case conversion
text = "hello WORLD , good morning , have a nice day"
textcomp = "     hello WORLD , Good Morning , have a nice day     "
print(text.upper()) #upper
print(text.lower()) #lower
print(text.title()) #title
print(text.capitalize()) #capitalize

print(text == textcomp) #false
print(text.lower() == textcomp.lower()) #false
print(text.strip() == textcomp.strip()) #false
print(text.lower().strip() == textcomp.lower().strip()) #true


# Exercise -------------------------------------------------------------

raw_text= "968-Maria, ( D@t@ Engineer ) ;; 27y  "
expected_clean_text = "name: Maria | role: Data Enginee | age: 27y"

raw_text_clean = raw_text.strip().replace(";;","").replace("@","a").replace(",","").replace("(","").replace(")","").replace("968-","name: ").replace(" D","| role: d").replace(" 27y"," | age: 27y").replace("  "," ")
raw_text_clean_1 = raw_text.replace(";;","").replace("@","a").replace(",","").replace("(","").replace(")","").replace("968-","name: ").replace(" D","| role: d").replace(" 27y"," | age: 27y").replace("  "," ")
print(raw_text_clean)


#------------------------------------------------------------------------













