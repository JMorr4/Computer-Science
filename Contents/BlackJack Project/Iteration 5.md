## Iteration 5

After Iteration 4, I hit a brick wall to the point where I realised I couldn't create a fully independantly UI based Blackjack game using Turtle alone; I had to use a command prompt to help, meaning I had to scrap the background and images, and instead resort to the turtle drawing pen to draw me shapes, numbers, letters, etc. Although I tried to keep some of my images, it looked terrible, as seen below:

#### Failed Test

![image](https://github.com/JMorr4/Computer-Science/assets/90699946/7343f7ac-74a7-4ecd-91e5-55ebc93b579d)

### Final Tests

#### Draw
![image](https://github.com/JMorr4/Computer-Science/assets/90699946/981d67fb-6d1c-4e3a-afe2-b0967e694037)

#### Win by dealer bust
![image](https://github.com/JMorr4/Computer-Science/assets/90699946/cf06347f-5c15-43b1-9537-cccac5946916)



### Final Code
```python
import random
import turtle

window = turtle.Screen()
window.title("BlackJack")
window.tracer(0)

cardsDir = "Images/"

updater = turtle.Turtle()
updater.ht()
updater.speed(0)
updater.up()
updater.goto(30, 0)
turtle.speed(0)
playerMoney = 1000
turtle.ht()

# Setting up lists
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
undealtCards = []

global numPresses
numPresses = 1

# Function to find the value of each card
def calculateValue(fileName):
    value = int(fileName.strip("Images/Spades Hearts Clubs Diamonds.gif"))

    if value > 9:
        value = 10

    return value


class Card:
    def __init__(self, number = None, suit = None):

        if suit is None:
            suit = random.choice(['D', 'S', 'C', 'H'])
            number = random.choice(['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])

            if number in ['K', 'Q', 'J']:
                number = [number, 10]

            else:
                number = [number, number]

        self.suit = suit
        self.number = number

    def getSuit(self):
        return self.suit

    def getNumber(self):
        return self.number[1]

    def writing(self, x, y):
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        turtle.write(self.number[0])
        turtle.up()
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.write(self.suit)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)

    def ace(self):
        if 'A' in self.number:
            x = int(input("Would you like your ace to equal 11 or 1?"))

            if x == 11:
                self.number[1] = 11

            elif x == 1:
                self.number[1] = 1

            else:
                ace(self)


def setup(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    for _ in range(2):

        for _ in range(2):
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)

        turtle.forward(50)


def drawcard(x, y):
    turtle.up()
    turtle.goto(x-25, y+30)
    turtle.down()

    for _ in range(2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)


def PcardUpdate(x, card_sum, playerMoney):
    updater.clear()

    updater.goto(30, 20)
    updater.write("Player Card sum: " + str(x))

    updater.goto(30, 0)
    updater.write("Dealer Card sum: " + str(card_sum))

    updater.goto(30, -20)
    updater.write("Player Money: " + str(playerMoney))


def bust(x, playerMoney):
    if x > 21:
        print("Bust!")

        return 0


def is_hit(currentPlayer):

    x = -25 + (currentPlayer * 50)
    choice = input('Hit or stand?')

    while choice.lower() not in ['hit', 'stand']:
        choice = input('Hit or stand')

    if choice.lower() == 'Hit':
        print('Hit it is')
        currentPlayer += 1

        XtraCard = Card()
        XtraCard.writing(x, -55)
        drawcard(x, -55)
        XtraCard.ace()

        return [XtraCard.getNumber(), currentPlayer]

    elif choice.lower() == 'stand':
        print('Ok')

        return [0, 0]

    else:
        print("I didn't understand")
        is_hit(currentPlayer)


def DHit(currentPlayer, playerHand, card_sum):
    x = -25 + (currentPlayer * 50)
    currentPlayer += 1

    XtraCard = Card()
    XtraCard.writing(x-55, 100)
    drawcard(x, 120)

    if XtraCard.getNumber() == 'A':

        if card_sum + 11 > 21:
            return [1, currentPlayer]

        elif card_sum + 11 == 21:
            return [11, currentPlayer]

        else:
            return [11, currentPlayer]

    return [XtraCard.getNumber(), currentPlayer]


def Dchecker(card_sum, x):
    
    if card_sum > 21:
        return 'dealer bust'

    elif card_sum > x and card_sum < 21:
        return 'dealer win'

    elif card_sum == x:
        return 'push'

    elif card_sum == 21:
        return 'dealer win'


def howmuch(player1):  # how much the player wants to bet
    bet = int(input("How much would you like to bet? (whole number)"))

    while bet > player1:
        bet = int(input("You can't bet more than you have."))

    while bet < 0:
        bet = int(input("How much would you like to bet? (whole positive number)"))

    while bet == 0:
        print("No empty bets allowed.")

        bet = int(input("How much would you like to bet? (whole positive number)"))
    return bet


def want_to_quit():
    choice = input("Would you like to quit?")

    while choice.lower() not in ['yes', 'no']:
        print("Sorry I didn't understand.")

        choice = input("Would you like to quit")

    if choice.lower() == 'yes':
        print("Ok, bye")

        return 'bye'

    elif choice.lower() == 'no':
        print("Ok")

        return


def play_round(playerMoney):
    PcardUpdate(0, 0, playerMoney)
    playerMoney = playerMoney

    bet = howmuch(playerMoney)

    PcardUpdate(0, 0, playerMoney)
    playerMoney -= bet
    counter = [0, 1]
    joe = [0, 1]

    setup(-100, 150)
    setup(-100, -25)

    # Dealer cards
    Dcard1 = Card()
    Dcard1.writing(-75, 100)

    # Player cards
    Pcard1 = Card()
    Pcard2 = Card()

    # Writes the card down
    Pcard1.writing(-75, -55)
    Pcard2.writing(-25, -55)

    # Checks to see if "Pcard" is ace
    Pcard1.ace()
    Pcard2.ace()

    x = Pcard1.getNumber() + Pcard2.getNumber()

    if x == 21:
        print("Blackjack!")
        playerMoney = playerMoney + 2 * bet

        return playerMoney

    PcardUpdate(x, Dcard1.getNumber(), playerMoney)

    while counter != [0, 0]:
        counter = is_hit(counter[1])
        x += counter[0]

        PcardUpdate(x, Dcard1.getNumber(), playerMoney)
        z = bust(x, playerMoney)

        if z == 0:
            return playerMoney

    card_sum = Dcard1.getNumber()

    if card_sum == 'A':
        card_sum = 11

    result = 'currentPlayer'

    while result not in ['dealer bust', 'dealer win', 'push']:
        joe = DHit(joe[1], x, card_sum)
        card_sum += joe[0]

        PcardUpdate(x, card_sum, playerMoney)
        result = Dchecker(card_sum, x)

    if result == 'dealer bust':
        print('Dealer bust!')
        playerMoney += 2*bet

        return playerMoney

    elif result == 'dealer win':
        print('Dealer win!')

        return playerMoney

    elif result == 'push':
        print('Push!')
        playerMoney += bet

        return playerMoney


while True:
    playerMoney = play_round(playerMoney)

    if playerMoney == 0:
        print("You ran out of money :(")

        break

    last_round = want_to_quit()
    turtle.clear()

    if last_round == 'bye':
        break
```




