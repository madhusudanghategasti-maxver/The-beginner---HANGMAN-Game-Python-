import random
#list of variables
words = [
    # Animals
    "wolf", "bear", "frog", "lion", "duck",
    "hawk", "fish", "deer",

    # Countries
    "peru", "cuba", "iraq", "iran", "chad",
    "fiji", "oman", "togo", "laos", "mali",

    # Food & Drink
    "rice", "cake", "milk", "soup", "corn",
    "beef", "taco", "lime", "salt", "pear",
    "soda", "mango",

    # Sports
    "golf", "yoga", "polo", "judo", "swim",
    "surf", "bowl", "race", "punt",

    # Technology
    "app", "bug", "data", "code", "chip",
    "byte", "file", "disk", "font", "icon",
    "loop", "node", "wifi", "scan", "sync",

    # Nature
    "tree", "leaf", "rain", "snow", "sand",
    "rock", "cave", "lake", "wave", "moon",
    "bush", "soil", "pond",

    # Household
    "mop", "pan", "cup", "jar", "rug",
    "tap", "bed", "fan", "mat", "key",
    "lamp", "fork", "door", "sink", "bowl",
    "soap", "sofa", "lock", "rope", "tape",
]
game=[]
game_Q=[]
life=6
#functions
#function for selecting word
def word_sel(word):
    global game
    global game_Q
    chosen_word=random.choice(word)
    for letter in chosen_word:
        game.append(letter)
        game_Q.append('_')
    return game, game_Q

#function for logic
def correct(game,let,game_Q):
    global hangman
    global life
    if let in game:
        index = game.index(let)
        game_Q[index]=let
        print(game_Q)
        print(hangman[life])
        print(f"****************************{life}/6 LIVES LEFT****************************")
    else:
        life-=1
        print(f"You guessed {let} that's not in the word. You lose a life.")
        print(hangman[life])
        print(f"****************************{life}/6 LIVES LEFT****************************")


#logo of the game
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

hangman=('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''')

#main statement of the prog
word_sel(words)
print(game)
print(f"Word to guess = {''.join(game_Q)}")
while life!=0:
    letter_guessed=input("guess a letter: ")
    correct(game,letter_guessed,game_Q)
    if life==0:
        print("***********************IT WAS squawk! YOU LOSE**********************")
        exit()
    elif game_Q==game:
        print("***********************WINNER WINER you fucking nigger!!**********************")
        exit()


