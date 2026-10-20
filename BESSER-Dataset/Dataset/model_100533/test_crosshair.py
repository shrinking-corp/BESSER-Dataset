from python_code import UseCaseDSL_ExceptionFlow

def test_UseCaseDSL_ExceptionFlow___init__():
    assert UseCaseDSL_ExceptionFlow.__init__(UseCaseDSL_ExceptionFlow(''), '') == None


from python_code import UseCaseDSL_AlternativeFlowAlternative
from python_code import UseCaseDSL_NamedFlow

def test_UseCaseDSL_NamedFlow___init__():
    assert UseCaseDSL_NamedFlow.__init__(UseCaseDSL_NamedFlow('', UseCaseDSL_NamedFlow=UseCaseDSL_AlternativeFlowAlternative()), '', UseCaseDSL_NamedFlow=UseCaseDSL_AlternativeFlowAlternative()) == None

