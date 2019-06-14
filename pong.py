import turtle

#set up the screen
win = turtle.Screen()
win.title("pong game")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

#paddle A
paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('red')
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b

#ball


#main game loop
while True:
    win.update()