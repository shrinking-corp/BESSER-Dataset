from python_code import choice_window
from python_code import cursor

def test_choice_window___init__():
    assert choice_window.__init__(choice_window('', cursor(), '\x00'), '\x00\x00', cursor(), '') == None


from python_code import cursor1

def test_cursor1___init__():
    assert cursor1.__init__(cursor1(0, 0, '', 0), 0, 0, '', 0) == None


from python_code import game_board1
from python_code import sudoku_board

def test_game_board1___init__():
    assert game_board1.__init__(game_board1(sudoku_board()), sudoku_board()) == None


from python_code import load

def test_load___init__():
    assert load.__init__(load(''), '') == None


from python_code import save

def test_save___init__():
    assert save.__init__(save(''), '') == None


from python_code import sudoku_board1

def test_sudoku_board1___init__():
    assert sudoku_board1.__init__(sudoku_board1(0, 0), 0, 0) == None


from python_code import cursor
from python_code import window

def test_window___init__():
    assert window.__init__(window('', cursor(), 0, 0, 0, 0), '', cursor(), 0, 0, 0, 0) == None

