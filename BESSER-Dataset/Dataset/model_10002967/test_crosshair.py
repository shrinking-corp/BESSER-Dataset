from python_code import CATEGORIAS

def test_CATEGORIAS___init__():
    assert CATEGORIAS.__init__(CATEGORIAS('', '', '', pRODUCTO4=set()), '', '', '', pRODUCTO4=set()) == None


from python_code import FOLLOW_MESSENGER

def test_FOLLOW_MESSENGER___init__():
    assert FOLLOW_MESSENGER.__init__(FOLLOW_MESSENGER('', '', '\x00\x00'), '', '', '') == None


from python_code import ROLES

def test_ROLES___init__():
    assert ROLES.__init__(ROLES('', '', '', usuario0=set()), '', '', '', usuario0=set()) == None


from python_code import STATUS2

def test_STATUS2___init__():
    assert STATUS2.__init__(STATUS2('', '\x00'), '\x00\x00', '') == None


from python_code import SUBSCRIPTION_BENEFITS

def test_SUBSCRIPTION_BENEFITS___init__():
    assert SUBSCRIPTION_BENEFITS.__init__(SUBSCRIPTION_BENEFITS('', '', '\x00\x00'), '', '', '') == None

