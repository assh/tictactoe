# import pygame
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH//COLS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

board = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

run = True
current_player = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE
            if board[row][col] == -1:
                if current_player == 1:
                    board[row][col] = 'O'                   
                else:
                    board[row][col] = 'X'
                current_player = current_player * -1

pygame.quit()
