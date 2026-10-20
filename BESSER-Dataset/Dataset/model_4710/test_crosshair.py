from python_code import SOS_adtmm_ADT

def test_SOS_adtmm_ADT___init__():
    assert SOS_adtmm_ADT.__init__(SOS_adtmm_ADT('\x00', SOS_adtmm_ADT=set(), SOS_adtmm_ADT43=set(), SOS_adtmm_ADT45=set(), SOS_adtmm_ADT48=set(), SOS_adtmm_ADT51=set()), '', SOS_adtmm_ADT=set(), SOS_adtmm_ADT43=set(), SOS_adtmm_ADT45=set(), SOS_adtmm_ADT48=set(), SOS_adtmm_ADT51=set()) == None


from python_code import SOS_adtmm_AbstractOperation

def test_SOS_adtmm_AbstractOperation___init__():
    assert SOS_adtmm_AbstractOperation.__init__(SOS_adtmm_AbstractOperation(''), '') == None


from python_code import SOS_adtmm_SortDeclaration

def test_SOS_adtmm_SortDeclaration___init__():
    assert SOS_adtmm_SortDeclaration.__init__(SOS_adtmm_SortDeclaration(''), '') == None


from python_code import SOS_adtmm_Variable
from python_code import Sort

def test_SOS_adtmm_Variable___init__():
    assert SOS_adtmm_Variable.__init__(SOS_adtmm_Variable('', SOS_adtmm_Variable=Sort()), '', SOS_adtmm_Variable=Sort()) == None


from python_code import SOS_adtmm_Operation
from python_code import SOS_adtmm_Variable
from python_code import SOS_set_ModelSort
from python_code import SOS_set_Set
from python_code import Sort

def test_SOS_set_ModelSort___init__():
    assert SOS_set_ModelSort.__init__(SOS_set_ModelSort('', '', Sort100=SOS_set_Set(), Sort57=SOS_adtmm_Variable('', SOS_adtmm_Variable=Sort()), Sort=SOS_adtmm_Operation(), Sort55=SOS_adtmm_Operation()), '', '', Sort100=SOS_set_Set(), Sort57=SOS_adtmm_Variable('', SOS_adtmm_Variable=Sort()), Sort=SOS_adtmm_Operation(), Sort55=SOS_adtmm_Operation()) == None

