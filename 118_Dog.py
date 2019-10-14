# create turtle
import turtle as trtl

#set turtle name and speed
dog = trtl.Turtle()
dog.speed(50)

# create word art "d"
dog.pensize(2)
dog.color("chocolate4")
dog.fillcolor("chocolate4")
dog.begin_fill()
dog.left(90)
dog.forward(60)
dog.right(90)
dog.forward(20)
dog.right(90)
dog.forward(60)
dog.right(90)
dog.forward(20)
dog.end_fill()
dog.begin_fill()
dog.right(180)
dog.circle(20,360)
dog.end_fill()
dog.penup()

# create word art "o"
dog.goto(60,0)
dog.pensize(10)
dog.pendown()
dog.circle(20)

# create word art "g"
dog.pensize(10)
dog.penup()
dog.goto(120,0)
dog.pendown()
dog.circle(20)
dog.goto(140,0)
dog.right(90)
dog.circle(-20,140,30)
dog.penup()

# draw dog head
dog.goto(-160,-160)
dog.left(50)
dog.pensize(2)
dog.color("darkorange3")
dog.fillcolor("darkorange3")
dog.begin_fill()
dog.left(90)
dog.forward(60)
dog.right(90)
dog.forward(120)
dog.right(90)
dog.forward(60)
dog.right(90)
dog.forward(120)
dog.end_fill()
dog.penup()

# draw dog nose
dog.goto(-280,-160)
dog.pendown()
dog.pencolor("black")
dog.fillcolor("black")
dog.begin_fill()
dog.circle(10)
dog.end_fill()
dog.penup()

# draw dog ear
dog.goto(-180,-200)
dog.pencolor("black")
dog.pendown()
dog.circle(20,360,3)
dog.penup()

# draw dog eye
dog.goto(-240,-180)
dog.fillcolor("white")
dog.begin_fill()
dog.circle(8)
dog.end_fill()
dog.goto(-240,-175)
dog.fillcolor("gray2")
dog.begin_fill()
dog.circle(4)
dog.end_fill()

wn = trtl.Screen()
wn.mainloop()