#loops to go through  values and aggregate data like sum, average, min, max, count, etc
scores = [90, 80, 70, 60, 50, 40, 30, 20, 10, 50]
total = 0
line =1
for score in scores:
    total += score
    print(f"Line: {line}, Score: {score}, Total: {total}")
    line += 1
print(f"Total: {total}, Average: {total/len(scores)}, Min: {min(scores)}, Max: {max(scores)}, Count: {len(scores)}")

#inconsistent casing $ unnessary spaces 
files = ["  file1.txt", "FILE2.CSV", "file3.txt", "File4.txt", "file5.txt", "file6.txt", "file7.txt", "file8.TXT", "file9.CSV", "file10.txt "]
line =1
for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"File {line}: {file}")
    line += 1

#print the 7 times table using for loop form 1 to 10
table = 7
#table = input("Enter the number to print the times table: ") 
for i in range(1,11):
    print(f"{table} x {i} = {int(table)*i}")

text = "*"
for i in range(1, 6):
    print(text*i)

for i in range(5, 0, -1):
    print(text*i)