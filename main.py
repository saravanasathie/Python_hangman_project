import random
from hangman_words import word_list
from hangman_art import logo, stages
chosen_word = random.choice(word_list)
display = []
print(logo)

for i in chosen_word:
    display += "_"
lives = 6
end = False

while not end:
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print(f'You\'ve already guessed {guess}')
    for i in range(len(chosen_word)):
        #print(f"Current position: {i}\nCurrent letter: {chosen_word[i]}\nGuessed letter: {guess}")
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
    print(f"{' '.join(display)}")
    # print(''.join(display))

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose")
            end = True
            print(f"The solution is {chosen_word}.")

    if "_" not in display:
        end = True
        print("You win")

    print(stages[lives])