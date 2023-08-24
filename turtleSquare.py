import turtle
turtle.title("Square in turtle ")
# turtle.bgcolor("skyblue" )
# turtle.shape("turtle")
# turtle.color("red","blue")
# turtle.circle(30)
# turtle.shape("circle")
# turtle.circle(60)
# turtle.shape("arrow")
# turtle.circle(90)
turtle.color("red","blue")  #color of turtleshape and the line 
turtle.speed(3)             # speed of turtle 
turtle.begin_fill()         #start of the color fill property
turtle.fillcolor("red")     #fill the Red color into the square 
 
turtle.bgcolor("skyblue")
turtle.shape("turtle")
turtle.forward(100)
turtle.right(90) 
turtle.bgcolor("pink")

turtle.shape("circle")
turtle.forward(100)
turtle.right(90)
turtle.bgcolor("yellow")

 
turtle.shape("arrow")
turtle.forward(100)
turtle.right(90)
turtle.bgcolor("green")
 

turtle.shape("classic")
turtle.forward(100)
turtle.right(90)
turtle.hideturtle()

turtle.end_fill()  #end of the color fill  property 
 
 
 

turtle.mainloop()
