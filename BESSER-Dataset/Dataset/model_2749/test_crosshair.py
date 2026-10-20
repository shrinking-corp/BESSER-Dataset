from python_code import B_B
from python_code import B_RootB

def test_B_B___init__():
    assert B_B.__init__(B_B(0, bs=B_RootB(), B=B_RootB()), 0, bs=B_RootB(), B=B_RootB()) == None

