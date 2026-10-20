from python_code import basic_CoreVersionDefault

def test_basic_CoreVersionDefault___init__():
    assert basic_CoreVersionDefault.__init__(basic_CoreVersionDefault('', '', '\x00\x00'), '', '', '') == None


from python_code import basic_Event

def test_basic_Event___init__():
    assert basic_Event.__init__(basic_Event('\x00\x00', '', basic_Event=set()), '', '', basic_Event=set()) == None


from python_code import basic_ExecutionEnvironment

def test_basic_ExecutionEnvironment___init__():
    assert basic_ExecutionEnvironment.__init__(basic_ExecutionEnvironment('', True, '', '', '', '', ''), '', False, '', '', '', '', '') == None


from python_code import basic_ExtJSProject

def test_basic_ExtJSProject___init__():
    assert basic_ExtJSProject.__init__(basic_ExtJSProject('', basic_ExtJSProject=set()), '', basic_ExtJSProject=set()) == None


from python_code import basic_TypeItem

def test_basic_TypeItem___init__():
    assert basic_TypeItem.__init__(basic_TypeItem(0, 0, '\x00\x00'), 0, 0, '') == None

