from random import choice

# Reading words from file
with open("word_list.txt", "r") as file_words:
    word_list = file_words.read().split("\n")
    get_word = choice(word_list)
    display_word = "-" * len(get_word)

# Game settings
tries = 12
guessed_letters = []

# Configuring the game
while True:
    print(display_word)
    print(f"You have {tries} tries left")
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You have already guessed that letter")
    else:
        guessed_letters.append(guess)
        if guess in get_word:
            for index, letter in enumerate(get_word):
                if letter == guess:
                    display_word = display_word[:index] + guess + display_word[index + 1:]
        else:
            tries -= 1

        # Checking game status
        if display_word == get_word:
            print(f"You win! The word was {get_word}")
            break
        elif tries == 0:
            print(f"You lose! The word was {get_word}")
            break

# Ending message
print("Thanks for playing our game!")