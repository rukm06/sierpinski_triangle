import turtle

def draw_triangle(tur,length):
    for i in range(3):
        tur.forward(length)
        tur.left(120)

def draw_sierpinski_triangle(tur,length,level):
    if level == 0:
        draw_triangle(tur,length)
    else:
        draw_sierpinski_triangle(tur,length/2,level-1)
        tur.forward(length)
        tur.left(120)
        draw_sierpinski_triangle(tur,length/2,level-1)
        tur.forward(length)
        tur.left(120)
        draw_sierpinski_triangle(tur,length/2,level-1)
        tur.forward(length)
        tur.left(120)

window = turtle.Screen()
window.bgcolor("red")
tur = turtle.Turtle()
tur.shape("turtle")
tur.color("yellow","green")
length = 300
level = 4
draw_sierpinski_triangle(tur,length,level)
window.exitonclick()
