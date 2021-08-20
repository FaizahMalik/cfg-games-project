from turtle import Turtle, Screen
import time


class TurtleWindow:
    def __init__(self):
        self.s = Screen()
        self.s.setup(width=0.9, height=0.9)
        self.s.colormode(255)
        self.s.bgcolor(157, 238, 238)
        self.s.title("Hangman? Pfffffft never heard of it")
        [self.t, self.t1, self.t2] = [Turtle(), Turtle(), Turtle()]
        self.t.reset()
        self.t.ht()  # t is turtle drawing
        self.t1.ht()  # t1 is for big messages that clear the screen
        self.t2.ht()  # t2 is for small side notes in the corner of the screen
        self.t.speed(10)
        self.t.pensize(8)
        self.t.penup()
        self.t.goto(0, -150)
        self.t.pendown()
        self.t.pencolor('dark green')

    def draw_word(self, word):
        """Draws the hidden word in the turtle window"""
        self.t1.pencolor(45, 83, 98)
        self.t1.clear()
        self.t1.speed(5)
        self.t1.pensize(4)
        self.t1.penup()
        self.t1.goto(-350, -250)
        self.t1.pendown()
        self.t1.write(word, move=False, align="center", font=("arial", 25, "normal"))
        return True

    def welcome_screen(self):
        """Shows the welcome screen which says "welcome to" and the WordGuesser logo below"""
        self.t.clear()
        self.t1.clear()
        self.t2.clear()
        font_size = 20
        for x in range(20):
            if x % 2 == 0:
                self.t2.pencolor(255, 232, 120)
            elif x == 19:
                self.t2.pencolor(255, 149, 107)
            else:
                self.t2.pencolor(255, 177, 113)
            self.t2.write("WORDGUESSER!", move=False, align="center", font=("Arial", font_size, "bold"))
            time.sleep(0.1)
            font_size += 3
        self.t2.penup()
        self.t2.goto(0, 100)
        self.t2.write("\n" + " W E L C O M E   T O ".center(44, "~") + "\n\n", move=False, align="center",
                      font=("Courier New", 20, "normal"))
        self.t2.pendown()
        time.sleep(3)
        self.t2.clear()
        return True

    def goodbye_screen(self):
        """Clears screen and thanks the user for playing"""
        self.s.clear()
        self.s.colormode(255)
        self.s.bgcolor(157, 238, 238)
        time.sleep(1)
        self.t2.write("\n" + " THANKS FOR PLAYING! ".center(44, "~"), move=False, align="center",
                      font=("Courier New", 25, "normal"))
        time.sleep(2)
        return True

    def turtle_text(self, string):
        """Function for adding small text on the bottom right of the screen without clearing anything else"""
        self.t2.pencolor(45, 83, 98)
        self.t2.penup()
        self.t2.goto(200, -250)
        self.t2.clear()
        self.t2.write(string, move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(0.5)
        return True

    def turtle_focused_text(self, string):
        """Used to add large text in the middle of the screen, clears the screen before and after message"""
        self.t2.pencolor(45, 83, 98)
        self.t.clear()
        self.t1.clear()
        self.t2.penup()
        self.t2.goto(0, 0)
        self.t2.clear()
        self.t2.write(string, move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(3)
        self.t2.clear()
        return True

    # draw body
    def draw_body(self):
        self.t.reset()
        self.t.ht()
        self.t.pensize(8)
        self.t.penup()
        self.t.goto(0, -150)
        self.t.pendown()
        self.t.pencolor('dark green')
        self.t.fillcolor('forest green')
        self.t.begin_fill()
        r = 150
        self.t.circle(r)
        self.t.end_fill()
        return True

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
        return True

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
        return True

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
        return True

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
        return True

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
        return True

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
        return True

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
        return True

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
        return True

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
        return True

    def clear_window(self):
        """Clears and resets entire turtle window - used for testing purposes"""
        self.t.clear()
        self.t1.clear()
        self.t2.clear()
        self.t.reset()
        self.t1.reset()
        self.t2.reset()


Donatello = TurtleWindow()
