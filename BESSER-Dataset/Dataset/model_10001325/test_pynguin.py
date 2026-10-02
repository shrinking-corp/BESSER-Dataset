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
    ABC,
    abstractmethod,
    annotations,
    bytecode_ArgsByteCode,
    bytecode_BopByteCode,
    bytecode_ByteCode,
    bytecode_CallByteCode,
    bytecode_DumpByteCode,
    bytecode_FalseBranchByteCode,
    bytecode_GoToByteCode,
    bytecode_HaltByteCode,
    bytecode_LabelByteCode,
    bytecode_LitByteCode,
    bytecode_LoadByteCode,
    bytecode_PopByteCode,
    bytecode_ReadByteCode,
    bytecode_ReturnByteCode,
    bytecode_StoreByteCode,
    bytecode_WriteByteCode,
    date,
    datetime,
    genmymodelreverse_C1,
    genmymodelreverse_C11,
    genmymodelreverse_C12,
    genmymodelreverse_C2,
    genmymodelreverse_C21,
    genmymodelreverse_java_io_IOException,
    genmymodelreverse_java_util_HashMap,
    genmymodelreverse_java_util_Map_Interface,
    genmymodelreverse_java_util_Scanner,
    genmymodelreverse_java_util_Vector,
    interpreter_ByteCodeLoader,
    interpreter_CodeTable,
    interpreter_Interpreter,
    interpreter_Program,
    interpreter_RunTimeStack,
    interpreter_VirtualMachine,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_1 = -3317
    var_92 = True
    var_94 = python_code_.interpreter_RunTimeStack(
        runStack="ftD|)Azgv`~E!J=", framePointers=var_1
    )
    var_95 = -17
    python_code_.interpreter_VirtualMachine(
        pc=-3523,
        isRunning=True,
        dumpState=var_92,
        returnAddrs=var_95,
        newRunStack5=var_94,
    )
    assert isinstance(var_94.virtualmachine4, python_code_.interpreter_VirtualMachine)


def test_1():
    var_98 = True
    python_code_.interpreter_Program(
        programMap="newRunStack5", byteCodeVector="/n(\t[0aN|"
    )
    python_code_.interpreter_VirtualMachine(
        pc=-1840, isRunning=var_98, dumpState=var_98, returnAddrs=1617
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_98 = False
    var_108 = python_code_.interpreter_Program(
        programMap="newRunStack5", byteCodeVector="/n(\t[0aN|"
    )
    python_code_.interpreter_VirtualMachine(
        pc=var_98,
        isRunning=var_98,
        dumpState=var_98,
        returnAddrs=var_98,
        newProgram3=var_108,
    )


def test_3():
    var_3 = lambda *args, **kwargs: [617.41, "nq4,", -1]
    var_111 = '7e"0`nU; 0FXS\\h:T'
    var_112 = python_code_.interpreter_ByteCodeLoader(
        input=var_3,
        programMap=var_111,
        lineCount=None,
        interpreter0="_interpreter_Program__virtualmachine2",
    )
    assert isinstance(var_112, python_code_.interpreter_ByteCodeLoader)
    var_113 = -762
    var_114 = True
    python_code_.interpreter_VirtualMachine(
        pc=var_113,
        isRunning=var_114,
        dumpState=True,
        returnAddrs=var_113,
        newRunStack5=None,
    )


def test_4():
    var_3 = lambda *args, **kwargs: [617.41, "nq4,", -1]
    var_111 = '7e"0`n4; 0FXS\\h:T'
    var_114 = python_code_.interpreter_ByteCodeLoader(
        input=var_3,
        programMap=var_111,
        lineCount=None,
        interpreter0="_interpreter_Program__virtualmachine2",
    )
    assert isinstance(var_114, python_code_.interpreter_ByteCodeLoader)
    var_115 = -1482
    var_116 = 1
    var_117 = python_code_.interpreter_VirtualMachine(
        pc=var_115,
        isRunning={"f": -1, 'vV\t:cT>JL^.599"j': True},
        dumpState=var_114,
        returnAddrs=var_116,
        newProgram3={False},
    )
    assert isinstance(var_117, python_code_.interpreter_VirtualMachine)


def test_5():
    python_code_.interpreter_RunTimeStack(runStack="uJ\n~&\x0cUOU", framePointers=2474)
    python_code_.interpreter_Program(programMap=">K =)7p=J", byteCodeVector="_Wd]\n>[")


def test_6():
    var_0 = "#;MzT#qcg"
    var_1 = python_code_.bytecode_ReadByteCode(byteCode=var_0)
    var_2 = -3042
    var_3 = python_code_.interpreter_RunTimeStack(
        runStack=var_0, framePointers=var_2, virtualmachine4=-310.72
    )
    assert var_3.virtualmachine4 == pytest.approx(-310.72, abs=0.01, rel=0.01)
    python_code_.bytecode_BopByteCode(byteCode=var_3, theOperator=var_2)
    var_6 = python_code_.genmymodelreverse_java_util_HashMap()
    var_7 = python_code_.bytecode_LabelByteCode
    python_code_.bytecode_ReturnByteCode(byteCode=var_7)
    var_12 = python_code_.bytecode_DumpByteCode(byteCode=var_1, theArg=var_7)
    python_code_.bytecode_StoreByteCode(
        storeValue=b"\xea\xb7\r", storeID=var_12, byteCode=var_0, theArg=var_7
    )
    var_16 = "eN&\x0c?~YJ"
    python_code_.interpreter_CodeTable(codeMap=var_12, byteCodesTXT=var_16)
    python_code_.bytecode_LabelByteCode(lineNO=var_7, byteCode=True, theArg=var_7)
    var_20 = ""
    python_code_.bytecode_LoadByteCode(byteCode=var_16, loadOffset=var_6, loadID=var_20)
    var_24 = "interpreter_Interpreter _interpreter_VirtualMachine__newRunStack5 virtualmachine2 interpreter_Interpreter"
    var_25 = '"+Hem\x0bP23n/cktGh'
    python_code_.bytecode_PopByteCode(byteCode=var_24, theArg=var_25, count=var_2)


def test_7():
    python_code_.interpreter_Program(
        programMap="{qlVI2Q`", byteCodeVector="1]SA1*4~#6\x0cff*"
    )


def test_8():
    python_code_.interpreter_ByteCodeLoader(
        input=None, programMap=" {`F\x0b\x0cOYk4s &k:e", lineCount=-4076
    )


def test_9():
    var_3 = lambda *args, **kwargs: [617.41, "nq4,", -1]
    var_4 = "interareter_RunTimeStack-bcl#1-_interpreter_VirtualMachine__newProgram3"
    var_5 = python_code_.interpreter_ByteCodeLoader(
        input=var_3,
        programMap=var_4,
        lineCount=None,
        interpreter0="_interpreter_Program__virtualmachine2",
    )
    assert isinstance(var_5, python_code_.interpreter_ByteCodeLoader)


def test_10():
    python_code_.genmymodelreverse_java_util_Vector()


def test_11():
    var_3 = lambda *args, **kwargs: [617.41, "nq4,", -1]
    var_111 = '7e"0`n4; 0FXS\\h:T'
    var_114 = python_code_.interpreter_ByteCodeLoader(
        input=var_3,
        programMap=var_111,
        lineCount=None,
        interpreter0="_interpreter_Program__virtualmachine2",
    )
    assert isinstance(var_114, python_code_.interpreter_ByteCodeLoader)
    python_code_.interpreter_CodeTable(
        codeMap=var_111,
        byteCodesTXT=[
            "interpreter_Programinterpreter_Program_interpreter_VirtualMachine__newRunStack5interpreter_VirtualMachine",
            3351,
            2,
        ],
    )


def test_12():
    python_code_.bytecode_WriteByteCode(byteCode=())


def test_13():
    var_102 = 1
    var_103 = "9x'qw$@G'}"
    var_1 = python_code_.bytecode_StoreByteCode(
        storeValue=var_102, storeID=var_103, byteCode=var_103, theArg=var_103
    )
    python_code_.interpreter_RunTimeStack(
        runStack="ftD|)Azgv`~E!J=", framePointers=var_1
    )


def test_14():
    python_code_.bytecode_ReturnByteCode(byteCode="")


def test_15():
    python_code_.bytecode_ReadByteCode(byteCode=None)


def test_16():
    var_3 = lambda *args, **kwargs: [617.41, "nq4,", -1]
    var_105 = "interareter_RunTimeStack-bcl#1-_interpreter_VirtualMachine__newProgram3"
    var_106 = python_code_.interpreter_ByteCodeLoader(
        input=var_3,
        programMap=var_105,
        lineCount=None,
        interpreter0="_interpreter_Program__virtualmachine2",
    )
    assert isinstance(var_106, python_code_.interpreter_ByteCodeLoader)
    var_107 = "&tz(%k\\?uy5h"
    var_108 = "3zdZD/PVn"
    python_code_.bytecode_LabelByteCode(lineNO=var_3, byteCode=var_107, theArg=var_108)
    var_110 = -2602
    python_code_.bytecode_PopByteCode(
        byteCode=b";\xbeB\xff\x84/\x15\x1d", theArg=var_3, count=var_110
    )


def test_17():
    var_3 = lambda *args, **kwargs: [617.41, "nq4,", -1]
    var_107 = "#O&L}NF7tC|nMf"
    var_108 = python_code_.interpreter_ByteCodeLoader(
        input=var_3,
        programMap=var_107,
        lineCount=None,
        interpreter0="_interpreter_Program__virtualmachine2",
    )
    assert isinstance(var_108, python_code_.interpreter_ByteCodeLoader)
    var_109 = 555
    python_code_.bytecode_LoadByteCode(byteCode=(), loadOffset=var_109, loadID=var_107)


def test_18():
    var_3 = lambda *args, **kwargs: [617.41, "nq4,", -1]
    var_105 = "interareter_RunTimeStack-bcl#1-_interpreter_VirtualMachine__newProgram3"
    var_106 = python_code_.interpreter_ByteCodeLoader(
        input=var_3,
        programMap=var_105,
        lineCount=None,
        interpreter0="_interpreter_Program__virtualmachine2",
    )
    assert isinstance(var_106, python_code_.interpreter_ByteCodeLoader)
    python_code_.bytecode_LitByteCode(byteCode=var_105, litValue=var_3, litID=[-1026])


def test_19():
    python_code_.bytecode_LabelByteCode(
        lineNO=-2545, byteCode="interpreter_RunTimeStack", theArg="bcl1"
    )


def test_20():
    python_code_.bytecode_HaltByteCode(byteCode=set())


def test_21():
    var_31 = "Vi"
    python_code_.interpreter_Program(programMap=None, byteCodeVector=var_31)
    var_34 = "5O\r> 5qM{T[p1gP"
    var_35 = -1214
    python_code_.bytecode_GoToByteCode(byteCode=var_34, theArg="*E{[;yx", lineNO=var_35)
    python_code_.bytecode_ReadByteCode(byteCode=b"'\xd5M\x9e")
    python_code_.bytecode_ReturnByteCode(byteCode=True)


def test_22():
    var_105 = "nterareter_RunTimeStack-bcl#1-_in2terpreter_Vi{rtualMachine__newProgram3"
    var_107 = python_code_.interpreter_ByteCodeLoader(
        input=var_105, programMap="", lineCount=-221, interpreter0=var_105
    )
    assert isinstance(var_107, python_code_.interpreter_ByteCodeLoader)
    python_code_.bytecode_FalseBranchByteCode(
        byteCode=complex(3499.5902, 1638.57), theArg=var_105, lineNO=var_105
    )


def test_23():
    var_3 = lambda *args, **kwargs: [617.41, "nq4,", -1]
    var_105 = (
        "interareter_RunTimeStack-\x0cbcl#1-_interpreter_VirtualMachine__newProgram3"
    )
    var_106 = python_code_.interpreter_ByteCodeLoader(
        input=var_3,
        programMap=var_105,
        lineCount=None,
        interpreter0="_interpreter_Program__virtualmachine2",
    )
    assert isinstance(var_106, python_code_.interpreter_ByteCodeLoader)
    var_107 = "_interpreter_ByteCodeLoader__interpreter0.interpreter_VirtualMachine._interpreter_Program__virtualmachine2.interpreter_VirtualMachine"
    var_108 = (
        "_interpreter_Program__virtualmachine2 newRunStack5 interpreter_VirtualMachine"
    )
    python_code_.bytecode_DumpByteCode(byteCode=var_107, theArg=var_108)


def test_24():
    python_code_.bytecode_CallByteCode(byteCode="|WG?", theArg="D_RgV\x0c|sG", lineNO=0)


def test_25():
    python_code_.bytecode_BopByteCode(byteCode="newProgram3", theOperator="newProgram3")


def test_26():
    python_code_.bytecode_ArgsByteCode(
        argCount=(False, 2328.71, -1062.34), byteCode="newRunStack5"
    )


def test_27():
    var_1 = -3317
    python_code_.interpreter_RunTimeStack(runStack={"Tc/": False}, framePointers=var_1)
    var_3 = lambda *args, **kwargs: [617.41, "nq4,", -1]
    var_4 = "interpreter_RunTimeStack-bcl1-_interpreter_VirtualMachine__newProgram3"
    var_5 = python_code_.interpreter_ByteCodeLoader(
        input=var_3,
        programMap=var_4,
        lineCount=None,
        interpreter0="_interpreter_Program__virtualmachine2",
    )
    assert isinstance(var_5, python_code_.interpreter_ByteCodeLoader)
    python_code_.bytecode_ReturnByteCode(byteCode={-54, True, True})
    python_code_.bytecode_ReadByteCode(byteCode=complex(2420.4, -44.2))
    var_49 = "]$@ i"
    python_code_.bytecode_WriteByteCode(byteCode=var_49)
    var_52 = "p312m"
    var_74 = False
    var_75 = python_code_.interpreter_VirtualMachine(
        pc=var_3,
        isRunning=var_52,
        dumpState=var_74,
        returnAddrs=-3593,
        newRunStack5=-553.02,
    )
    assert isinstance(var_75, python_code_.interpreter_VirtualMachine)


@pytest.mark.xfail(strict=True)
def test_28():
    var_3 = lambda *args, **kwargs: [617.41, "nq4,", -1]
    var_111 = '7e"0`nU; FXS\\h:T'
    var_112 = python_code_.interpreter_ByteCodeLoader(
        input=var_3,
        programMap=var_111,
        lineCount=None,
        interpreter0="_interpreter_Program__virtualmachine2",
    )
    assert isinstance(var_112, python_code_.interpreter_ByteCodeLoader)
    var_114 = "_interpreter_ByteCodeLoader__interpreter0"
    var_115 = 1181
    var_116 = False
    var_117 = python_code_.interpreter_VirtualMachine(
        pc=var_115,
        isRunning=var_112,
        dumpState=var_116,
        returnAddrs=var_116,
        newRunStack5=var_115,
    )
    assert isinstance(var_117, python_code_.interpreter_VirtualMachine)
    python_code_.interpreter_Program(
        programMap=var_114, byteCodeVector=var_114, virtualmachine2=var_117
    )


@pytest.mark.xfail(strict=True)
def test_29():
    var_98 = True
    var_104 = python_code_.interpreter_Program(
        programMap="_interpreter_VirtualMachine__newRunStack5",
        byteCodeVector="TAu,2yN\\\r#%0k3P\x0ccC=",
        virtualmachine2=var_98,
    )
    assert isinstance(var_104, python_code_.interpreter_Program)
    python_code_.interpreter_VirtualMachine(
        pc=var_98,
        isRunning=var_98,
        dumpState=var_98,
        returnAddrs=var_98,
        newProgram3=var_104,
    )


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = "5\x0b&"
    python_code_.bytecode_WriteByteCode(byteCode=var_0)
    var_2 = python_code_.bytecode_DumpByteCode(byteCode=var_0, theArg=var_0)
    var_3 = bool
    python_code_.bytecode_GoToByteCode(byteCode=var_3, theArg=var_3, lineNO=var_3)
    python_code_.bytecode_LitByteCode(byteCode=var_0, litValue=var_3, litID=var_2)
    var_6 = python_code_.genmymodelreverse_C1()
    var_10 = "interpreter_RunTimeStackvirtualmachine4"
    var_11 = -1
    python_code_.bytecode_PopByteCode(byteCode=var_10, theArg=var_0, count=var_11)
    var_13 = "o#S\r?N"
    python_code_.interpreter_CodeTable(
        codeMap=var_13,
        byteCodesTXT=b"\xef\xaa\x9b\x9f\xf0\xda\x91A\xac\xb92@\xa8\x8e\x04",
    )
    python_code_.bytecode_LabelByteCode(
        lineNO=var_11,
        byteCode=var_3,
        theArg=b"\x06\xbd5\xc0\x9c\xdd}=\xdf\xf4\x1c\x19\xba\xb9[,J\x1f\xd5",
    )
    var_24 = python_code_.interpreter_RunTimeStack(
        runStack=True, framePointers=var_3, virtualmachine4=b"\x15Y\x1fh!G\xf3"
    )
    assert isinstance(var_24, python_code_.interpreter_RunTimeStack)
    python_code_.interpreter_VirtualMachine(
        pc=var_11, isRunning=(), dumpState=var_3, returnAddrs=var_6, newRunStack5=var_24
    )
    assert isinstance(var_24.virtualmachine4, python_code_.interpreter_VirtualMachine)


@pytest.mark.xfail(strict=True)
def test_31():
    var_110 = "@\\Quvf&#Wjm6"
    var_111 = 1740
    python_code_.interpreter_RunTimeStack(runStack=var_110, framePointers=var_111)
    var_114 = lambda *args, **kwargs: False
    var_115 = True
    var_116 = -1356
    var_117 = -2091
    var_118 = python_code_.interpreter_VirtualMachine(
        pc=var_116,
        isRunning=None,
        dumpState=var_115,
        returnAddrs=var_117,
        newProgram3=b"q\x1e\xac\xed\xe7\x8f",
    )
    assert isinstance(var_118, python_code_.interpreter_VirtualMachine)
    python_code_.interpreter_Program(
        programMap=var_114,
        byteCodeVector=b"\x97\xb7\xe7\x94\x99.\xe0+\x1b\x15$Oi",
        virtualmachine2=var_118,
    )
