
import pygame 
import sys
import os

#initilize the pygame
pygame.init()

WIDTH,HEIGHT =900,500

#setup display
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GAME")


SPACESHIP_WIDTH ,SPACESHIP_HEIGHT =60,40

FPS=60 #controling speed of while loop using clock tick


#OS is used to maintain directory seperator for all devices   

#assets folder name and corresponding image you want to load

YELLOW_SPACHESHIP_IMAGE =pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))

#scaling is used to resize the image of the spaceship
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACHESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)


RED_SPACHESHIP_IMAGE =pygame.image.load(os.path.join( 'Assets','spaceship_red.png'))

RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACHESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

def draw_window():

    screen.fill("aqua")
    screen.blit(YELLOW_SPACESHIP,(100,100)) #blit ley chai surface lai screen ma halcha
    screen.blit(RED_SPACESHIP,(800,100)) 

    pygame.display.update()



def main():
    clock=pygame.time.Clock()  #this helps to maintain 60 fps 
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit() 
               sys.exit()


    
        draw_window()


if __name__=="__main__" :           
     main()