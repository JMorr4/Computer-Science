# BlackJack Python Project

```python
import turtle

window = turtle.Screen()
window.title("BlackJack")
window.setup(width=800, height=800)
window.tracer(0)

window.bgpic("BlackJack.gif")
window.addshape("Jack of Clubs.gif")

ae=turtle.Turtle()
ae.shape('Jack of Clubs.gif')

window.listen()
ae.ondrag(ae.goto)
ae.pu()
ae.goto(250,-250)

while True:
    window.update()
```

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


##card + ".gif"

##ae = turtle.Turtle()
##ae.shape(card)
##
##window.listen()
##ae.ondrag(ae.goto)
##ae.pu()
##ae.goto(250,-250)

####for a in range(10):
##shape = window.addshape("Ace of Spades.gif")
##window.addshape("Ace of Hearts.gif")
##window.addshape("Ace of Clubs.gif")
##window.addshape("Ace of Diamonds.gif")
##
##window.addshape("King of Spades.gif")
##window.addshape("King of Hearts.gif")
##window.addshape("King of Clubs.gif")
##window.addshape("King of Diamonds.gif")
##
##window.addshape("Jack of Clubs.gif")
##window.addshape("Eight of Clubs.gif")
##
##def listAppending(shape):
##
##
##
##def cardOnScreen(a):
##    card = turtle.Turtle()
##    card.shape(cardList[random.randint(a)])
##
##
##
##
### Back of Card
##ae=turtle.Turtle()
##ae.shape('Back of Card.gif')
##
##window.listen()
##ae.ondrag(ae.goto)
##ae.pu()
##ae.goto(-250,-250)
##
##
### Jack of Clubs
##ae=turtle.Turtle()
##ae.shape('Jack of Clubs.gif')
##
##window.listen()
##ae.ondrag(ae.goto)
##ae.pu()
##ae.goto(250,-250)
##
##
##window.addshape("Ace of Clubs.gif")
##
##ae=turtle.Turtle()
##ae.shape('Ace of Clubs.gif')
##
##window.listen()
##ae.ondrag(ae.goto)
##ae.pu()
##ae.goto(200,-250)


##ae=turtle.Turtle()
##ae.shape('Eight of Clubs.gif')
##
##window.listen()
##ae.ondrag(ae.goto)
##ae.pu()
##ae.goto(150,-250)
##
##
##while True:
##    window.update()
```

## Images

I had to spend a lot of time managing the images I was going to use for the UI in this project. It took a while finding, cutting, cropping and downloading everything, but they've been clumped together and uploaded [here](https://github.com/JMorr4/Computer-Science/blob/main/Contents/BlackJack%20Project/Images.md).
