from python_code import eol_module_NameExpression
from python_code import eol_module_OperationDefinition

def test_eol_module_NameExpression___init__():
    assert eol_module_NameExpression.__init__(eol_module_NameExpression('', False, eol_module_NameExpression=eol_module_OperationDefinition()), '', False, eol_module_NameExpression=eol_module_OperationDefinition()) == None

