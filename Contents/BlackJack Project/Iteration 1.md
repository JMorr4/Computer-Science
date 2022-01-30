## Iteration 1

For my first stab at this project, I was just discovering the inbuilt turtle module in python. Although we'd covered it in class before, I'd never really fully grasped any way to properly utilise it. However, after a some time, I managed to work out how to set up a new window, modify it, and deploy images onto it's screen. I even found out how to move these images using my mouse. 

However, at this time, I hadn't fully decided whether Blackjack was for me, so there were only a couple of images downloaded on my computer, one being the green poker background and the Jack of Clubs.

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

<br>

During the coding, I realised all new images spawned at coordinates (0,0). I found a way to change this with the ```goto(x, y)``` feature. This is what the output of my first iteration looks like, keeping in mind I'm able to move this card around.

<br>

![image](https://user-images.githubusercontent.com/90699946/151679215-8f782b58-7819-427b-b0d7-81bde3045f37.png)



<br>



## Images

Next, I had to spend a lot of time managing the images I was going to use for the UI in this project. It took a while finding, cutting, cropping and downloading everything, but, to save space, they've been clumped together and uploaded in a seperate file [here](https://github.com/JMorr4/Computer-Science/blob/main/Contents/BlackJack%20Project/Images.md). At this point I had named each of these images as such: "Jack of Clubs", etc. Later, I would have to go through the painstaking process of renaming all of these to better names suited for my program.
