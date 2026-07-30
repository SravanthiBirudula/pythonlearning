numbers =[1,2,3,4,5,6,7,8,9,10]
print("Numbers in the list are: ", numbers)
print("Even numbers in the list are: ", [num for num in numbers if num % 2 == 0])
print("Odd numbers in the list are: ", [num for num in numbers if num % 2 != 0])
print("max:", max(numbers))
print("min:", min(numbers)) 
print("sum:", sum(numbers))
print("total count:", len(numbers))
print("average:", sum(numbers)/len(numbers))
print("count of 5:", numbers.count(5))
print("index of 5:", numbers.index(5))
print("sorted list:", sorted(numbers))
print("reversed list:", list(reversed(numbers)))
print("squared list:", [num**2 for num in numbers])
print("cubed list:", [num**3 for num in numbers])
print("even numbers squared:", [num**2 for num in numbers if num % 2 == 0])
print("any number greater than 5:", any(num > 5 for num in numbers))
print("all numbers greater than 0:", all(num > 0 for num in numbers))
print("is 5 in the list:", 5 in numbers)
print("is 5 not in the list:", 5 not in numbers)
print("is 11 in the list:", 11 in numbers)
# is operator checks if an element is present in a list or not, it returns True if the element is present in the list, otherwise it returns False.
print("is 11 in the list:", 11 in numbers)
print("index of 5:", numbers.index(5))
print(type(numbers))
one, two,*details,ten= numbers
print("one:", one)
one,_,_,*details,ten= numbers
print("ten:", ten)
print("details:", details)
print(numbers[0:5]) #print first 5 elements
print(numbers[-5:]) #print last 5 elements
print(numbers[::2]) #print every second element
 
print(numbers[1:9:2]) #print every second element from index 1 to 9
print(numbers[5]) #print the element at index 5

print("all:", all(numbers)) #check if all elements are true
print("all:", all([1,2,3,4,5])) #check if all elements are true
print("all:", all([0,1,2,3,4,5])) #check if all elements are false
print("all:",all(['a','b','c'])) #check if all elements are true
print("all:",all(['a','','c'])) #check if all elements are false
print("any:", any(numbers)) #check if any element is true
print("any:", any(['a','','c'])) #check if any element is true
print("any:", any([0,1,2,3,4,5])) #check if any element is true

list1=[1,2,3,4,5]
list3=[1,2,3,4,5]
list2=[6,7,8,9,10]
print("concatenated list:", list1 + list2)
print(list1==list2) #check if two lists are equal
print("list1 is list2:", list1 is list2) #check if two lists are the same object
print("list1 is list3:", list1 is list3) #check if two lists are the same object

letters = ['a','b','c','d','e']
print("letters:", letters)
letters.append('f') #add an element to the end of the list
print("letters after append:", letters)
letters.insert(2, 'z') #insert 'z' at index 2
print("letters after insert:", letters)
#sort the list in ascending order
letters.sort() #sort the list in ascending order
print("letters after sort:", letters)
letters.remove('z') #remove 'z' from the list
print("letters after remove:", letters)
letters.pop() #remove the last element from the list
print("letters after pop:", letters)
letters.clear() #remove all elements from the list
print("letters after clear:", letters)


#matrix append
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print("matrix:", matrix)
matrix.append([10,11,12]) #add a new row to the matrix
print("matrix after append:", matrix)
matrix[1].append(13) #add a new element to the second row
print("matrix after append to second row:", matrix)
matrix[0].insert(1, 14) #insert a new element at index 1 of the first row
print("matrix after insert to first row:", matrix)
matrix[2].insert(-1,15) #insert a new element at index -1 of the third row
print("matrix after insert to third row:", matrix)
matrix[3].append(5) #remove the element 5 from the second row
#print the matrix in a formatted way
for row in matrix:
    print(row)


#sorting list
letters = ['d','a','c','b','e']
print("letters:", letters)
letters.sort() #sort the list in ascending order
print("letters after sort:", letters)
letters.sort(reverse=True) #sort the list in descending order
print("letters after sort reverse:", letters)

letters = ['d','a','c','b','e']
print("letters:", letters)
new_letters = sorted(letters) #sort the list in ascending order and return a new list
print("new letters after sorted:", new_letters) 
new_letters_desc = sorted(letters, reverse=True) #sort the list in descending order and return a new list
print("new letters after sorted reverse:", new_letters_desc)

matrix = [['a', 'b', 'c'],
          ['d', 'e', 'f'],  
          ['g', 'h', 'i'],
          ['d', 'e', 'f']]


matrix.sort(key=lambda x: x[1]) #sort the matrix based on the second element of each row
print("matrix after sort based on second element:", matrix)

for row in matrix:
    print(row)

#reverse the list 

letters = ['d','a','c','b','e']
print("letters:", letters)
letters.reverse() #reverse the list
print("letters after reverse:", letters)
new_letters = list(reversed(letters)) #reverse the list and return a new list
print("new letters after reversed:", new_letters)