"""This file defines useful functions for the hanged program.
We use the program data contained in data.py"""
import os
import pickle
from random import choice
from data import *

# Score management
def retrieve_scores():
    """This function retrieves the saved scores if the file
       exists.
       In all cases, we return a dictionary,
      either the unpickled object,
       or an empty dictionary.
       We rely on score_file_name defined in data.py"""
    if not os.path.exists(scores_file_name):  # the file doesn't exists
        scores = {}
    else:  # The file exists
        # we retrieve the file
        scores_file = open(scores_file_name, "rb")
        my_depickler = pickle.Unpickler(scores_file)
        scores = my_depickler.load()
        scores_file.close()
    return scores
# Hangman Game Functions
def choose_word():
    """This function returns the word chosen from the list of words
    wordlist.
    We use the choice function of the random module (see help)."""
    return choice(words_list)
def retrieve_letter():
    """This function retrieves a letter entered by
    the user. If the retrieved string is not a letter,
    we recursively call the function until we obtain a letter"""
    letter = input("Type a letter: ")
    letter = letter.lower()
    if len(letter) > 1 or not letter.isalpha():
        print("You have not entered a valid letter.")
        return retrieve_letter()
    else:
        return letter
def save_scores(scores):
    """This function is responsible for recording the scores in the
    file file_name_scores. It receives as parameter the dictionary of
    score to save """
    scores_file = open(scores_file_name, "wb")  #
    my_pickler = pickle.Pickler(scores_file)
    my_pickler.dump(scores)
    scores_file.close()

# Functions managing user input
def retrieve_user_name():
    """Function responsible for retrieving the user_name.
    The user_name must be at least 4 characters long,
    numbers and letters exclusively.
    If this name is not valid, we recursively call the function
    to get a new one"""
    user_name = input("Enter your name: ")
    # Put the first letter in uppercase and the others in lowercase.
    user_name = user_name.capitalize()
    if not user_name.isalnum() or len(user_name) < 4:
        print("This name is invalid.")
        # We call the function again to have another name
        return retrieve_user_name()
    else:
        return user_name
def retrieve_hidden_word(full_word, letters_found):
    """This function returns a hidden word in whole or in part, in
    function:
    - of the original word (str type)
    - letters already found (type list)
    We return the original word with * replacing the letters that
    we have not yet found."""
    hidden_word = ""
    for letter in full_word:
        if letter in letters_found:
            hidden_word += letter
        else:
            hidden_word += "*"
    return hidden_word










