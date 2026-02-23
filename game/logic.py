
ROWS = 6
COLS = 7

EMPTY = "."
P1 = "X"
P2 = "O"

# ---------- BOARD LOGIC ----------
def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]


def find_drop_row(board, col):
    """Gravity: returns lowest empty row in column, or None if full."""
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r
    return None


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS


def check_winner_from_cell(board, r, c, dr, dc, piece):
    """Checks 4 in a row starting at (r,c) stepping (dr,dc)."""
    for k in range(4):
        rr = r + dr * k
        cc = c + dc * k
        if not in_bounds(rr, cc) or board[rr][cc] != piece:
            return False
    return True


def is_winner(board, piece):
    dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # horiz, vert, diag, anti-diag
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != piece:
                continue
            for dr, dc in dirs:
                if check_winner_from_cell(board, r, c, dr, dc, piece):
                    return True
    return False


def is_draw(board):
    """Draw if all columns are full (top row has no EMPTY)."""
    return all(board[0][c] != EMPTY for c in range(COLS))

