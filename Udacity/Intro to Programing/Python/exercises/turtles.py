import turtle


# ------------------------------ORIGINAL-----------------------------------------------------
# def draw_square():
#     """ Window creates the screen and color, Brad makes the turtle and moves it) """
#     window = turtle.Screen()
#     window.bgcolor('blue')
#
#     count = 0
#     brad = turtle.Turtle()
#     brad.shape('turtle')
#     brad.color('yellow')
#     brad.speed(3)
#
#     # angie = turtle.Turtle()       # if angie is before the while loop then she will go first
#     # angie.shape('arrow')
#     # angie.color('green')
#     # angie.circle(100)
#
#     while count < 4:
#         brad.forward(100)   # draws line
#         brad.right(90)      # 90* angle
#         count += 1
#
#     window.exitonclick()
#
#     angie = turtle.Turtle()         # if angie is bellow the loop then she will go last
#     angie.shape('arrow')
#     angie.color('green')
#     angie.circle(100)
#
#
# draw_square()




# -----------------------------------------MY GUESS-------------------------------------------
# class Draw(object):
#     window = turtle.Screen()  # makes screen
#     window.bgcolor('dark blue')  # color of screen
#     turtle.Turtle()
#     window.exitonclick()  # closes screen
#
#     def __init__(self, name):
#         name.shape()
#         name.color()
#         name.speed()
#
#
# class Square(Draw):
#     brad = turtle.Turtle()
#     brad.shape('turtle')
#     brad.color('yellow')
#     brad.speed(3)
#
#     def draw_square(self, brad):
#         """ Window creates the screen and color, Brad makes the turtle and moves it) """
#         count = 0
#         while count < 4:
#             brad.forward(100)  # draws line
#             brad.right(90)  # 90* angle
#             count += 1
#
#     # angie = turtle.Turtle()       # if angie is before the while loop then she will go first
#     # angie.shape('arrow')
#     # angie.color('green')
#     # angie.circle(100)
#
#
# class Circle(Draw):
#     angie = turtle.Turtle()         # if angie is bellow the loop then she will go last
#     angie.shape('arrow')
#     angie.color('green')
#     angie.circle(100)
#
#
# class Triangle(Draw):
#     frank = turtle.Turtle()
#     frank.shape('triangle')
#     frank.color('blank')
#
#     def draw_triangle(self, frank):
#         count = 0
#         while count < 3:
#             frank.forward(100)
#             frank.right(30)
#             count += 1



# ----------------------------------------- THERE'S -------------------------------------------
# def draw_square(some_turtle):
#     for i in range(1, 5):
#         some_turtle.forward(100)
#         some_turtle.right(90)
#
#
# def draw_triangle(some_turtle):
#     for i in range(1,4):
#         some_turtle.forward(200)
#         some_turtle.left(120)
#
# def draw_art():
#     window = turtle.Screen()
#     window.bgcolor('black')
#
#     brad = turtle.Turtle()
#     brad.shape('turtle')
#     brad.color('yellow')
#     brad.speed(2)
#     brad.pensize(6)
#     draw_square(brad)
#
#     angie = turtle.Turtle()
#     angie.shape('arrow')
#     angie.color('blue')
#     angie.pensize(8)
#     angie.circle(100)
#
#     tom = turtle.Turtle()
#     tom.shape('circle')
#     tom.color('green')
#     draw_triangle(tom)
#
#     window.exitonclick()
#
# draw_art()



# ------------------------------------ WITH CLASSES---------------------------------------
def draw_square(some_turtle):
    # count = 0
    # while count < 36: #36
    #     for i in range(1, 5):
    #         some_turtle.forward(100)
    #         some_turtle.right(90)
    #         if i == 4:
    #             some_turtle.right(10)
    #             count += 1

    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(200)
        some_turtle.left(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('black')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(0)
    brad.pensize(2)
    for i in range(1, 37):  # runs 36 times
        draw_square(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(300)

    # angie = turtle.Turtle()
    # angie.shape('arrow')
    # angie.color('blue')
    # angie.pensize(25)
    # angie.circle(100)
    #
    # tom = turtle.Turtle()
    # tom.shape('circle')
    # tom.color('green')
    # draw_triangle(tom)

    window.exitonclick()

draw_art()