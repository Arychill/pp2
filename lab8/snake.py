import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = (1, 0)

    def move(self):
        # Move the snake by adding a new head and removing the tail
        head = (self.body[0][0] + self.direction[0] * GRID_SIZE, self.body[0][1] + self.direction[1] * GRID_SIZE)
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        # Increase snake length by adding a new head without removing the tail
        head = (self.body[0][0] + self.direction[0] * GRID_SIZE, self.body[0][1] + self.direction[1] * GRID_SIZE)
        self.body.insert(0, head)

    def draw(self, surface):
        # Draw snake
        for segment in self.body:
            pygame.draw.rect(surface, BLACK, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    def check_collision(self):
        # Check if snake collides with itself or the border
        if (self.body[0][0] < 0 or self.body[0][0] >= WIDTH or
                self.body[0][1] < 0 or self.body[0][1] >= HEIGHT):
            return True
        for segment in self.body[1:]:
            if self.body[0] == segment:
                return True
        return False

# Food class
class Food:
    def __init__(self):
        self.position = self.generate_food_position()

    def generate_food_position(self):
        # Generate random position for food
        while True:
            x = random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE
            y = random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE
            if (x, y) not in snake.body:
                return (x, y)

    def draw(self, surface):
        # Draw food
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Main function
def main():
    global SPEED  # Declare SPEED as a global variable
    SPEED = 10  # Initial speed
    # Initialize screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Initialize font for displaying text
    font = pygame.font.Font(None, 36)

    # Initialize game objects
    global snake
    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()
    score = 0
    level = 1

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        # Move snake
        snake.move()

        # Check collision with food
        if snake.body[0] == food.position:
            snake.grow()
            food.position = food.generate_food_position()
            score += 1
            if score % 3 == 0:
                level += 1
                SPEED += 3
                pygame.display.set_caption(f"Snake Game - Level {level}")

        # Check collision with border or itself
        if snake.check_collision():
            print("Game Over! Your score:", score)
            pygame.quit()
            quit()

        # Draw everything
        screen.fill(WHITE)
        # Draw score and level text
        score_text = font.render(f"Score: {score}", True, BLACK)
        level_text = font.render(f"Level: {level}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()

        # Control game speed
        clock.tick(SPEED)

if __name__ == "__main__":
    main()
