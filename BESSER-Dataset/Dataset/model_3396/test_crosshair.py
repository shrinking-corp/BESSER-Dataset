from python_code import ramRoot_GenericNode
from python_code import ramRoot_MT__Element

def test_ramRoot_MT__Element___init__():
    assert ramRoot_MT__Element.__init__(ramRoot_MT__Element(False, '\x00', ramRoot_MT__Element=ramRoot_GenericNode()), False, '\x00', ramRoot_MT__Element=ramRoot_GenericNode()) == None


from python_code import ramRoot_MTpre__Element

def test_ramRoot_MTpre__Element___init__():
    assert ramRoot_MTpre__Element.__init__(ramRoot_MTpre__Element(True), False) == None

