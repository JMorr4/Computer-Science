import turtle

window = turtle.Screen()
window.setup(width=800, height=800)
window.tracer(0)


window.addshape("ae.gif")

ae=turtle.Turtle()
ae.shape('ae.gif')

while True:
    window.update()
