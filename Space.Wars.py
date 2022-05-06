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
        self.x += 5

    def test_hit(self,x,y,r):
        return (x < self.x + self.w + r) and (self.y >= y - (self.h + r)) and (x + r >= self.x) and (self.y <= y + (self.h + r))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

pygame.init()

screen = pygame.display.set_mode((1000, 500))
ammo = 10
done = False
is_blue = True
square_x = 30.0
square_y = 30.0
Score = 0
circle_x = 960
circle_y = 460
circle_r = 20
square_w = 60
square_h = 60
hearts = 10
lasers = []
clock = pygame.time.Clock()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if len(lasers) < ammo:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                lasers.append(Laser(screen,square_x,square_y))
    if circle_x <= 0:
        circle_y = random.randint(50, 450)

    # This moves the circle across the screen
    circle_x -= 10
        # Move based on what the person types
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: square_y -= 10
    if pressed[pygame.K_DOWN]: square_y += 10
    if pressed[pygame.K_LEFT]: square_x -= 10
    if pressed[pygame.K_RIGHT]: square_x += 10
    if square_y>440:
        square_y = 440
    if circle_x<0:
        circle_x = 1000
    if square_x<0:
        square_x = 0
    if square_x>1000:
        square_x = 1000
    if square_y<0:
        square_y = 0

    # print("Number of lives: ")
    if circle_x == 0:     # Set the screen red
            hearts -= 1
    else:
        # Set the screen black
        screen.fill((0, 0, 0))

    for laser in lasers:
        laser.move()
        if laser.x >= 1000:
            lasers.remove(laser)
        elif laser.test_hit(circle_x,circle_y,circle_r):
            circle_x = 1000
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
    pygame.draw.rect(screen, color, pygame.Rect(square_x, square_y, 60, 60))
    white = (255, 255, 255)
    pygame.draw.circle(screen, white, (int(circle_x), int(circle_y)), 40)
    pygame.display.flip()

    clock.tick(60)

pygame.time.wait(1000)
