#
# Example of use a simple decorator 
#
# Recall that a decorator is just a regular Python function. 
# All the usual tools for easy reusability are available. 
# Let’s move the decorator to its own module that can be used 
# in many other functions.

def my_decorator(func):
    def wrapper():
        print("**************")
        func()
        print("**************")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()