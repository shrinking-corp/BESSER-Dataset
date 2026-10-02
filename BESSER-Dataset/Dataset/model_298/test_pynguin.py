#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    BookCategory,
    Enum,
    date,
    datetime,
    library_Book,
    library_Library,
    library_Writer,
    time,
)


def test_0():
    var_10 = python_code_.library_Library(name="v", library_Library=set())
    assert isinstance(var_10, python_code_.library_Library)


def test_1():
    var_10 = python_code_.library_Library(name=[], library_Library3=None)
    assert isinstance(var_10, python_code_.library_Library)


def test_2():
    var_12 = python_code_.library_Library(
        name="library_Library", library_Library3={True, -388}
    )
    assert isinstance(var_12, python_code_.library_Library)


def test_3():
    var_0 = python_code_.library_Writer(name="gl^", library_Writer=None, author=set())
    assert isinstance(var_0, python_code_.library_Writer)


def test_4():
    var_0 = python_code_.library_Writer(name=";\t`'EQgDxi\x0c6,@^N'\"", Writer=None)
    assert isinstance(var_0, python_code_.library_Writer)


@pytest.mark.xfail(strict=True)
def test_5():
    var_8 = ""
    var_9 = int
    var_10 = python_code_.library_Book(title=var_8, pages=var_9, category=var_8)
    python_code_.library_Writer(name=var_8, Writer=var_10)


def test_6():
    var_0 = python_code_.library_Writer(
        name={"library_Book:_library_Writer__Writer:Book", -911.27, True},
        Writer={},
        author=None,
    )
    assert var_0.Writer == {}
    var_0.writeBook(
        library_category=(False,), library_pages=False, library_booksname=var_0
    )
    var_2 = list
    var_3 = -1504
    python_code_.library_Book(title=var_2, pages=var_3, category=var_3)


def test_7():
    var_15 = python_code_.library_Writer(name=(), library_Writer=True)
    assert isinstance(var_15, python_code_.library_Writer)


def test_8():
    python_code_.library_Book(
        title="_library_Book__Booklibrary_Book", pages=-2153, category="^&", Book=None
    )


def test_9():
    var_0 = python_code_.library_Writer(
        name="V", Writer=None, library_Writer=None, author=set()
    )
    assert isinstance(var_0, python_code_.library_Writer)
    var_8 = python_code_.library_Book(
        title="ZVzf~\nL~M[{+7A )zJ", pages=2964, category="V&", Book=var_0
    )
    assert isinstance(var_8, python_code_.library_Book)


def test_10():
    var_10 = python_code_.library_Library(name="67M5bpfEU!f6", library_Library3=set())
    assert isinstance(var_10, python_code_.library_Library)
    var_11 = python_code_.library_Book(
        title=None, pages=2597, category=2624, library_Book=var_10
    )
    assert isinstance(var_11, python_code_.library_Book)


def test_11():
    var_13 = python_code_.library_Writer(
        name="J^>,B'OZ[DSR\x0c^\x0c", Writer=None, author=set()
    )
    assert isinstance(var_13, python_code_.library_Writer)
    var_15 = python_code_.library_Book(
        title=[3484.03],
        pages=(
            1455.15,
            "_library_Writer__library_Writer-author-_library_Writer__library_Writer-ScienceFiction",
            391,
        ),
        category=var_13,
        books={-4169, 1152.0, -722},
        Book=var_13,
    )
    assert isinstance(var_15, python_code_.library_Book)


def test_12():
    python_code_.BookCategory.Mystery


def test_13():
    var_12 = python_code_.library_Library(
        name="_library_Book__Book", library_Library3={False}
    )
    assert isinstance(var_12, python_code_.library_Library)
    var_13 = python_code_.library_Writer(name=False, library_Writer=var_12)
    assert isinstance(var_13, python_code_.library_Writer)


def test_14():
    var_12 = python_code_.library_Library(name="yE;")
    assert isinstance(var_12, python_code_.library_Library)
    var_15 = python_code_.library_Writer(
        name=var_12, library_Writer=var_12, author={138.29}
    )
    assert isinstance(var_15, python_code_.library_Writer)
    var_15.writeBook(
        library_category=complex(2802.8772901, -1708.8983677),
        library_pages=var_12,
        library_booksname=var_12,
    )


def test_15():
    var_10 = "og{\nu|BFp+<cnQXqDR0"
    var_11 = python_code_.library_Book(
        title="H3{Vqgl5G", pages=-2221, category="2Kn@b#3\rsOj", Book=var_10
    )
    assert isinstance(var_11, python_code_.library_Book)


def test_16():
    var_13 = python_code_.library_Writer(
        name="_library_Library__library_Library3.author._library_Writer__library_Writer",
        author=set(),
    )
    assert isinstance(var_13, python_code_.library_Writer)
    var_16 = python_code_.library_Book(
        title="library_Library_library_Book__bookslibrary_Library3",
        pages=1016,
        category="_library_Book__library_Book_library_Book__books_library_Book__library_Booklibrary_Library3",
        library_Book=var_13,
        Book=var_13,
    )
    assert isinstance(var_16, python_code_.library_Book)


@pytest.mark.xfail(strict=True)
def test_17():
    var_0 = python_code_.library_Writer(
        name="V", Writer=None, library_Writer=None, author=set()
    )
    assert isinstance(var_0, python_code_.library_Writer)
    python_code_.library_Book(
        title="_library_Library__library_Library:Writer",
        pages=0,
        category="0JO=%%l9#aD^]Xb8",
        books=var_0,
        library_Book=None,
        Book=var_0,
    )


def test_18():
    var_0 = python_code_.library_Library(name=239, library_Library3={})
    assert isinstance(var_0, python_code_.library_Library)
    var_2 = 'B2h=)"D'
    var_3 = 384
    var_4 = python_code_.library_Book(
        title=var_2, pages=var_3, category=var_2, library_Book=var_0, Book=var_2
    )
    assert isinstance(var_4, python_code_.library_Book)
    var_5 = python_code_.library_Writer(name=var_2, author={var_4})
    assert isinstance(var_5, python_code_.library_Writer)
    var_6 = abs
    var_5.writeBook(
        library_category=complex(-1931.123383, -4635.941857),
        library_pages=4855,
        library_booksname=var_6,
    )
    python_code_.library_Writer(name=var_2, Writer=None)
    var_20 = python_code_.library_Library(name="_library_Book__Book")
    assert isinstance(var_20, python_code_.library_Library)


@pytest.mark.xfail(strict=True)
def test_19():
    var_7 = python_code_.library_Library(
        name=(), library_Library=b"&\xf2N\xd3c;8\x9d\xe2\xb3\xab"
    )
    assert isinstance(var_7, python_code_.library_Library)
    var_9 = python_code_.library_Writer(
        name=["_library_Writer__library_Writer,Writer", False, True],
        Writer=0,
        library_Writer=var_7,
    )
    assert var_9.Writer == 0
    var_15 = "!VX"
    var_16 = python_code_.library_Book(
        title=var_15, pages=None, category=var_7, books=var_7, library_Book=var_15
    )
    assert isinstance(var_16, python_code_.library_Book)
    python_code_.library_Writer(name=var_15, Writer=var_16)


def test_20():
    var_7 = python_code_.library_Library(
        name=(), library_Library=b"&\xf2N\xd3c;8\x9d\xe2\xb3\xab"
    )
    assert isinstance(var_7, python_code_.library_Library)
    var_9 = python_code_.library_Writer(
        name=["_library_Writer__library_Writer,Writer", False, True],
        Writer=0,
        library_Writer=var_7,
    )
    assert var_9.Writer == 0
    var_14 = python_code_.library_Library(
        name="_library_Writer__Writer_library_Writer__author", library_Library=set()
    )
    assert isinstance(var_14, python_code_.library_Library)


@pytest.mark.xfail(strict=True)
def test_21():
    var_13 = python_code_.BookCategory.Biography
    var_14 = -1307
    var_15 = "library_Book"
    var_16 = complex
    var_17 = python_code_.library_Writer(name=var_16, Writer=-918, author=(False,))
    assert isinstance(var_17, python_code_.library_Writer)
    python_code_.library_Book(title=var_13, pages=var_14, category=var_15, books=var_17)
    assert isinstance(var_17.Writer, python_code_.library_Book)


def test_22():
    var_9 = "^"
    var_10 = python_code_.library_Writer(name=var_9)
    assert isinstance(var_10, python_code_.library_Writer)
    var_14 = "BIF^Mjt"
    var_15 = -3411
    var_16 = python_code_.library_Writer
    var_17 = python_code_.library_Book(
        title=var_14, pages=var_15, category=var_9, Book=var_16
    )
    assert isinstance(var_17, python_code_.library_Book)
    var_18 = "GEWn<"
    python_code_.library_Book(title=var_18, pages=var_15, category=var_10)


def test_23():
    var_10 = python_code_.library_Library(
        name="", library_Library={789}, library_Library3={True}
    )
    assert isinstance(var_10, python_code_.library_Library)
    var_12 = python_code_.library_Book(
        title="GY}o*9\\\tHa,\toSm\x0cT", pages=-801, category="KLYs=c"
    )
    var_13 = python_code_.library_Library(
        name="=23o}", library_Library3={True, var_12, ""}
    )
    assert isinstance(var_13, python_code_.library_Library)
    var_14 = "o"
    var_15 = python_code_.library_Writer(name=var_14, library_Writer=var_13)
    assert isinstance(var_15, python_code_.library_Writer)


def test_24():
    var_12 = python_code_.library_Book(
        title="94&Q#j;", pages=-1182, category="books", library_Book=None
    )
    var_13 = python_code_.library_Writer(
        name="_library_Book__Book,_library_Book__books",
        author={var_12, "_library_Library__library_Library3", -322.12},
    )
    assert isinstance(var_13, python_code_.library_Writer)


def test_25():
    var_12 = python_code_.library_Book(
        title="QN<", pages=246, category="_library_Book__books"
    )
    var_16 = ""
    var_17 = python_code_.library_Writer(name=var_16)
    assert isinstance(var_17, python_code_.library_Writer)
    var_19 = python_code_.library_Library(
        name="zmL3f4>Y>",
        library_Library={-2569.78, var_17, -3314.91},
        library_Library3={var_16},
    )
    assert isinstance(var_19, python_code_.library_Library)
    var_20 = var_17.writeBook(
        library_category=complex(-3424.3739959, -1598.576),
        library_pages=var_17,
        library_booksname=var_17,
    )
    var_21 = python_code_.library_Writer(
        name=var_12, library_Writer=var_19, author=var_20
    )
    assert isinstance(var_21, python_code_.library_Writer)


def test_26():
    var_21 = "li\x0brary_L/brary"
    var_23 = python_code_.library_Book(
        title="2\n75Pd3!K^f&LN{v?9w", pages=2, category=var_21, Book=var_21
    )
    assert isinstance(var_23, python_code_.library_Book)
    var_24 = python_code_.library_Writer(name="E(FcGD%", author={var_23})
    assert isinstance(var_24, python_code_.library_Writer)
