## Farm

```python
import random

#creating the class
class Crop():
        # Docstring
    """Crop Class""" 

    # constructor
    def __init__(self,growthRate, lightNeed, waterNeed):
        
        #set the attributes with initial values
        #self refers to itself (the class)
        #private variables
        self._growth = 0
        self._daysGrowing = 0
        self._growthRate = growthRate
        self._lightNeed = lightNeed
        self._waterNeed = waterNeed
        self._status = "Seed"
        self._type = "Generic"

    # Creating methods, which are functions attached to a class
    def needs(self):
        # returns a dictionary
        return {"light need":self._lightNeed, "water need":self._waterNeed}

    
    def report(self):
        return {"type":self._type, "status":self._status, "growth":self._growth, "daysGrowing":self._daysGrowing}


    def grow(self,light,water):
        if light >= self._lightNeed and water >= self._waterNeed:
            # grow crop
            self._growth += self._growthRate
        # update details 
        self._daysGrowing += 1
        self._update_status()


    # Private method shown by _
    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"


# You can pass an instance into a function
def auto_grow(crop,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)


# try except error handling
def manual_grow(crop):
    valid = False
    while not valid:
        try:
            light = int(input("Enter a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Invalid value entered, please enter again")
        except ValueError:
            print("Invalid value entered, please enter again")
            
    valid = False
    while not valid:
        try:
            water = int(input("Enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Invalid value entered, please enter again")
        except ValueError:
            print("Invalid value entered, please enter again")

    crop.grow(light,water)


def display_menu():
    print("\n1. Grow crop manually\n2. Grow automatically over 30 days\n3. Report Status\n0. Exit program")

    validOption = False
    while not validOption:
        try:
            choice = int(input("> "))
            if 0 <= choice <= 4:
                validOption = True
            else:
                print("Invalid option entered, please enter again")
        except ValueError:
             print("Invalid option entered, please enter again")

    return choice


def manage_crop(crop):
    
    end = False
    
    while not end:
        menu = display_menu()
        
        if menu == 1:
            manual_grow(crop)
            
        elif menu == 2:
            auto_grow(crop,30)
            
        elif menu == 3:
            print(crop.report())

        elif menu == 0:
            end = True
        
    
def main():
    # instanciate the class
    newCrop = Crop(1,4,3)
    manage_crop(newCrop)




if __name__=='__main__':
    main()

```

<br>

## Crops

```python
from Wheat import *
from Potato import *

def display_menu():
    print("\nWhich crop would you like to create")
    print("1. Potato\n2. Wheat")

    validOption = False
    
    while not validOption:
        try:
            choice = int(input("> "))
            
            if 0 <= choice <= 2:
                validOption = True
                
            else:
                print("Invalid option entered, please enter again")
                
        except ValueError:
             print("Invalid option entered, please enter again")

    return choice

def create_crop():
    choice = display_menu()
    
    if choice == 1:
        newCrop = Potato()
        
    elif choice == 2:
        newCrop = Wheat()
        
    return newCrop

def main():
    newCrop = create_crop()
    manage_crop(newCrop)

if __name__ == "__main__":
    main()

```

<br>

## Animal Class

```python

import random

#creating the class
class Animal:
    # Docstring
    """Animal Class""" 

    # constructor
    def __init__(self, growthRate, foodNeed, waterNeed):

        #set the attributes with initial values
        #self refers to itself (the class)
        #private variables
        self._weight = 0
        self._daysGrowing = 0
        self._growthRate = growthRate
        self._foodNeed = foodNeed
        self._waterNeed = waterNeed
        self._status = "Baby"
        self._type = "Generic"

    # Creating methods for reporting
    def needs(self):
        return {"food need":self._foodNeed, "water need":self._waterNeed}

    def report(self):
        return {"type":self._type, "status":self._status, "weight":self._weight, "daysGrowing":self._daysGrowing}

    #grow the animal
    def grow(self,food,water):
        if food >= self._foodNeed and water >= self._waterNeed:
            self._weight += self._growthRate
            
        # update details 
        self._daysGrowing += 1
        self._update_status()

    # Private method shown by _
    def _update_status(self):
        
        if self._weight > 40:
            self._status = "Elderly"
            
        elif self._weight > 20:
            self._status = "Mature"
            
        elif self._weight > 10:
            self._status = "Young"
            
        elif self._weight > 5:
            self._status = "Child"

    def return_type(self):
        return self._type


# you can pass an instance into a function
def autoGrow(animal,days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        
        animal.grow(food,water)


# try except error handling
def manualGrow(animal):
    valid = False
    while not valid:
        try:
            food = int(input("Enter a food value (1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Invalid value entered, please enter again")
        except ValueError:
            print("Invalid value entered, please enter again")
            
    valid = False
    while not valid:
        try:
            water = int(input("Enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Invalid value entered, please enter again")
        except ValueError:
            print("Invalid value entered, please enter again")

    animal.grow(food,water)


# User menu for testing
def display_menu():
    print("\n1. Grow animal manually\n2. Grow automatically over 30 days\n3. Report Status\n0. Exit program")

    validOption = False
    
    while not validOption:
        try:
            choice = int(input("> "))
            if 0 <= choice <= 4:
                validOption = True
                
            else:
                print("Invalid option entered, please enter again")
                
        except ValueError:
             print("Invalid option entered, please enter again")

    return choice

def manage_animal(animal):
    
    # print("currectly managing {0} animal".format(animal.return_type()))
    
    end = False
    
    while not end:
        menu = display_menu()
        
        if menu == 1:
            manualGrow(animal)
            
        elif menu == 2:
            autoGrow(animal,30)
            
        elif menu == 3:
            print("animal needs", animal.needs())
            print("animal report", animal.report())
            
        elif menu == 0:
            end = True
            
    print("See you next time")
    
def main():
    # instanciate the class
    newanimal = Animal(1,4,3)
    manage_animal(newanimal)

if __name__ == "__main__":
    main()

```

<br>

## Wheat

```python
# potato module interits from the crop class module 
from Farm import *

class Wheat(Crop):
    """Wheat Crop"""

    def __init__(self):
        # call the parent (superclass) constructor with defult values for wheat
        # growth rate = 3, light need = 4, water need = 2
        super().__init__(3,4,2)
        self._type = "Wheat"

    #override grow method for this subclass (polymorphism)
    def grow(self,light,water):
        if light >= self._lightNeed and water >= self._waterNeed:
            # added functionality to adjust for different crop type
            if self._status == "Young" :
                self._growth += self._growthRate * 1.5
            elif self._status == "Mature" :
                self._growth += self._growthRate * 2
            else:
                self._growth += self._growthRate
        # update details 
        self._daysGrowing += 1
        self._update_status()

def main():
    wheatCrop = Wheat()
    manual_grow(wheatCrop)
    print(wheatCrop.report())

if __name__ == "__main__":
    main()

```

<br>

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

    # Manually grow the crop
    manualGrow(potatoCrop)
    print(potatoCrop.report())

if __name__ == "__main__":
    main()

```

<br>

## Cows

```python
# clone of wheat class
from Animal_Class import *

class Cow(Animal):
    """Cow Animal"""

    def __init__(self):
        # call the parent (superclass) constructor with defult values for wheat
        # growth rate = 3, food need = 4, water need = 2
        super().__init__(3,4,2)
        
        self._type = "Cow"

    #override grow method for this subclass (polymorphism)
    def grow(self,food,water):
        if food >= self._foodNeed and water >= self._waterNeed:
            
            # added functionality to adjust for different crop type
            if self._status == "Young" :
                self._weight += self._growthRate * 1.5
                
            elif self._status == "Mature" :
                self._weight += self._growthRate * 2
                
            else:
                self._weight += self._growthRate
                
        # update details 
        self._daysGrowing += 1
        self._update_status()

def main():
    cowAnimal = Cow()
    manual_grow(cowAnimal)
    
    print(cowAnimal.report())

if __name__ == "__main__":
    main()
```

<br>

## Sheep

```python
from Animal_Class import *

class Sheep(Animal):
    """Sheep Animal"""

    def __init__(self):
        # growth rate = 1, food need = 2, water need = 6
        
        super().__init__(1,2,6)
        self._type = "Sheep"

    #override grow method for this subclass (polymorphism)
    def grow(self,food,water):
        if food >= self._foodNeed and water >= self._waterNeed:
            
            # added functionality to adjust for different crop type
            if self._status == "Seedling" :
                self._weight += self._growthRate * 1.5
                
            elif self._status == "Yound" :
                self._weight += self._growthRate * 1.2
                
            else:
                self._weight += self._growthRate
                
        # update details 
        self._daysGrowing += 1
        self._update_status()

def main():
    sheepAnimal = Sheep()
    manualGrow(sheepAnimal)
    
    print(sheepAnimal.report())

if __name__ == "__main__":
    main()

```
