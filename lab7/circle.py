import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Set colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set ball properties
ball_radius = 25
ball_x = (WIDTH - ball_radius * 2) // 2
ball_y = (HEIGHT - ball_radius * 2) // 2
ball_speed = 20

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - ball_speed >= 20:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_speed <= HEIGHT - ball_radius:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_speed >= 20:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_speed <= WIDTH - ball_radius:
                    ball_x += ball_speed

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
