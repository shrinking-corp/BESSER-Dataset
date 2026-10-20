from python_code import xtextTest_MyTokens
from python_code import xtextTest_Tokens

def test_xtextTest_MyTokens___init__():
    assert xtextTest_MyTokens.__init__(xtextTest_MyTokens('', '', 0, xtextTest_MyTokens=xtextTest_Tokens()), '\x00', '', 0, xtextTest_MyTokens=xtextTest_Tokens()) == None

