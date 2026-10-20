from python_code import EFM_Cardinality

def test_EFM_Cardinality___init__():
    assert EFM_Cardinality.__init__(EFM_Cardinality(0, 0, 0), 0, 0, 0) == None


from python_code import EFM_Comparison
from python_code import EFM_FMElement

def test_EFM_Comparison___init__():
    assert EFM_Comparison.__init__(EFM_Comparison('', EFM_Comparison=EFM_FMElement(), EFM_Comparison32=EFM_FMElement()), '', EFM_Comparison=EFM_FMElement(), EFM_Comparison32=EFM_FMElement()) == None


from python_code import EFM_Operation
from python_code import EFM_Requires

def test_EFM_Requires___init__():
    assert EFM_Requires.__init__(EFM_Requires('', EFM_Requires=set(), EFM_Requires23=EFM_Operation()), '', EFM_Requires=set(), EFM_Requires23=EFM_Operation()) == None

