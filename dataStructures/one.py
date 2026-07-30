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
print(numbers[::-1]) #print the list in reverse order
print(numbers[1:9:2]) #print every second element from index 1 to 9
print(numbers[5]) #print the element at index 5

print("all:", all(numbers)) #check if all elements are true
print("any:", any(numbers)) #check if any element is true
