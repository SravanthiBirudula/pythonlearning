#copying

letters = ['a', 'b', 'c', 'd', 'e']
print("letters:", letters)
letters_copy_2 = letters
print("letters copy using assignment:", letters_copy_2)
letters_copy_2.append('f') #adding 'f' to the letters_copy_2 list
print("letters after adding 'f' to letters_copy_2:", letters)
print("original letters list:", letters)
letters_copy_3 = list(letters) #copying the list using list() constructor
print("letters copy using list() constructor:", letters_copy_3)
letters_copy_1 = letters.copy() #copying the list using copy() method
letters_copy_1.append('g') #adding 'g' to the letters_copy_1 list
letters.remove('a') #removing 'a' from the letters_copy_1 list
print("letters copy using copy() method:", letters_copy_1)
print("original letters list:", letters)
#copying the list using slicing
letters_copy = letters[:]
print("letters copy using slicing:", letters_copy)

#matrix copying

matrix =[['a', 'b', 'c'],
         ['d', 'e', 'f'],   
         ['g', 'h', 'i']]

matrix_copy_1 = matrix.copy() #copying the matrix using copy() method
matrix.pop()
matrix_copy_1[0].append('j') #adding 'j' to the first row of the matrix_copy_1
print("original matrix:", matrix)
print("matrix copy using copy() method:", matrix_copy_1)

#deep copying the matrix using deepcopy() method from copy module
import copy 
matrix_copy_2 = copy.deepcopy(matrix) #deep copying the matrix using deepcopy() method
matrix_copy_2[0].append('k') #adding 'k' to the first row of the matrix_copy_2
print("original matrix:", matrix)   
print("matrix copy using deepcopy() method:", matrix_copy_2)



#testing is operator
original = [['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']]

#assignment
copy1 = original
print("same object?:", original is copy1, "\n") #True
cpoy2 = original.copy()
print("same object?:", original is cpoy2) #False
print("shared reference?:", original[0] is cpoy2[0], "\n") #True

copy3 = copy.deepcopy(original)
print("same object?:", original is copy3) #False   
print("shared reference?:", original[0] is copy3[0]) #False

