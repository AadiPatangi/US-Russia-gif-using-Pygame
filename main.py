import pygame, sys
from pygame.locals import *
import time


pygame.init()#initialize the pygame module

screen = pygame.display.set_mode((500,500))

#colors
GRAY = (211, 211, 211)
YELLOW = (255, 204, 0)
LIGHT_YELLOW = (255,255,102)

DARK_BLUE = (0, 0, 200)
LIGHT_BLUE = (173, 216, 230)

GREEN = (1, 50, 32)
LIGHT_GREEN = (76, 187, 23)
RED = (255, 0, 0)
WHITE = (255,255,255)
ORANGE = (255,180,0)
BLUE = (0,0,255)

BROWN = (101, 67, 33)
arrow = "up"
fontObj = pygame.font.Font('freesansbold.ttf', 90)
textDay = fontObj.render("RUSSIA", True, RED, LIGHT_BLUE)
textNight = fontObj.render("HI",True, GREEN, LIGHT_BLUE)
textPos = textDay.get_rect()
textPos.center = (250, 200)
fontObj = pygame.font.Font('freesansbold.ttf', 90)

fontObj2 = pygame.font.Font('freesansbold.ttf', 32)
textROCKET = fontObj.render("Day", True, RED, DARK_BLUE)
textPos2 = textROCKET.get_rect()
textPos2.center = (450, 150)






textROCKET = fontObj.render("SPUTNIK 1", True, GRAY, LIGHT_BLUE)
fontObj = pygame.font.Font('freesansbold.ttf', 17)
textROCKET = fontObj.render("SPUTNIK 1", True, GRAY, LIGHT_BLUE)
textPos1 = textDay.get_rect()
textPos1.center = (250, 50)

textNight =  fontObj.render("Night", True, RED, DARK_BLUE)
textNightPos = textNight.get_rect()
textNightPos.center = (250, 50)


textNight =  fontObj.render(" AMERICA", True, GRAY, GREEN)
textNightPos = textNight.get_rect()
textNightPos.center = (500, 50)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()        
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                arrow = "up"
            elif event.key == K_DOWN:
                arrow = "down"


    if arrow == "up":
        screen.fill(LIGHT_BLUE)
        pygame.draw.rect(screen, BROWN, [360, 400, 30, 45])
        pygame.draw.polygon(screen, LIGHT_GREEN, [[450, 400], [375, 250], [300, 400]])
        pygame.draw.polygon(screen, LIGHT_GREEN, [[440, 350], [375, 230], [310, 350]])
        pygame.draw.circle(screen, YELLOW, (125, 125), 75, 0)
        screen.blit(textDay, textPos)
        pygame.draw.rect(screen ,WHITE,[200,50,5,40])
        pygame.draw.rect(screen,DARK_BLUE,[200,50,40,5])
        pygame.draw.rect(screen,RED,[200,55,40,5])
        pygame.draw.rect(screen,DARK_BLUE,[200,60,40,5])
        pygame.draw.rect(screen,RED,[200,65,40,5])
        pygame.draw.rect(screen,YELLOW,[375,40,90,90])
        pygame.draw.polygon(screen,RED,[[377, 40],[500,40],[400,10]])
        pygame.draw.rect(screen,ORANGE,[377,130,15,60])
        pygame.draw.rect(screen,ORANGE,[400,130,15,60])
        pygame.draw.rect(screen,ORANGE,[420,130,15,60])
        pygame.draw.rect(screen,ORANGE,[440,130,15,60])
        screen.blit(textROCKET, textPos2)



        

        



    pygame.display.update()


    if arrow == "down":
        screen.fill(WHITE)
        pygame.draw.rect(screen, BROWN, [360, 400, 30, 45])
        pygame.draw.polygon(screen, GREEN, [[450, 400], [375, 250], [300, 400]])
        pygame.draw.polygon(screen, GREEN, [[440, 350], [375, 230], [310, 350]])
        pygame.draw.rect(screen, GRAY, [150, 390, 10, 60])
        pygame.draw.rect(screen, BLUE, [155, 390, 60, 10])
        pygame.draw.rect(screen, RED, [155, 400, 60, 10])
        pygame.draw.rect(screen, BLUE, [155, 410, 60, 10])
        pygame.draw.rect(screen, RED, [155, 420, 60, 10])



    
    
    pygame.display.update()

