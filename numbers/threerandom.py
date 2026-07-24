#random numbers
import random
print(random.random()) # generates a random float between 0 and 1
print(random.randint(1, 10)) # generates a random integer between 1 and 10
print(random.uniform(1, 10)) # generates a random float between 1 and 10
print(random.choice(['apple', 'banana', 'cherry'])) # randomly selects an item from a list
print(random.sample(range(1, 100), 5)) # randomly selects 5 unique numbers from a range of 1 to 100
random_number = random.randint(1, 100) # generates a random integer between 1 and 100
print(random_number)