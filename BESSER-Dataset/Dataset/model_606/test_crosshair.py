from python_code import SMVC_List
from python_code import SMVC_SupportedOperation

def test_SMVC_SupportedOperation___init__():
    assert SMVC_SupportedOperation.__init__(SMVC_SupportedOperation('', '\x00', SMVC_SupportedOperation=SMVC_List()), '\x00\x00', '', SMVC_SupportedOperation=SMVC_List()) == None

