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

All 52 cards in the deck, at the moment, spawn in on top of each other. However, using ```goto(250 - n, -250)```, I could view them in a neat array. Unfortunately, this was useless, as I didn't actually want the user to see all these cards.
