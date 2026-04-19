import turtle
import random

def draw_rectangle(t, x, y, width, height, color, border=None):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    if border:
        t.pencolor(border)
    else:
        t.pencolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.pencolor("black") 

def draw_triangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.pencolor("black")
    t.begin_fill()
    t.goto(x + width / 2, y + height)
    t.goto(x + width, y)
    t.goto(x, y)
    t.end_fill()

def draw_battlements(t, x, y, width, height, count, color):
    bw = width / (count * 2 - 1)
    for i in range(count):
        bx = x + i * 2 * bw
        draw_rectangle(t, bx, y, bw, height, color, "black")

def draw_window(t, x, y, width, height):
    draw_rectangle(t, x, y, width, height, "#FFD700", "black")
    t.penup()
    t.goto(x + width/2, y)
    t.pendown()
    t.pencolor("black")
    t.pensize(2)
    t.goto(x + width/2, y + height)
    t.penup()
    t.goto(x, y + height/2)
    t.pendown()
    t.goto(x + width, y + height/2)
    t.pensize(1)

def draw_star(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.color("white")
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_flag(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pencolor("black")
    t.pensize(2)
    t.pendown()
    t.goto(x, y + 40)
    t.pensize(1)
    t.fillcolor("#DC143C")
    t.begin_fill()
    t.goto(x + 30, y + 30)
    t.goto(x, y + 15)
    t.end_fill()

def draw_tree(t, x, y):
    draw_rectangle(t, x - 10, y, 20, 40, "#4A2E1B", "black")
    t.penup()
    t.goto(x, y + 30)
    t.fillcolor("#1C5D2A")
    t.pencolor("black")
    t.pendown()
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def main():
    screen = turtle.Screen()
    screen.title("Beautiful GOA Castle")
    screen.bgcolor("#0B132B")  
    screen.setup(width=900, height=700)
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    t.penup()
    t.goto(-350, 220)
    t.color("#FFFACD")
    t.begin_fill()
    t.circle(45)
    t.end_fill()
    
    for _ in range(40):
        sx = random.randint(-450, 450)
        sy = random.randint(50, 350)
        ssize = random.randint(3, 8)
        draw_star(t, sx, sy, ssize)
    
    draw_rectangle(t, -450, -350, 900, 150, "#194A22")
    
    draw_rectangle(t, -450, -250, 900, 50, "#1C5D99")   
    t.pencolor("#3581D8")
    t.pensize(2)
    for i in range(3):
        t.penup()
        t.goto(-400, -210 - (i*12))
        t.pendown()
        t.forward(800)
    t.pensize(1)
    
    draw_tree(t, -350, -200)
    draw_tree(t, -400, -180)
    draw_tree(t, 350, -170)
    draw_tree(t, 410, -200)
    
    castle_color = "#6E6E6E"
    light_gray   = "#848484"
    dark_gray    = "#4C4C4C"
    
    draw_rectangle(t, -180, -200, 360, 220, castle_color, "black")
    draw_battlements(t, -180, 20, 360, 25, 8, castle_color)
    
    draw_rectangle(t, -260, -200, 70, 270, light_gray, "black")
    draw_battlements(t, -270, 70, 90, 20, 4, light_gray)
    draw_window(t, -235, -50, 20, 40)
    draw_window(t, -235, 15, 20, 40)
    draw_flag(t, -225, 90)
    
    draw_rectangle(t, 190, -200, 70, 270, light_gray, "black")
    draw_battlements(t, 180, 70, 90, 20, 4, light_gray)
    draw_window(t, 215, -50, 20, 40)
    draw_window(t, 215, 15, 20, 40)
    draw_flag(t, 225, 90)

    draw_rectangle(t, -120, -200, 60, 320, dark_gray, "black")
    draw_triangle(t, -135, 120, 90, 80, "#4A0000")
    draw_window(t, -100, 35, 20, 40)
    draw_flag(t, -90, 200)

    draw_rectangle(t, 60, -200, 60, 320, dark_gray, "black")
    draw_triangle(t, 45, 120, 90, 80, "#4A0000")
    draw_window(t, 80, 35, 20, 40)
    draw_flag(t, 90, 200)

    draw_rectangle(t, -50, -200, 100, 390, castle_color, "black")
    draw_triangle(t, -65, 190, 130, 100, "#6A040F")  
    draw_window(t, -15, 60, 30, 45)
    draw_window(t, -15, 125, 30, 45)
    draw_flag(t, 0, 290)
    
    draw_rectangle(t, -65, -260, 130, 60, "#483C32", "black") 
    t.pencolor("silver")
    t.pensize(2)
    t.penup(); t.goto(-65, -260); t.pendown(); t.goto(-65, -120)
    t.penup(); t.goto(65, -260); t.pendown(); t.goto(65, -120)
    t.pensize(1)
    
    draw_rectangle(t, -40, -200, 80, 90, "#1F1209", "black")

    t.penup()
    t.goto(40, -110)
    t.setheading(90)
    t.pendown()
    t.fillcolor("#1F1209")
    t.pencolor("black")
    t.begin_fill()
    t.circle(40, 180)
    t.end_fill()
    t.setheading(0)
    
    t.penup()
    t.goto(-80, -20)
    t.pendown()
    t.fillcolor("#FFD700") 
    t.pencolor("black")
    t.begin_fill()
    for _ in range(2):
        t.forward(160)
        t.left(90)
        t.forward(45)
        t.left(90)
    t.end_fill()
    
    t.penup()
    t.goto(0, -15)
    t.color("#8B0000")
    t.write("GOA", align="center", font=("Verdana", 28, "bold"))
    
    t.goto(0, 280)
    t.color("gold")

    t.write("GOA KINGDOM", align="center", font=("Courier", 36, "bold"))

    turtle.done()

if __name__ == "__main__":
    main()
