```python
import random

class Crop:
    """A generic food crop"""

    # Constructor
    def __init__(self, growthRate, lightNeed, waterNeed):
        # Set the attribute with an inital value

        self.growth = 0
        self.daysGrowing = 0
        self.growthRate = growthRate
        self.lightNeed = lightNeed
        self.waterNeed = waterNeed
        self.status = "Seed"
        self.type = "Generic"

        ## the above attributes are prefixed with an underscore to indicate
        ## that they should not be accessed directly from outside the class

    # Method to indicate the needs of the crop
    def needs(self):
        # Return a dictionary containing the light and water needs
        return {"light need": self.lightNeed, "water need": self.waterNeed}

    # Method to report information about the current state of the crop
    def report(self):
        # Return a dictionary containing the type, status, growth and days growing
        return{"type":self.type, "status":self.status, "growth":self.growth, "days growing": self.daysGrowing}

    def updateStatus(self):
        if self.growth > 15:
            self.status = "Old"

        elif self.growth > 10:
            self.status = "Mature"

        elif self.growth > 5:
            self.status = "Young"

        elif self.growth > 0:
            self.status = "Seedling"

        elif self.status == 0:
            self,status = "Seed"

    def grow(self, light, water):
        if light >= self.lightNeed and water >= self.waterNeed:
            self.growth += self.growthRate

        # Increment days growing
        self.daysGrowing += 1
        # Update the status
        self.updateStatus()

def autoGrow(crop, days):
    # Grow the crop
    for day in range(days):
        light = random.randint(1, 10)
        water = random.randint(1, 10)
        crop.grow(light, water)

def manualGrow(crop):
    # Get the light and water values from the user
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True

            else:
                print("Value entered not valid - please enter a value between 1 and 10")

        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")

    valid = False

    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))

            if 1 <= water <= 10:
                valid = True

            else:
                print("Value entered not valid - please enter a value between 1 and 10")

        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")

    # Grow the crop
    crop.grow(light, water)


def displayMenu():
    print("1. Grow manually over one day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("Please select an option from the above menu")


def get_menu_choice():
    optionValid = False

    while not optionValid:
        try:
            choice = int(input("Option Selected: "))

            if 0 <= choice <= 4:
                optionValid = True

            else:
                print("Please enter a valid option")

        except ValueError:
            print("Please enter a valid option")
            
    return choice

def manageCrop(crop):
    print("This is the crop management process")
    print()

    noexit = True

    while noexit:
        displayMenu()
        option = get_menu_choice()

        print()

        if option == 1:
            manualGrow(crop)
            print()

        elif option == 2:
            autoGrow(crop, 30)
            print()

        elif option == 3:
            print(crop.report())

        elif option == 0:
            noexit = False
            print()

    print("Thank you for using the crop management program")


    
    
def main():
    # Instaniate the class
    newCrop = Crop(1, 4, 3)
    manageCrop(newCrop)

if __name__ == "__main__":
    main()
```

## Potato

```python

from Farm import *

class Potato(Crop):
    """A potato crop"""

    # Constructor
    def __init__(self):
        # Call the parent class constructor with default values for potato
        # growth rate = 1, light need = 3, water need = 6

        super().__init__(1, 3, 6)
        self.type = "Potato"

    # Override grow methods for subclass
    def grow(self, light, water):
        if light >= self.lightNeed and water >= self.waterNeed:
            if self.status == "Seedling" and water > self.waterNeed:
                self.growth += self.growthRate * 1.5

            elif self.status == "Young" and water > self.waterNeed:
                self.growth += self.growthRate * 1.25

            else:
                self.growth += self.growthRate

        # Increment day growing
        self.daysGrowing += 1

        # Update the status
        self.updateStatus()
            

def main():
    # Create a new potato crop
    potatoCrop = Potato()

    print(potatoCrop.report())

    # Manually grow the crop
    manualGrow(potatoCrop)
    print(potatoCrop.report())
    manualGrow(potatoCrop)
    print(potatoCrop.report())

if __name__ == "__main__":
    main()
```

## Crops

```python
from Farm import *
from Potato import *

def display_menu():
    print()
    print("Which crop would you like to create>")
    ()
    print("1. Potato")
    print("2. Wheat")
    print()

def select_option():
    validOption = False

    while not validOption:
        try:
            choice = int(input("Option selected: "))
            if choice in (1, 2):
                validOption = True

            else:
                print("Please enter a valid option")

        except ValueError:
            print("Please enter a valid option")

    return choice

def createCrop():
    displayMenu()
    choice = select_option()

    if choice == 1:
        newCrop = Potato()

    elif choice == 2:
        newCrop = Wheat()

    return newCrop

def main():
    newCrop = createCrop()
    manageCrop(newCrop)

if __name__ == "__main__":
    main()
```

## Wheat

```python
from Farm import *

class Wheat(Crop):
    """A potato crop"""

    # Constructor
    def __init__(self):
        # Call the parent class constructor with default values for potato
        # growth rate = 1, light need = 3, water need = 6

        super().__init__(1, 3, 6)
        self.type = "Wheat"

    # Override grow methods for subclass
    def grow(self, light, water):
        if light >= self.lightNeed and water >= self.waterNeed:
            if self.status == "Seedling" and water > self.waterNeed:
                self.growth += self.growthRate * 1.5

            elif self.status == "Young" and water > self.waterNeed:
                self.growth += self.growthRate * 1.25

            else:
                self.growth += self.growthRate

        # Increment day growing
        self.daysGrowing += 1

        # Update the status
        self.updateStatus()
            

def main():
    # Create a new wheat crop
    WheatCrop = Wheat()

    print(WheatCrop.report())

    # Manually grow the crop
    manualGrow(WheatCrop)
    print(WheatCrop.report())
    manualGrow(WheatCrop)
    print(WheatCrop.report())

if __name__ == "__main__":
    main()
```
