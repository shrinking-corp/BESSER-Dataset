from python_code import NestedClass1
from python_code import root_RootClass

def test_root_RootClass___init__():
    assert root_RootClass.__init__(root_RootClass('', root_RootClass=NestedClass1()), '', root_RootClass=NestedClass1()) == None


from python_code import NestedClass1
from python_code import root_noLiterals_NoLitClass

def test_root_noLiterals_NoLitClass___init__():
    assert root_noLiterals_NoLitClass.__init__(root_noLiterals_NoLitClass('', root_noLiterals_NoLitClass=NestedClass1()), '', root_noLiterals_NoLitClass=NestedClass1()) == None

