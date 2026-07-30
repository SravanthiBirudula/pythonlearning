mul_2 = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y: x + y  

print(mul_2(5))  # Output: 10
print(multiply(3, 4))  # Output: 12 
print(add(10, 5))  # Output: 15


check_char_exists = lambda x: x in 'python'
print(check_char_exists('p'))  # Output: True

#ask user to enter an charecter and check if it exists in the string 'python'
#user_input = input("Enter a character to check if it exists in the string : ")
check_char_exists = lambda x: x in 'sravanthi'
#print(check_char_exists(user_input))


prices = ['$5.99', '$9.99', '$14.99']
# Convert prices to float values
convert_price_simp  = lambda p : float(p.replace('$', ''))
convert_price = lambda price: float(price[1:])
float_prices = list(map(convert_price, prices))
float_prices_simp = list(map(convert_price_simp, prices))
print(float_prices)
print(float_prices_simp)

#lambda + filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter even numbers using lambda and filter
get_even_numbers = lambda x: x % 2 == 0
even_numbers = list(filter(get_even_numbers, numbers))

prices=[100, 200, 300, 400, 500,120,90,80,70,60,50,40,30,20,10]
filter_prices = lambda x: x > 100
filtered_prices = list(filter(filter_prices, prices))

students = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 22},
    {'name': 'Charlie', 'age': 19}
]
# Filter students older than 20 5
filter_students = lambda student: student['age'] > 20
older_students = list(filter(filter_students, students))
print(older_students)  # Output: [{'name': 'Bob', 'age': 22}]

student_marks = [['John', 85], ['Jane', 92], ['Jim', 78], ['Jack', 90]]
# Filter students with marks greater than 80
filter_high_marks = lambda student: student[1] > 80
high_mark_students = list(filter(filter_high_marks, student_marks))
print(high_mark_students)  # Output: [['John', 85], ['Jane', 92], ['Jack', 90]]

# create a list of tuples with student names and their marks
student_marks = [('John', 85), ('Jane', 92), ('Aim', 78), ('Jack', 90)]
filter_stu= lambda i :i[0].startswith('j')
filtered_students = list(filter(filter_stu, student_marks))
print(filtered_students)  # Output: [('John', 85), ('Jane', 92), ('Jack', 90)]