from python_code import ChessGameController

def test_ChessGameController___init__():
    assert ChessGameController.__init__(ChessGameController('', '\x00'), '\x00\x00', '') == None

from python_code import ChessBoard
from python_code import Piece

def test_Piece___init__():
    assert Piece.__init__(Piece('', chessBoard1=ChessBoard()), '', chessBoard1=ChessBoard()) == None

from python_code import Position

def test_Position___init__():
    assert Position.__init__(Position(0, 0), 0, 0) == None

from python_code import ChessBoard
from python_code import Piece
from python_code import Position
from python_code import Square

def test_Square___init__():
    assert Square.__init__(Square(Position(0, 0), Piece('\x00\x00', chessBoard1=ChessBoard())), Position(0, 0), Piece('', chessBoard1=ChessBoard())) == None
