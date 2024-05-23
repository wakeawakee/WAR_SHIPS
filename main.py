
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
VELOCITY = 5

#OS is used to maintain directory seperator for all devices   

#assets folder name and corresponding image you want to load

YELLOW_SPACHESHIP_IMAGE =pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))

#scaling is used to resize the image of the spaceship
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACHESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)


RED_SPACHESHIP_IMAGE =pygame.image.load(os.path.join( 'Assets','spaceship_red.png'))

RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACHESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

def draw_window(red,yellow):
    screen.fill("aqua")

    #blit ley chai surface lai screen ma halcha
    screen.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) #yellow is rectangle and x and y are corresponding values
    screen.blit(RED_SPACESHIP,(red.x,red.y)) 

    pygame.display.update()



def yellow_ship_movement(key_pressed ,yellow):
        if key_pressed[pygame.K_a]: #if a key is pressed moves to left
            yellow.x-= VELOCITY #subtracting to move towards left because the leftmost part is (0,0) in pygame
                                #so if we subtract we move towards left techincally towards (0,0)    
        if key_pressed[pygame.K_d]:#right
            yellow.x+=VELOCITY #if we add we move away from (0,0) which means towards right

        if key_pressed[pygame.K_w]: #up
            yellow.y-= VELOCITY  

        if key_pressed[pygame.K_s]: #down
            yellow.y+=VELOCITY    


def red_ship_movement(key_pressed ,red):
        if key_pressed[pygame.K_LEFT]: #if a key is pressed moves to left
            red.x-= VELOCITY #subtracting to move towards left because the leftmost part is (0,0) in pygame
                                #so if we subtract we move towards left techincally towards (0,0)    
        if key_pressed[pygame.K_RIGHT]:#right
            red.x+=VELOCITY #if we add we move away from (0,0) which means towards right

        if key_pressed[pygame.K_UP]: #up
            red.y-= VELOCITY  

        if key_pressed[pygame.K_DOWN]: #down
            red.y+=VELOCITY    



def main():
    #makes rectange of x and y dimension and spaceship width/height is wrapped around it
    red=pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow=pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)


    clock=pygame.time.Clock()  #this method helps to maintain 60 fps 
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit() 
               sys.exit()

        key_pressed=pygame.key.get_pressed()
        
        yellow_ship_movement(key_pressed,yellow)
        red_ship_movement(key_pressed,red)

        draw_window(red , yellow)
         

if __name__=="__main__" :           
     main()