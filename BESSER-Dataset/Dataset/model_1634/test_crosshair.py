from python_code import ptn103_AbstractNode
from python_code import ptn103_Place

def test_ptn103_AbstractNode___init__():
    assert ptn103_AbstractNode.__init__(ptn103_AbstractNode('', ptn103_AbstractNode=ptn103_Place()), '', ptn103_AbstractNode=ptn103_Place()) == None


from python_code import ptn103_AbstractTransition
from python_code import ptn103_Place

def test_ptn103_AbstractTransition___init__():
    assert ptn103_AbstractTransition.__init__(ptn103_AbstractTransition('', ptn103_AbstractTransition=ptn103_Place(), ptn103_AbstractTransition9=set()), '', ptn103_AbstractTransition=ptn103_Place(), ptn103_AbstractTransition9=set()) == None

