from python_code import scxml_CondEventTransition
from python_code import scxml_TransitionSource

def test_scxml_CondEventTransition___init__():
    assert scxml_CondEventTransition.__init__(scxml_CondEventTransition('', '\x00', scxml_CondEventTransition=scxml_TransitionSource()), '\x00\x00', '', scxml_CondEventTransition=scxml_TransitionSource()) == None


from python_code import scxml_Conditional

def test_scxml_Conditional___init__():
    assert scxml_Conditional.__init__(scxml_Conditional(''), '') == None


from python_code import scxml_Content

def test_scxml_Content___init__():
    assert scxml_Content.__init__(scxml_Content(''), '') == None


from python_code import scxml_HistoryState
from python_code import scxml_State

def test_scxml_HistoryState___init__():
    assert scxml_HistoryState.__init__(scxml_HistoryState('', scxml_HistoryState=scxml_State()), '', scxml_HistoryState=scxml_State()) == None


from python_code import scxml_Donedata
from python_code import scxml_Param

def test_scxml_Param___init__():
    assert scxml_Param.__init__(scxml_Param('', '\x00', scxml_Param=scxml_Donedata()), '\x00\x00', '', scxml_Param=scxml_Donedata()) == None


from python_code import scxml_AbstractSimpleState
from python_code import scxml_Transition
from python_code import scxml_TransitionTarget

def test_scxml_TransitionTarget___init__():
    assert scxml_TransitionTarget.__init__(scxml_TransitionTarget('', scxml_TransitionTarget=scxml_Transition(), scxml_TransitionTarget18=scxml_AbstractSimpleState()), '', scxml_TransitionTarget=scxml_Transition(), scxml_TransitionTarget18=scxml_AbstractSimpleState()) == None


from python_code import scxml_EClass
from python_code import scxml_XObject

def test_scxml_XObject___init__():
    assert scxml_XObject.__init__(scxml_XObject('', '', False, scxml_XObject=scxml_EClass()), '\x00', '', False, scxml_XObject=scxml_EClass()) == None

def test_scxml_XObject_registerAdapter():
    assert scxml_XObject.registerAdapter(scxml_XObject('', '', False, scxml_XObject=scxml_EClass())) == None

