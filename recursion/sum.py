# Recursive function to find sum of a list
def sum(list, i, n, count):
    # Base case
    if n <= i:
        return count

    count += L[i]

    # Going into the recursion
    return sum(list, i + 1, n, count)

L = [1, 2, 3, 4, 5]
count = 0
n = len(L)
print(sum(L, 0, n, count))