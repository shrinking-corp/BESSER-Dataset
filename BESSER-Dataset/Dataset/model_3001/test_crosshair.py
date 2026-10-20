from python_code import typeB_BlockB
from python_code import typeB_InPortB

def test_typeB_InPortB___init__():
    assert typeB_InPortB.__init__(typeB_InPortB('', typeB_InPortB=typeB_BlockB()), '', typeB_InPortB=typeB_BlockB()) == None


from python_code import typeB_BlockB
from python_code import typeB_OutPortB

def test_typeB_OutPortB___init__():
    assert typeB_OutPortB.__init__(typeB_OutPortB('', typeB_OutPortB4=typeB_BlockB(), typeB_OutPortB=typeB_BlockB()), '', typeB_OutPortB4=typeB_BlockB(), typeB_OutPortB=typeB_BlockB()) == None


from python_code import typeB_PortB

def test_typeB_PortB___init__():
    assert typeB_PortB.__init__(typeB_PortB(0), 0) == None

