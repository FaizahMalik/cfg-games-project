![img.png](README_images/wordguesser_logo.png)

---
## ABOUT

---

Our group project, WordGuesser, is entirely written in Python (apart from README.md which is in English).

Includes the following modules:
- ### Turtle
  - Used to allow program to create a drawing of a turtle in steps each time the user guesses a letter incorrectly 
  - Also, for displaying messages and the hidden word in the Turtle Graphics window.
  - Allows the user to input messages in a text bar within a small pop-up window titled 'WordGuesser'


---

## HOW TO PLAY

---

- #### Run main.py
  - A new window titled "Hangman? Pfffffft never heard of it" should appear
- Answer the questions on the pop-up window
- Start guessing and have fun!
- Alternatively, open up your terminal, navigate to correct folder and type `python main.py` to run the game
---

- #### create_json_wordsfile.py
  - The code in this file was used to create our json words file. Do not run it again.
- #### levels.py
  - The main logic of the game can be found here. Each level is separated into a subclass (Beginner, Medium, Hard). This file is imported into main.py
- #### main.py
  - This is where the game is run from.
- #### test_main.py
  - Thia is the file with the unit tests for the main.py file. Instructions on how to run the tests are at the bottom of the file, as well as at the bottom of the main.py file.
- #### test_levels.py
  - This is where you will find the unit tests we have written for our levels.py file, instructions on how to run the tests are at the bottom of the file
- #### test_turtle_window.py
  - Here you will find the unit tests we have written for the turtle_window.py file, instructions on how to run the tests are at the bottom of the file
- #### turtle_window.py
  - This is where the code that runs the turtle module can be found.
  - Includes the class TurtleWindow with methods that allow us to:
    - Create the turtle drawing in steps, method-by-method;
    - Clear and reset everything in Turtle.
- #### word_picker.py
  - This is where the WordPicker class which allows the user to play Campaign mode.
- #### words_list.json
  - This file includes all the words we use in the WordGuesser game.
