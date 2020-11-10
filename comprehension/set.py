#
# Example using set comprehensions
#

quote = "Life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)