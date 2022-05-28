# This file implements the word_game.
# Helper modules are in word_module.py

import word_module_level_2 as wm

# Playing a game is done in the following steps:

# YOU HAVE TO DO THIS

"""
Allow the user to play a series of hands

* Asks the user to input a total number of hands

* Accumulates the score for each hand into a total score for the
  entire series

* For each hand, before playing, ask the user if they want to substitute
  one letter for another. If the user inputs 'yes', prompt them for their
  desired letter. This can only be done once during the game. Once the
  substitue option is used, the user should not be asked if they want to
  substitute letters in the future.

* For each hand, ask the user if they would like to replay the hand.
  If the user inputs 'yes', they will replay the hand and keep
  the better of the two scores for that hand.  This can only be done once
  during the game. Once the replay option is used, the user should not
  be asked if they want to replay future hands. Replaying the hand does
  not count as one of the total number of hands the user initially
  wanted to play.

* Note: if you replay a hand, you do not get the option to substitute
        a letter - you must play whatever hand you just had.

* prints the total score for the series of hands and finished the program

word_list: list of lowercase strings
"""

# print welcome message and get going
print("Welcome to the physics718 word game!")
print("====================================")
print()

# load word list:
word_list = wm.load_words()

hand_size = 10 # size of a hand; you can change this if yu want to!

print()
print("Now we can start!")
n_hands = int(input("How many hands do you want to play? "))

total_score = 0
for i in range(n_hands):
    #hand = { 'a': 1, 'c' : 1, 'i' : 1, '*' : 1, 'p' : 1, 'r' : 1, 't' : 1 }
    #hand = { 'd': 2, '*' : 1, 'a' : 1, 'o' : 1, 'u' : 1, 't' : 1 }
    hand = wm.deal_hand(hand_size)
    hand_score = wm.play_hand(hand, word_list)
    total_score = total_score + hand_score

print()
print("Total score over {0} hands: {1}".format(n_hands, total_score))
print("Game over!")
