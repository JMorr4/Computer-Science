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

## Field

```python

import random

from Potato import *
from Wheat import *
from Sheep import *
from Cow import *


class Field:
    """Field simulation with animals and crops"""

    # Constructor
    def __init__(self,maxAnimals, maxCrops):
        self._animals = [] 
        self._crops = []
        self._maxAnimals = maxAnimals
        self._maxCrops = maxCrops

    def add_crop(self,crop):
        if len(self._crops) < self._maxCrops:
            self._crops.append(crop)
            return True
        
        else:
            return False

    def add_animal(self,animal):
        if len(self._animals) < self._maxAnimals:
            self._animals.append(animal)
            return True
        
        else:
            return False
        
    def remove_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)

    def report_contents(self):
        cropReport = []
        animalReport = []
        
        for crop in self._crops:
            cropReport.append(crop.report())
            
        for animal in self._animals:
            animalReport.append(animal.report())
            
        return {"crops": cropReport,"animals": animalReport}

    def report_needs(self):
        food = 0
        light = 0
        water = 0
        
        for crop in self._crops:
            needs = crop.needs()
            
            if needs["light need"] > light:
                light = needs["light need"]
                
            if needs["water need"] > water:
                water = needs["water need"]
                
        for animal in self._animals:
            needs = animal.needs()
            food += needs["food need"]
            
            if needs["water need"] > water:
                water = needs["water need"]
        
        return {"food":food, "light": light, "water":water}

    def grow_field(self,food,light,water):
        for crop in self._crops:
            crop.grow(light,water)

        foodTotalNeed = 0
        
        for animal in self._animals:
            needs = animal.needs()
            foodTotalNeed += needs["food need"]
            
        if food > foodTotalNeed:
            extraFood = food - foodTotalNeed
            food = foodTotalNeed
            
        else:
            extraFood = 0

        for animal in self._animals:
            needs = animal.needs()
            
            if food >= needs["food need"]:
                food -= needs["food need"]
                feed = needs["food need"]
                
            else: 
                feed = 0

            if extraFood > 0:
                extraFood -= 1
                feed += 1
            animal.grow(feed,water)
        

def display_crops(cropList):
    print("\nCrops growing in this field:")
    index = 1
    for crop in cropList:
        print("{0}. {1}".format(index,crop.report()))
        index += 1

def display_animals(animalList):
    print("\nAnimals in this field:")
    index = 1
    for animal in animalList:
        print("{0}. {1}".format(index,animal.report()))
        index += 1

def select_crop(listLen):
    validOption = False
    
    while not validOption:
        try:
            choice = int(input("Please select a crop\n > "))
            if choice in range(1,listLen+1):
                validOption = True
            else:
                print("Invalid option entered, please enter again")
                
        except ValueError:
             print("Invalid option entered, please enter again")

    return choice - 1

def select_animal(listLen):
    validOption = False
    
    while not validOption:
        try:
            choice = int(input("Please select a animal\n > "))
            
            if choice in range(1,listLen+1):
                validOption = True
                
            else:
                print("Invalid option entered, please enter again")
                
        except ValueError:
             print("Invalid option entered, please enter again")

    return choice - 1

def remove_field_crop(field):
    if len(field._crops) > 0:
        display_crops(field._crops)
        selected = select_crop(len(field._crops))
        
        return field.remove_crop(selected)
    
    else:
        print("no crops in field")
        return "not"

def remove_field_animal(field):
    if len(field._animals) > 0:
        display_animals(field._animals)
        selected = select_animal(len(field._animals))
        
        return field.remove_animal(selected)
    
    else:
        print("no animals in field")
        return "not"

def add_field_crop(field):
    choice = display_crop_menu()
    if choice == 1:
        if field.add_crop(Potato()):
            print("\nNew crop added")
        else:
            print("\nCannot plant: Field is full")
            
    if choice == 2:
        if field.add_crop(Wheat()):
            print("\nNew crop added")
            
        else:
            print("\nCannot plant: Field is full")

def add_field_animal(field):
    choice = display_animal_menu()

    if choice == 1:
        if field.add_animal(Sheep()):
            print("\nNew animal added")
            
        else:
            print("\nCannot add new animal: Field is full")
            
    if choice == 2:
        if field.add_animal(Cow()):
            print("\nNew animal added")
            
        else:
            print("\Cannot add new animal: Field is full")


def autoGrow(field,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        
        field.grow_field(food,light,water)

def manualGrow(field):
    print("Enter a light value between 1-10 for the whole field")
    light = get_menu_choice(0, 10)
    
    print("Enter a water value between 1-10 for the whole field")
    water = get_menu_choice(0, 10)
    
    print("Enter a food value between 1-100 for the animals")
    food = get_menu_choice(0, 100)

    for i in range(10):
        field.grow_field(food,light,water)

def display_crop_menu():
    print("Which type of crop would you like to add")
    print("\n1. Potato\n2. Wheat\n0. Return to previous menu")
    
    return get_menu_choice(0, 2)

def display_animal_menu():
    print("Which type of animal would you like to add")
    print("\n1. Sheep\n2. Cow\n0. Return to previous menu")
    
    return get_menu_choice(0, 2)

def display_main():
    print("1. Plant a crop")
    print("2. Harvest a crop")
    print("3. Raise an animal")
    print("4. Slaughter an animal")
    print("5. Grow field manually")
    print("6. Grow field automatically")
    print("7. Report field status")
    print("8. Report field requirements")
    print("0. Exit Program")
    
    return get_menu_choice(0, 8)

def get_menu_choice(lower, upper):
    validOption = False
    while not validOption:
        try:
            choice = int(input("\n> "))
            if lower <= choice <= upper:
                validOption = True
            else:
                print("Invalid value entered, please enter again")
        except ValueError:
             print("Invalid value entered, please enter again")

    return choice

def manage_field(field):
    print("Welcome to the field management program")
    
    end = False
    
    while not end:
        menu = display_main()
        
        if menu == 1:
            add_field_crop(field)
            
        elif menu == 2:
            removed = remove_field_crop(field)
            
            print("Crop {0} removed".format(removed))
            
        elif menu == 3:
            add_field_animal(field)
            
        elif menu == 4:
            removed = remove_field_animal(field)
            
            print("Animal {0} removed".format(removed))
            
        elif menu == 5:
            manualGrow(field)
            
        elif menu == 6:
            autoGrow(field,30)
            
        elif menu == 7:
            print(field.report_contents())
            
        elif menu == 8:
            needs = field.report_needs()
            
            for key, value in needs.items():
                print(key, " : ", value)
                
        elif menu == 0:
            end = True
            
    print("\nSee you next time")
        
def main():
    field1 = Field(3,12)
    manage_field(field1)

if __name__ == "__main__":
    main()

```

<br>

## Animal Main

```python

from Cow import *
from Sheep import *

def display_menu():
    print("\nWhich animal would you like to create")
    print("1. Cow")
    print("2. Sheep")

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

def create_animal():
    choice = display_menu()
    
    if choice == 1:
        newAnimal = Cow()
        
    elif choice == 2:
        newAnimal = Sheep()
        
    return newAnimal

def main():
    newAnimal = create_animal()
    manage_animal(newAnimal)

if __name__ == "__main__":
    main()
```
