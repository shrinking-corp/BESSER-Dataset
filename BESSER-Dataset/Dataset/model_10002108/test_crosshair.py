from python_code import Bot
from python_code import Card_Interface
from python_code import Hand

def test_Bot___init__():
    assert Bot.__init__(Bot('', Hand('\x00', card4=Card_Interface())), '\x00\x00', Hand('', card4=Card_Interface())) == None


from python_code import Card_Interface
from python_code import Hand

def test_Hand___init__():
    assert Hand.__init__(Hand('', card4=Card_Interface()), '', card4=Card_Interface()) == None


from python_code import Card_Interface
from python_code import Hand
from python_code import Human

def test_Human___init__():
    assert Human.__init__(Human('', Hand('\x00', card4=Card_Interface())), '\x00\x00', Hand('', card4=Card_Interface())) == None


from python_code import Card_Interface
from python_code import Piquet

def test_Piquet___init__():
    assert Piquet.__init__(Piquet(Card_Interface()), Card_Interface()) == None

