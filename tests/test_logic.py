import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from game.logic import (
    ROWS, COLS, EMPTY, P1, P2,
    create_board, find_drop_row, drop_piece,
    is_winner, is_draw
)


# Helper function to simulate real moves
def drop(board, col, piece):
    row = find_drop_row(board, col)
    assert row is not None
    drop_piece(board, row, col, piece)
    return row


# ---------- Board creation ----------
def test_board_is_empty_and_correct_size():
    board = create_board()

    assert len(board) == ROWS
    assert all(len(r) == COLS for r in board)
    assert all(cell == EMPTY for row in board for cell in row)


# ---------- Gravity ----------
def test_drop_goes_to_bottom():
    board = create_board()
    row = drop(board, 0, P1)
    assert row == ROWS - 1


def test_drop_stacks():
    board = create_board()
    r1 = drop(board, 0, P1)
    r2 = drop(board, 0, P2)

    assert r1 == ROWS - 1
    assert r2 == ROWS - 2


def test_column_full_returns_none():
    board = create_board()

    for _ in range(ROWS):
        drop(board, 1, P1)

    assert find_drop_row(board, 1) is None


# ---------- Wins ----------
def test_horizontal_win():
    board = create_board()
    for c in range(4):
        drop(board, c, P1)

    assert is_winner(board, P1)


def test_vertical_win():
    board = create_board()
    for _ in range(4):
        drop(board, 2, P2)

    assert is_winner(board, P2)


def test_diagonal_win():
    board = create_board()

    # build diagonal \
    drop(board, 0, P1)

    drop(board, 1, P2)
    drop(board, 1, P1)

    drop(board, 2, P2)
    drop(board, 2, P2)
    drop(board, 2, P1)

    drop(board, 3, P2)
    drop(board, 3, P2)
    drop(board, 3, P2)
    drop(board, 3, P1)

    assert is_winner(board, P1)


def test_not_winner_with_three():
    board = create_board()
    for c in range(3):
        drop(board, c, P1)

    assert not is_winner(board, P1)


# ---------- Draw ----------
def test_not_draw_on_empty_board():
    board = create_board()
    assert not is_draw(board)