from python_code import mindstorms_GoBackward

def test_mindstorms_GoBackward___init__():
    assert mindstorms_GoBackward.__init__(mindstorms_GoBackward(0, False), 0, False) == None


from python_code import mindstorms_GoForward

def test_mindstorms_GoForward___init__():
    assert mindstorms_GoForward.__init__(mindstorms_GoForward(0, False), 0, False) == None


from python_code import mindstorms_NamedElement

def test_mindstorms_NamedElement___init__():
    assert mindstorms_NamedElement.__init__(mindstorms_NamedElement(''), '') == None


from python_code import mindstorms_Rotate

def test_mindstorms_Rotate___init__():
    assert mindstorms_Rotate.__init__(mindstorms_Rotate(0, False), 0, False) == None

