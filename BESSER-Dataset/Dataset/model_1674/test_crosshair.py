from python_code import syswb101_Named

def test_syswb101_Named___init__():
    assert syswb101_Named.__init__(syswb101_Named(''), '') == None


from python_code import syswb101_NamedElement

def test_syswb101_NamedElement___init__():
    assert syswb101_NamedElement.__init__(syswb101_NamedElement(''), '') == None


from python_code import syswb101_System
from python_code import syswb101_Workbench

def test_syswb101_Workbench___init__():
    assert syswb101_Workbench.__init__(syswb101_Workbench('', syswb101_Workbench=set(), syswb101_Workbench2=set(), syswb101_Workbench4=syswb101_System(), syswb101_Workbench6=set(), syswb101_Workbench8=set()), '', syswb101_Workbench=set(), syswb101_Workbench2=set(), syswb101_Workbench4=syswb101_System(), syswb101_Workbench6=set(), syswb101_Workbench8=set()) == None

