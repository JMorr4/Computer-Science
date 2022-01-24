```python
from turtle import *
import turtle

screen = turtle.Screen()
 
def draw(radius):
    for i in range(2):
        turtle.circle(radius, 90)
        turtle.circle(radius/2, 90)

screen.setup(500,500)

screen.bgcolor("black")

colours =["violet", "blue", "green", "yellow", "orange", "red"]
 
angle = 10
ind = 0

turtle.speed(100)

for i in range(36):
    
    turtle.seth(-angle)
    turtle.color(colours[ind])
     
    if ind == 5:
        ind = 0
    else:
        ind += 1
     
    draw(80)
    
    angle += 10
 
turtle.hideturtle()
turtle.done()
```
