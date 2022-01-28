```python
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


    
def main():
    # Instaniate the class
    newCrop = Crop(1, 4, 3)
    # Test to see whether it works or not
    print(newCrop.needs()["light need"])
    print(newCrop.report())
    newCrop.grow(4, 4)
    print(newCrop.report())

if __name__ == "__main__":
    main()
```
