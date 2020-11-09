#
# Examples of use and comparison lambda function with def functions
#

def increment(x):
    return x + 1

# Use increment function
print("Increment without lambda:", increment(1))

# Transform to lambda function
increment = lambda x: x + 1
print("Increment with lambda:", increment(1))

result = (lambda x, y: x * y)(5, 5)
print("Multiplier lambda:", result)