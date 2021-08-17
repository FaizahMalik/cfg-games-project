from turtle import Turtle, Screen
import time

# t = Turtle()
# t1 = Turtle()
# t2 = Turtle()
# t3 = Turtle()


# TODO make class an iterator?!?!?!?!

class TurtleWindow:
    def __init__(self):
        self.s = Screen()
        self.s.setup(width=1.0, height=1.0)
        self.s.title("Hangman? Pfffffft never heard of it")
        [self.t, self.t1, self.t2, self.t3] = [Turtle(), Turtle(), Turtle(), Turtle()]
        self.t.reset()
        self.t.ht()  # t is turtle drawing
        self.t1.ht()  # t1 is for big messages that clear the screen
        self.t2.ht()  # t2 is for small side notes in the corner of the screen
        self.t3.ht()
        self.t.speed(10)
        self.t.pensize(8)
        self.t.penup()
        self.t.goto(0, -150)
        self.t.pendown()
        self.t.pencolor('dark green')

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
        self.t.penup()
        self.t.goto(0, -150)
        self.t.pendown()
        self.t.pencolor('dark green')
        self.t.fillcolor('forest green')
        self.t.begin_fill()
        r = 150
        self.t.circle(r)
        self.t.end_fill()

    # draw head
    def draw_head(self):
        self.t.pensize(4)
        self.t.penup()
        self.t.goto(-40, 150)
        self.t.pendown()
        self.t.pencolor('olive drab')
        self.t.fillcolor('olive drab')
        self.t.begin_fill()
        self.t.left(90)
        self.t.forward(30)
        for i in range(45):
            self.t.forward(3)
            self.t.right(4)
        self.t.forward(35)
        self.t.end_fill()

    # draw leg 1
    def draw_leg1(self):
        self.t.penup()
        self.t.goto(-85, 125)
        self.t.pendown()
        self.t.pencolor('olive drab')
        self.t.fillcolor('olive drab')
        self.t.begin_fill()
        self.t.right(135)
        self.t.forward(10)
        for i in range(45):
            self.t.forward(2)
            self.t.left(4)
        self.t.forward(10)
        self.t.end_fill()
        # self.t.done()

    # draw leg 2
    def draw_leg2(self):
        self.t.penup()
        self.t.goto(85, 125)
        self.t.pendown()
        self.t.pencolor('olive drab')
        self.t.fillcolor('olive drab')
        self.t.begin_fill()
        self.t.left(90)
        self.t.forward(10)
        for i in range(45):
            self.t.forward(2)
            self.t.right(4)
        self.t.forward(10)
        self.t.end_fill()
        # self.t.done()

    # draw leg 3
    def draw_leg3(self):
        self.t.penup()
        self.t.goto(-85, -125)
        self.t.pendown()
        self.t.pencolor('olive drab')
        self.t.fillcolor('olive drab')
        self.t.begin_fill()
        self.t.forward(10)
        for i in range(45):
            self.t.forward(2)
            self.t.right(4)
        self.t.forward(10)
        self.t.end_fill()
        # self.t.done()

    # draw leg 4
    def draw_leg4(self):
        self.t.penup()
        self.t.goto(85, -125)
        self.t.pendown()
        self.t.pencolor('olive drab')
        self.t.fillcolor('olive drab')
        self.t.begin_fill()
        self.t.right(90)
        self.t.forward(10)
        for i in range(45):
            self.t.forward(2)
            self.t.left(4)
        self.t.forward(10)
        self.t.end_fill()
        # # self.t.done()

    # draw tail
    def draw_tail(self):
        self.t.penup()
        self.t.goto(-15, -150)
        self.t.pendown()
        self.t.pencolor('olive drab')
        self.t.fillcolor('olive drab')
        self.t.begin_fill()
        self.t.right(180)
        self.t.forward(30)
        self.t.left(90)
        self.t.forward(30)
        self.t.end_fill()
        # # self.t.done()

    # draw back
    def draw_back_middle(self):
        self.t.pensize(10)
        self.t.penup()
        self.t.goto(-34, -60)
        self.t.pendown()
        self.t.pencolor('dark green')
        self.t.right(45)
        for i in range(6):
            self.t.forward(75)
            self.t.right(300)


    # draw back pattern
    def draw_back_line(self):
        self.t.pencolor('dark green')
        self.t.right(120)
        self.t.forward(78)
        self.t.penup()
        self.t.goto(41, -60)
        self.t.pendown()
        self.t.left(60)
        self.t.forward(78)
        self.t.penup()
        self.t.goto(75, 5)
        self.t.pendown()
        self.t.left(60)
        self.t.forward(75)
        self.t.penup()
        self.t.goto(42, 70)
        self.t.pendown()
        self.t.left(60)
        self.t.forward(68)
        self.t.penup()
        self.t.goto(-35, 70)
        self.t.pendown()
        self.t.left(60)
        self.t.forward(68)
        self.t.penup()
        self.t.goto(-70, 5)
        self.t.pendown()
        self.t.left(60)
        self.t.forward(72)


    # draw eyes
    def draw_eyes(self):
        self.t.penup()
        self.t.goto(-10, 185)
        self.t.pendown()
        self.t.circle(3)
        self.t.penup()
        self.t.goto(13, 185)
        self.t.pendown()
        self.t.circle(3)


    def draw_word(self, word):
        self.t1.pencolor(38, 70, 83)
        self.t1.clear()
        self.t1.speed(5)
        self.t1.pensize(4)
        self.t1.penup()
        self.t1.goto(-390, -250)
        self.t1.pendown()
        self.t1.write(word, move=False, align="Left", font=("arial", 25, "normal"))

    def welcome_screen(self):
        font_size = 1
        for x in range(20):
            if x % 2 == 0:
                self.t2.pencolor(249, 249, 121)
            elif x == 19:
                self.t2.pencolor(255, 145, 0)
            else:
                self.t2.pencolor(255, 193, 69)
            self.t2.write("WORDGUESSER!", move=False, align="center", font=("Arial", font_size, "bold"))
            time.sleep(0.1)
            font_size += 3
        self.t2.penup()
        self.t2.goto(0, 30)
        self.t2.write("\n" + " WELCOME TO ".center(44, "~") + "\n\n", move=False, align="center",
                     font=("Courier New", 20, "normal"))
        self.t2.pendown()
        time.sleep(4)
        self.t2.clear()

    def turtle_text(self, string):
        self.t2.pencolor(38, 70, 83)
        self.t2.penup()
        self.t2.goto(200, -250)
        self.t2.clear()
        self.t2.write(string, move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(0.5)

    def turtle_focused_text(self, string):
        self.t2.pencolor(38, 70, 83)
        self.t.clear()
        self.t1.clear()
        self.t3.clear()
        self.t2.penup()
        self.t2.goto(0, 0)
        self.t2.clear()
        self.t2.write(string, move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(3)

    # def attempts_left(self, num):
    #     self.t3.pencolor(38, 70, 83)
    #     self.t3.penup()
    #     self.t3.goto(200, 250)
    #     self.t3.clear()
    #     self.t3.write(f"Attempts remaining: {num}", move=False, align="center", font=("Courier New", 20, "bold"))
    #     time.sleep(0.5)

Donatello = TurtleDrawing()


    # def turtle_win(self, word):  # FIXME help
    #     self.t2.pencolor(38, 70, 83)
    #     self.t2.clear()
    #     self.t.clear()
    #     self.t2.penup()
    #     self.t2.goto(0, 0)
    #     self.t2.write("Well done, you win!", move=False, align="center", font=("Courier New", 20, "bold"))
    #     self.t2.write(f"The word was '{word}'", move=False, align="center", font=("Courier New", 20, "bold"))
    #     time.sleep(3)

    # def turtle_lose(self, word):
    #     self.t2.pencolor(38, 70, 83)
    #     self.t2.clear()
    #     self.t.clear()
    #     self.t2.penup()
    #     self.t2.goto(0, 0)
    #     self.t2.pencolor()
    #     self.t2.write("You ran out of attempts", move=False, align="center",
    #             font=("Courier New", 25, "bold"))
    #     self.t2.write(f"The word was: '{word}'. \n", move=False, align="center", font=("Courier New", 25, "bold"))
    #     time.sleep(3)

    # def already_guessed(self, letter):
    #     self.t2.pencolor(38, 70, 83)
    #     self.t2.ht()
    #     self.t2.penup()
    #     self.t2.goto(200, -250)
    #     self.t2.clear()
    #     self.t2.write(f'\nYou have already guessed the letter "{letter}"! Try again.', move=False, align="center",
    #              font=("arial", 18, "normal"))
    #     time.sleep(1)



    # # for more difficulty:
    # def draw_legs(self):
    #     self.t.draw_leg1()
    #     self.t.draw_leg2()
    #     self.t.draw_leg3()
    #     self.t.draw_leg4()

    # def draw_back(self):
    #     self.t.draw_back_middle()
    #     self.t.draw_back_line()


# Donatello_ = self.t.Turtle(visible=False)
# Donatello_speed = self.t.speed(5000)
# Donatello_pensize = self.t.pensize(8)
# Donatello_penup = self.t.penup()
# Donatello_goto = self.t.goto(0, -150)
# Donatello_pendown = self.t.pendown()
# Donatello_ht = self.t.ht()

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

# self.t.mainloop()

# # # # self.t.done()
# self.t.Screen().exitonclick()
