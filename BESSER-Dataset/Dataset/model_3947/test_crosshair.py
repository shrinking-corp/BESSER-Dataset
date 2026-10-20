from python_code import PathExp_Element

def test_PathExp_Element___init__():
    assert PathExp_Element.__init__(PathExp_Element(''), '') == None


from python_code import PathExp_Internal
from python_code import PathExp_PathExp
from python_code import PathExp_Transition

def test_PathExp_Internal___init__():
    assert PathExp_Internal.__init__(PathExp_Internal(0, State10=PathExp_Transition(), State8=PathExp_Transition(), State=PathExp_PathExp()), 0, State10=PathExp_Transition(), State8=PathExp_Transition(), State=PathExp_PathExp()) == None

