from python_code import wxyz_NamedElt

def test_wxyz_NamedElt___init__():
    assert wxyz_NamedElt.__init__(wxyz_NamedElt(''), '') == None


from python_code import wxyz_Model
from python_code import wxyz_X

def test_wxyz_X___init__():
    assert wxyz_X.__init__(wxyz_X('', wxyz_X=wxyz_Model()), '', wxyz_X=wxyz_Model()) == None


from python_code import wxyz_Y

def test_wxyz_Y___init__():
    assert wxyz_Y.__init__(wxyz_Y(''), '') == None


from python_code import wxyz_Z

def test_wxyz_Z___init__():
    assert wxyz_Z.__init__(wxyz_Z(''), '') == None

