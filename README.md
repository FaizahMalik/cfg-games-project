![img.png](README_images/wordguesser_logo.png)

---

## ABOUT

---

WordGuesser is our group project for the Code First Girls Nanodegree 2021. It is entirely written in Python (apart from README.md which is in English).
This game allows the user to guess characters in a given word for a limited number of tries. Once the attempts are exhausted, the user loses. If the user guesses the word correctly, they win.

### Project plan

---

**MVP**

Our plan was to first define and create a Minimum Viable Product (MVP). As an MVP, program should allow the user to:
- select a random word from a words list, 
- show the hidden words in a "_ _ _ _" format 
- allow the user to guess a letter or word
- process that guess and tell them whether they are wrong or right
- replace the hidden word "_ _ _ _" with the correctly guessed characters in the right positions
- ask the user again until the whole word has been guessed

---

**New Features**

Once this MVP was achieved we added new features on a rolling basis using Kanban and Scrum project organisation techniques.
The new features we achieved are detailed below:

  - Create different **difficulty levels** (Beginner, Medium, Hard) using inheritance.


  - Create a new **words list** file which will have a huge list of words so that the user is less likely to get the same word twice.


  - Add a new game mode called **Campaign** where the user can make their way through given tasks.


  - **Draw a picture of a turtle** in steps using Turtle Graphics each time the user guesses incorrectly.


  - **Display messages on the Turtle screen** alerting whether the user guessed a wrong character, right character or the correct full word.


  - Check whether the user **already guessed a letter** and alert them, also don't take away from remaining attempts


  - Detect special characters and alert that **only exclusively letters** are allowed, again don't take away from remaining attempts


  - During the mode selection process, if the **user spells 'campaign' or 'levels' wrong**, alert them and ask again until correct.


  - Same with the level selection process, if the **user spells any of the levels wrong**, alert and ask again until correct


  - Make the program more user-friendly by:

    - Allowing the program to take **user inputs from Turtle** window pop-ups rather than from console.
    
    - Adding a **welcome, goodbye and loading screen**
    - Tell the user which mode and which difficulty they are playing during the loading screen



### Modules

---

- **Turtle**
  - Used to allow program to create a drawing of a turtle in steps each time the user guesses a letter incorrectly 
  - Also, for displaying messages and the hidden word in the Turtle Graphics window.
  - Allows the user to input messages in a text bar within a small pop-up window titled 'WordGuesser'


- **Random**
  - Allows the program to select a random choice from a list of words to be guessed so that the user does not receive the same word everytime


- **Json**
  - Used as a way for the program to write the entire words list into a json file which will be used to select words from.

- **NLTK**
  - Used to generate the list of words for the game

- **Collections - counter**
  - From Collections we use the counter function to identify words with all unique characters from the words list and have the user guess them in the unique characters task in campaign mode.
  

- **Unittest**
  - Allows us to write unit tests for each function or class method in the program to ensure that they all work

  


---

## HOW TO PLAY

---

- **Instructions**
  - Run `main.py`
  - A new window titled "Hangman? Pfffffft never heard of it" should appear
  - Questions will appear on a pop-up window
  - Answer the questions and tell WordGuesser which game mode you would like to play
  - Start guessing and have fun!
  - You have the option to play again at the end.
  - Alternatively you can open up your terminal, navigate to correct folder and type `python main.py` to run the game


- **Levels Mode**
  - This mode will allow you to select between Beginner, Medium or Hard difficulty
  - The number of attempts between difficulties varies as such:
    - Beginner: 9
    - Medium: 8
    - Hard: 7
  - You can enter a custom list of words to guess from too if you'd like!


- **Campaign Mode**
  - This mode will run through 10 given tasks.
  - Each task comes with instructions like "Guess a word with all unique characters"
  - This mode uses Beginner difficulty by default
  
---

  ## FILES

---

- `create_json_wordsfile.py`
  - The code in this file was used to create our json words file. Do not run it again.
- `levels.py`
  - The main logic of the game can be found here. Each level is separated into a subclass (Beginner, Medium, Hard). This file is imported into main.py
- `main.py`
  - This is where the game is run from.
- `test_main.py`
  - This is the file with the unit tests for the main.py file. Instructions on how to run the tests are at the bottom of the file, as well as at the bottom of the main.py file.
- `test_levels.py`
  - This is where you will find the unit tests we have written for our levels.py file, instructions on how to run the tests are at the bottom of the file
- `test_turtle_window.py`
  - Here you will find the unit tests we have written for the turtle_window.py file, instructions on how to run the tests are at the bottom of the file
- `turtle_window.py`
  - This is where the code that runs the turtle module can be found.
  - Includes the class TurtleWindow with methods that allow us to:
    - Create the turtle drawing in steps, method-by-method;
    - Clear and reset everything in Turtle.
    - Display text, focused or on the side
    - Show the welcome and goodbye screens
- `word_picker.py`
  - This is where the WordPicker class which allows the user to play Campaign mode.
- `words_list.json`
  - This file includes all the words we use in the WordGuesser game.

  
