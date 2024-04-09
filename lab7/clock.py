import pygame
import sys
import time
import math

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (850, 850)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Mickey Clock")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load images
clock_image = pygame.image.load("clock.png")
clock_rect = clock_image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))

right_hand_image = pygame.image.load("right_hand.png")
left_hand_image = pygame.image.load("left_hand.png")

# Function to rotate an image
def rotate_image(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image.get_rect(center=clock_rect.center).center)
    return rotated_image, rotated_rect

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    current_time = time.localtime()
    seconds_angle = -current_time.tm_sec * 6  # 6 degrees per second
    minutes_angle = -current_time.tm_min * 6  # 6 degrees per minute

    # Rotate hands
    right_hand, right_rect = rotate_image(right_hand_image, minutes_angle)
    left_hand, left_rect = rotate_image(left_hand_image, seconds_angle)

    # Clear the screen
    window.fill(white)

    # Blit clock onto the window
    window.blit(clock_image, clock_rect)

    # Blit hands onto the window
    window.blit(right_hand, right_rect)
    window.blit(left_hand, left_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
