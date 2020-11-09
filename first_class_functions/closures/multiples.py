# Closure: functions can be defined inside of other functions
# as well and these are aptly called inner functions.

def multiples(factor):
    def intern(value):
        return value * factor

    return intern

# We make multiples of 2
multiples_2 = multiples(2)

# We make multiples of 7
multiples_7 = multiples(7)

print(multiples_2(10))
print(multiples_7(10))

# Other form to call this
print(multiples(2)(10))
print(multiples(7)(10))
