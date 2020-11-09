# 
# Python program to demostrate pure functions
#

# A pure function that does not change the input list
# and return a new list with the result
def pure_func(original_list):
    new_list = []

    for item in original_list:
        new_list.append(item**2)

    return new_list

# A non pure function that does change the input list
def no_pure_func(original_list):
    for i in range(len(original_list)):
        original_list[i] = original_list[i]**2

#
# In this example we can see the effects in non pure function
# The pure function not change the input list, return a new
# list with the result. The non pure function modifies the input
# list and that list is modified in main function too.
# You lost the original list.
if __name__ == "__main__":
    # Not pure function
    original_list = [1, 2, 3, 4]
    no_pure_func(original_list)

    # Never print the original list. Is lost
    print("Original List:", original_list)
    print("Original List after call func:", original_list)

    # The same example with pure function
    original_list = [1, 2, 3, 4]
    modified_list = pure_func(original_list)

    print("Original List:", original_list)
    print("Modified List:", modified_list)