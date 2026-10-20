from python_code import Interpreter_ByteCodeLoader

def test_Interpreter_ByteCodeLoader___init__():
    assert Interpreter_ByteCodeLoader.__init__(Interpreter_ByteCodeLoader('', '', '\x00\x00'), '', '', '') == None


from python_code import Interpreter_ByteCode_Args

def test_Interpreter_ByteCode_Args___init__():
    assert Interpreter_ByteCode_Args.__init__(Interpreter_ByteCode_Args(0), 0) == None


from python_code import Interpreter_ByteCode_BOP

def test_Interpreter_ByteCode_BOP___init__():
    assert Interpreter_ByteCode_BOP.__init__(Interpreter_ByteCode_BOP(''), '') == None


from python_code import Interpreter_ByteCode_Call

def test_Interpreter_ByteCode_Call___init__():
    assert Interpreter_ByteCode_Call.__init__(Interpreter_ByteCode_Call('', 0), '', 0) == None


from python_code import Interpreter_ByteCode_Dump

def test_Interpreter_ByteCode_Dump___init__():
    assert Interpreter_ByteCode_Dump.__init__(Interpreter_ByteCode_Dump(''), '') == None


from python_code import Interpreter_ByteCode_FalseBranch

def test_Interpreter_ByteCode_FalseBranch___init__():
    assert Interpreter_ByteCode_FalseBranch.__init__(Interpreter_ByteCode_FalseBranch(0, '\x00'), 0, '\x00') == None


from python_code import Interpreter_ByteCode_GoTo

def test_Interpreter_ByteCode_GoTo___init__():
    assert Interpreter_ByteCode_GoTo.__init__(Interpreter_ByteCode_GoTo(0, '\x00'), 0, '\x00') == None


from python_code import Interpreter_ByteCode_Label

def test_Interpreter_ByteCode_Label___init__():
    assert Interpreter_ByteCode_Label.__init__(Interpreter_ByteCode_Label(''), '') == None


from python_code import Interpreter_ByteCode_Lit

def test_Interpreter_ByteCode_Lit___init__():
    assert Interpreter_ByteCode_Lit.__init__(Interpreter_ByteCode_Lit('', 0), '', 0) == None


from python_code import Interpreter_ByteCode_Load

def test_Interpreter_ByteCode_Load___init__():
    assert Interpreter_ByteCode_Load.__init__(Interpreter_ByteCode_Load('', 0), '', 0) == None


from python_code import Interpreter_ByteCode_Pop

def test_Interpreter_ByteCode_Pop___init__():
    assert Interpreter_ByteCode_Pop.__init__(Interpreter_ByteCode_Pop(0), 0) == None


from python_code import Interpreter_ByteCode_Return

def test_Interpreter_ByteCode_Return___init__():
    assert Interpreter_ByteCode_Return.__init__(Interpreter_ByteCode_Return(''), '') == None


from python_code import Interpreter_ByteCode_Store

def test_Interpreter_ByteCode_Store___init__():
    assert Interpreter_ByteCode_Store.__init__(Interpreter_ByteCode_Store('', 0, 0), '\x00', 0, 0) == None

