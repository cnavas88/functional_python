
# Objects can behave as functions when we make them callable
# such as object(). This is accomplished using the __call__ method.
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return self.greeting + " " + name

# Every time we initiate an object of the Greeter class,
# we create a new object that can be called with a new name

morning = Greeter("good morning")  # Creates a calleable object
print(morning("John"))
print(morning("Maria"))