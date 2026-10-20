from python_code import OclTest_Apple
from python_code import OclTest_Stem

def test_OclTest_Apple___init__():
    assert OclTest_Apple.__init__(OclTest_Apple('', OclTest_Apple=OclTest_Stem()), '', OclTest_Apple=OclTest_Stem()) == None

def test_OclTest_Apple_label():
    assert OclTest_Apple.label(OclTest_Apple('', OclTest_Apple=OclTest_Stem()), 0) == None

def test_OclTest_Apple_preferredLabel():
    assert OclTest_Apple.preferredLabel(OclTest_Apple('', OclTest_Apple=OclTest_Stem()), 0) == None

def test_OclTest_Apple_newApple():
    assert OclTest_Apple.newApple(OclTest_Apple('', OclTest_Apple=OclTest_Stem())) == None


from python_code import OclTest_Tree

def test_OclTest_Tree___init__():
    assert OclTest_Tree.__init__(OclTest_Tree('', OclTest_Tree=set(), OclTest_Tree17=set()), '', OclTest_Tree=set(), OclTest_Tree17=set()) == None

