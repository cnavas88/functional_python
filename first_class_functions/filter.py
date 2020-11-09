#
# Example use first class function FILTER
#

filter_fn = lambda x: True if (x % 2 == 0) else False

scores = [3, 6, 8, 3, 5, 7]
even_scores = filter(filter_fn, scores)

print(list(even_scores))

#
# The same example not using first class function filter
#

def get_odd(x):
    if (x % 2 == 0):
        return True
    else:
        return False

scores = [3, 6, 8, 3, 5, 7]
odd_scores = []

for i in range(len(scores)):
    if get_odd(scores[i]):
        odd_scores.append(scores[i])

print(odd_scores)