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

After this, I just coded a lot of little changes to the code. First of all, I added a way to prevent the same card being dealt twice, and I also made a new function called ```generateRandomCardOnClick()```, with its only purpose being to trash those annoying x and y parameters. This meant that I could, in the future, call the function ```generateRandomCard()``` and be able to pass in other parameters.

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

You may also notice the line: ```cardValue = calculateValue(fileName)```. This links back to a function I made to calculate the value of each card, following the rules of Blackjack, where all coloured cards (e.g. Jacks, Queens, Kings) have their values capped at 10. I have yet to make a rule for the ace card.

```python
def calculateValue(fileName):
    value = int(fileName.strip("Images/Spades Hearts Clubs Diamonds.gif"))

    if value > 9:
        value = 10

    return value
```

So far, there isn't actually any point to me calculating the value of each card, it's only feature in my code is outputted in the command prompt after the card has spawned:

![image](https://user-images.githubusercontent.com/90699946/155899099-7464ff4e-a4b2-4ec1-a614-3f49217a3b90.png)

<br>

Next, I switched up some aspects of the UI. I changed the square buttons to some trendy new circles, a red one and a yellow one. I deleted the grey square, mainly because I couldn't remember why I put it there in the first place. I changed the background, because I got bored of looking at the old one all the time, and I repositioned the buttons.

![image](https://user-images.githubusercontent.com/90699946/155899376-25116002-62a6-495a-8a41-fc62e4a3ce29.png)

The reason there are some random cards on the screen is because they are now the starting cards dealt to you at the beginning of the game. The ones on the top half of the screen belong to the computer, the ones on the bottom are yours. I spent a long time fiddling around with using ```goto()``` to try and move a string, such as "Images/Diamonds5.gif", but I couldn't find a way to fetch the card I wanted to position from an embedded function, still in it's correct form, so I had to just adapt the contents of the variables instead:

```python
## Player starting cards
for a in range(2):
    randomNumber = random.randint(0, len(undealtCards)-1)

    fileName = undealtCards[randomNumber]
    cardValue = calculateValue(fileName)

    print(fileName)
    print(cardValue)
        
    startingCard = addingCards(fileName)
    startingCard.goto(-100 + (a*30), -150)

    undealtCards.remove(fileName)


## Computer starting cards
for a in range(2):
    randomNumber = random.randint(0, len(undealtCards)-1)

    fileName = undealtCards[randomNumber]
    cardValue = calculateValue(fileName)

    print(fileName)
    print(cardValue)
        
    startingCard = addingCards(fileName)
    startingCard.goto(-100 + (a*30), 150)

    undealtCards.remove(fileName)
```

<br>

## Final Code

With all that said, here's my final code:

<br>

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
    startingCard.goto(-100 + (a*30), -150)

    undealtCards.remove(fileName)


## Computer starting cards
for a in range(2):
    randomNumber = random.randint(0, len(undealtCards)-1)

    fileName = undealtCards[randomNumber]
    cardValue = calculateValue(fileName)

    print(fileName)
    print(cardValue)
        
    startingCard = addingCards(fileName)
    startingCard.goto(-100 + (a*30), 150)

    undealtCards.remove(fileName)



## Infinite loop
while True:
    window.update()
```
