import pygame
import random

class Laser:
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.h = 10
        self.w = 60
        self.color = ((0, 255, 0))

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
screen_x = 500
screen_y = 1000
screen = pygame.display.set_mode((screen_y, screen_x))
ammo = 10
Random_box = random.randint(1, 1000)
done = False
is_blue = True
speed = 10
level = 1
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
lasers = []
Meteor_scale = 2.0
Meteor_w = int(80*Meteor_scale)
Meteor_h = int(54*Meteor_scale)
spaceship_w = 130
spaceship_h = 130
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
    circle_x-= speed
    if Score >= high_score:
        speed += 5
        high_score += 500
        level += 1
        # Move based on what the person types
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: square_y -= 15
    if pressed[pygame.K_DOWN]: square_y += 15
    if pressed[pygame.K_LEFT]: square_x -= 15
    if pressed[pygame.K_RIGHT]: square_x += 15
    if square_y>370:
        square_y = 370
    if circle_x<0:
        circle_x = screen_y
    if square_x<0:
        square_x = 0
    if square_x>screen_y:
        square_x = screen_y
    if square_y<0:
        square_y = 0
    # print("Number of lives: ")
    if circle_x >= screen_y:     # Set the screen red
            hearts -= 1
    else:
        # Set the screen black
        screen.fill((0, 0, 0))
    for laser in lasers:
        laser.move()
        if laser.x >= screen_y:
            lasers.remove(laser)
        elif laser.test_hit(circle_x,circle_y):
            circle_x = screen_y
            lasers.remove(laser)
            circle_y = random.randint(100, 300)
            Score += 10
        else:
            laser.draw()
    # desplay text
    myfont = pygame.font.SysFont('lobster', 50)
    textsurface = myfont.render('Ammo: %d' % (ammo - len(lasers)), False, (255, 100, 10))
    screen.blit(textsurface,(600, 40))

    myfont = pygame.font.SysFont('lobster', 50)
    textsurface = myfont.render('Level: %d' % level, False, (255, 100, 10))
    screen.blit(textsurface,(800, 40))

    myfont = pygame.font.SysFont('lobster', 50)
    textsurface = myfont.render('Hearts: %d' % hearts, False, (255, 100, 10))
    screen.blit(textsurface,(200, 40))
    if hearts < 1:
        myfont = pygame.font.SysFont('Comic Sans MS', 220)
        textsurface = myfont.render('GAME OVER', False, (255, 0, 0))
        screen.blit(textsurface,(25, 200))
        done = True
    myfont = pygame.font.SysFont('lobster', 50)
    textsurface = myfont.render('Score: %d' % Score, False, (255, 100, 10))
    screen.blit(textsurface,(380, 40))
    if is_blue: color = (255, 200, 10)
    else: color = (100, 255, 0)
    white = (255, 255, 255)
    Meteor(circle_x,circle_y)
    Spaceship(square_x,square_y)
    pygame.display.flip()

    clock.tick(100)

pygame.time.wait(1000)
