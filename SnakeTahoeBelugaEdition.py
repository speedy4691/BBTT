import pygame
import time
import random
import pickle

pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 1000
dis_height = 800
map_width = 200
map_height =560
map_width0 =420
map_height0 =135
map_width1 =310
map_height1 =250
map_height2 =215

delay=750

try:
    with open('score.dat', 'rb') as file:
        score = pickle.load(file)
except:
        score = 0
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Tahoe Belugas')
 
clock = pygame.time.Clock()
 
snake_block = 25
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Belugas Brought Back To Tahoe: " + str(score), True, black)
    dis.blit(value, [240, 0])
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        player_image = pygame.image.load("beluga.png").convert_alpha()
        player_rect = player_image.get_rect(center = (x[0], x[1]))
        dis.blit(player_image,player_rect)
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 15, dis_height / 2])
 
 
def gameLoop():
    game_over = False
    game_close = False
    x1 = (map_width+400-17+map_width0) / 2
    y1 = (map_height+20+map_height0) / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
    
    foodx = round(random.randrange(map_width0+10, map_width+map_width0-20)/ 10 )*10
    foody = round(random.randrange(map_height0+20, map_height+map_height0-10) / 10 )*10
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            if score < Length_of_snake - 1: 
                with open('score.dat', 'wb') as file:
                    pickle.dump(Length_of_snake - 1, file)
            End_Message1_1 =score_font.render("You Lost!", True, black)
            dis.blit(End_Message1_1, [160, 100])
            End_Message1_2 =score_font.render("Better Go Buy Some BBTT swag", True, yellow)
            dis.blit(End_Message1_2, [335, 100])
            End_Message2= score_font.render("Belugas Brought Back to Tahoe = " + str(Length_of_snake - 1), True, black)
            dis.blit(End_Message2, [215, 200])
            End_Message3 =score_font.render("Space - Play Again or ESC - Quit", True, black)
            dis.blit(End_Message3, [230, 300])
            with open('score.dat', 'rb') as file:
                Top = pickle.load(file)
            End_Message4= score_font.render("Local Highscore = " + str(Top), True, black)
            dis.blit(End_Message4, [330, 400])

            End_Message5 =score_font.render("Global Highscores", True, black)
            dis.blit(End_Message5, [50, 500])
            Website_image = pygame.image.load("Snake Tahoe.png").convert_alpha()
            Website_rect = Website_image.get_rect(center = (200, 650))
            dis.blit(Website_image,Website_rect)
            End_Message6 =score_font.render("DM Highscore Here", True, black)
            dis.blit(End_Message6, [625, 500])
            IG_image = pygame.image.load("IG.png").convert_alpha()
            IG_rect = IG_image.get_rect(center = (800, 650))
            dis.blit(IG_image,IG_rect)
            End_Message7= score_font.render("V1.1", True, black)
            dis.blit(End_Message7, [465, 620])

            pygame.display.update()
            
            
            
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()
                        
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

                    
        if x1 < map_width0 and y1 >= map_height2+map_height1:
            pygame.time.delay(delay)
            game_close = True
        if x1 < map_width0 and y1 < map_height1:
            pygame.time.delay(delay)
            game_close = True
        if x1 >= map_width+map_width0 :
            pygame.time.delay(delay)
            game_close = True
        if x1 < map_width1:
            pygame.time.delay(delay)
            game_close = True
        if y1 < map_height0:
            pygame.time.delay(delay)
            game_close = True
        if y1 >= map_height0+map_height:
            pygame.time.delay(delay)
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        Tahoe_map = pygame.image.load("Tahoe_Map2.png").convert_alpha()
        Tahoe_rect = Tahoe_map.get_rect(center = (dis_width / 2, dis_height / 2))
        dis.blit(Tahoe_map,Tahoe_rect)
       
        fish_image = pygame.image.load("Fish.png").convert_alpha()
        fish_rect = fish_image.get_rect(center = (foodx, foody))
        dis.blit(fish_image,fish_rect)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:

                pygame.time.delay(delay)
                game_close = True
                
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        our_snake(snake_block, snake_List)
        snake_speed = 10 + 1*Length_of_snake
 
        pygame.display.update()
 
        if (x1 <= foodx + 15 and x1 >= foodx - 15) and (y1 <= foody + 15 and y1 >= foody - 15):
            Random=random.randint(1,10)
            if Random == 10:
                #foodx = round(random.randrange(map_width1+20, map_width+map_width0-20)/ 10 )*10
                #foody = round(random.randrange(map_height1+20, map_height2+map_height1-20) / 10 )*10
                foodx = round(random.randrange(map_width1+20, map_width0-20)/ 10 )*10
                foody = round(random.randrange(map_height1+20, map_height2+map_height1-20) / 10 )*10
            else:
                #foodx = round(random.randrange(map_width0+10, map_width+map_width0-20)/ 10 )*10
                #foody = round(random.randrange(map_height0+20, map_height+map_height0-10) / 10 )*10
                foodx = round(random.randrange(map_width0+10, map_width+map_width0-20)/ 10 )*10
                foody = round(random.randrange(map_height0+20, map_height+map_height0-10) / 10 )*10
            Length_of_snake += 1
            snake_speed = 10 + 1*Length_of_snake
 
         
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop() 
