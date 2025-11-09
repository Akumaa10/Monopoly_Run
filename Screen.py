import pygame
import pygame_gui
import random

moneybase = 10
playermoney = 10000
spaces = 32
currentspace = 1
buffs = {"doubledice":False}
properties = {1:"brown_1", 2: "brown_2", 6: "light_blue_1", 7: "light_blue_2", 9:"pink_1", 11:"pink_2", 14:"orange_1", 15:"orange_2", 17:"red_1", 19:"red_2", 21:"yellow_1",22:"yellow_2", 25: "green_1", 26:"green_2", 30:"dark blue_1", 31:"dark_blue_2" }
properties_names = {
    "brown": ["brown1", "brown2"],
    "light_blue": ["light_blue1", "light_blue2"],
    "pink": ["pink1", "pink2"], 
    "orange": ["orange1", "orange2"], 
    "red": ["red1", "red2"], 
    "yellow":["yellow1", "yellow2"], 
    "green":["green1", "green2"], 
    "dark_blue":["dark_blue1", "dark_blue2"]
    }
propertymulti = {"brown": 10, "light_blue":20, "pink":30, "orange":40, "red":50, "yellow":60, "green":70, "dark_blue":80}
owned_spaces = {"brown":0, "light_blue":0, "pink":0, "orange":0, "red":0, "yellow":0, "green":0, "dark_blue":0}
spaces_prices = {"brown":60, "light_blue": 100, "pink": 140, "orange": 200, "red":250, "yellow":260, "green": 300, "dark_blue":400}

def getmoneymulti():
    total = 0
    for color in owned_spaces:
        total += owned_spaces[color] * propertymulti[color]
    return total

def collecttuituion():
    total = 0
    for color in owned_spaces:
        total += owned_spaces[color] * propertymulti[color]
    return total

#checks if player lands on property and if a popup should be triggered
def landedonproperty():
    global currentspace
    global playermoney
    if currentspace in properties:
        color = properties[currentspace]
        price = spaces_prices[color]
        if playermoney >= price:
            return True
    return False

def rolldice():
    global currentspace
    global playermoney

    roll1 = random.randint(1,6)
    roll2 = 0
    if buffs["doubledice"]:
        roll2 = random.randint(1,6)
    currentspace += roll1 + roll2
    playermoney += (roll1 + roll2) * moneybase
    landedonproperty()
    print(currentspace, "Current space")
    if currentspace > 40:
        currentspace %= 40
        playermoney += 200 + collecttuituion()



def checkmouseclick(x,y):
    if y < 638:
        rolldice()
        return
    #add functionality for navbar buttons here


    return



pygame.init()
SCREEN_W, SCREEN_H = 400, 719
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
navbar = pygame.image.load("images/Rectangle_1.png").convert_alpha()
screen.fill((255, 255, 255))
navbar = pygame.transform.scale(navbar, (SCREEN_W, 100))

clickarea = ((0,700), (400, 100))

running = True
while running:
    screen.blit(navbar, (0, 638))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coord = event.pos
            checkmouseclick(coord[0], coord[1])
    pygame.display.flip()
pygame.quit()
