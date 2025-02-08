import pygame 
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minecraft Demo")

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
BROWN = (139, 69, 19)

# Block settings
block_size = 50
blocks = [(WIDTH//2, HEIGHT//2)]  # Initial block position

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            x, y = blocks[-1]
            if event.key == K_LEFT:
                blocks.append((x - block_size, y))
            elif event.key == K_RIGHT:
                blocks.append((x + block_size, y))
            elif event.key == K_UP:
                blocks.append((x, y - block_size))
            elif event.key == K_DOWN:
                blocks.append((x, y + block_size))
    
    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, BROWN, (block[0], block[1], block_size, block_size))
    
    pygame.display.flip()
    
pygame.quit()
