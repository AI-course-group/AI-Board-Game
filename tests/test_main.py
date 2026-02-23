import pytest

# change this import to match your actual module
from game.main import Gongalonga


def test_gongalonga_returns_expected_value():
    result = Gongalonga()
    # replace with what it SHOULD return
    assert result is "Hello, World!"


def test_gongalonga_type():
    result = Gongalonga()
    # example: ensure it returns a string (change if needed)
    assert isinstance(result, str)


#def test_gongalonga_specific_case():
    # if Gongalonga takes arguments, example:
    # assert Gongalonga(2, 3) == 5

    # placeholder so pytest doesn't complain
    #assert Gongalonga() == Gongalonga() 