import random
import time

import pygame

#Initializes the pygame module
pygame.init()

#Sets the display of the screen
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height)) #(Width, Height)
pygame.display.update()

#The Caption you see on the top right of the window
pygame.display.set_caption("Test Snake Game")

#Variables
green = (0, 204, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (50, 153, 213)


#Makes the whole game run slower (Its wonky without this, like real fucking wonky)
frame_rate = pygame.time.Clock()
speed = 25

font = pygame.font.SysFont(None, 30)
def message(msg):
    text = font.render(msg, True, red)
    display.blit(text, [250, 250])

def score(score):
    value = font.render("Score: " + str(score), True, red)
    display.blit(value, [0, 0])

def player(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, white, [x[0], x[1], snake_block, snake_block])

def game_loop():

    #While loop control
    game_over = False
    game_close = False

    #Player Variables
    player_change_x = 0
    player_change_y = 0
    player_x = display_width / 2
    player_y = display_height / 2
    snake_block = 10

    snake_list = []
    snake_length = 1

    #Fruit Variables
    food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    fruit_width = 10
    fruit_height = 10

    while game_over != True:

        #Quit/Retry Loop
        while game_close == True:
            display.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again")
            #score(snake_list - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        #Main Game Loop
        for event in pygame.event.get():

            #Quit Function
            if event.type == pygame.QUIT:
                game_over = True

            #Player controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_change_x = 0
                    player_change_y = 10
                elif event.key == pygame.K_UP:
                    player_change_x = 0
                    player_change_y = -10
                elif event.key == pygame.K_RIGHT:
                    player_change_x = 10
                    player_change_y = 0
                elif event.key == pygame.K_LEFT:
                    player_change_x = -10
                    player_change_y = 0
            """
            elif event.type == pygame.KEYUP:
                player_change_x = 0
                player_change_y = 0
            """

        if player_x >= display_width or player_x < 0 or player_y >= display_height or player_y < 0:
            game_close = True

        player_x = player_x + player_change_x
        player_y = player_y + player_change_y

        #Sets screen to chosen color
        display.fill(blue)

        #Draw the snake head (Rectangle)
        #pygame.draw.rect(display, blue, [player_x, player_y, snake_block, snake_block]) #[x_position, y_position, element_width, element_height]
        pygame.draw.rect(display, green, [food_x, food_y, fruit_width, fruit_height])

        #Initialize the snake head, and body.
        snake_head = []
        snake_head.append(player_x)
        snake_head.append(player_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        #If snake bites its own body, you lose.
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        player(snake_block, snake_list)
        score(snake_length - 1)

        #Updates the screen (Always at the end of the loop)
        pygame.display.update()

        #Check if recording
        if player_x == food_x and player_y == food_y:
            #print("Point")
            food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            snake_length = snake_length + 1

        #frame rate
        frame_rate.tick(speed)

    #Game Over Display
    #message("Game Over")

    pygame.quit()
    quit()

game_loop()

pygame.display.update()
time.sleep(2)