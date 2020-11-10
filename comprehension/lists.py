#
# Examnples of comprehension lists vs map or for loops
#

# Example: Create a simply list
# You can use a list comprehensions

x = [x for x in range(10)]
print(x)

# Or  you can use loops
numbers = []

for x in range(10):
    numbers.append(x)

print(numbers)

# Example: multiplying parts of a list

multiplied = [item*3 for item in [3, 5, 4]]
print(multiplied)

# Example: Show the first letter of each word

listOfWords = ["this", "is", "a", "list", "of", "words"]

items = [word[0] for word in listOfWords]
print(items)

# Example: Lower/Upper case converter

lower = [letter.lower() for letter in ["A", "B", "C"]]
print(lower)

upper = [letter.upper() for letter in ["a", "b", "c"]]
print(upper)

#
# Comparison list comprehensions - for loop - lambda function
#

# For loop
h_letters = []

for letter in "human":
    h_letters.append(letter)

print(h_letters)

# List comprehension
h_letters = [letter for letter in "human"]
print(h_letters)

# Lambda function
letters = list(map(lambda x: x, "human"))
print(letters)

# Example: Conditionals in list comprehensions
number_list = [x for x in range(20) if x % 2 == 0]
print(numbers)

# Example: nested conditional (FILTERING)
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

# Example: if... else with list comprehension (TO CHANGE VALUE)
obj = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(obj)