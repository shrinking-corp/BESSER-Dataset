from python_code import Ornaments

def test_Ornaments___init__():
    assert Ornaments.__init__(Ornaments(''), '') == None


from python_code import User

def test_User___init__():
    assert User.__init__(User(0, product4=set()), 0, product4=set()) == None

