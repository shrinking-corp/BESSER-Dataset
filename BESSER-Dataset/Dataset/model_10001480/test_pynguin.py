#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    Bishop,
    BoardValidator,
    BoardValidatorInterface_Interface,
    BoardView,
    BoardViewInterface_Interface,
    ChessBoard,
    ChessBoardInterface_Interface,
    ChessGame,
    ChessGameController,
    Enum,
    King,
    Knigh,
    Pawn,
    Piece,
    PieceType,
    Player,
    Position,
    Queen,
    Rook,
    Square,
    annotations,
    color,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.Piece(attribute="s-i\\7RH@Ylede4a")


def test_1():
    var_22 = python_code_.Piece(attribute=set(), chessBoard1=True)
    assert isinstance(var_22, python_code_.Piece)


def test_2():
    python_code_.Pawn()


def test_3():
    python_code_.ChessGameController(
        attribute=complex(2271.9, -2505.0), attribute2="ChessBoard"
    )


def test_4():
    python_code_.Position(x=707, y=-695)


def test_5():
    python_code_.Square(position=-1375.8, piece=True)
