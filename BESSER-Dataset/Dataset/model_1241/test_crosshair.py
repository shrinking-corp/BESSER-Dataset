from python_code import LogExp
from python_code import imperativeocl_AssertExp

def test_imperativeocl_AssertExp___init__():
    assert imperativeocl_AssertExp.__init__(imperativeocl_AssertExp('', imperativeocl_AssertExp=LogExp()), '', imperativeocl_AssertExp=LogExp()) == None


from python_code import imperativeocl_AssignExp

def test_imperativeocl_AssignExp___init__():
    assert imperativeocl_AssignExp.__init__(imperativeocl_AssignExp(''), '') == None


from python_code import imperativeocl_TemplateParameterType

def test_imperativeocl_TemplateParameterType___init__():
    assert imperativeocl_TemplateParameterType.__init__(imperativeocl_TemplateParameterType(''), '') == None


from python_code import imperativeocl_VariableInitExp

def test_imperativeocl_VariableInitExp___init__():
    assert imperativeocl_VariableInitExp.__init__(imperativeocl_VariableInitExp(''), '') == None

