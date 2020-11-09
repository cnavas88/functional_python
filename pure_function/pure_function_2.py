#
# Other example of pure functions pluralize the words
#
def non_pure_pluralize(words):
    for i in range(len(words)):
        word = words[i]
        if word.endswith("s") or word.endswith("x"):
            word += "es"
        elif word.endswith("y"):
            word = word[:-1] + "ies"
        else:
            word += "s"

        words[i] = word

#
# This pure function not modify the input list. Create the new
# list with the result and return that list
#
def pure_pluralize(words):
    result = []

    for i in range(len(words)):
        word = words[i]
        if word.endswith("s") or word.endswith("x"):
            word += "es"
        elif word.endswith("y"):
            word = word[:-1] + "ies"
        else:
            word += "s"

        result.append(word)
        
    return result        

if __name__ == "__main__":
    # Pluralize dictionary with non pure function
    dictionary = ["fox", "boss", "orange", "toes", "fairy", "cup"]
    non_pure_pluralize(dictionary)

    print("Non pure pluralize:", dictionary)

    # Pluralize dictionary with PURE function
    original_dictionary = ["fox", "boss", "orange", "toes", "fairy", "cup"]
    modified_dictionary = pure_pluralize(original_dictionary)

    print("Original Dictionary:", original_dictionary)
    print("Modified Dictionary:", modified_dictionary)