from python_code import kiamaas_Node
from python_code import kiamaas_Plus
from python_code import kiamaas_Top

def test_kiamaas_Node___init__():
    assert kiamaas_Node.__init__(kiamaas_Node(0, 0, kiamaas_Node=kiamaas_Top(), kiamaas_Node2=kiamaas_Plus(), kiamaas_Node5=kiamaas_Plus()), 0, 0, kiamaas_Node=kiamaas_Top(), kiamaas_Node2=kiamaas_Plus(), kiamaas_Node5=kiamaas_Plus()) == None


from python_code import kiamaas_Num

def test_kiamaas_Num___init__():
    assert kiamaas_Num.__init__(kiamaas_Num(0), 0) == None

