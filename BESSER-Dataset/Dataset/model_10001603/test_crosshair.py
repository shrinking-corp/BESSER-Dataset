from python_code import Chef

def test_Chef___init__():
    assert Chef.__init__(Chef(0, '', '', '', 0), 0, '', '', '', 0) == None


from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer(0, '', '', '', 0), 0, '', '', '', 0) == None


from python_code import Food

def test_Food___init__():
    assert Food.__init__(Food(0, '', 0), 0, '', 0) == None


from python_code import Food_Category

def test_Food_Category___init__():
    assert Food_Category.__init__(Food_Category(0, '', '', '', 0), 0, '', '', '', 0) == None


from python_code import Food_Items

def test_Food_Items___init__():
    assert Food_Items.__init__(Food_Items(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import Food_Sub_Category

def test_Food_Sub_Category___init__():
    assert Food_Sub_Category.__init__(Food_Sub_Category(0, '\x00', '', ''), 0, '', '', '') == None


from python_code import Material

def test_Material___init__():
    assert Material.__init__(Material(0, '', '', '', ''), 0, '', '', '', '') == None


from python_code import Order

def test_Order___init__():
    assert Order.__init__(Order(0, 0, '', '', ''), 0, 0, '', '', '') == None


from python_code import Table

def test_Table___init__():
    assert Table.__init__(Table(0, 0, '\x00\x00'), 0, 0, '') == None

