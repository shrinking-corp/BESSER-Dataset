from python_code import wh_Command
from python_code import wh_Commands

def test_wh_Command___init__():
    assert wh_Command.__init__(wh_Command('', wh_Command=wh_Commands()), '', wh_Command=wh_Commands()) == None

