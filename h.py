import turtle

def draw_square(some_turtle):
	count = 0
	while(count<=3):
		some_turtle.forward(100)
		some_turtle.right(90)
		count += 1

def draw_art() :
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)

	window.exitonclick()
	
draw_art()
