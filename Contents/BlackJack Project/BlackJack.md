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

![image](https://user-images.githubusercontent.com/90699946/151679215-8f782b58-7819-427b-b0d7-81bde3045f37.png)

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

## Images

I had to spend a lot of time managing the images I was going to use for the UI in this project. It took a while finding, cutting, cropping and downloading everything, but they've been clumped together and uploaded [here](https://github.com/JMorr4/Computer-Science/blob/main/Contents/BlackJack%20Project/Images.md).
