## Iteration 4

To start off with, I wanted to change IDEs from Python IDLE to Visual Studio 2019, in order to access more features to help me. During this, I needed to do some folder admin and hardcoding directories into my code.

Changed over to visual studio

Added some code to prevent the same card from spawning twice, and also to stop the program crashing whenever the cards ran out

![image](https://user-images.githubusercontent.com/90699946/155420666-74fc249c-8343-442f-8453-43b464198e06.png)

![image](https://user-images.githubusercontent.com/90699946/155622477-ec494a99-2cbf-4a49-bbcd-c3920ef6afdd.png)

```python

import turtle
import random
import time


## BlackJack UI
window = turtle.Screen()
window.title("BlackJack")
window.setup(width = 800, height = 800)
window.tracer(0)
# Max Height: 1000
# Max Width: 1750

cardsDir = "Images/"
window.bgpic(cardsDir + "Background.gif")


# Setting up lists
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
cards = []
cardsValue = []




# Function to find the value of each card
def valueOfCard(fileName):
    value = int(fileName.strip("Images/Spades Hearts Clubs Diamonds.gif"))

    if value > 9:
        value = 10

    cardsValue.append(value)


## Function to deploy cards onto screen
def addingCards(fileName):
    card = turtle.Turtle()
    card.shape(fileName)

    window.listen()
    card.ondrag(card.goto)
    card.pu()

    window.update()



## Add all card images to the turtle database
for suit in suits:
    
    for a in range(1, 14):
        cardName = suit + str(a)
        fileName = cardsDir + cardName + ".gif"

        valueOfCard(fileName)

        window.addshape(fileName)
        cards.append(fileName)



## Red circle
def redCircle():
    redCircle.falseSquare = turtle.Turtle()
    redCircle.falseSquare.speed(10)
    redCircle.falseSquare.shape("circle")
    redCircle.falseSquare.color("red")
    redCircle.falseSquare.shapesize(stretch_wid = 5, stretch_len = 5)
    redCircle.falseSquare.penup()
    redCircle.falseSquare.goto(-300, 0)


## Generate card function
def generateCard(x, y):
    window.addshape(cardsDir + 'Back of Card.gif')
    ae = turtle.Turtle()
    ae.shape(cardsDir + 'Back of Card.gif')

    ae.ondrag(ae.goto)
    ae.pu()
    ae.goto(200, 0)

        

## Yellow circle
def yellowCircle():
    yellowCircle.trueSquare = turtle.Turtle()
    yellowCircle.trueSquare.speed(10)
    yellowCircle.trueSquare.shape("circle")
    yellowCircle.trueSquare.color("yellow")
    yellowCircle.trueSquare.shapesize(stretch_wid = 5, stretch_len = 5)
    yellowCircle.trueSquare.penup()
    yellowCircle.trueSquare.goto(300, 0)


## Random card function
def generateRandomCardOnClick(x, y):
    generateRandomCard()

def generateRandomCard():

    if len(cards) == 0:
            print("Out of Cards!")

    else:
        randomNumber = random.randint(0, len(cards)-1)
        fileName = cards[randomNumber]

        print(fileName)
        addingCards(fileName)
        #cards.remove(fileName)

        value = cardsValue[randomNumber]
        print(value)
        #cardsValue.remove(cardsValue[randomNumber])



## Call function
window.listen()
redCircle()
redCircle.falseSquare.onclick(generateCard)

## Call function
window.listen()

yellowCircle()
yellowCircle.trueSquare.onclick(generateRandomCardOnClick)

print(cardsValue)
print(cards)




while True:
    window.update()
```
