## Iteration 3

Before my next step,

```python
import turtle
import random
import time


## BlackJack UI
cardsInSuit = 13

suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
cards = []

window = turtle.Screen()
window.title("BlackJack")
window.setup(width = 1200, height = 800)
window.tracer(0)
# Max Height: 1000
# Max Width: 1750

window.bgpic("BlackJack.gif")



## Function to deploy cards onto screen
def addingCards(fileName):
        ae = turtle.Turtle()
        ae.shape(fileName)

        window.listen()
        ae.ondrag(ae.goto)
        ae.pu()
        ae.goto(0, 0)

        window.update()


## Add all card images to the turtle database
for suit in suits:
    
    for n in range(1, cardsInSuit + 1):
        cardName = suit + str(n)
        fileName = cardName + ".gif"

        window.addshape(fileName)
        cards.append(fileName)




## Squares Grey Background
falseSquare = turtle.Turtle()
falseSquare.speed(10)
falseSquare.shape("square")
falseSquare.color("light grey")
falseSquare.shapesize(stretch_wid = 10, stretch_len = 20)
falseSquare.penup()
falseSquare.goto(-500, 300)


## Red square
falseSquare = turtle.Turtle()
falseSquare.speed(10)
falseSquare.shape("square")
falseSquare.color("red")
falseSquare.shapesize(stretch_wid = 5, stretch_len = 5)
falseSquare.penup()
falseSquare.goto(-500, 300)

## Generate card function
def generateCard(x, y):
    window.addshape('Back of Card.gif')
    ae=turtle.Turtle()
    ae.shape('Back of Card.gif')

    ae.ondrag(ae.goto)
    ae.pu()
    ae.goto(200, 0)

## Call function
window.listen()
falseSquare.onclick(generateCard)




## Green square
trueSquare = turtle.Turtle()
trueSquare.speed(10)
trueSquare.shape("square")
trueSquare.color("green")
trueSquare.shapesize(stretch_wid = 5, stretch_len = 5)
trueSquare.penup()
trueSquare.goto(-400, 300)

## Other function
def generateRandomCard(x, y):
    fileName = random.choice(cards)
    print(fileName)
    addingCards(fileName)

## Call function
window.listen()
trueSquare.onclick(generateRandomCard)


while True:
    window.update()
```

![image](https://user-images.githubusercontent.com/90699946/151679288-b5a8306f-7606-4822-960d-01a1df2d7007.png)
