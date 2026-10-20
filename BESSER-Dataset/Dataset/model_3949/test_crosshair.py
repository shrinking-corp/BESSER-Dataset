from python_code import PathExp_Bool_attrElement

def test_PathExp_Bool_attrElement___init__():
    assert PathExp_Bool_attrElement.__init__(PathExp_Bool_attrElement(True), False) == None


from python_code import PathExp_Element

def test_PathExp_Element___init__():
    assert PathExp_Element.__init__(PathExp_Element(''), '') == None


from python_code import PathExp_Internal
from python_code import PathExp_PathExp
from python_code import PathExp_Transition

def test_PathExp_Internal___init__():
    assert PathExp_Internal.__init__(PathExp_Internal(0, State=PathExp_PathExp(), State10=PathExp_Transition(), State8=PathExp_Transition()), 0, State=PathExp_PathExp(), State10=PathExp_Transition(), State8=PathExp_Transition()) == None

