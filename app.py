# import pygame
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH//COLS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill((255, 255, 255))

pygame.display.set_caption("Tic Tac Toe")

board = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(WIN, (0, 0, 0), (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
            if board[row][col] != -1:
                if board[row][col] == 'O':
                    pygame.draw.circle(WIN, (0, 0, 0), (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), SQUARE_SIZE//2 - 10, 1)
                else:
                    pygame.draw.line(WIN, (0, 0, 0), (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + 10), (col * SQUARE_SIZE + SQUARE_SIZE - 10, row * SQUARE_SIZE + SQUARE_SIZE - 10), 1)
                    pygame.draw.line(WIN, (0, 0, 0), (col * SQUARE_SIZE + SQUARE_SIZE - 10, row * SQUARE_SIZE + 10), (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + SQUARE_SIZE - 10), 1)


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
    
    draw_grid()
    pygame.display.update()

pygame.quit()
