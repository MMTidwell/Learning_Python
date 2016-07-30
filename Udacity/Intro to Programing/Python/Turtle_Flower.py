import turtle


def draw_flower(drawling):
    for i in range(1, 5):
        drawling.forward(80)
        drawling.right(90)


def draw():
    window = turtle.Screen()
    window.bgcolor('light blue')

    flower = turtle.Turtle()
    flower.color('dark blue')
    flower.speed(0)
    flower.shape('circle')

    count = 0
    while count < 36:
        draw_flower(flower)
        flower.right(10)
        count += 1
    flower.home()
    flower.right(90)
    flower.forward(300)

    window.exitonclick()


draw()