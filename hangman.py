"""This file contains the hangman game.
It relies on files:
- data.py
- functions.py"""

from data import *
from functions import *
# We retrieve the scores of the game
scores = retrieve_scores()
# We retrieve a user_name
user = retrieve_user_name()
# If the user does not yet have a score, we add it
if user not in scores.keys():
 scores[user] = 0 # 0 point to start
# Our variable to know when to stop the game
continue_part = 'o'
while continue_part != 'n':
 print("Player {0}: {1} point(s)".format(user,scores[user]))
 word_to_find = choose_word()
 letters_found = []
 word_find = retrieve_hidden_word(word_to_find, letters_found)
 nb_chances = nb_moves
 while word_to_find!=word_find and nb_chances>0:
  print("Mot à trouver {0} (encore {1}chances)".format(word_find, nb_chances))
  letter = retrieve_letter()
  if letter in letters_found: # The letter has already been chosen
   print("You have already chosen this letter.")
  elif letter in word_to_find: # The letter is in the word to find
   letters_found.append(letter)
   print("Good game.")
  else:
   nb_chances -= 1
   print("... no, this letter is not found in the word...")
   word_find = retrieve_hidden_word(word_to_find,letters_found)
  # Have we found the word or are our chances exhausted ?
  if word_to_find==word_find:
   print("Congratulations ! You found the word{0}.".format(word_to_find))
  else:
   print("HANGEMAN!!! You lost.")
  # We update the user's score
   scores[user] += nb_chances
   continue_part = input("Would you like to continue the game(Y/N) ?")
   continue_part = continue_part.lower()
   # The game is over, we record the scores
   save_scores(scores)
   # We display the user's scores
   print("You end the game with {0} points.".format(scores[user]))