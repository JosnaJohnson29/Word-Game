🎮 Wordle Game – Python

A simple Wordle-style word guessing game developed using Python.

The player has 6 attempts to guess a randomly selected 5-letter word. The program provides colored feedback to help the player identify the correct letters and their positions.

📌 Features
🎯 Guess a random 5-letter word
🔢 Maximum of 6 attempts
✅ Checks whether the entered word is valid
🟢 Green indicates the letter is in the correct position
🟡 Yellow indicates the letter exists in the secret word but is in the wrong position
⚪ White indicates the letter is not in the secret word
📋 Displays remaining attempts
🎉 Shows a success message when the word is solved
❌ Shows the secret word if all attempts are used
🛠️ Technologies Used
Python
Random module
Colorama
File Handling
Classes and Objects
Lists and Sets
Functions
Loops
Conditional Statements
📂 Project Structure
Wordle-Game/
│
├── play_wordle.py
├── wordle.py
├── letter_state.py
├── convert_words.py
│
├── data/
│   ├── word_source.txt
│   └── wordle_words.txt
│
└── README.md
📄 File Description
play_wordle.py

This is the main file used to run the game.

It:

Loads the word list
Selects a random secret word
Takes the player's guesses
Validates the guesses
Displays the results
Shows whether the player won or lost

The game continues while attempts are available.

wordle.py

Contains the main Wordle class.

The game is configured for:

5-letter words
6 maximum attempts

It checks whether guessed letters are present in the secret word and whether they are in the correct position.

letter_state.py

Contains the LetterState class.

It keeps track of:

The letter
Whether the letter exists in the secret word
Whether the letter is in the correct position
convert_words.py

This program reads words from the source file and keeps only words that contain exactly 5 letters. These words are then saved into wordle_words.txt.

📦 Installation

Make sure Python is installed on your computer.

Install the required package:

pip install colorama
▶️ How to Run

Open the project folder in VS Code or a terminal.

Run:

python play_wordle.py

The program will ask:

Type your guess:

Enter a valid 5-letter word.

🎮 How the Game Works
The program selects a random 5-letter word.
The player enters a guess.
The program checks the guess.
The letters are displayed with different colors.
The player gets up to 6 attempts.
If the player guesses correctly, the game displays a success message.
If all attempts are used, the secret word is displayed.
🟢🟡⚪ Color Meaning
Color	Meaning
🟢 Green	Letter is in the correct position
🟡 Yellow	Letter exists but is in the wrong position
⚪ White	Letter is not in the secret word

The program uses colorama to display these results in the terminal.

💡 Example
Type your guess: HOUSE

Your results so far...

You have 5 attempts remaining.

The game continues until the player solves the word or uses all 6 attempts.

📚 What I Learned

Through this project, I practiced:

Python classes and objects
Functions
File handling
Lists and sets
Loops
Conditional statements
Random word selection
User input validation
Working with external Python packages
Organizing Python code into multiple files
🚀 Future Improvements

Possible improvements include:

Add difficulty levels
Add a score system
Add a replay option
Keep track of wins and losses
Add more word categories
Create a graphical user interface

Linkedin URL:https://lnkd.in/p/gjMH75KN

