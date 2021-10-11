#
# Author : Arno Theron
# ID : 19779399
#
# shrimp.py - Simulation of brine shrimp
#
# Revisions:
# 2/10/2019 - Base version for assignment
# 29/10/2019 - Final version of assignment

# Imported modules
import random
import pygame as pyg
import time
import sys

pyg.init()

# Parameter sweep variables
if len(sys.argv) < 4:
    print("Error: Not enough arguments")
    print("Using default values")
    n = 75  # Number of shrimps
    maxVel = 2  # Maximum velocity
    randDeath = 1  # Random chance of death
else:
    n = int(sys.argv[1])
    maxVel = int(sys.argv[2])
    randDeath = int(sys.argv[3])

print("\nPARAMETERS\n")
print("Number of shrimp", n)
print("Maximum velocity", maxVel)
print("Chance of death", randDeath)

# Window Setup [1]
WINX = 1200
WINY = 800
win = pyg.display.set_mode((WINX, WINY))
pyg.display.set_caption("Shrimp Simulation")

# Loads the images for the sprites used [2]
adultSpriteF = pyg.image.load(
    'Images\Adult_Female.png').convert()
eggSprite = pyg.image.load(
    'Images\Egg.png').convert()
hatchlingSprite = pyg.image.load(
    'Images\Hatchling.png').convert()
juvenileSprite = pyg.image.load(
    'Images\Juvenile.png').convert()
adultSpriteM = pyg.image.load(
    'Images\Adult_Male.png').convert()
deadSprite = pyg.image.load(
    'Images\Dead.png').convert()

clock = pyg.time.Clock()


# Creating a class to hold the attributes and function for the shrimp
class Shrimp(pyg.sprite.Sprite):
    # Initialising the attributes of the shrimp
    def __init__(self, x, y, sex):

        # Positions and velocity attributes of the shrimp
        self.x = x
        self.y = y
        self.xVel = 0
        self.yVel = 0

        # Attributes of a sprite [2]
        super().__init__()  # Initialising the inherited features
        self.image = eggSprite
        self.size = self.image.get_size()
        self.image.set_colorkey(pyg.Color("white"))

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.width = self.size[0]
        self.height = self.size[1]

        # Randomising time periods for each stage of shrimp life
        self.egg_time = random.randint(30, 250)
        self.hatchling_time = random.randint(self.egg_time + 100,
                                             self.egg_time + 2000)
        self.juvenile_time = random.randint(self.hatchling_time + 100,
                                            self.hatchling_time + 2000)
        self.adult_time = random.randint(self.juvenile_time + 100,
                                         self.juvenile_time + 2000)

        # Other attributes
        self.state = "egg"
        self.age = 0
        self.sex = sex
        self.prob = 20  # Percentage chance to change in direction
        self.cd = 0  # Cool down before reproducing

    # Defining what the console outputs when asked to print the value of
    # each shrimp
    def __str__(self):
        return self.state + "(" + str(self.x) + "," + str(self.y) + ")"

    # Creating a function to increment age of shrimp
    def ageChange(self):
        self.age += 1  # Incrementing age
        if random.randint(0, 10000) < randDeath:  # Random chance of death
            self.state = "dead"

        # Changing states according to lifetime
        elif self.state == "egg":
            if self.age > self.egg_time:
                self.state = "hatchling"

        elif self.state == "hatchling":
            if self.age > self.hatchling_time:
                self.state = "juvenile"

        elif self.state == "juvenile":
            if self.age > self.juvenile_time:
                self.state = "adult"

        elif self.state == "adult":
            if self.age > self.adult_time:
                self.state = "dead"

    # Sets a velocity based on the state of the shrimp
    def getVel(self):

        if self.state == "egg":  # Makes an egg fall
            self.xVel = 0
            self.yVel = 2

        elif self.state == "dead":  # Makes a dead shrimp float
            self.xVel = 0
            self.yVel = -2

        else:
            # Creating a random probability to change velocity
            if random.randint(0, 100) <= self.prob:
                randx = random.randint(-maxVel, maxVel)
                randy = random.randint(-maxVel, maxVel)

                self.xVel = randx
                self.yVel = randy
            self.prob = 4

    # Sets the velocity based on parameters given when called
    def setVel(self, xVel, yVel):
        self.xVel = xVel
        self.yVel = yVel

    # Sets the position based on parameters given when called
    def setPos(self, x, y):
        self.rect.center = (x, y)

    # Gets the current position of the shrimp
    def getPos(self):
        self.x = self.rect.center[0]
        self.y = self.rect.center[1]

    # Updates the position of the shrimp [1]
    def move(self):
        self.getPos()
        self.getSize()
        self.x += self.xVel
        self.y += self.yVel

        # Boundaries for the x coordinates
        if self.x < self.width/2:
            self.x = self.width/2
            self.prob = 100
        elif self.x > WINX - self.width/2:
            self. x = WINX - self.width/2
            self.prob = 100

        # Boundaries for the y coordinates
        if self. y < self.height/2:
            self.y = self.height/2
            self.prob = 100
        elif self.y > WINY - self.height/2:
            self.y = WINY - self.height/2
            self.prob = 100

        self.rect.center = (int(self.x), int(self.y))

    # Sets the image of the sprite depending on the state of the shrimp
    def getImage(self):
        if self.state == "egg":
            self.image = eggSprite

        elif self.state == "hatchling":
            self.image = hatchlingSprite

        elif self.state == "juvenile":
            self.image = juvenileSprite

        elif self.state == "adult" and self.sex == "male":
            self.image = adultSpriteM
        elif self.state == "adult" and self.sex == "female":
            self.image = adultSpriteF

        else:
            self.image = deadSprite

        # Creates a transparent background to the sprites by ignoring
        # 'white' pixels
        self.image.set_colorkey(pyg.Color("white"))

    # Creates a function to draw the hitbox of the shrimp to the screen [1]
    def hitBox(self):
        pyg.draw.rect(win, pyg.Color("red"), (self.x - self.width/2,
                                              self.y - self.height/2,
                                              self.width,
                                              self.height), 1)

    # Gets the width and height of the sprite
    def getSize(self):
        self.size = self.image.get_size()
        self.width = self.size[0]
        self.height = self.size[1]

    # Checks if a collision occurs and moves the sprite if one does [3]
    # Method taken from https://www.youtube.com/watch?v=NO31P0UvutM
    def collide(self, spriteGroup):
        if pyg.sprite.spritecollide(self, spriteGroup, False):
            self.xVel = -self.xVel
            self.yVel = -self.yVel
            self.move()

    # Creates a new egg if conditions are right for reproduction
    def rep(self, spriteGroup):
        # Checks and records collision in a list
        ls = pyg.sprite.spritecollide(self, spriteGroup, False)
        if len(ls) > 0:
            other = ls[0]
            # Checks conditions for reproduction
            if not(self.sex == other.sex) and self.state == "adult" and\
                    other.state == "adult" and self.cd == 0 and other.cd == 0:
                # Creates new egg
                if random.randint(0, 100) <= 50:
                    sex = "male"
                else:
                    sex = "female"
                egg = Shrimp(self.x, self.y - self.height, sex)
                delete = False
                # Moves egg out of collision radius of parent
                while pyg.sprite.spritecollide(egg, shrimpsGroup, False)\
                        and delete == False:
                    egg.setVel(0, 1)
                    egg.move()
                    egg.getPos()
                    if egg.y >= WINY - egg.height:
                        delete = True
                if delete == True:
                    shrimpsGroup.add(egg)
                self.cd = 60
                other.cd = 60


# Creating a function that updates the display window [1]
def redrawGameWindow():
    win.fill((70, 150, 200))  # Fills the background with RGB(70, 150, 200)
    shrimpsGroup.draw(win)  # Draws the shrimp
    pyg.display.update()  # Refreshes the display


# Creating a group that holds all the shrimps in the simulation
shrimpsGroup = pyg.sprite.Group()
a = 0
while a < n:
    # Generates sex with 50% probability of either sex
    if random.randint(0, 100) <= 50:
        sex = "male"
    else:
        sex = "female"
    shrimp = Shrimp(0, 0, sex)
    randX = random.randint(int(shrimp.size[0]/2), WINX - int(shrimp.size[0]/2))
    randY = random.randint(int(shrimp.size[1]/2), WINY - int(shrimp.size[1]/2))
    shrimp.setPos(randX, randY)
    if not pyg.sprite.spritecollideany(shrimp, shrimpsGroup):
        shrimpsGroup.add(shrimp)
        a += 1
    else:
        del shrimp


def main():
    global startTime
    global endTime

    startTime = time.time()
    endTime = 999999999

    run = True

    while run:
        # Sets the number of frames shown per second (FPS)
        clock.tick(120)

        # Updates the information of each shrimp
        for i in shrimpsGroup:
            if i.cd > 0:
                i.cd -= 1
            i.ageChange()
            i.getImage()

            # Movement of the shrimp
            i.getVel()
            i.move()

            # Runs the reproduction function
            shrimpsGroup.remove(i)
            i.rep(shrimpsGroup)
            shrimpsGroup.add(i)

            # Runs collision function [3]
            shrimpsGroup.remove(i)
            i.collide(shrimpsGroup)
            shrimpsGroup.add(i)

            # Removes dead shrimp from top of the screen
            if int(i.y) <= int(i.height)/2 and i.state == "dead":
                shrimpsGroup.remove(i)

        redrawGameWindow()

        # Records time when all shrimp are dead
        living = []
        for i in shrimpsGroup:
            if i.state != "dead":
                living.append(i)
        if len(living) == 0 and endTime > time.time():
            endTime = time.time()

        # Exits the python program if the window is closed [1]
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                run = False


# Runs the program
main()

if endTime == 999999999:
    endTime = time.time()
    print("\nThe colony still lives, after ", (endTime - startTime)*15, "days")
else:
    print("\nThe shrimp colony survived for ", (endTime - startTime), "days")

'''
References
[1] - Tech With Tim. Tech With Tim [Internet]. Finishing Touches; 
      [cited 2019 Oct 24]. Available from: 
      https://techwithtim.net/tutorials/game-development-with-python/pygame-
      tutorial/pygame-tutorial/
[2] - KidsCanCode LLC. KidsCanCode [Internet]. Pygame Lesson 1-3: More About 
      Sprites; 2019 [cited 2019 Oct 29]. Available from 
      http://kidscancode.org/blog/2016/08/pygame_1-3_more-about-sprites/ 
[3] - Brian Wilkinson. [Internet] 2019. [Video], Sprite Collision Detection 
      in Pygame; [cited  2019 Oct 29]; [6 min. 40sec.]. Available from: 
      https://www.youtube.com/watch?v=NO31P0UvutM  
'''
