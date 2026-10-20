from python_code import kernel_commons_NamedElement

def test_kernel_commons_NamedElement___init__():
    assert kernel_commons_NamedElement.__init__(kernel_commons_NamedElement(''), '') == None


from python_code import kernel_expressions_Expression
from python_code import kernel_statements_Jump

def test_kernel_expressions_Expression___init__():
    assert kernel_expressions_Expression.__init__(kernel_expressions_Expression(kernel_expressions_Expression=set(), LabellableElement=kernel_statements_Jump()), kernel_expressions_Expression=set(), LabellableElement=kernel_statements_Jump()) == None

def test_kernel_expressions_Expression_getUsedVariables():
    assert kernel_expressions_Expression.getUsedVariables(kernel_expressions_Expression(kernel_expressions_Expression=set(), LabellableElement=kernel_statements_Jump())) == None

def test_kernel_expressions_Expression_getDefinedVariables():
    assert kernel_expressions_Expression.getDefinedVariables(kernel_expressions_Expression(kernel_expressions_Expression=set(), LabellableElement=kernel_statements_Jump())) == None


from python_code import kernel_parameters_Parameter

def test_kernel_parameters_Parameter___init__():
    assert kernel_parameters_Parameter.__init__(kernel_parameters_Parameter('', False), '', False) == None


from python_code import kernel_references_Argument

def test_kernel_references_Argument___init__():
    assert kernel_references_Argument.__init__(kernel_references_Argument()) == None

def test_kernel_references_Argument_getCorrespondingParameter():
    assert kernel_references_Argument.getCorrespondingParameter(kernel_references_Argument()) == None


from python_code import kernel_statements_ParallelBlock

def test_kernel_statements_ParallelBlock___init__():
    assert kernel_statements_ParallelBlock.__init__(kernel_statements_ParallelBlock(''), '') == None

