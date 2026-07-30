#iterable

#list is iterable
letters=['a','b','c','d','e'] #656756776 cannot be iterated
numbers=[1,2,3,4,5]
new_list =[]
for l in letters:
    new_list.append(l.upper())    
   # print(l)
    print(new_list)


print(list(enumerate(letters,start=1))) 
print(list(reversed(letters)))

for index, letter in enumerate(letters, start=1):
    print(f"Index: {index}, Letter: {letter}")

for i in reversed(letters):
    print(f"Letter: {i}")

print(list(zip(letters, numbers)))

for l, n in zip(letters, numbers):
    print(l,n)


#--------------------------------------------map--------------------------------------

map_list = list(map(str.upper, letters))
print(map_list)

numbers_s= ['1', '2', '3', '4', '5']
map_list_2 = list(map(int, numbers_s))
print(map_list_2)

names = ['  Alice  ', 'Bob  ', '   Charlie']
map_list_3 = list(map(str.strip, names))
print(map_list_3)

for l in map_list_3:
    print(f"Name: {l}")

for l in map(str.strip, names):
    print(f"Name S: {l}")


#---------------------------------------------------------------------------------------------

letter_fil=['a','', 'c', None, 'e',False]
filtered_list = list(filter(None, letter_fil))
filtered_list_1 = list(filter(bool, letter_fil))
print(filtered_list)
print(filtered_list_1)


items = ['apple', 'banana', 'cherry', 'date','123','456','789']
filtered_items = list(filter(str.isalpha, items))
filtered_items_int= list(filter(str.isdigit, items))
print(filtered_items_int)
print(filtered_items)

for i in filtered_items:
    print(f"Item: {i}")





    


