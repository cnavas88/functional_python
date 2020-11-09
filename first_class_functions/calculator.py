def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def calculator(opcode):
    if opcode == 1:
        return add
    elif opcode == 2:
        return sub
    else:
        return mult

my_calc = calculator(2) # My calc is a substractor
result = my_calc(5, 4)
print(result)

my_calc = calculator(9) # My calc is now a multiplier
result = my_calc(5, 4)
print(result)