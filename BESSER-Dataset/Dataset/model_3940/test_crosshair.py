from python_code import myDsl01_Attribute

def test_myDsl01_Attribute___init__():
    assert myDsl01_Attribute.__init__(myDsl01_Attribute('', False), '', False) == None


from python_code import myDsl01_Button

def test_myDsl01_Button___init__():
    assert myDsl01_Button.__init__(myDsl01_Button('', '\x00'), '\x00\x00', '') == None


from python_code import myDsl01_Label

def test_myDsl01_Label___init__():
    assert myDsl01_Label.__init__(myDsl01_Label(''), '') == None

