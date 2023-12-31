import pygame
from globals import SQUARE_SIZE, board, WIDTH, HEIGHT, WIN, ROWS, COLS

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(WIN, (0, 0, 0), (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
            if board[row][col] != -1:
                if board[row][col] == 'O':
                    pygame.draw.circle(WIN, (0, 0, 0), (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), SQUARE_SIZE//2 - 10, 7)
                else:
                    pygame.draw.line(WIN, (0, 0, 0), (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + 10), (col * SQUARE_SIZE + SQUARE_SIZE - 10, row * SQUARE_SIZE + SQUARE_SIZE - 10), 7)
                    pygame.draw.line(WIN, (0, 0, 0), (col * SQUARE_SIZE + SQUARE_SIZE - 10, row * SQUARE_SIZE + 10), (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + SQUARE_SIZE - 10), 7)

def draw_popup(text):
    # Create a new surface (i.e., a popup)
    popup = pygame.Surface((200, 100))  # Adjust the size as needed
    popup.fill((200, 200, 200))  # Adjust the color as needed

    # Create a font object
    font = pygame.font.Font(None, 36)  # Adjust the size as needed

    # Render the text
    text_surface = font.render(text, True, (0, 0, 0))  # Adjust the color as needed

    # Get the width and height of the text surface
    text_width, text_height = text_surface.get_size()

    # Draw the text onto the popup surface
    popup.blit(text_surface, ((200 - text_width) // 2, (100 - text_height) // 2))  # Adjust the size as needed

    # Draw the popup onto the main surface
    WIN.blit(popup, ((WIDTH - 200) // 2, (HEIGHT - 100) // 2))  # Adjust the size as needed
