import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH//COLS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill((255, 255, 255))

board = [[-1 for _ in range(COLS)] for _ in range(ROWS)]