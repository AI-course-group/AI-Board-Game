import pygame
import sys

from game.logic import (
    ROWS, COLS, P1, P2,
    create_board, find_drop_row, drop_piece, is_winner, is_draw
)
# ---------- UI SETTINGS ----------
CELL = 100
WIDTH = COLS * CELL
HEIGHT = (ROWS + 1) * CELL  # extra row at top for hover / text

BLUE = (30, 60, 200)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
YELLOW = (240, 220, 70)
WHITE = (255, 255, 255)

# ---------- GAME STATE / RESET ----------
def reset_game():
    """Return a fresh game state."""
    state = {
        "board": create_board(),
        "current": P1,
        "game_over": False,
        "winner_text": "",
        "hover_col": None,
    }
    return state


# ---------- INPUT / UPDATE ----------
def handle_input(state, event):
    """Handle a single pygame event and mutate state accordingly."""
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.MOUSEMOTION:
        state["hover_col"] = event.pos[0] // CELL

    if event.type == pygame.KEYDOWN:
        # Press R to restart anytime
        if event.key == pygame.K_r:
            state.update(reset_game())
            return

    if event.type == pygame.MOUSEBUTTONDOWN and not state["game_over"]:
        col = event.pos[0] // CELL
        if not (0 <= col < COLS):
            return

        board = state["board"]
        row = find_drop_row(board, col)
        if row is None:
            return  # column full

        current = state["current"]
        drop_piece(board, row, col, current)

        if is_winner(board, current):
            state["game_over"] = True
            state["winner_text"] = f"{current} wins! (Press R to restart)"
        elif is_draw(board):
            state["game_over"] = True
            state["winner_text"] = "Draw! (Press R to restart)"
        else:
            state["current"] = P2 if current == P1 else P1


def update_game(state, dt):
    """Game update step (useful later for animations)."""
    # For now, nothing time-based. This is here so your structure scales cleanly.
    pass


# ---------- DRAW ----------
def draw_game(screen, font, state):
    screen.fill(BLACK)

    board = state["board"]
    current = state["current"]
    hover_col = state["hover_col"]

    # Top bar: hover disc or winner text
    if state["game_over"]:
        text = font.render(state["winner_text"], True, WHITE)
        screen.blit(text, (20, 20))
    else:
        if hover_col is not None and 0 <= hover_col < COLS:
            color = RED if current == P1 else YELLOW
            pygame.draw.circle(
                screen,
                color,
                (hover_col * CELL + CELL // 2, CELL // 2),
                CELL // 2 - 8,
            )

        turn_text = font.render(f"Turn: {current} (R to restart)", True, WHITE)
        screen.blit(turn_text, (20, 20))

    # Draw board grid + discs
    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL
            y = (r + 1) * CELL  # shifted down by 1 row

            pygame.draw.rect(screen, BLUE, (x, y, CELL, CELL))

            piece = board[r][c]
            if piece == P1:
                color = RED
            elif piece == P2:
                color = YELLOW
            else:
                color = BLACK

            pygame.draw.circle(
                screen,
                color,
                (x + CELL // 2, y + CELL // 2),
                CELL // 2 - 8,
            )

    pygame.display.flip()

# ---------- MAIN ----------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connect 4")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)

    state = reset_game()

    while True:
        dt = clock.tick(60) / 1000.0  # seconds since last frame

        for event in pygame.event.get():
            handle_input(state, event)

        update_game(state, dt)
        draw_game(screen, font, state)


if __name__ == "__main__":
    main()