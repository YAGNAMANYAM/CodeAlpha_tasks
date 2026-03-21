import random
words = ["apple", "roses", "chair", "green", "black"]
word = random.choice(words)
display = []
for letter in word:
    display.append("_")
guesses_left = 6
guessed_letters = []
print("Welcome to Hangman Game!")
# Game loop
while guesses_left > 0:
    print("\nWord:", " ".join(display))
    print("Guesses left:", guesses_left)
    guess = input("Enter a letter: ").lower()
    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        guesses_left -= 1
    if "_" not in display:
        print("\nYou won! The word was:", word)
        break
if guesses_left == 0:
    print("\nYou lost! The word was:", word)