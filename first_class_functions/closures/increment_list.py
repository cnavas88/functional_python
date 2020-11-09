def increment(inc):
    # create a function that loops and adds the increment
    def add_increment(numbers):
        new_numbers = []
        for n in numbers:
            new_numbers.append(n + inc)

        return new_numbers

    # We return the function as we do any other value
    return add_increment

add5 = increment(5)
print(add5([0, 5, 10, 15]))