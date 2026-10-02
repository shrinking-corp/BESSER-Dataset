from python_code import bytecode_ArgsByteCode

def test_bytecode_ArgsByteCode___init__():
    assert bytecode_ArgsByteCode.__init__(bytecode_ArgsByteCode(0, '\x00'), 0, '\x00') == None

from python_code import bytecode_BopByteCode

def test_bytecode_BopByteCode___init__():
    assert bytecode_BopByteCode.__init__(bytecode_BopByteCode('', '\x00'), '\x00\x00', '') == None

from python_code import bytecode_CallByteCode

def test_bytecode_CallByteCode___init__():
    assert bytecode_CallByteCode.__init__(bytecode_CallByteCode('', '', 0), '\x00', '', 0) == None

from python_code import bytecode_DumpByteCode

def test_bytecode_DumpByteCode___init__():
    assert bytecode_DumpByteCode.__init__(bytecode_DumpByteCode('', '\x00'), '\x00\x00', '') == None

from python_code import bytecode_FalseBranchByteCode

def test_bytecode_FalseBranchByteCode___init__():
    assert bytecode_FalseBranchByteCode.__init__(bytecode_FalseBranchByteCode('', '', 0), '\x00', '', 0) == None

from python_code import bytecode_GoToByteCode

def test_bytecode_GoToByteCode___init__():
    assert bytecode_GoToByteCode.__init__(bytecode_GoToByteCode('', '', 0), '\x00', '', 0) == None

from python_code import bytecode_HaltByteCode

def test_bytecode_HaltByteCode___init__():
    assert bytecode_HaltByteCode.__init__(bytecode_HaltByteCode(''), '') == None

from python_code import bytecode_LabelByteCode

def test_bytecode_LabelByteCode___init__():
    assert bytecode_LabelByteCode.__init__(bytecode_LabelByteCode(0, '', '\x00\x00'), 0, '', '') == None

from python_code import bytecode_LitByteCode

def test_bytecode_LitByteCode___init__():
    assert bytecode_LitByteCode.__init__(bytecode_LitByteCode('', 0, '\x00\x00'), '', 0, '') == None

from python_code import bytecode_LoadByteCode

def test_bytecode_LoadByteCode___init__():
    assert bytecode_LoadByteCode.__init__(bytecode_LoadByteCode('', 0, '\x00\x00'), '', 0, '') == None

from python_code import bytecode_PopByteCode

def test_bytecode_PopByteCode___init__():
    assert bytecode_PopByteCode.__init__(bytecode_PopByteCode('', '', 0), '\x00', '', 0) == None

from python_code import bytecode_ReadByteCode

def test_bytecode_ReadByteCode___init__():
    assert bytecode_ReadByteCode.__init__(bytecode_ReadByteCode(''), '') == None

from python_code import bytecode_ReturnByteCode

def test_bytecode_ReturnByteCode___init__():
    assert bytecode_ReturnByteCode.__init__(bytecode_ReturnByteCode(''), '') == None

from python_code import bytecode_StoreByteCode

def test_bytecode_StoreByteCode___init__():
    assert bytecode_StoreByteCode.__init__(bytecode_StoreByteCode(0, '\x00', '', ''), 0, '', '', '') == None

from python_code import bytecode_WriteByteCode

def test_bytecode_WriteByteCode___init__():
    assert bytecode_WriteByteCode.__init__(bytecode_WriteByteCode(''), '') == None

from python_code import genmymodelreverse_java_util_Scanner
from python_code import interpreter_ByteCodeLoader
from python_code import interpreter_Interpreter

def test_interpreter_ByteCodeLoader___init__():
    assert interpreter_ByteCodeLoader.__init__(interpreter_ByteCodeLoader(genmymodelreverse_java_util_Scanner(), '', 0, interpreter0=interpreter_Interpreter()), genmymodelreverse_java_util_Scanner(), '', 0, interpreter0=interpreter_Interpreter()) == None

from python_code import interpreter_CodeTable

def test_interpreter_CodeTable___init__():
    assert interpreter_CodeTable.__init__(interpreter_CodeTable('', '\x00'), '\x00\x00', '') == None
