## Iteration 4

To start off with, I wanted to change IDEs from Python IDLE to Visual Studio 2019, in order to access more features to help me. During this, I created a seperate folder for images instead of having all my files in the same folder. This meant I had to hardcode the directory into my code:

```python
cardsDir = "Images/"
window.bgpic(cardsDir + "Background.gif")
```

This also meant that every item in the array ```undealtCards``` was changed, making the list even more of an eyesore to look at than before.

```python
for suit in suits:
    
    for a in range(1, 14):
        cardName = suit + str(a)
        fileName = cardsDir + cardName + ".gif"

        window.addshape(fileName)
        undealtCards.append(fileName) 
```

After this, I just coded a lot of little changes to the code. First of, I added a way to prevent the same card being dealt twice:

```python
def generateRandomCardOnClick(x, y):
    generateRandomCard()

def generateRandomCard():

    if len(undealtCards) == 0:
            print("Out of Cards!")

    else:
        randomNumber = random.randint(0, len(undealtCards)-1)

        fileName = undealtCards[randomNumber]
        cardValue = calculateValue(fileName)

        print(fileName)
        print(cardValue)
        
        addingCards(fileName)
        undealtCards.remove(fileName)
```


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
undealtCards = []



# Function to find the value of each card
def calculateValue(fileName):
    value = int(fileName.strip("Images/Spades Hearts Clubs Diamonds.gif"))

    if value > 9:
        value = 10

    return value


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

        window.addshape(fileName)
        undealtCards.append(fileName)



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

    if len(undealtCards) == 0:
            print("Out of Cards!")

    else:
        randomNumber = random.randint(0, len(undealtCards)-1)

        fileName = undealtCards[randomNumber]
        cardValue = calculateValue(fileName)

        print(fileName)
        print(cardValue)
        
        addingCards(fileName)
        undealtCards.remove(fileName)



## Call function
window.listen()
redCircle()
redCircle.falseSquare.onclick(generateCard)

## Call function
window.listen()

yellowCircle()
yellowCircle.trueSquare.onclick(generateRandomCardOnClick)



while True:
    window.update()
```


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
undealtCards = []



# Function to find the value of each card
def calculateValue(fileName):
    value = int(fileName.strip("Images/Spades Hearts Clubs Diamonds.gif"))

    if value > 9:
        value = 10

    return value


## Function to deploy cards onto screen
def addingCards(fileName):
    card = turtle.Turtle()
    card.shape(fileName)

    window.listen()
    card.ondrag(card.goto)
    card.pu()

    window.update()

    return card


## Add all card images to the turtle database
for suit in suits:
    
    for a in range(1, 14):
        cardName = suit + str(a)
        fileName = cardsDir + cardName + ".gif"

        window.addshape(fileName)
        undealtCards.append(fileName)



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

    if len(undealtCards) == 0:
            print("Out of Cards!")

    else:
        randomNumber = random.randint(0, len(undealtCards)-1)

        fileName = undealtCards[randomNumber]
        cardValue = calculateValue(fileName)

        print(fileName)
        print(cardValue)
        
        addingCards(fileName)
        undealtCards.remove(fileName)



## Call function
window.listen()
redCircle()
redCircle.falseSquare.onclick(generateCard)

## Call function
window.listen()

yellowCircle()
yellowCircle.trueSquare.onclick(generateRandomCardOnClick)



## Player starting cards
for a in range(2):
    randomNumber = random.randint(0, len(undealtCards)-1)

    fileName = undealtCards[randomNumber]
    cardValue = calculateValue(fileName)

    print(fileName)
    print(cardValue)
        
    startingCard = addingCards(fileName)
    startingCard.goto(-100 + (a*30), -100)

    undealtCards.remove(fileName)


## Computer starting cards
for a in range(2):
    randomNumber = random.randint(0, len(undealtCards)-1)

    fileName = undealtCards[randomNumber]
    cardValue = calculateValue(fileName)

    print(fileName)
    print(cardValue)
        
    startingCard = addingCards(fileName)
    startingCard.goto(-100 + (a*30), 100)

    undealtCards.remove(fileName)



## Infinite loop
while True:
    window.update()
```
