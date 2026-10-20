from python_code import graphEditor_Factornode

def test_graphEditor_Factornode___init__():
    assert graphEditor_Factornode.__init__(graphEditor_Factornode('', '\x00'), '\x00\x00', '') == None


from python_code import graphEditor_GraphElement

def test_graphEditor_GraphElement___init__():
    assert graphEditor_GraphElement.__init__(graphEditor_GraphElement(''), '') == None


from python_code import graphEditor_Variablenode

def test_graphEditor_Variablenode___init__():
    assert graphEditor_Variablenode.__init__(graphEditor_Variablenode('\x00', 0.0, False), '', 0.0, False) == None

