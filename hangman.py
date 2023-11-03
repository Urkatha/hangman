import random

class Hangman:
    def __init__(self, word_list, num_lives=6):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' if letter.isalpha() else letter for letter in self.word]
        self.guesses = set()

    def display_word(self):
        return ' '.join(self.word_guessed)

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guesses:
            return "You already guessed this letter!"
        self.guesses.add(letter)
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
            if '_' not in self.word_guessed:
                return "Congratulations! You guessed the word: " + self.word
            else:
                return "Good guess!"
        else:
            self.num_lives -= 1
            if self.num_lives <= 0:
                return "Game Over! The word was: " + self.word
            else:
                return "Wrong guess! You have {} lives left.".format(self.num_lives)

# List of words for the game
word_list = ["python", "hangman", "developer", "programming", "computer", "keyboard", "monitor"]

# Main game loop
if __name__ == "__main__":
    game = Hangman(word_list)
    print("Welcome to Hangman!")
    print(game.display_word())

    while '_' in game.word_guessed and game.num_lives > 0:
        guess = input("Guess a letter: ")
        result = game.guess_letter(guess)
        print(result)
        print(game.display_word())

    if '_' not in game.word_guessed:
        print("Congratulations! You guessed the word: " + game.word)
    else:
        print("Game Over! The word was: " + game.word)
