from python_code import Draw_Path

def test_Draw_Path___init__():
    assert Draw_Path.__init__(Draw_Path('', '\x00'), '\x00\x00', '') == None


from python_code import User

def test_User___init__():
    assert User.__init__(User('', 0, 0, '', ''), '', 0, 0, '', '') == None


from python_code import Weekly_Chart

def test_Weekly_Chart___init__():
    assert Weekly_Chart.__init__(Weekly_Chart('', '', 0), '\x00', '', 0) == None

