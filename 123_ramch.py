#   a123_apple_1.py
import turtle as trtl
from random import *
import time

#setup but cooler
apple_image = "apple.gif" # Store the file name of your shape

#screen
wn = trtl.Screen()
wn.setup(610, 410)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
#five fruits list
currentfruits = []
#letter management
#makes it so two of the same letter never appear but once a letter is used it will reappear
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","t","u","v","w","x","y","z"]
inuse = []
#fonts
fonttype = ("Monospace", 20, "bold")
ptime = time.time()
dtime = 0

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def indicator(realslimwriter,let,pos):
    realslimwriter.goto(pos[0]-(len(let)*5),pos[1]-20)
    realslimwriter.write(let,font=fonttype)

#fruit class
class fruit:
  def fall(self):
    global currentfruits
    #stop fruit from falling twice
    if not self.hasfell:
      #add fruit to the falling fruit
      currentfruits.append(self)
      self.realslimwriter.clear()
      self.hasfell = True
  def __init__(self):
    #display letter on fruit
    self.realslimwriter = trtl.Turtle()
    self.realslimwriter.penup()
    self.realslimwriter.hideturtle()
    self.realslimwriter.color("#FFFFFF")
    self.realslimwriter.speed(0)
    #makes the fruit fruit itself
    self.Turt = trtl.Turtle()
    self.Turt.penup()
    self.Turt.speed(0)
    self.Turt.goto(randint(-200,200),randint(0,200))
    #moves letter being used to the in use list
    self.let = letters.pop(randint(0,len(letters)-1))
    global inuse
    inuse.append(self.let)
    #stops fruit from falling while already falling
    self.hasfell = False
    #the fruitening pt 2
    draw_apple(self.Turt)
    #makes text become real
    indicator(self.realslimwriter,self.let,self.Turt.position())
    #physics var for falling
    self.velocity = 0
    #bind event to function
    wn.onkeypress(self.fall,self.let)

#create 5 fruits
for i in range(5):
  fruit()

def Main():
  #globalize previous time and calculate delta time
  global ptime
  t = time.time()
  dtime = abs(t-ptime)
  print(dtime)
  #go through fruits
  if len(currentfruits) > 0:
    for num,self in enumerate(currentfruits):
      #check if apple is above the death plane
      if self.Turt.ycor() > -250:
        #apply physics :)
        self.velocity -= 600 * (dtime)
        self.Turt.goto(self.Turt.xcor(),(self.Turt.ycor() + (self.velocity*(dtime))))
      else:
        #kill the fruit
        currentfruits.pop(num)
        global inuse, letters
        #return used letter from dead fruit
        letters.append(inuse.pop(inuse.index(self.let)))
        fruit() #new fruit
        del self #kill the class
  ptime = t #set the previous time for next iteration
  wn.ontimer(Main,1)

Main()

wn.listen()
wn.mainloop()