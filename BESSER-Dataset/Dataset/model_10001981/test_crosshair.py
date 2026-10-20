from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount('\x00', 0.0), '', 0.0) == None


from python_code import ClassA

def test_ClassA___init__():
    assert ClassA.__init__(ClassA(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC('', 0.0, 0, ''), '', 0.0, 0, '') == None


from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import DBController
from python_code import User_abstract_

def test_DBController___init__():
    assert DBController.__init__(DBController(User_abstract_('\x00\x00', '', '', '')), User_abstract_('', '', '', '')) == None


from python_code import ProductDetail

def test_ProductDetail___init__():
    assert ProductDetail.__init__(ProductDetail('', '', '', '', 0, 0.0), '', '\x00', '', '', 0, 0.0) == None


from python_code import ProductShow

def test_ProductShow___init__():
    assert ProductShow.__init__(ProductShow('', '', '', '', 0, 0.0, ''), '', '', '', '', 0, 0.0, '') == None


from python_code import ProductShow2

def test_ProductShow2___init__():
    assert ProductShow2.__init__(ProductShow2('', '', '', '', 0, 0.0), '', '\x00', '', '', 0, 0.0) == None


from python_code import Shoe

def test_Shoe___init__():
    assert Shoe.__init__(Shoe('', '', '', '', '', 0, 0, 0.0, '', ''), '', '', '', '', '', 0, 0, float('nan'), '', '') == None


from python_code import User_abstract_

def test_User_abstract____init__():
    assert User_abstract_.__init__(User_abstract_('\x00\x00', '', '', ''), '', '', '', '') == None

