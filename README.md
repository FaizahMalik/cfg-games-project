![img.png](README_images/wordguesser_logo.png)

---
##ABOUT

---

Our group project, WordGuesser, is entirely written in Python (apart from README.md which is in English).

Includes the following modules:
- ###Turtle
  - Used to allow program to create a drawing of a turtle in steps each time the user guesses a letter incorrectly 
  - Also for displaying messages and the hidden word in the Turtle Graphics window.
  - Allows the user to input messages in a text bar within a small pop-up window titled 'WordGuesser'


---

## HOW TO PLAY

---

- #### Run main.py
  - A new window titled "Hangman? Pfffffft never heard of it" should appear
- Answer the questions on the pop-up window.
- Start guessing and have fun!
- Alternatively, open up your terminal, navigate to correct folder and type `python main.py` to run the game
---

- #### create_json_wordsfile.py
  - The code in this file was used to create our json words file.
- #### levels.py
  - The main logic of the game can be found here. This file is imported into main.py
- #### main.py
  - This where the game is run from.
- #### test_levels.py
  - This is where you will find the unit tests we have written for our main.py file, instructions on how to run the tests are at the bottom of the file
- #### test_turtle_window.py
  - Here you will find the unit tests we have written for the turtle_window.py file, instructions on how to run the tests are at the bottom of the file
- #### turtle_window.py
  - This is where the code that runs the turtle module can be found.
  - Includes the class TurtleWindow with methods that allow us to:
    - Create the turtle drawing in steps, method-by-method
    - Clear and reset everything in Turtle.
    - 
- #### words_list.json
  - This file includes all the words we use in the WordGuesser game.