from python_code import ptn_AbstractNode
from python_code import ptn_Place

def test_ptn_AbstractNode___init__():
    assert ptn_AbstractNode.__init__(ptn_AbstractNode(0, '', 0, ptn_AbstractNode=ptn_Place()), 0, '', 0, ptn_AbstractNode=ptn_Place()) == None


from python_code import ptn_AbstractTransition
from python_code import ptn_Place

def test_ptn_AbstractTransition___init__():
    assert ptn_AbstractTransition.__init__(ptn_AbstractTransition('', ptn_AbstractTransition9=set(), ptn_AbstractTransition=ptn_Place()), '', ptn_AbstractTransition9=set(), ptn_AbstractTransition=ptn_Place()) == None


from python_code import ptn_Transition

def test_ptn_Transition___init__():
    assert ptn_Transition.__init__(ptn_Transition(0), 0) == None

