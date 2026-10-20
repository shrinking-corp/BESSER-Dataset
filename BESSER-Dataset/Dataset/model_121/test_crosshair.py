from python_code import ccsl_CompositeRule

def test_ccsl_CompositeRule___init__():
    assert ccsl_CompositeRule.__init__(ccsl_CompositeRule('\x00', ccsl_CompositeRule=set()), '', ccsl_CompositeRule=set()) == None


from python_code import InjectionStrategy
from python_code import ccsl_AtomicRule
from python_code import ccsl_FaultTypeDescription

def test_ccsl_FaultTypeDescription___init__():
    assert ccsl_FaultTypeDescription.__init__(ccsl_FaultTypeDescription('\x00\x00', ccsl_FaultTypeDescription=ccsl_AtomicRule(), ccsl_FaultTypeDescription7=set(), ccsl_FaultTypeDescription9=InjectionStrategy()), '', ccsl_FaultTypeDescription=ccsl_AtomicRule(), ccsl_FaultTypeDescription7=set(), ccsl_FaultTypeDescription9=InjectionStrategy()) == None


from python_code import ccsl_action_ArithmeticOperatorMap

def test_ccsl_action_ArithmeticOperatorMap___init__():
    assert ccsl_action_ArithmeticOperatorMap.__init__(ccsl_action_ArithmeticOperatorMap('', '\x00'), '\x00\x00', '') == None


from python_code import ccsl_assignment_Assignment
from python_code import statements_Statement

def test_ccsl_assignment_Assignment___init__():
    assert ccsl_assignment_Assignment.__init__(ccsl_assignment_Assignment('', ccsl_assignment_Assignment=statements_Statement()), '', ccsl_assignment_Assignment=statements_Statement()) == None


from python_code import ccsl_assignment_UnaryAssignment

def test_ccsl_assignment_UnaryAssignment___init__():
    assert ccsl_assignment_UnaryAssignment.__init__(ccsl_assignment_UnaryAssignment(''), '') == None


from python_code import ccsl_controlFlow_SwitchCaseBlock

def test_ccsl_controlFlow_SwitchCaseBlock___init__():
    assert ccsl_controlFlow_SwitchCaseBlock.__init__(ccsl_controlFlow_SwitchCaseBlock(''), '') == None


from python_code import ccsl_datatype_ArrayType
from python_code import datatype_DataType

def test_ccsl_datatype_ArrayType___init__():
    assert ccsl_datatype_ArrayType.__init__(ccsl_datatype_ArrayType('', ccsl_datatype_ArrayType=datatype_DataType()), '', ccsl_datatype_ArrayType=datatype_DataType()) == None


from python_code import ccsl_elements_Element

def test_ccsl_elements_Element___init__():
    assert ccsl_elements_Element.__init__(ccsl_elements_Element(''), '') == None


from python_code import ccsl_expressions_ArithmeticExpression

def test_ccsl_expressions_ArithmeticExpression___init__():
    assert ccsl_expressions_ArithmeticExpression.__init__(ccsl_expressions_ArithmeticExpression(''), '') == None


from python_code import ccsl_expressions_BooleanExpression

def test_ccsl_expressions_BooleanExpression___init__():
    assert ccsl_expressions_BooleanExpression.__init__(ccsl_expressions_BooleanExpression(''), '') == None


from python_code import ccsl_filters_CompositeFilter

def test_ccsl_filters_CompositeFilter___init__():
    assert ccsl_filters_CompositeFilter.__init__(ccsl_filters_CompositeFilter('', ccsl_filters_CompositeFilter=set()), '', ccsl_filters_CompositeFilter=set()) == None


from python_code import Element
from python_code import ccsl_filters_CountFilter

def test_ccsl_filters_CountFilter___init__():
    assert ccsl_filters_CountFilter.__init__(ccsl_filters_CountFilter('', '', ccsl_filters_CountFilter=set(), ccsl_filters_CountFilter130=Element(), ccsl_filters_CountFilter133=Element()), '', '', ccsl_filters_CountFilter=set(), ccsl_filters_CountFilter130=Element(), ccsl_filters_CountFilter133=Element()) == None


from python_code import ccsl_filters_EquationFilter

def test_ccsl_filters_EquationFilter___init__():
    assert ccsl_filters_EquationFilter.__init__(ccsl_filters_EquationFilter('', ccsl_filters_EquationFilter=set(), ccsl_filters_EquationFilter171=set()), '', ccsl_filters_EquationFilter=set(), ccsl_filters_EquationFilter171=set()) == None


from python_code import ccsl_filters_Filter

def test_ccsl_filters_Filter___init__():
    assert ccsl_filters_Filter.__init__(ccsl_filters_Filter(''), '') == None


from python_code import ccsl_filters_RegexMatch

def test_ccsl_filters_RegexMatch___init__():
    assert ccsl_filters_RegexMatch.__init__(ccsl_filters_RegexMatch(''), '') == None


from python_code import ccsl_filters_SameNameFilter

def test_ccsl_filters_SameNameFilter___init__():
    assert ccsl_filters_SameNameFilter.__init__(ccsl_filters_SameNameFilter('', ccsl_filters_SameNameFilter=set()), '\x00', ccsl_filters_SameNameFilter=set()) == None


from python_code import Context
from python_code import ccsl_filters_SuperClassClosureFilter
from python_code import complexType_JClass

def test_ccsl_filters_SuperClassClosureFilter___init__():
    assert ccsl_filters_SuperClassClosureFilter.__init__(ccsl_filters_SuperClassClosureFilter('', ccsl_filters_SuperClassClosureFilter=complexType_JClass(), ccsl_filters_SuperClassClosureFilter183=complexType_JClass(), ccsl_filters_SuperClassClosureFilter186=Context()), '', ccsl_filters_SuperClassClosureFilter=complexType_JClass(), ccsl_filters_SuperClassClosureFilter183=complexType_JClass(), ccsl_filters_SuperClassClosureFilter186=Context()) == None


from python_code import ccsl_invocation_Invocation

def test_ccsl_invocation_Invocation___init__():
    assert ccsl_invocation_Invocation.__init__(ccsl_invocation_Invocation('', ccsl_invocation_Invocation=set()), '', ccsl_invocation_Invocation=set()) == None


from python_code import ccsl_literalValues_LiteralValue

def test_ccsl_literalValues_LiteralValue___init__():
    assert ccsl_literalValues_LiteralValue.__init__(ccsl_literalValues_LiteralValue(''), '') == None


from python_code import ccsl_method_Constructor

def test_ccsl_method_Constructor___init__():
    assert ccsl_method_Constructor.__init__(ccsl_method_Constructor(''), '') == None


from python_code import ccsl_filters_SameNameFilter
from python_code import ccsl_method_Method
from python_code import datatype_DataType

def test_ccsl_method_Method___init__():
    assert ccsl_method_Method.__init__(ccsl_method_Method('', '', '', '', ccsl_method_Method=datatype_DataType(), namedElements_NamedElement=ccsl_filters_SameNameFilter('', ccsl_filters_SameNameFilter=set())), '', '', '', '', ccsl_method_Method=datatype_DataType(), namedElements_NamedElement=ccsl_filters_SameNameFilter('\x00', ccsl_filters_SameNameFilter=set())) == None


from python_code import ccsl_method_SimpleMethod

def test_ccsl_method_SimpleMethod___init__():
    assert ccsl_method_SimpleMethod.__init__(ccsl_method_SimpleMethod('\x00\x00', '', ccsl_method_SimpleMethod=set()), '', '', ccsl_method_SimpleMethod=set()) == None


from python_code import Element
from python_code import ccsl_AtomicRule
from python_code import ccsl_context_Context
from python_code import ccsl_datatype_DataType
from python_code import ccsl_faultTypeDescription_InjectionAction
from python_code import ccsl_filters_AtomicFilter
from python_code import ccsl_filters_CountFilter
from python_code import ccsl_filters_ImplicityContainerFilter
from python_code import ccsl_filters_ImplicityOperandFilter
from python_code import ccsl_filters_TemplateFilter
from python_code import ccsl_namedElements_NamedElement
from python_code import ccsl_numberFunctions_GetIndexOf
from python_code import ccsl_statements_Access

def test_ccsl_namedElements_NamedElement___init__():
    assert ccsl_namedElements_NamedElement.__init__(ccsl_namedElements_NamedElement('', '', Element45=ccsl_statements_Access(), Element194=ccsl_numberFunctions_GetIndexOf(), Element131=ccsl_filters_CountFilter('', '', ccsl_filters_CountFilter=set(), ccsl_filters_CountFilter130=ccsl_datatype_DataType(), ccsl_filters_CountFilter133=Element()), Element=ccsl_AtomicRule(), Element134=ccsl_filters_CountFilter('', '', ccsl_filters_CountFilter=set(), ccsl_filters_CountFilter130=Element(), ccsl_filters_CountFilter133=Element()), Element140=ccsl_filters_ImplicityContainerFilter(), Element118=ccsl_filters_AtomicFilter(), Element136=ccsl_filters_ImplicityOperandFilter(), Element115=ccsl_faultTypeDescription_InjectionAction(), Element122=ccsl_filters_TemplateFilter(), Element143=ccsl_filters_ImplicityContainerFilter(), Element111=ccsl_context_Context(), Element197=ccsl_numberFunctions_GetIndexOf()), '', '', Element45=ccsl_statements_Access(), Element194=ccsl_numberFunctions_GetIndexOf(), Element131=ccsl_filters_CountFilter('', '', ccsl_filters_CountFilter=set(), ccsl_filters_CountFilter130=Element(), ccsl_filters_CountFilter133=Element()), Element=ccsl_AtomicRule(), Element134=ccsl_filters_CountFilter('', '', ccsl_filters_CountFilter=set(), ccsl_filters_CountFilter130=Element(), ccsl_filters_CountFilter133=Element()), Element140=ccsl_filters_ImplicityContainerFilter(), Element118=ccsl_filters_AtomicFilter(), Element136=ccsl_filters_ImplicityOperandFilter(), Element115=ccsl_faultTypeDescription_InjectionAction(), Element122=ccsl_filters_TemplateFilter(), Element143=ccsl_filters_ImplicityContainerFilter(), Element111=ccsl_context_Context(), Element197=ccsl_numberFunctions_GetIndexOf()) == None


from python_code import ccsl_numberFunctions_CcslIntegerLiteral

def test_ccsl_numberFunctions_CcslIntegerLiteral___init__():
    assert ccsl_numberFunctions_CcslIntegerLiteral.__init__(ccsl_numberFunctions_CcslIntegerLiteral(''), '') == None


from python_code import ccsl_statements_Block

def test_ccsl_statements_Block___init__():
    assert ccsl_statements_Block.__init__(ccsl_statements_Block('', ccsl_statements_Block=set()), '', ccsl_statements_Block=set()) == None


from python_code import ccsl_statements_InstanceCreation
from python_code import datatype_ObjectType
from python_code import method_Constructor

def test_ccsl_statements_InstanceCreation___init__():
    assert ccsl_statements_InstanceCreation.__init__(ccsl_statements_InstanceCreation('', ccsl_statements_InstanceCreation=datatype_ObjectType(), ccsl_statements_InstanceCreation39=method_Constructor(), ccsl_statements_InstanceCreation42=set()), '', ccsl_statements_InstanceCreation=datatype_ObjectType(), ccsl_statements_InstanceCreation39=method_Constructor(), ccsl_statements_InstanceCreation42=set()) == None


from python_code import ccsl_variable_FieldVariable

def test_ccsl_variable_FieldVariable___init__():
    assert ccsl_variable_FieldVariable.__init__(ccsl_variable_FieldVariable('', '\x00'), '\x00\x00', '') == None


from python_code import ccsl_variable_Variable
from python_code import datatype_DataType

def test_ccsl_variable_Variable___init__():
    assert ccsl_variable_Variable.__init__(ccsl_variable_Variable('', ccsl_variable_Variable=datatype_DataType()), '', ccsl_variable_Variable=datatype_DataType()) == None

