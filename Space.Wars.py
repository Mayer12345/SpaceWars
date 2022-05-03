import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1000, 500))
done = False
is_blue = True
square_x = 30.0
square_y = 30.0
circle_x = 960
circle_y = 460
circle_r = 20
square_w = 60
square_h = 60
hearts = 10
laser_x = 60
laser_y = 60
laser_w = 10
laser_h = 10
laser_draw = False
clock = pygame.time.Clock()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
if laser_x > 1000:
    laser_draw = False
green = ((0, 255, 0))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            laser_draw = True
            laser_x = square_x
            laser_y = square_y
    if circle_x <= 0:
        circle_y = random.randint(0, 500)

    laser_x += 5
    # This moves the circle across the screen
    circle_x -= 5
        # Move based on what the person types
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: square_y -= 10
    if pressed[pygame.K_DOWN]: square_y += 10
    if pressed[pygame.K_LEFT]: square_x -= 10
    if pressed[pygame.K_RIGHT]: square_x += 10
    if laser_draw == True:
        if (circle_x < laser_x + laser_w + circle_r) and (laser_y >= circle_y - (laser_h + circle_r)) and (circle_x + circle_r >= laser_x):
            circle_x = 1000
            laser_draw = False
            circle_y = random.randint(10, 490)
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
    # Check if the circle hits the square

    # print("Number of lives: ")
    if circle_x == 0:     # Set the screen red
            hearts -= 1
    else:
        # Set the screen blue
        screen.fill((0, 0, 0))
    # desplay text
    myfont = pygame.font.SysFont('lobster', 50)
    textsurface = myfont.render('Hearts: %d' % hearts, False, (255, 100, 10))
    screen.blit(textsurface,(200, 40))
    if hearts < 1:
        myfont = pygame.font.SysFont('Comic Sans MS', 220)
        textsurface = myfont.render('GAME OVER', False, (255, 0, 0))
        screen.blit(textsurface,(25, 200))
        done = True
    if laser_x == 1000:
        laser_draw = False
    if laser_draw == True:
        pygame.draw.rect(screen, green, pygame.Rect(laser_x, laser_y, 60, 10))
    if is_blue: color = (255, 200, 10)
    else: color = (100, 255, 0)
    pygame.draw.rect(screen, color, pygame.Rect(square_x, square_y, 60, 60))
    white = (255, 255, 255)
    pygame.draw.circle(screen, white, (int(circle_x), int(circle_y)), 40)
    pygame.display.flip()

    clock.tick(60)

pygame.time.wait(1000)
