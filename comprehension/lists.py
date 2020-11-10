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