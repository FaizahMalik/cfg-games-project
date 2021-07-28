import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(8)
t.penup()
t.goto(0,-150)
t.pendown()
t.ht()


# draw circle body
def draw_body():
    r = 150
    t.circle(r)

# draw head
def draw_head():
    t.penup()
    t.goto(-40, 150)
    t.pendown()
    t.left(90)
    t.forward(30)
    for i in range(45):
        t.forward(3)
        t.right(4)
    t.forward(35)

# draw leg 1
def draw_leg1():
    t.penup()
    t.goto(-85, 125)
    t.pendown()
    t.right(135)
    t.forward(10)
    for i in range(45):
        t.forward(2)
        t.left(4)
    t.forward(10)

# draw leg 2
def draw_leg2():
    t.penup()
    t.goto(85, 125)
    t.pendown()
    t.left(90)
    t.forward(10)
    for i in range(45):
        t.forward(2)
        t.right(4)
    t.forward(10)

# draw leg 3
def draw_leg3():
    t.penup()
    t.goto(-85, -125)
    t.pendown()
    t.forward(10)
    for i in range(45):
        t.forward(2)
        t.right(4)
    t.forward(10)

# draw leg 4
def draw_leg4():
    t.penup()
    t.goto(85, -125)
    t.pendown()
    t.right(90)
    t.forward(10)
    for i in range(45):
        t.forward(2)
        t.left(4)
    t.forward(10)

# draw tail
def draw_tail():
    t.penup()
    t.goto(-15, -150)
    t.pendown()
    t.right(180)
    t.forward(30)
    t.left(90)
    t.forward(30)

# draw back
def draw_back_middle():
    t.penup()
    t.goto(-34, -60)
    t.pendown()
    t.right(45)
    for i in range(6):
        t.forward(75)
        t.right(300)

# draw back pattern
def draw_back_line():
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

# draw eyes
def draw_eyes():
    t.penup()
    t.goto(-10, 185)
    t.pendown()
    t.circle(3)
    t.penup()
    t.goto(13, 185)
    t.pendown()
    t.circle(3)

# # for more difficulty:
# def draw_legs():
#     draw_leg1()
#     draw_leg2()
#     draw_leg3()
#     draw_leg4()

# def draw_back():
#     draw_back_middle()
#     draw_back_line()

draw_body()
draw_head()
draw_leg1()
draw_leg2()
draw_leg3()
draw_leg4()
draw_tail()
draw_back_middle()
draw_back_line()
draw_eyes()


turtle.mainloop()

