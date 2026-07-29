items=[1,3,5,7,9,2,11,13,15]
for i in items:
    print("Round :",i)
else:
    print("Loop is completed")


#else + break

for i in items:
    if i % 2 == 0:
        print("Even number found, breaking the loop", i)
        break
else:
    print("No even number found, loop is completed")


#list of names check for any missing vaues

names = ["John", "Jane", "Jim", None, "Jack", "Jill", "Joe"]
for name in names:
    if name is None:
        print("Missing name found, breaking the loop")
        break
else:
    print("No missing names found, loop is completed")


# check if all files are .csv

files = ["file1.csv", "file2.csv", "file3.csv", "file4.csv", "file5.txt"]
for file in files:
    if not file.endswith(".csv"):
        print("Non-csv file found, breaking the loop", file)
        break
else:
    print("All files are csv, loop is completed")

#another way to check if all files are .csv

# for file in files:
#     if file.endswith(".csv"):
#         print("All files are csv, loop is completed")
#     else:
#         print("Non-csv file found, breaking the loop", file)
#         break

#check duplicates values in files names list

files = ['file1.csv', 'file2.csv', 'file3.csv', 'file4.csv', 'file5.txt', 'file.csv']
for file in files:
    if files.count(file) > 1:
        print("Duplicate file found")
        break
else:
    print("All files  are unique")