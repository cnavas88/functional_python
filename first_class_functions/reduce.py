#
# use example of first class function reduce
#

import functools

lambda_reduce = lambda x, y: x + y

scores = [1, 2, 3, 4, 5]
total = functools.reduce(lambda_reduce, scores, 0)
print(total)

#
# The same example without using reduce function
#

scores = [1, 2, 3, 4, 5]
total = 0

for i in scores:
    total += i

print(total)

