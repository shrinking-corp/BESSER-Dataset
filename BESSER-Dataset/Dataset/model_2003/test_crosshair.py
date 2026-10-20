from python_code import trace_Failure

def test_trace_Failure___init__():
    assert trace_Failure.__init__(trace_Failure(''), '') == None


from python_code import trace_FunctionCall

def test_trace_FunctionCall___init__():
    assert trace_FunctionCall.__init__(trace_FunctionCall('', '\x00'), '\x00\x00', '') == None


from python_code import trace_FunctionReturn

def test_trace_FunctionReturn___init__():
    assert trace_FunctionReturn.__init__(trace_FunctionReturn('', '\x00'), '\x00\x00', '') == None


from python_code import trace_Output

def test_trace_Output___init__():
    assert trace_Output.__init__(trace_Output(''), '') == None


from python_code import trace_SimpleValue

def test_trace_SimpleValue___init__():
    assert trace_SimpleValue.__init__(trace_SimpleValue(''), '') == None

