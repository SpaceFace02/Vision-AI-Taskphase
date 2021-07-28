import pygame
import time
import random

pygame.init()

# Snake width and height and other display params
snake_width = 10
snake_height = 10
display_width = 600
display_height = 400
snake_list = []
length_snake = 1 # Originally

# The display, (window that shows up)
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

# GLOBAL VARIABLES
score = 0

# INITIAL POSITION
x1 = 300
y1 = 200

is_game_on = True

delta_x = 0
delta_y = 0

# Food params, must be divisible by 10 to be exact on the grid
food_x = round(random.randrange(0, display_width - 5) / 10.0) * 10.0
food_y = round(random.randrange(0, display_height - 5) / 10.0) * 10.0

clock = pygame.time.Clock()

# End game on collision with walls
def end_game():
    # None defaults to pygame default font
    font_text = pygame.font.SysFont(None, 50)
    textsurface = font_text.render("You lost!!", False, (255, 0, 0))
    display.blit(textsurface, (display_width * 0.34, display_height * 0.4))
    # Updates display
    pygame.display.flip()

def check_collision(x1, y1):
    if (x1 >= 600 or x1 < 0 or y1 >= 400 or y1 < 0):
        global is_game_on
        end_game()
        clock.tick(0.8)
        is_game_on = False

# Appending the snake blocks
def draw_snake(snake_width, snake_height, snake_list):
    for element in snake_list:
        pygame.draw.rect(display, (255,255,255), (element[0], element[1], snake_width, snake_height))

def show_score(score):   
    font_text = pygame.font.SysFont(None, 30)
    textsurface = font_text.render("Your Score: " + str(score), False, (0,255,0))
    display.blit(textsurface, (display_width * 0.01, display_height * 0.03))
    # Updates display
    pygame.display.flip()

while is_game_on:
    # Handling events for quitting, keystrokes and arrow keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                delta_x = 10
                delta_y = 0
            elif event.key == pygame.K_LEFT:
                delta_x = -10
                delta_y = 0
            elif event.key == pygame.K_UP:
                delta_y = -10
                delta_x = 0
            elif event.key == pygame.K_DOWN:
                delta_y = 10
                delta_x = 0

    # Updating position, this also updates snake_element which is updates and deletes whenever length of snake remains the sname.
    x1 = x1 + delta_x
    y1 = y1 + delta_y
    
    # Checking for collision
    check_collision(x1, y1)

    display.fill((0,0,0))
    pygame.draw.rect(display, (0,0,255), (food_x, food_y, snake_width, snake_height))
    show_score(score)

    # Tuple having the x and y values, we can't use tuples as they are immutable, so we have to use lists
    snake_element = []
    snake_element.append(x1)
    snake_element.append(y1)
    snake_list.append(snake_element)

    # Deleting extra snake elements which are added everytime the loop runs, the cycle of run and delete.
    if len(snake_list) > length_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_element:
            end_game()
            is_game_on = False    

    # Width is 10, height is 10, x1 and y1 are left and top positions respectively.
    draw_snake(snake_width, snake_height, snake_list)

    pygame.display.update()
    
    # if snake eats food, then
    if x1 == food_x and y1 == food_y:
        score += 1
        food_x = round(random.randrange(0, display_width - snake_width) / 10.0) * 10.0
        food_y = round(random.randrange(0, display_height - snake_width) / 10.0) * 10.0
        length_snake += 1

    clock.tick(10)
    
pygame.quit()
quit()
 
