# BlackJack Python Project

## [Iteration 1](https://github.com/JMorr4/Computer-Science/blob/main/Contents/BlackJack%20Project/Iteration%201.md)

## Iteration 2

So I'd managed to code how to add images onto the screen, and I had all these necessary images, the next step was to just code them all into my program. Easier said than done. Or rather, it's harder to find a truly efficient way to do it. Although I'm awful at coding, it still seemed so stupid to me that I would have to waste almost 60 lines on code that would just add 60 images to the python dictionary. So I came up with this code:

```python
import turtle
import random

cardsInSuit = 13

suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')

window = turtle.Screen()
window.title("BlackJack")
window.setup(width = 800, height = 800)
window.tracer(0)
# Max Height: 1000
# Max Width: 1750

window.bgpic("BlackJack.gif")


for suit in suits:
    
    for n in range(1, cardsInSuit + 1):
        card = suit + str(n)

        fileName = card + ".gif"
        window.addshape(fileName)
        
        ae = turtle.Turtle()
        ae.shape(fileName)

        window.listen()
        ae.ondrag(ae.goto)
        ae.pu()
        ae.goto(250,-250)

        window.update()

while True:
    window.update()
```

<br>

This took me way too long, but I'd managed to code what I'd wanted efficiently. However, the hardest task I underwent was having to rename all 52 card images just for this to work. Anyway, here's the output:

<br>

![image](https://user-images.githubusercontent.com/90699946/151679246-09be05ea-e304-417d-a685-2174dd646a39.png)



<br>



## Iteration 3

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
