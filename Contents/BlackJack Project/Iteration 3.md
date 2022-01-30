## Iteration 3

There's a large jump from my code in the second iteration to the third, but I couldn't really find a good boundary between the two. But moving on, my aim here was to create a button that, when clicked, allowed a random card to be generated from the 52 available ones. At first, I aimed to have the "Back of Card" image as the button I would press, but that hope quickly died after hours of failing to find a way to do this. Hopefully, in the future, I can change this, but for now I had to think of something else.

So I did. I decided to create two different coloured turtle squares: Red and green. One of these would generate a random card, the other would pretty much be useless for now until I found  use for it. At first I couldn't find a way to make a turtle button, so I experimented with the tkinter module:

```python
## Button
import turtle

def button():
    window = turtle.Screen()
    window.setup(400, 300)
    return turtle.textinput("title", "prompt")

answer = button()
print(answer)
```

<br>

This came up with a prompt for the user to input some text, which wasn't what I wanted.

![image](https://user-images.githubusercontent.com/90699946/151709181-10f69b61-8a10-4d7b-bb23-91ab0c286cf8.png)

<br>

However, I eventually managed to find a function: ```onclick()```, that allowed an event to occur if the user clicked on a shape, which was *exactly* what I wanted. I created two turtle squares, red and green, shoved them into the top left portion of the window, and coded in a string for each to print depending on which colour I clicked. It worked.

I then changed the buttons to produce a different image each depending on which one I clicked. That also worked.

Now the challenge was to generate a *random* image when I clicked on the green one. I adapted the nested loop from the second iteration for part of it to be inside a function:

```python
def addingCards(fileName):
        ae = turtle.Turtle()
        ae.shape(fileName)

        window.listen()
        ae.ondrag(ae.goto)
        ae.pu()
        ae.goto(0, 0)

        window.update()
```

<br>

Then I created an array called "cards", and added ```cards.append(fileName)``` into the nested loop, so I would have all 52 cards in a list. I used this to allow a random card to be selected from the list, then outputted as an image onto the screen. All this would happen if the user clicked on the green box. It worked. The final result is as shown:

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

<br>

At the moment, all the red button does is generate the "Back of Card" image when pressed. You can also see the results of each click in the python shell on the left hand side, as the image selected from the list is also printed out here. Unfortunately, there isn't anything to stop the same card being displayed twice, so that'll have to be fixed in future iterations.

<br>

![image](https://user-images.githubusercontent.com/90699946/151679288-b5a8306f-7606-4822-960d-01a1df2d7007.png)













