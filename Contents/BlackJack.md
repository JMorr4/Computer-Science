REMEMBER: Download images on own computer

```python
import turtle

window = turtle.Screen()
window.title("BlackJack")
window.setup(width=800, height=800)
window.tracer(0)

window.bgpic("BlackJack.gif")
window.addshape("Jack of Clubs.gif")

ae=turtle.Turtle()
ae.shape('Jack of Clubs.gif')

window.listen()
ae.ondrag(ae.goto)
ae.pu()
ae.goto(250,-250)

while True:
    window.update()
```

```python
import turtle
import random

cardList = ["S1.gif", "H2", ""]
suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')

window = turtle.Screen()
window.title("BlackJack")
window.setup(width = 800, height = 800)
window.tracer(0)
# Max Height: 1000
# Max Width: 1750

window.bgpic("BlackJack.gif")


for suit in suits:
    
    for n in range(1,14):
        card = suit + str(n)

        name = card + ".gif"
        window.addshape(name)
        
        ae = turtle.Turtle()
        ae.shape(name)

        window.listen()
        ae.ondrag(ae.goto)
        ae.pu()
        ae.goto(250,-250)

        window.update()

while True:
    window.update()


##card + ".gif"

##ae = turtle.Turtle()
##ae.shape(card)
##
##window.listen()
##ae.ondrag(ae.goto)
##ae.pu()
##ae.goto(250,-250)

####for a in range(10):
##shape = window.addshape("Ace of Spades.gif")
##window.addshape("Ace of Hearts.gif")
##window.addshape("Ace of Clubs.gif")
##window.addshape("Ace of Diamonds.gif")
##
##window.addshape("King of Spades.gif")
##window.addshape("King of Hearts.gif")
##window.addshape("King of Clubs.gif")
##window.addshape("King of Diamonds.gif")
##
##window.addshape("Jack of Clubs.gif")
##window.addshape("Eight of Clubs.gif")
##
##def listAppending(shape):
##
##
##
##def cardOnScreen(a):
##    card = turtle.Turtle()
##    card.shape(cardList[random.randint(a)])
##
##
##
##
### Back of Card
##ae=turtle.Turtle()
##ae.shape('Back of Card.gif')
##
##window.listen()
##ae.ondrag(ae.goto)
##ae.pu()
##ae.goto(-250,-250)
##
##
### Jack of Clubs
##ae=turtle.Turtle()
##ae.shape('Jack of Clubs.gif')
##
##window.listen()
##ae.ondrag(ae.goto)
##ae.pu()
##ae.goto(250,-250)
##
##
##window.addshape("Ace of Clubs.gif")
##
##ae=turtle.Turtle()
##ae.shape('Ace of Clubs.gif')
##
##window.listen()
##ae.ondrag(ae.goto)
##ae.pu()
##ae.goto(200,-250)


##ae=turtle.Turtle()
##ae.shape('Eight of Clubs.gif')
##
##window.listen()
##ae.ondrag(ae.goto)
##ae.pu()
##ae.goto(150,-250)
##
##
##while True:
##    window.update()
```

![All Cards](https://user-images.githubusercontent.com/90699946/145810994-6806f77a-7d5b-4455-b2b8-e5d57945b75e.gif)
![BlackJack](https://user-images.githubusercontent.com/90699946/145813149-70fc240d-a934-4a4b-9a73-a8370b42ef17.gif)

# Clubs
![Ace of Clubs](https://user-images.githubusercontent.com/90699946/145811128-c4d20a04-1347-4ac3-a473-bdc628bbe1a5.gif)
![Eight of Clubs](https://user-images.githubusercontent.com/90699946/145811166-781f02d6-45b1-45b2-b77b-1f90d6b1deb7.gif)
![Five of Clubs](https://user-images.githubusercontent.com/90699946/145812964-07b76c5e-fff1-4b82-877a-f92fc0f21072.gif)
![Four of Clubs](https://user-images.githubusercontent.com/90699946/145812974-c51e99db-acc1-40b3-943b-467562a9e11c.gif)
![King of Clubs](https://user-images.githubusercontent.com/90699946/145813004-7f3a9b02-35f8-4ef1-808d-89a036ff8a02.gif)
![Nine of Clubs](https://user-images.githubusercontent.com/90699946/145813018-2cee6388-d2c5-4d77-9964-cd206e8c6254.gif)
![Queen of Clubs](https://user-images.githubusercontent.com/90699946/145813033-0aaed16c-8ec5-447d-99e5-2e3670c40c8e.gif)
![Seven of Clubs](https://user-images.githubusercontent.com/90699946/145813043-31b02370-7d36-4068-a612-1a0aff5d049c.gif)
![Six of Clubs](https://user-images.githubusercontent.com/90699946/145813069-01ecc940-4727-41f7-9dc2-7a294405c9c9.gif)
![Ten of Clubs](https://user-images.githubusercontent.com/90699946/145813074-42c0551f-875a-49c6-b38d-d181aa3b1cfe.gif)
![Three of Clubs](https://user-images.githubusercontent.com/90699946/145813078-0944b786-e0a2-4533-9778-f51a33a91968.gif)
![Two of Clubs](https://user-images.githubusercontent.com/90699946/145813085-11a0fca6-19cf-47c9-8759-40910596d5d7.gif)
![Jack of Clubs](https://user-images.githubusercontent.com/90699946/145813158-46370eb7-5745-4f66-9bf4-5bb73713bf93.gif)

# Spades
![Ace of Spades](https://user-images.githubusercontent.com/90699946/146025728-ab4693fa-e077-4bd9-8aeb-197d9ef5d66c.gif)
![Two of Spades](https://user-images.githubusercontent.com/90699946/146025736-186e7196-25d8-40e5-895c-6b65c4beb0b6.gif)
![Three of Spades](https://user-images.githubusercontent.com/90699946/146025756-19fbf5ac-74d6-4574-9a3f-356bc09af4a1.gif)
![Four of Spades](https://user-images.githubusercontent.com/90699946/146025779-20485a37-d749-49df-bf6e-6ab480db7313.gif)
![Five of Spades](https://user-images.githubusercontent.com/90699946/146025787-b6f543a8-b0c3-459c-bef3-effb7408e3c7.gif)
![Six of Spades](https://user-images.githubusercontent.com/90699946/146025792-19772109-2d76-43ce-b2e0-845b75954026.gif)
![Seven of Spades](https://user-images.githubusercontent.com/90699946/146025803-a9f24dee-41fb-473f-880a-e284528c22bf.gif)
![Eight of Spades](https://user-images.githubusercontent.com/90699946/146025810-ac52a549-b3cd-4fb8-8f31-66882bff52c2.gif)
![Nine of Spades](https://user-images.githubusercontent.com/90699946/146025824-cd1ca92b-f0b2-4c65-b2cc-754d24b061e8.gif)
![Ten of Spades](https://user-images.githubusercontent.com/90699946/146025835-b0295f29-ff6a-49ee-9197-458270830ae1.gif)
![Jack of Spades](https://user-images.githubusercontent.com/90699946/146025852-4dcb7e17-ac56-4481-84cb-7905ec9b415e.gif)
![Queen of Spades](https://user-images.githubusercontent.com/90699946/146025867-1d90cd8e-7852-4250-af33-be82c8b4bb75.gif)
![King Of Spades](https://user-images.githubusercontent.com/90699946/146025873-ee63c3ce-9531-4031-bba3-8e9f80a62ccf.gif)

# Hearts
![King of Hearts](https://user-images.githubusercontent.com/90699946/146025968-ea955880-7253-490a-b0e9-0d7d1754859a.gif)
![Queen of Hearts](https://user-images.githubusercontent.com/90699946/146025973-67e0ebf2-b737-423a-aac5-bcdb01ef11de.gif)
![Jack of Hearts](https://user-images.githubusercontent.com/90699946/146025976-e771cdbf-fcdb-47d7-93c5-9feecd771bf5.gif)
![Ten of Hearts](https://user-images.githubusercontent.com/90699946/146025978-d151c34a-eff2-4d6d-8578-d8d9599b4154.gif)
![Nine of Hearts](https://user-images.githubusercontent.com/90699946/146025981-f0cd5208-38b8-4f6e-8269-5d2942b3df68.gif)
![Eight of Hearts](https://user-images.githubusercontent.com/90699946/146026550-3b1bdff0-c723-4c90-8608-dfc7dbcf6d14.gif)
![Seven of Hearts](https://user-images.githubusercontent.com/90699946/146025986-39ca2a41-52e4-40fc-a578-09d2d48871d2.gif)
![Six of Hearts](https://user-images.githubusercontent.com/90699946/146025987-de2dad95-3fd2-4e77-b678-8099b7595c5e.gif)
![Five of Hearts](https://user-images.githubusercontent.com/90699946/146025988-cc2382d9-3854-44c6-86d4-098bf2153161.gif)
![Four of Hearts](https://user-images.githubusercontent.com/90699946/146025991-b7ba6aba-2d70-4687-bc32-60c61905dfc4.gif)
![Three of Hearts](https://user-images.githubusercontent.com/90699946/146025992-c5228e81-e3b0-4a54-afc3-d44723b67a48.gif)
![Two of Hearts](https://user-images.githubusercontent.com/90699946/146025993-99eca57e-a7bc-407d-9dfd-568b3caaf2a7.gif)
![Ace of Hearts](https://user-images.githubusercontent.com/90699946/146025995-cd2b3239-7aa9-45b4-824c-97184e28a1f9.gif)

# Diamonds
![King of Diamonds](https://user-images.githubusercontent.com/90699946/146026108-b939e1bd-6a61-4e33-9001-0f2ee184bb1a.gif)
![Queen of Diamonds](https://user-images.githubusercontent.com/90699946/146026111-421cf7c2-44d6-4f37-8ac5-0d36bbfb84c5.gif)
![Jack of Diamonds](https://user-images.githubusercontent.com/90699946/146026112-14ae6c80-688f-4018-a53a-f8ff2c9daf91.gif)
![Ten of Diamonds](https://user-images.githubusercontent.com/90699946/146026113-d1079d0f-e468-4b25-8ea0-c7b146aeb5b7.gif)
![Nine of Diamonds](https://user-images.githubusercontent.com/90699946/146026114-7fefbb49-8e08-4355-ac7a-5ac9eecc902e.gif)
![Eight of Diamonds](https://user-images.githubusercontent.com/90699946/146026116-ff2eaf1b-e610-4f31-86aa-05e0783bf9a1.gif)
![Seven of Diamonds](https://user-images.githubusercontent.com/90699946/146026117-026fec00-7a69-4267-85e5-03fb377b0b01.gif)
![Six of Diamonds](https://user-images.githubusercontent.com/90699946/146026119-a6e63a18-c1bf-4008-aa13-9c240fa1ef5e.gif)
![Five of Diamonds](https://user-images.githubusercontent.com/90699946/146026120-9b2b1ac2-a289-4b8c-9b0d-161d7a31baca.gif)
![Four of Diamonds](https://user-images.githubusercontent.com/90699946/146026123-9f784563-ed5b-46a7-8288-96dcb72d954f.gif)
![Three of Diamonds](https://user-images.githubusercontent.com/90699946/146026126-de598122-70d2-49f3-a90c-f24dd21385a4.gif)
![Two of Diamonds](https://user-images.githubusercontent.com/90699946/146026127-50af6713-f947-47b5-9806-16d3bdbe0687.gif)
![Ace of Diamonds](https://user-images.githubusercontent.com/90699946/146026128-db1480fd-766b-4bdf-8d42-694f75eeb9fd.gif)





# The Back of a Card

![Back of Card](https://user-images.githubusercontent.com/90699946/149178525-064b5cf0-df7a-42d9-ad68-f61615e0f906.gif)
