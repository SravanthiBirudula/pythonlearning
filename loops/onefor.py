for i in (1,2,3,4,5):
    print("Round :",i)
    print(f"Round : {i}")

items =(1,2,3,4,5) #tuple
for i in items:
    print("Round :",i)
    print(f"Round : {i}")

items =(1,2,3,4,'HI') #tuple
for i in items:
    print("Round :",i)
    print(f"Round : {i}")

items =[1,2,3,4,'HI'] #list
for i in items:
    print("Round :",i)
    print(f"Round f : {i}")

items =" python "
for i in items:  
    print(f"Data characters: {i}")

for i in items.strip():  
    print(f"Data characters: {i}")

for i in range(10): #stop
    print(f"Range stop : {i}")

for i in range(1, 10): #start, stop
    print(f"Range start, stop : {i}")

for i in range(1, 10, 2): #start, stop, step
    print(f"Range start, stop, step - odd number : {i}")

for i in range(0, 10, 2): #start, stop, step
    print(f"Range start, stop, step - even number : {i}")

#dictionary for loop
dict = {"name": "John", "age": 30, "city": "New York"}
for key in dict:
    print(f"Key: {key}, Value: {dict[key]}")

#file for loop
# with open("test.txt", "r") as file:
#     # for line in file:
#     #     print(f"Line: {line} line number: file.readline()") 
        
#     #     print(f"Line: {line.strip()}") #empty line
#     #     #print(f"Line {file.tell()}: {line.strip()}") #add line number infront of each line not working as expected, file.tell() returns the current position of the file pointer in bytes, not the line number. To get the line number, you can use enumerate() function.
#     #     print(f"Line {file.readline()}: {line.strip()}") #add line number infront of each line not working as expected, file.readline() returns the current line number, not the line number. To get the line number, you can use enumerate() function.
#         #print(f"Line {enumerate(file)}: {line.strip()}") #add line number infront of each line not working as expected, enumerate() returns an enumerate object, which is an iterator that yields pairs of index and value. To get the line number, you can use a for loop with enumerate() function.
#     for i, line in enumerate(file, 1):
#         print(f"Line test {i}: {line.strip()}") #correct way to add line number infront of each line

with open("test.txt", "r") as file:
     content = file.read()
     lines = content.split(",")     
for line_number, line in enumerate(lines, 1):
        print(f"Line{line_number} : {line.strip()}\n") #correct way to add line number infront of each line
