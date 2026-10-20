from python_code import ptn104_AbstractNode
from python_code import ptn104_Place

def test_ptn104_AbstractNode___init__():
    assert ptn104_AbstractNode.__init__(ptn104_AbstractNode('', ptn104_AbstractNode=ptn104_Place()), '', ptn104_AbstractNode=ptn104_Place()) == None


from python_code import ptn104_AbstractTransition
from python_code import ptn104_Place

def test_ptn104_AbstractTransition___init__():
    assert ptn104_AbstractTransition.__init__(ptn104_AbstractTransition('', ptn104_AbstractTransition=ptn104_Place(), ptn104_AbstractTransition9=set()), '', ptn104_AbstractTransition=ptn104_Place(), ptn104_AbstractTransition9=set()) == None

