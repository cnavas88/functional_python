#
# Example use map function
#

multiply_four = lambda x: x * 4

scores = [1, 2, 3, 4, 5]
result_map = map(multiply_four, scores)

print(list(result_map))

#
# The same example without first-class map function
#

def multiply_four_fn(x):
    return x * 4

scores = [1, 2, 3, 4, 5]

for i in range(len(scores)):
    scores[i] = multiply_four_fn(scores[i])

print(scores)
