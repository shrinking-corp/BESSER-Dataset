from python_code import refinher3_DNamedElement

def test_refinher3_DNamedElement___init__():
    assert refinher3_DNamedElement.__init__(refinher3_DNamedElement(''), '') == None


from python_code import refinher3_DG
from python_code import refinher3_M

def test_refinher3_M___init__():
    assert refinher3_M.__init__(refinher3_M('', refinher3_M=refinher3_DG(), refinher3_M13=set(), refinher3_M16=set()), '', refinher3_M=refinher3_DG(), refinher3_M13=set(), refinher3_M16=set()) == None


from python_code import refinher3_DG
from python_code import refinher3_E
from python_code import refinher3_N

def test_refinher3_N___init__():
    assert refinher3_N.__init__(refinher3_N('', refinher3_N=refinher3_E(), refinher3_N3=refinher3_E(), refinher3_N9=refinher3_DG()), '', refinher3_N=refinher3_E(), refinher3_N3=refinher3_E(), refinher3_N9=refinher3_DG()) == None

