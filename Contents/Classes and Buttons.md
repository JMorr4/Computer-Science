## Buttons

```python
# import everything from tkinter module
from tkinter import *   
 
# create a tkinter window
window = Tk()             
 
# Open window having dimension 100x100
window.geometry("100x100")
 
# Create a Button
btn = Button(window, text = 'Click me !', bd = '5', command = window.destroy)
 
# Set the position of button on the top of window.  
btn.pack(side = 'top')   
 
window.mainloop()
```

<br>

## Classes

```python
class classOne:
    num = 5

class classTwo:
    num = 10

classOne = classOne()
classTwo = classTwo()

print(classOne.num)
print(classTwo.num)
```
