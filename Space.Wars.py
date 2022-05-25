import pygame
import random

class Laser:
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.h = 10
        self.w = 60
        self.color = LaserColor[laserNumber[current_color]]

    def move(self):
        self.x += 12

    def test_hit(self,x,y):
        r = Meteor_h/2
        x += r
        y += r
        r -= 5
        return (x < self.x + self.w + r) and (self.y >= y - (self.h + r)) and (x + r >= self.x) and (self.y <= y + (self.h + r))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
pygame.init()
screen_x = 1000
screen_y = 500
screen = pygame.display.set_mode((screen_x, screen_y))
ammo = 10
Random_box = random.randint(1, 1000)
done = False
is_blue = True
speed = 10
level = 1
LaserColor = {'green': (0,255,0),
'mint': (10,255,150),
'silver': (150,150,150),
'tan': (200,100,100),
'gray': (100,100,100),
'pink': (255,0,255),
'purple': (100,0,120),
'magenta': (200,10,150),
'yellow': (255,255,0),
'gold': (200,200,0),
'orange': (255,100,5),
'blue': (0,0,255),
'white': (255,255,255),
'black': (0,0,0),
'red': (255,0,0),}
current_color = 0
#laserNumber = [x for x in LaserColor.keys()]
laserNumber = ['green','mint','silver','tan','gray','pink','purple','magenta','yellow','gold','orange','blue','white','black','red',]
high_score = 500
square_x = 30.0
square_y = 30.0
Score = 0
circle_x = 960
circle_y = random.randint(130,370)
circle_r = 65
square_w = 60
square_h = 60
hearts = 10
colorTime = 0
lasers = []
Meteor_scale = 2.0
Meteor_w = int(80*Meteor_scale)
Meteor_h = int(54*Meteor_scale)
spaceship_w = 130
spaceship_h = 130
SpaceBackground_w = screen_x
SpaceBackground_h = screen_y
clock = pygame.time.Clock()
pygame.font.init() # you have to call this at the start,
SpaceshipImg = pygame.image.load('Spaceship.png')
SpaceshipImg = pygame.transform.scale(SpaceshipImg, (spaceship_w,spaceship_h ))
def Spaceship(square_x, square_y):
    screen.blit(SpaceshipImg,(square_x,square_y))
MeteorImg = pygame.image.load('Meteor.png')
MeteorImg = pygame.transform.scale(MeteorImg,(Meteor_w,Meteor_h ))
def Meteor(circle_x, circle_y):
    screen.blit(MeteorImg,(circle_x,circle_y))
SpaceBackgroundImg = pygame.image.load('SpaceBackground.jpg')
SpaceBackgroundImg = pygame.transform.scale(SpaceBackgroundImg, (SpaceBackground_w,SpaceBackground_h ))
def SpaceBackground(screen_x, screen_y):
    screen.blit(SpaceBackgroundImg,(0,0))
                       # if you want to use this module.
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if len(lasers) < ammo:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                lasers.append(Laser(screen,square_x + spaceship_w,square_y +spaceship_h/2))
    if circle_x <= 0:
        circle_y = random.randint(130,370)

    # This moves the circle across the screen
    SpaceBackground(screen_x,screen_y)
    circle_x-= speed
    if Score >= high_score:
        speed += 5
        high_score += 500
        level += 1
    colorTime -= 1
        # Move based on what the person types
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: square_y -= 15
    if pressed[pygame.K_DOWN]: square_y += 15
    if pressed[pygame.K_LEFT]: square_x -= 15
    if pressed[pygame.K_RIGHT]: square_x += 15
    if pressed[pygame.K_l] and colorTime <= 0:
        current_color += 1
        colorTime = 6
    if current_color == len(laserNumber): current_color = 0
    if square_y>370:
        square_y = 370
    if circle_x<0:
        circle_x = screen_x
    if square_x<0:
        square_x = 0
    if square_x>screen_x:
        square_x = screen_x
    if square_y<0:
        square_y = 0
    # print("Number of lives: ")
    if circle_x >= screen_x:     # Set the screen red
            hearts -= 1
    for laser in lasers:
        laser.move()
        if laser.x >= screen_x:
            lasers.remove(laser)
        elif laser.test_hit(circle_x,circle_y):
            circle_x = screen_x
            lasers.remove(laser)
            circle_y = random.randint(100, 300)
            Score += 10
        else:
            laser.draw()
    # desplay text
    myfont = pygame.font.SysFont('lobster', 50)
    textsurface = myfont.render('Ammo: %d' % (ammo - len(lasers)), False, LaserColor['red'])
    screen.blit(textsurface,(600, 40))

    myfont = pygame.font.SysFont('lobster', 50)
    textsurface = myfont.render('Level: %d' % level, False, LaserColor['red'])
    screen.blit(textsurface,(800, 40))

    myfont = pygame.font.SysFont('lobster', 50)
    textsurface = myfont.render('Color: %s' % laserNumber[current_color], False, LaserColor['red'])
    screen.blit(textsurface,(200, 450))

    myfont = pygame.font.SysFont('lobster', 50)
    textsurface = myfont.render('Hearts: %d' % hearts, False, LaserColor['red'])
    screen.blit(textsurface,(200, 40))
    if hearts < 1:
        myfont = pygame.font.SysFont('Comic Sans MS', 220)
        textsurface = myfont.render('GAME OVER', False, LaserColor['red'])
        screen.blit(textsurface,(25, 200))
        done = True
    myfont = pygame.font.SysFont('lobster', 50)
    textsurface = myfont.render('Score: %d' % Score, False, LaserColor['red'])
    screen.blit(textsurface,(380, 40))
    if is_blue: color = (255, 200, 10)
    else: color = (100, 255, 0)
    Meteor(circle_x,circle_y)
    Spaceship(square_x,square_y)
    pygame.display.flip()

    clock.tick(100)

pygame.time.wait(1000)
