## Factorial

```python
def factorial(n):
    numberList = []
    num = 1
    
    for a in range(n):
        number = n - a
        numberList.append(number)
        num = num * numberList[a]
    
    return num



number = int(input("What is the number? "))

print(factorial(number))
```
