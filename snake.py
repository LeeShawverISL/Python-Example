import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 15

# Load apple image
APPLE_IMAGE = pygame.image.load("apple.png")
APPLE_IMAGE = pygame.transform.scale(APPLE_IMAGE, (CELL_SIZE, CELL_SIZE))

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake and Fruit
snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = (CELL_SIZE, 0)
fruit_pos = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
             random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

# Timer
start_time = pygame.time.get_ticks()

# Font for timer and game over
font = pygame.font.SysFont(None, 35)

def draw_snake(snake):
    """Draws the snake."""
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_fruit(fruit_pos):
    """Draws the fruit."""
    screen.blit(APPLE_IMAGE, fruit_pos)

def show_timer():
    """Displays the timer."""
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    timer_surface = font.render(f"Time: {elapsed_time}s", True, WHITE)
    screen.blit(timer_surface, (10, 10))

def game_over():
    """Ends the game."""
    screen.fill(BLACK)
    game_over_surface = font.render("Game Over!", True, RED)
    screen.blit(game_over_surface, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Check for collision with fruit
    if new_head == fruit_pos:
        fruit_pos = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                     random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
    else:
        snake.pop()  # Remove the tail if no fruit eaten

    # Check for collision with walls
    if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
        new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
        game_over()

    # Check for collision with itself
    if new_head in snake[1:]:
        game_over()

    # Draw everything
    draw_snake(snake)
    draw_fruit(fruit_pos)
    show_timer()

    # Refresh screen
    pygame.display.flip()
    clock.tick(FPS)

# Write your code here :-)
