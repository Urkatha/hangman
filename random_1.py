
import random
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
random_word = random.choice(word_list)
word = random_word

print(word)

guess = input("Enter a single letter: ")
print("You guessed:", guess)
