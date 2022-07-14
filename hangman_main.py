import random
# from replit import clear

import hangman_words
from hangman_art import logo,stages,you_win,you_lose,game_over,game_completed

print(logo)

chosen_word=random.choice(hangman_words.word_list)
word_length=len(chosen_word)

display=[]
for letter in range(word_length):
    display+='_'

end_of_game=False
life=6

while not end_of_game:  
    guess=input("Guess the letter = ").lower()
    # clear()
    
    if guess in display:
        print(f"You've already guessed {guess}")
    for  position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word.You lose life.")
        life-=1
        if life==0:
            end_of_game=True 
            print(you_lose)           

    print(display)
    if '_' not in display:
        end_of_game=True 
        print(you_win)
        

    # print(stages[life])    

    if life==0:
        print(game_over)

    if '_' not in display:
        print(game_completed)    