
#  This is a hangman game in python

This game allows you to manipulate files in python

The first point of the mission is to create a hangman game. Project description: the computer chooses a
random word in a list, a word of eight letters maximum. The player tries to find the letters making up the word. Every
Suddenly, he grabbed a letter. If the letter appears in the word, the computer displays the word with the letters already found. Those who do not
are not yet are replaced by stars (*). The player has 8 chances. Beyond that, he loses.
We are going to complicate the rules a little by asking the player to give their name at the start of the game. This will allow the
program to record your score.

#The technical side of the problem: 

I remind you that the player must not
only give one letter at a time and the program must check that this is the case before continuing. We will
split our program into three files:
The data.py file which will contain the variables necessary for our application (the list of words, the number of
authorized chances…).
The functions.py file which will contain the functions useful to our application. There, I am not giving you any clear list,
I advise you to think about it carefully, with a sheet of paper and a pen if that helps you (What are the actions of my
program ? What can I put in functions?).
Finally, our hangman.py file which will contain our hangman game.

#Manage scores:

we will save to a file
data, which we will call scores (without any extension) the scores of the game. These scores will be in the form of a
dictionary: in keys, we will have the names of the players and in values ​​the scores, in the form of integers.
The following cases must be managed:
The file does not exist. There, we create an empty dictionary, no score was found.
Player is not in the dictionary. In this case, we add it with a score of 0.

## Documentation

[Documentation](https://docs.python.org/release/3.12.2/tutorial/index.html)


## 🚀 About Author
Bonevy BEBY is an Accross Plateforms Archictecturer, an Engineer and Trainer. He's also passionnate with DevOPs and Cloud Services.


## 🛠 Skills
Javascript, HTML, CSS,java,Javascript,Typescript,Python,PHP,DOT.NET...





