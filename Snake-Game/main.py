import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Define the display size
display_width = 600
display_height = 400

# Create the window
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game - Mahdi Mashayekhi')

# Define the snake block size
block_size = 10

# Set the clock speed
clock = pygame.time.Clock()

# Define the font for displaying the score
font = pygame.font.SysFont(None, 25)

def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [display_width/6, display_height/3])

def game_loop():
    game_exit = False
    game_over = False

    # Start the snake in the center of the screen
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    # Create the snake
    snake_list = []
    snake_length = 1

    # Generate the first goal
    goal_x = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    goal_y = round(random.randrange(0, display_height-block_size)/10.0)*10.0

    while not game_exit:

        while game_over == True:
            game_display.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Move the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # Check if the snake runs off the screen
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True

        # Update the position of the snake
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Draw the background
        game_display.fill(white)

        # Draw the goal
        pygame.draw.rect(game_display, red, [goal_x, goal_y, block_size, block_size])

        # Add the head of the snake to the snake_list
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        # Remove the tail of the snake if it gets too long
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake hits itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        # Draw the snake
        snake(block_size, snake_list)

        # Display the score
        score = str(snake_length-1)
        score_text = font.render("Score: " + score, True, black)
        game_display.blit(score_text, [0, 0])

        # Update the display
        pygame.display.update()

        # Check if the goal has been reached
        if lead_x == goal_x and lead_y == goal_y:
            goal_x = round(random.randrange(0, display_width-block_size)/10.0)*10.0
            goal_y = round(random.randrange(0, display_height-block_size)/10.0)*10.0
            snake_length += 1

        # Set the clock speed
        clock.tick(25)

    # Quit the game
    pygame.quit()
    quit()

# Start the game loop
game_loop()

