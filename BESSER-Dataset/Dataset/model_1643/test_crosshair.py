from python_code import kiamaas_Composite
from python_code import kiamaas_Node
from python_code import kiamaas_Top

def test_kiamaas_Node___init__():
    assert kiamaas_Node.__init__(kiamaas_Node('', '\x00', kiamaas_Node=kiamaas_Top(), kiamaas_Node2=kiamaas_Composite()), '\x00\x00', '', kiamaas_Node=kiamaas_Top(), kiamaas_Node2=kiamaas_Composite()) == None

