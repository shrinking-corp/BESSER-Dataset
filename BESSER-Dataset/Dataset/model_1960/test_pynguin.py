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
    ABC,
    ByteFile,
    Enum,
    File,
    FileEncoding,
    FileHandler,
    FileOwner,
    abstractmethod,
    date,
    datetime,
    file_ByteFile,
    file_File,
    file_FileHandler,
    file_FileInMemory,
    file_FileLocal,
    file_FileOutput,
    file_FileOwner,
    file_FileReaderWriter,
    file_FileRemote,
    file_Files,
    time,
)


def test_0():
    var_2 = python_code_.file_File(Name="V/")
    assert isinstance(var_2, python_code_.file_File)


def test_1():
    var_1 = "K3:Fl:Is%<7D\\hYp|2(t"
    var_5 = python_code_.file_File(Name="}*C8a49un*", file_File=var_1, file_File7=var_1)
    assert isinstance(var_5, python_code_.file_File)


def test_2():
    var_1 = "K3:Fl:Is<7D\\hYp|2(t"
    var_2 = python_code_.file_File(Name=var_1, file_File3=var_1)
    assert isinstance(var_2, python_code_.file_File)


def test_3():
    var_28 = python_code_.file_File(Name="P#O28!moQ;", file_File5=True)
    assert isinstance(var_28, python_code_.file_File)


def test_4():
    python_code_.FileEncoding.UTF_16LE


def test_5():
    var_10 = python_code_.file_Files(Name=-1428.0)
    assert isinstance(var_10, python_code_.file_Files)


def test_6():
    var_10 = python_code_.file_FileReaderWriter(
        ReadFeedback="9\x0c>hXd6c7",
        CloseFeedback=complex(707.4162, -4605.92),
        Open={},
        WriteFeedback=complex(-784.8, 1399.508),
    )
    assert isinstance(var_10, python_code_.file_FileReaderWriter)


def test_7():
    var_1 = " pckDA"
    var_13 = python_code_.file_File(
        Name="}*C8a49un*", file_File=var_1, file_File7=var_1
    )
    assert isinstance(var_13, python_code_.file_File)
    var_16 = True
    var_17 = python_code_.file_FileReaderWriter(
        ReadFeedback=var_1, CloseFeedback=var_1, Open=var_16, WriteFeedback=var_16
    )
    assert isinstance(var_17, python_code_.file_FileReaderWriter)
    var_17.writeFile(file_file=[])


def test_8():
    var_1 = " pcDA"
    var_9 = python_code_.file_File(Name="}*C8a49un*", file_File=var_1, file_File7=var_1)
    assert isinstance(var_9, python_code_.file_File)
    var_10 = python_code_.file_FileOutput
    var_11 = python_code_.file_FileReaderWriter(
        ReadFeedback=var_9,
        CloseFeedback=var_10,
        Open=var_10,
        WriteFeedback=b"\x14\x12P\xc5\xe8",
    )
    assert isinstance(var_11, python_code_.file_FileReaderWriter)
    var_11.close()


def test_9():
    var_18 = python_code_.File()
    var_19 = python_code_.file_File(
        Name={"file_FileOwner": -2165.24, "": True, "_XT&": False}, file_File5=var_18
    )
    assert isinstance(var_19, python_code_.file_File)
    var_20 = "_file_File__file_File5:file_FileOutput"
    var_21 = python_code_.file_FileReaderWriter(
        ReadFeedback=var_20, CloseFeedback=var_18, Open=var_19, WriteFeedback=var_20
    )
    assert isinstance(var_21, python_code_.file_FileReaderWriter)
    var_21.readFile(file_file=var_19)


def test_10():
    var_1 = " pcDA"
    var_10 = python_code_.file_File(
        Name="}*C8a49un*", file_File=var_1, file_File7=var_1
    )
    assert isinstance(var_10, python_code_.file_File)
    var_11 = python_code_.file_FileReaderWriter(
        ReadFeedback=var_1,
        CloseFeedback=var_1,
        Open=b"\xcd\xb3\xaf\xfd\xab\xc6\x9a\xe9\x1c\x84\xe09\xaef\xe8[",
        WriteFeedback=complex(2141.31, -554.1791),
    )
    assert isinstance(var_11, python_code_.file_FileReaderWriter)
    var_11.getWriteFeedback(file_file=None)


def test_11():
    var_1 = " \n#k"
    var_22 = python_code_.file_File(
        Name=var_1, file_File=var_1, file_File3=var_1, file_File5=var_1
    )
    assert isinstance(var_22, python_code_.file_File)
    var_23 = python_code_.file_FileReaderWriter(
        ReadFeedback={},
        CloseFeedback="\n|K~3=7",
        Open=var_1,
        WriteFeedback=complex(1359.34964, 302.0),
    )
    assert isinstance(var_23, python_code_.file_FileReaderWriter)
    var_23.getReadFeedback(file_file=var_22)


def test_12():
    var_9 = python_code_.file_ByteFile(Encoding=complex(385.81, 847.035))
    assert isinstance(var_9, python_code_.file_ByteFile)


def test_13():
    var_5 = python_code_.file_FileInMemory(Content="c]ZzTJD\nb#ZO6gj")
    assert isinstance(var_5, python_code_.file_FileInMemory)


def test_14():
    var_11 = python_code_.file_FileRemote(URL="US_ASCII UTF_16BE")
    assert isinstance(var_11, python_code_.file_FileRemote)


def test_15():
    var_4 = python_code_.file_FileLocal(FilePath='~X("')
    assert isinstance(var_4, python_code_.file_FileLocal)
