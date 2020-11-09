# Functions, like other objects, can be stored inside of data
# structures. For instance, we can create a dictionary of int 
# to func. This is useful for when the ins is a shorthand for
# a procedure to be performed.

def foo():
    print("Foooo")

def bar():
    print("Baaar")

mapping = {
    0: foo,
    1: bar
}

x = input() # get integer value from user
mapping[x]() # Call the func returned by dictionary access