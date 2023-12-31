import pygame
from visual import draw_grid, draw_popup
from logic import game_condition
from globals import SQUARE_SIZE, board

        
def main():
    pygame.init()
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()

    run = True
    current_player = 1

    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")
    players = {1: player1, -1: player2}
    
    while run:
        clock.tick(10)
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

        winner = game_condition()
        if winner != -1 and winner != -2:
            if winner == 'O':
                winner = 1
            else:
                winner = 2
            draw_popup(f"{players[current_player]} wins!")
            pygame.display.update()
            pygame.time.wait(2500)  # Wait for 2 seconds
            run = False
        elif winner == -2:
            draw_popup("It's a tie!")
            pygame.display.update()
            pygame.time.wait(2500)
            run = False

        print(f"It's {players[current_player]}'s turn.")

    pygame.quit()

if __name__ == '__main__':
    main()