from python_code import roc_CompleteAction

def test_roc_CompleteAction___init__():
    assert roc_CompleteAction.__init__(roc_CompleteAction(''), '') == None


from python_code import roc_Direction

def test_roc_Direction___init__():
    assert roc_Direction.__init__(roc_Direction('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import roc_FullDirectedAction

def test_roc_FullDirectedAction___init__():
    assert roc_FullDirectedAction.__init__(roc_FullDirectedAction('', '\x00'), '\x00\x00', '') == None


from python_code import roc_LeftRightDirectedAction

def test_roc_LeftRightDirectedAction___init__():
    assert roc_LeftRightDirectedAction.__init__(roc_LeftRightDirectedAction(''), '') == None


from python_code import roc_LeftRightDirection

def test_roc_LeftRightDirection___init__():
    assert roc_LeftRightDirection.__init__(roc_LeftRightDirection('', '\x00'), '\x00\x00', '') == None


from python_code import roc_SingleAction

def test_roc_SingleAction___init__():
    assert roc_SingleAction.__init__(roc_SingleAction(''), '') == None

