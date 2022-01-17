```python
import random
import operator

symbols = ["+", "-", "*", "/"]

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }

score = 0

for a in range(10):
    numberOne = random.randint(0,100)
    numberTwo = random.randint(0,100)

    symbol = symbols[random.randint(0,3)]

    if symbol == ("/"):
        numberOne = numberTwo * random.randint(1,20)
    
    userAnswer = float(input("What is " + str(numberOne) + str(symbol) + str(numberTwo) + "? "))

    answer = ops[str(symbol)](numberOne,numberTwo)

    if userAnswer == answer:
        score += 1
        print("Correct!\n")

    else:
        print("Wrong answer! Correct answer was", str(answer), "\n")

print("You got", score, "out of 10!")
```
