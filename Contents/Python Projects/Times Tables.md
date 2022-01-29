``` python

name = input("What is your name? ")

print("Enter times table, start number and end number")

TT = int(input("Times table: "))
StartNumber = int(input("Start number: "))
EndNumber = int(input("End number: "))

print("Hi,", name, "... here is your times table")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━")

numbers = [TT, StartNumber, EndNumber]
length = EndNumber - StartNumber

for a in range(length+1):
    answer = (StartNumber + a) * TT
    int(input(str(StartNumber + a) + " * " + str(TT) + ": "))
    print("The answer was", answer, "\n")

```
