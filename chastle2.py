import turtle

def draw_rectangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_battlements(t, x, y, width, height, count, color):
    bw = width / (count * 2 - 1)
    for i in range(count):
        bx = x + i * 2 * bw
        draw_rectangle(t, bx, y, bw, height, color)

def draw_triangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x + width / 2, y + height)
    t.goto(x + width, y)
    t.goto(x, y)
    t.end_fill()

def main():
    screen = turtle.Screen()
    screen.title("GOA Castle")
    screen.bgcolor("skyblue")
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    draw_rectangle(t, -400, -250, 800, 100, "forestgreen")
    
    castle_color = "#8b8c89"
    dark_gray = "#696a66"
    
    draw_rectangle(t, -150, -150, 300, 200, castle_color)
    draw_battlements(t, -150, 50, 300, 30, 6, castle_color)
    
    draw_rectangle(t, -220, -150, 70, 280, dark_gray)
    draw_battlements(t, -230, 130, 90, 25, 3, dark_gray)
    
    draw_rectangle(t, 150, -150, 70, 280, dark_gray)
    draw_battlements(t, 140, 130, 90, 25, 3, dark_gray)
    
    draw_rectangle(t, -60, 50, 120, 120, castle_color)
    draw_triangle(t, -75, 170, 150, 100, "firebrick")
    
    draw_rectangle(t, -40, -150, 80, 100, "saddlebrown")
    t.penup()
    t.goto(40, -50)
    t.setheading(90)
    t.pendown()
    t.fillcolor("saddlebrown")
    t.begin_fill()
    t.circle(40, 180)
    t.end_fill()
    t.setheading(0)
    
    draw_rectangle(t, -195, 20, 20, 40, "lightblue")
    draw_rectangle(t, 175, 20, 20, 40, "lightblue")
    draw_rectangle(t, -120, -30, 30, 50, "lightblue")
    draw_rectangle(t, 90, -30, 30, 50, "lightblue")
    draw_rectangle(t, -20, 90, 40, 50, "lightblue")
    
    t.penup()
    t.goto(0, 180)  
    t.color("gold")
    t.write("GOA", align="center", font=("Arial", 28, "bold"))
    
    t.goto(0, -90)
    t.color("black")
    t.write("GOA", align="center", font=("Arial", 16, "bold"))

    turtle.done()

if __name__ == "__main__":
    main()
