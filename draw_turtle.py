from turtle import Turtle, Screen
import time

t = Turtle()
t1 = Turtle()
s = Screen()

# TODO turtle window goes unresponsive in between drawings, we could find a fix for that?
# TODO make class an iterator

class TurtleDrawing:
    def __init__(self):
        t.speed(10)
        t.pensize(8)
        t.penup()
        t.goto(0, -150)
        t.pendown()
        t.ht()
        s.setup(500, 600)

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
        t1.clear()
        t1.speed(5)
        t1.pensize(4)
        t1.penup()
        t1.goto(-290, -250)
        t1.pendown()
        t1.ht()
        t1.write(word, move=False, align="Left", font=("arial", 25, "normal"))

    def correct_word(self, word):
        t.clear()
        t.penup()
        t.goto(-100, 0)
        t.write(f"Well done, you win! \n", move=False, align="center", font=("arial", 25, "bold"))
        t.write(f"The word was '{word}'", move=False, align="center", font=("arial", 25, "bold"))
        time.sleep(3)

    def game_lost(self, word):
        t.clear()
        t.penup()
        t.goto(-100, 0)
        t.pencolor('black')
        t.write(f"\nWrong guess!\n\nYou ran out of attempts", move=False, align="center",
                font=("arial", 25, "normal"))
        t.write(f"The word was: '{word}'. \n", move=False, align="center", font=("arial", 25, "bold"))
        time.sleep(3)


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
