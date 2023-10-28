#Omar Shahwan   10/28/23    WORDLE
#The following project codes a Wordle game in which the user tries to find what the hidden five-letter word is within six guesses.
#User is prompted to input a word, given 'Y' for letters in the word in a different place, 'G' for letters in the right place, and '_' for incorrect.


import random

words = ["ABOUT","AUDIO","BAKED","BINGE","CLOUD","COUCH","FLARE","FLOAT","SNIPE","STARE"]
answer = random.choice(words)

def get_clue(ans, guess):
    clue = ""
    for idx, letter in enumerate(guess):
        if letter == ans[idx]:
            clue += "G"
        elif letter in ans:
            clue += "Y"
        else:
            clue += "_"
    return clue
    
for x in range(1,7):
    guess = input("Word? ")[0:5]
    guess = guess.upper()
    print (get_clue(answer, guess), x)
    if answer == guess:
        break
