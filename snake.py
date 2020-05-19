import pygame
import random

pygame.init()

#board parameters
size = 20
n = 20

display_width = size*n
display_height = size * n
gameDisplay = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()
crashed = False
black = (0,0,0)
red = (200,0,0)
white = (255,255,255)

#snake object
#if wall is hit then stop drawing snake and the game will end
def snake(x,y):
    if(x>0 and y>0 and x<display_height-2*size and y<display_width-2*size):
        pygame.draw.rect(gameDisplay,black,(x,y,size,size))
    elif(x == 0 or y == 0 or y == display_height-size or x == display_width-size):
        pygame.draw.rect(gameDisplay,white,(x,y,size,size))
        
# a function that tracks the length of the tail and 
#increments it when the snake eats an apple
#returns an array with the coordinates of the tail
def visited(arr,score):                                                                   
    temp = []
    if len(arr)>=score:
        for i in range(1,score+2):
            temp.append(arr[-i])
            pygame.draw.rect(gameDisplay,black,(arr[-i][0],arr[-i][1],size,size))
    
    return temp

#places an apple on the board
def apple(x,y):
    pygame.draw.rect(gameDisplay,red,(x,y,size,size))
               
#draws the grid for the game
def drawBoard():
    for i in range(1,30):
        
        pygame.draw.rect(gameDisplay, black,(i*n,size,1,size*(n-2)))
        pygame.draw.rect(gameDisplay, black,(size,i*n,size*(n-2),1))
        
#checks if the snake has bitten its tail
def is_gameOver():
    if(len(own_tail)>1):
        for i in range(1,len(own_tail)):
            if x == int(own_tail[i][0]) and y == int(own_tail[i][1]):
                return True
    return False

#code to be implemented later for displaying the score
def text_object(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()
def message_display(text):
    score_text = pygame.font.Font("freesansbold.ttf",24)
    TextSurf, TextRect = text_object(text, score_text)
    TextRect.center = ((size),(size))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

#initial position of the snake      
x = (display_width*0.2 )
y = (display_height*0.2)

#movement steps for the snake
#initially set to 0
dx = 0
dy = 0

#array to store previous positions
#of the snake
tail = []
score = 0

#initial position of apple
#could be set to a random number as well
appl_x = 160
appl_y = 160
while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -size
                dy = 0
            if event.key == pygame.K_RIGHT:
                dx = size
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = size
                dx = 0
            if event.key == pygame.K_UP:
                dy = -size
                dx = 0    
                
    x += dx
    y += dy
    tail.append([x,y])
    gameDisplay.fill(white)
    drawBoard()
    apple(appl_x,appl_y)
    
    #if snake eats an apple then 
    #make a new apple somewhere else
    #on the board
    if x == appl_x and y == appl_y:
        score += 1
        appl_x = size*random.randint(1,n-2)
        appl_y = size*random.randint(1,n-2)
        
    own_tail = visited(tail,score)
    
    if is_gameOver():
        print("GAME OVER")
        crashed = True
    #if boundary is hit then
    #end the game
    if x ==0 or y ==0 or y ==display_height-size or x == display_width-size:
        crashed = True
    
    print(own_tail)
    visited(tail,score)
    snake(x,y)
    pygame.display.update()
    
    clock.tick(7)
    
pygame.quit()
quit()
