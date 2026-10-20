from python_code import PathExp_Element

def test_PathExp_Element___init__():
    assert PathExp_Element.__init__(PathExp_Element(''), '') == None


from python_code import PathExp_Final
from python_code import PathExp_PathExp
from python_code import PathExp_Transition

def test_PathExp_Final___init__():
    assert PathExp_Final.__init__(PathExp_Final(True, State=PathExp_PathExp(), State9=PathExp_Transition(), State11=PathExp_Transition()), False, State=PathExp_PathExp(), State9=PathExp_Transition(), State11=PathExp_Transition()) == None


from python_code import PathExp_Initial
from python_code import PathExp_PathExp
from python_code import PathExp_Transition

def test_PathExp_Initial___init__():
    assert PathExp_Initial.__init__(PathExp_Initial(True, State=PathExp_PathExp(), State9=PathExp_Transition(), State11=PathExp_Transition()), False, State=PathExp_PathExp(), State9=PathExp_Transition(), State11=PathExp_Transition()) == None


from python_code import PathExp_Internal
from python_code import PathExp_PathExp
from python_code import PathExp_Transition

def test_PathExp_Internal___init__():
    assert PathExp_Internal.__init__(PathExp_Internal(0, State=PathExp_PathExp(), State9=PathExp_Transition(), State11=PathExp_Transition()), 0, State=PathExp_PathExp(), State9=PathExp_Transition(), State11=PathExp_Transition()) == None

