from turtle import Turtle, Screen
import time

t = Turtle()
t1 = Turtle()
t2 = Turtle()
t.ht()
t1.ht()
t2.ht()
s = Screen()
s.title("Hangman? Pfffffft never heard of it.")

# t2 is small messages
# t1 is big messages
# t is turtle drawing

# TODO make class an iterator?!?!?!?!
# FIXME game lost function works but correct word function doesn't?!?!?1

class TurtleDrawing:
    def __init__(self):
        t.speed(10)
        t.pensize(8)
        t.penup()
        t.goto(0, -150)
        t.pendown()

    # def __iter__(self):
    #     self.n = 0
    #     return self
    #
    # def __next__(self):
    #     if self.n <= self.max:
    #         result = 2 ** self.n
    #         self.n += 1
    #         return result
    #     else:
    #         raise StopIteration

    # draw circle body
    # def initialise(self):
    #     screen = turtle.getscreen()
    #     screen.colormode(255)
    #     screen.setup(width=700, height=700)
    #     Donatello.bgcolor(87, 217, 255)

    def draw_body(self):
        t.penup()
        t.goto(0, -150)
        t.pendown()
        t.pencolor('dark green')
        t.fillcolor('forest green')
        t.begin_fill()
        r = 150
        t.circle(r)
        t.end_fill()

    # draw head
    def draw_head(self):
        t.pensize(4)
        t.penup()
        t.goto(-40, 150)
        t.pendown()
        t.pencolor('yellow green')
        t.fillcolor('yellow green')
        t.begin_fill()
        t.left(90)
        t.forward(30)
        for i in range(45):
            t.forward(3)
            t.right(4)
        t.forward(35)
        t.end_fill()

    # draw leg 1
    def draw_leg1(self):
        t.penup()
        t.goto(-85, 125)
        t.pendown()
        t.pencolor('yellow green')
        t.fillcolor('yellow green')
        t.begin_fill()
        t.right(135)
        t.forward(10)
        for i in range(45):
            t.forward(2)
            t.left(4)
        t.forward(10)
        t.end_fill()
        # t.done()

    # draw leg 2
    def draw_leg2(self):
        t.penup()
        t.goto(85, 125)
        t.pendown()
        t.pencolor('yellow green')
        t.fillcolor('yellow green')
        t.begin_fill()
        t.left(90)
        t.forward(10)
        for i in range(45):
            t.forward(2)
            t.right(4)
        t.forward(10)
        t.end_fill()
        # t.done()

    # draw leg 3
    def draw_leg3(self):
        t.penup()
        t.goto(-85, -125)
        t.pendown()
        t.pencolor('yellow green')
        t.fillcolor('yellow green')
        t.begin_fill()
        t.forward(10)
        for i in range(45):
            t.forward(2)
            t.right(4)
        t.forward(10)
        t.end_fill()
        # t.done()

    # draw leg 4
    def draw_leg4(self):
        t.penup()
        t.goto(85, -125)
        t.pendown()
        t.pencolor('yellow green')
        t.fillcolor('yellow green')
        t.begin_fill()
        t.right(90)
        t.forward(10)
        for i in range(45):
            t.forward(2)
            t.left(4)
        t.forward(10)
        t.end_fill()
        # # t.done()

    # draw tail
    def draw_tail(self):
        t.penup()
        t.goto(-15, -150)
        t.pendown()
        t.pencolor('yellow green')
        t.fillcolor('yellow green')
        t.begin_fill()
        t.right(180)
        t.forward(30)
        t.left(90)
        t.forward(30)
        t.end_fill()
        # # t.done()

    # draw back
    def draw_back_middle(self):
        t.pensize(10)
        t.penup()
        t.goto(-34, -60)
        t.pendown()
        t.pencolor('dark green')
        t.right(45)
        for i in range(6):
            t.forward(75)
            t.right(300)
            # # t.done()

    # draw back pattern
    def draw_back_line(self):
        t.pencolor('dark green')
        t.right(120)
        t.forward(78)
        t.penup()
        t.goto(41, -60)
        t.pendown()
        t.left(60)
        t.forward(78)
        t.penup()
        t.goto(75, 5)
        t.pendown()
        t.left(60)
        t.forward(75)
        t.penup()
        t.goto(42, 70)
        t.pendown()
        t.left(60)
        t.forward(68)
        t.penup()
        t.goto(-35, 70)
        t.pendown()
        t.left(60)
        t.forward(68)
        t.penup()
        t.goto(-70, 5)
        t.pendown()
        t.left(60)
        t.forward(72)
        # # t.done()

    # draw eyes
    def draw_eyes(self):
        t.penup()
        t.goto(-10, 185)
        t.pendown()
        t.circle(3)
        t.penup()
        t.goto(13, 185)
        t.pendown()
        t.circle(3)
        # # t.done()

    def draw_word(self, word):
        t1.pencolor(38, 70, 83)
        t1.clear()
        t1.speed(5)
        t1.pensize(4)
        t1.penup()
        t1.goto(-290, -250)
        t1.pendown()
        t1.write(word, move=False, align="Left", font=("arial", 25, "normal"))

    def welcome_screen(self):
        font_size = 1
        for x in range(20):
            if x % 2 == 0:
                t2.pencolor(249, 249, 121)
            elif x == 19:
                t2.pencolor(255, 145, 0)
            else:
                t2.pencolor(255, 193, 69)
            t2.write("WORDGUESSER!", move=False, align="center", font=("Arial", font_size, "bold"))
            time.sleep(0.1)
            font_size += 3
        t2.penup()
        t2.goto(0, 30)
        t2.write("\n" + " WELCOME TO ".center(44, "~") + "\n\n", move=False, align="center",
                     font=("Courier New", 20, "normal"))
        t2.pendown()
        time.sleep(4)
        t2.clear()

    def turtle_text(self, string):
        t2.pencolor(38, 70, 83)
        t2.penup()
        t2.goto(80, -300)
        t2.clear()
        t2.write(string, move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(0.5)

    def turtle_focused_text(self, string):
        t2.pencolor(38, 70, 83)
        t.clear()
        t1.clear()
        t2.penup()
        t2.goto(0, 0)
        t2.clear()
        t2.write(string, move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(3)

    def turtle_win(self, word):  # FIXME help
        t2.pencolor(38, 70, 83)
        t2.clear()
        t.clear()
        t2.penup()
        t2.goto(0, 0)
        t2.write("Well done, you win!", move=False, align="center", font=("Courier New", 20, "bold"))
        t2.write(f"The word was '{word}'", move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(3)

    def turtle_lose(self, word):
        t2.pencolor(38, 70, 83)
        t2.clear()
        t.clear()
        t2.penup()
        t2.goto(0, 0)
        t2.pencolor()
        t2.write("You ran out of attempts", move=False, align="center",
                font=("Courier New", 25, "bold"))
        t2.write(f"The word was: '{word}'. \n", move=False, align="center", font=("Courier New", 25, "bold"))
        time.sleep(3)

    def already_guessed(self, letter):
        t2.pencolor(38, 70, 83)
        t2.ht()
        t2.penup()
        t2.goto(200, -250)
        t2.clear()
        t2.write(f'\nYou have already guessed the letter "{letter}"! Try again.', move=False, align="center",
                 font=("arial", 18, "normal"))
        time.sleep(1)

Donatello = TurtleDrawing()


    # # for more difficulty:
    # def draw_legs(self):
    #     t.draw_leg1()
    #     t.draw_leg2()
    #     t.draw_leg3()
    #     t.draw_leg4()

    # def draw_back(self):
    #     t.draw_back_middle()
    #     t.draw_back_line()


# Donatello_ = t.Turtle(visible=False)
# Donatello_speed = t.speed(5000)
# Donatello_pensize = t.pensize(8)
# Donatello_penup = t.penup()
# Donatello_goto = t.goto(0, -150)
# Donatello_pendown = t.pendown()
# Donatello_ht = t.ht()

# Donatello = TurtleDrawing()

# Donatello.draw_body()
# Donatello.draw_head()
# Donatello.draw_leg1()
# Donatello.draw_leg2()
# Donatello.draw_leg3()
# Donatello.draw_leg4()
# Donatello.draw_tail()
# Donatello.draw_back_middle()
# Donatello.draw_back_line()
# Donatello.draw_eyes()

# t.mainloop()

# # # # t.done()
# t.Screen().exitonclick()
