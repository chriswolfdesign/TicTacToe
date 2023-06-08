import pygame

from model.cli_game import CLIGame

FG = (255, 255, 255)
BG = (0, 0, 0)
SQUARE_COLOR = (255, 255, 255)
RECT_SIDE = 140

if __name__ == "__main__":
    game = CLIGame()

    pygame.init()
    pygame.display.set_caption("Play Tic-Tac-Toe!")

    screen = pygame.display.set_mode([1000, 1000])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render(f"Current Player: {game.current_player.player_char.value}", True, FG, BG)
        text_rect = text.get_rect()
        text_rect.center = (450, 100)
        screen.blit(text, text_rect)

        rects = [
                pygame.Rect(250, 200, RECT_SIDE, RECT_SIDE),
                pygame.Rect(400, 200, RECT_SIDE, RECT_SIDE),
                pygame.Rect(550, 200, RECT_SIDE, RECT_SIDE),
                pygame.Rect(250, 350, RECT_SIDE, RECT_SIDE),
                pygame.Rect(400, 350, RECT_SIDE, RECT_SIDE),
                pygame.Rect(550, 350, RECT_SIDE, RECT_SIDE)
        ]

        for rect in rects:
            pygame.draw.rect(screen, SQUARE_COLOR, rect)

        pygame.display.flip()

    pygame.quit()
