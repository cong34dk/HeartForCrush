from tkinter.ttk import Style
import turtle

#tạo đề mục
t=turtle.Turtle()
turtle.title("Heart for crush")
screen=turtle.Screen()
screen.bgcolor("Pink")
#Import text
Style=('Courier',30,'italic')
turtle.write('Công         Lover',font=Style,align='center')
# Vẽ trái tim
t.pensize(10)
t.color("red")
t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)
t.end_fill()
t.pensize(10)
#Tắt chương trình khi click ra ngoài
t.screen.exitonclick()