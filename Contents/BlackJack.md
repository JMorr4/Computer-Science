```python
import turtle

window = turtle.Screen()
window.title("BlackJack")
window.setup(width=800, height=800)
window.tracer(0)


window.addshape("BlackJack.gif")

ae=turtle.Turtle()
ae.shape('BlackJack.gif')

while True:
    window.update()
```
