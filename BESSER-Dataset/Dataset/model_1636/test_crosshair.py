from python_code import ptntim101_AbstractNode
from python_code import ptntim101_Place

def test_ptntim101_AbstractNode___init__():
    assert ptntim101_AbstractNode.__init__(ptntim101_AbstractNode('', 0, 0, ptntim101_AbstractNode=ptntim101_Place()), '\x00', 0, 0, ptntim101_AbstractNode=ptntim101_Place()) == None


from python_code import ptntim101_AbstractTransition
from python_code import ptntim101_Place

def test_ptntim101_AbstractTransition___init__():
    assert ptntim101_AbstractTransition.__init__(ptntim101_AbstractTransition('', ptntim101_AbstractTransition=ptntim101_Place(), ptntim101_AbstractTransition9=set()), '', ptntim101_AbstractTransition=ptntim101_Place(), ptntim101_AbstractTransition9=set()) == None


from python_code import ptntim101_Transition

def test_ptntim101_Transition___init__():
    assert ptntim101_Transition.__init__(ptntim101_Transition(0), 0) == None

