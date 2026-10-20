from python_code import effbd2_DataPort

def test_effbd2_DataPort___init__():
    assert effbd2_DataPort.__init__(effbd2_DataPort(''), '') == None


from python_code import effbd2_EffbdElement

def test_effbd2_EffbdElement___init__():
    assert effbd2_EffbdElement.__init__(effbd2_EffbdElement(''), '') == None


from python_code import effbd2_FunctionSpecification
from python_code import effbd2_Out

def test_effbd2_FunctionSpecification___init__():
    assert effbd2_FunctionSpecification.__init__(effbd2_FunctionSpecification(0, 0, '', effbd2_FunctionSpecification=set(), effbd2_FunctionSpecification10=set(), effbd2_FunctionSpecification12=set(), effbd2_FunctionSpecification14=effbd2_Out(), effbd2_FunctionSpecification16=set()), 0, 0, '', effbd2_FunctionSpecification=set(), effbd2_FunctionSpecification10=set(), effbd2_FunctionSpecification12=set(), effbd2_FunctionSpecification14=effbd2_Out(), effbd2_FunctionSpecification16=set()) == None


from python_code import effbd2_ItemContent
from python_code import effbd2_Transformed

def test_effbd2_ItemContent___init__():
    assert effbd2_ItemContent.__init__(effbd2_ItemContent('', effbd2_ItemContent=effbd2_Transformed()), '', effbd2_ItemContent=effbd2_Transformed()) == None

