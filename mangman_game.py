
import random

words =["python", "java", "kotlin", "javascript"]

def get_letter_frequency(w):
    letters_set = set(w)   
    combis = {}
    for item in letters_set:
        inds =[]
        for i, l in enumerate(w):
            if l == item:
                inds.append(i)
        combis[item] = inds  
    return combis

def guess_letter(word, to_guess, attempt, already_guessed):
    lst_frequencies = get_letter_frequency(word)
    letter = input("Input a letter:")
    if len(letter) != 1:
        print("You should input a single letter")
        return "".join(to_guess), attempt, already_guessed
    elif not letter.isalpha() or not letter.islower():
        print("It is not an ASCII lowercase letter")
        return "".join(to_guess), attempt, already_guessed
    else:
        if letter in already_guessed:
            print("You already typed this letter")
            return "".join(to_guess), attempt, already_guessed
        elif letter in word:
                already_guessed.append(letter)
                indexes = lst_frequencies.get(letter)
                for i in indexes:
                    to_guess[i] = letter          
                return "".join(to_guess), attempt, already_guessed
        else:
                already_guessed.append(letter)
                print("No such letter in the word")
                return "".join(to_guess), attempt+1, already_guessed

def start():
    attempt = 0
    winner = random.choice(words)     
    already_guessed =[]
    to_guess = "-" * len(winner)
    
    while attempt < 8:
        print()
        print(to_guess)
        to_guess = list(to_guess)
        to_guess, attempt, already_guessed = guess_letter(winner, to_guess, attempt, already_guessed)
        
        
    if to_guess == winner:
        print(to_guess)
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")

def play_game():
    print("H A N G M A N")
    while True:
        move = input('Type "play" to play the game, "exit" to quit:')
        if move == "play":
            start()
        else:
            break
        
        
play_game()