from python_code import minilang_Boolean

def test_minilang_Boolean___init__():
    assert minilang_Boolean.__init__(minilang_Boolean(True), False) == None


from python_code import minilang_Integer

def test_minilang_Integer___init__():
    assert minilang_Integer.__init__(minilang_Integer(0), 0) == None


from python_code import minilang_PrintStr

def test_minilang_PrintStr___init__():
    assert minilang_PrintStr.__init__(minilang_PrintStr(''), '') == None


from python_code import minilang_PrintVar

def test_minilang_PrintVar___init__():
    assert minilang_PrintVar.__init__(minilang_PrintVar(''), '') == None


from python_code import minilang_VariableRef

def test_minilang_VariableRef___init__():
    assert minilang_VariableRef.__init__(minilang_VariableRef(''), '') == None

