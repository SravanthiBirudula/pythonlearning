#combining
letters = ['a', 'b', 'c']
words = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3]

#combining two lists using + operator
combined = letters + words+numbers
print("combined list:", combined)

comb =[letters, words, numbers]
print("combined list using list of lists:", comb)

numbers.extend(letters) #combining two lists using extend() method
print("letters",letters)
print("numbers",numbers)

#combining using zip() function
raw = zip(letters, words, numbers)
combined_zip = list(raw)
print("raw zip:", raw)
print("Ziped :::", combined_zip)


id=[101,102,103]
names=['Alice','Bob','Charlie']

combined_info = list(zip(id, names))
print("Combined info:", combined_info)

comb_info_dict = dict(zip(id, names))
print("Combined info as dictionary:", comb_info_dict)

