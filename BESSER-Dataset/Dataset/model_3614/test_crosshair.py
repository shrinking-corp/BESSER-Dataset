from python_code import r1_After

def test_r1_After___init__():
    assert r1_After.__init__(r1_After(''), '') == None


from python_code import r1_AggregateExpression
from python_code import r1_Expression

def test_r1_AggregateExpression___init__():
    assert r1_AggregateExpression.__init__(r1_AggregateExpression('', r1_AggregateExpression=r1_Expression()), '', r1_AggregateExpression=r1_Expression()) == None


from python_code import r1_AliasRef

def test_r1_AliasRef___init__():
    assert r1_AliasRef.__init__(r1_AliasRef(''), '') == None


from python_code import r1_AliasedQuerySource
from python_code import r1_Expression
from python_code import r1_Query

def test_r1_AliasedQuerySource___init__():
    assert r1_AliasedQuerySource.__init__(r1_AliasedQuerySource('', r1_AliasedQuerySource=r1_Expression(), r1_AliasedQuerySource142=r1_Query()), '', r1_AliasedQuerySource=r1_Expression(), r1_AliasedQuerySource142=r1_Query()) == None


from python_code import r1_As
from python_code import r1_TypeSpecifier

def test_r1_As___init__():
    assert r1_As.__init__(r1_As('', '\x00', r1_As=r1_TypeSpecifier()), '\x00\x00', '', r1_As=r1_TypeSpecifier()) == None


from python_code import r1_Before

def test_r1_Before___init__():
    assert r1_Before.__init__(r1_Before(''), '') == None


from python_code import r1_ByColumn

def test_r1_ByColumn___init__():
    assert r1_ByColumn.__init__(r1_ByColumn(''), '') == None


from python_code import r1_CalculateAge

def test_r1_CalculateAge___init__():
    assert r1_CalculateAge.__init__(r1_CalculateAge(''), '') == None


from python_code import r1_CalculateAgeAt

def test_r1_CalculateAgeAt___init__():
    assert r1_CalculateAgeAt.__init__(r1_CalculateAgeAt(''), '') == None


from python_code import r1_CodeSystemDef

def test_r1_CodeSystemDef___init__():
    assert r1_CodeSystemDef.__init__(r1_CodeSystemDef('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import r1_Contains

def test_r1_Contains___init__():
    assert r1_Contains.__init__(r1_Contains(''), '') == None


from python_code import r1_Convert
from python_code import r1_TypeSpecifier

def test_r1_Convert___init__():
    assert r1_Convert.__init__(r1_Convert('', r1_Convert=r1_TypeSpecifier()), '', r1_Convert=r1_TypeSpecifier()) == None


from python_code import r1_Current

def test_r1_Current___init__():
    assert r1_Current.__init__(r1_Current(''), '') == None


from python_code import r1_DateTimeComponentFrom

def test_r1_DateTimeComponentFrom___init__():
    assert r1_DateTimeComponentFrom.__init__(r1_DateTimeComponentFrom(''), '') == None


from python_code import r1_DefineClause
from python_code import r1_Expression
from python_code import r1_Query

def test_r1_DefineClause___init__():
    assert r1_DefineClause.__init__(r1_DefineClause('', r1_DefineClause=r1_Expression(), r1_DefineClause145=r1_Query()), '', r1_DefineClause=r1_Expression(), r1_DefineClause145=r1_Query()) == None


from python_code import r1_DifferenceBetween

def test_r1_DifferenceBetween___init__():
    assert r1_DifferenceBetween.__init__(r1_DifferenceBetween(''), '') == None


from python_code import r1_DurationBetween

def test_r1_DurationBetween___init__():
    assert r1_DurationBetween.__init__(r1_DurationBetween(''), '') == None


from python_code import r1_Element

def test_r1_Element___init__():
    assert r1_Element.__init__(r1_Element('', r1_Element=set()), '', r1_Element=set()) == None


from python_code import r1_Ends

def test_r1_Ends___init__():
    assert r1_Ends.__init__(r1_Ends(''), '') == None


from python_code import r1_Expression
from python_code import r1_ExpressionDef

def test_r1_ExpressionDef___init__():
    assert r1_ExpressionDef.__init__(r1_ExpressionDef('', '', '\x00\x00', r1_ExpressionDef=r1_Expression()), '', '', '', r1_ExpressionDef=r1_Expression()) == None


from python_code import r1_ExpressionRef

def test_r1_ExpressionRef___init__():
    assert r1_ExpressionRef.__init__(r1_ExpressionRef('', '\x00'), '\x00\x00', '') == None


from python_code import r1_Expression
from python_code import r1_Filter

def test_r1_Filter___init__():
    assert r1_Filter.__init__(r1_Filter('', r1_Filter=r1_Expression(), r1_Filter62=r1_Expression()), '', r1_Filter=r1_Expression(), r1_Filter62=r1_Expression()) == None


from python_code import r1_Expression
from python_code import r1_First

def test_r1_First___init__():
    assert r1_First.__init__(r1_First('', r1_First=r1_Expression()), '', r1_First=r1_Expression()) == None


from python_code import r1_Expression
from python_code import r1_ForEach

def test_r1_ForEach___init__():
    assert r1_ForEach.__init__(r1_ForEach('', r1_ForEach69=r1_Expression(), r1_ForEach=r1_Expression()), '', r1_ForEach69=r1_Expression(), r1_ForEach=r1_Expression()) == None


from python_code import r1_IdentifierRef

def test_r1_IdentifierRef___init__():
    assert r1_IdentifierRef.__init__(r1_IdentifierRef('', '\x00'), '\x00\x00', '') == None


from python_code import r1_In

def test_r1_In___init__():
    assert r1_In.__init__(r1_In(''), '') == None


from python_code import r1_IncludedIn

def test_r1_IncludedIn___init__():
    assert r1_IncludedIn.__init__(r1_IncludedIn(''), '') == None


from python_code import r1_Includes

def test_r1_Includes___init__():
    assert r1_Includes.__init__(r1_Includes(''), '') == None


from python_code import r1_Instance

def test_r1_Instance___init__():
    assert r1_Instance.__init__(r1_Instance('\x00', r1_Instance=set()), '', r1_Instance=set()) == None


from python_code import r1_Expression
from python_code import r1_Interval

def test_r1_Interval___init__():
    assert r1_Interval.__init__(r1_Interval('', '\x00', r1_Interval=r1_Expression(), r1_Interval99=r1_Expression(), r1_Interval102=r1_Expression(), r1_Interval105=r1_Expression()), '\x00\x00', '', r1_Interval=r1_Expression(), r1_Interval99=r1_Expression(), r1_Interval102=r1_Expression(), r1_Interval105=r1_Expression()) == None


from python_code import r1_Is
from python_code import r1_TypeSpecifier

def test_r1_Is___init__():
    assert r1_Is.__init__(r1_Is('', r1_Is=r1_TypeSpecifier()), '', r1_Is=r1_TypeSpecifier()) == None


from python_code import r1_Expression
from python_code import r1_Last

def test_r1_Last___init__():
    assert r1_Last.__init__(r1_Last('', r1_Last=r1_Expression()), '', r1_Last=r1_Expression()) == None


from python_code import r1_Literal

def test_r1_Literal___init__():
    assert r1_Literal.__init__(r1_Literal('', '\x00'), '\x00\x00', '') == None


from python_code import r1_MaxValue

def test_r1_MaxValue___init__():
    assert r1_MaxValue.__init__(r1_MaxValue(''), '') == None


from python_code import r1_Meets

def test_r1_Meets___init__():
    assert r1_Meets.__init__(r1_Meets(''), '') == None


from python_code import r1_MeetsAfter

def test_r1_MeetsAfter___init__():
    assert r1_MeetsAfter.__init__(r1_MeetsAfter(''), '') == None


from python_code import r1_MeetsBefore

def test_r1_MeetsBefore___init__():
    assert r1_MeetsBefore.__init__(r1_MeetsBefore(''), '') == None


from python_code import r1_MinValue

def test_r1_MinValue___init__():
    assert r1_MinValue.__init__(r1_MinValue(''), '') == None


from python_code import r1_NamedTypeSpecifier

def test_r1_NamedTypeSpecifier___init__():
    assert r1_NamedTypeSpecifier.__init__(r1_NamedTypeSpecifier(''), '') == None


from python_code import r1_Null

def test_r1_Null___init__():
    assert r1_Null.__init__(r1_Null(''), '') == None


from python_code import r1_FunctionDef
from python_code import r1_OperandDef
from python_code import r1_TypeSpecifier

def test_r1_OperandDef___init__():
    assert r1_OperandDef.__init__(r1_OperandDef('', '\x00', r1_OperandDef=r1_FunctionDef(), r1_OperandDef127=r1_TypeSpecifier()), '\x00\x00', '', r1_OperandDef=r1_FunctionDef(), r1_OperandDef127=r1_TypeSpecifier()) == None


from python_code import r1_OperandRef

def test_r1_OperandRef___init__():
    assert r1_OperandRef.__init__(r1_OperandRef(''), '') == None


from python_code import r1_Overlaps

def test_r1_Overlaps___init__():
    assert r1_Overlaps.__init__(r1_Overlaps(''), '') == None


from python_code import r1_OverlapsAfter

def test_r1_OverlapsAfter___init__():
    assert r1_OverlapsAfter.__init__(r1_OverlapsAfter(''), '') == None


from python_code import r1_OverlapsBefore

def test_r1_OverlapsBefore___init__():
    assert r1_OverlapsBefore.__init__(r1_OverlapsBefore(''), '') == None


from python_code import r1_Expression
from python_code import r1_ParameterDef
from python_code import r1_TypeSpecifier

def test_r1_ParameterDef___init__():
    assert r1_ParameterDef.__init__(r1_ParameterDef('', '', '\x00\x00', r1_ParameterDef=r1_Expression(), r1_ParameterDef132=r1_TypeSpecifier()), '', '', '', r1_ParameterDef=r1_Expression(), r1_ParameterDef132=r1_TypeSpecifier()) == None


from python_code import r1_ParameterRef

def test_r1_ParameterRef___init__():
    assert r1_ParameterRef.__init__(r1_ParameterRef('', '\x00'), '\x00\x00', '') == None


from python_code import r1_ProperContains

def test_r1_ProperContains___init__():
    assert r1_ProperContains.__init__(r1_ProperContains(''), '') == None


from python_code import r1_ProperIn

def test_r1_ProperIn___init__():
    assert r1_ProperIn.__init__(r1_ProperIn(''), '') == None


from python_code import r1_ProperIncludedIn

def test_r1_ProperIncludedIn___init__():
    assert r1_ProperIncludedIn.__init__(r1_ProperIncludedIn(''), '') == None


from python_code import r1_ProperIncludes

def test_r1_ProperIncludes___init__():
    assert r1_ProperIncludes.__init__(r1_ProperIncludes(''), '') == None


from python_code import r1_Expression
from python_code import r1_Property

def test_r1_Property___init__():
    assert r1_Property.__init__(r1_Property('', '\x00', r1_Property=r1_Expression()), '\x00\x00', '', r1_Property=r1_Expression()) == None


from python_code import r1_Quantity

def test_r1_Quantity___init__():
    assert r1_Quantity.__init__(r1_Quantity('', '\x00'), '\x00\x00', '') == None


from python_code import r1_QueryDefineRef

def test_r1_QueryDefineRef___init__():
    assert r1_QueryDefineRef.__init__(r1_QueryDefineRef(''), '') == None


from python_code import r1_Expression
from python_code import r1_Retrieve

def test_r1_Retrieve___init__():
    assert r1_Retrieve.__init__(r1_Retrieve('', '', '', '', '', '', '\x00', '', r1_Retrieve=r1_Expression(), r1_Retrieve161=r1_Expression()), '', '', '', '', '', '', '', '', r1_Retrieve=r1_Expression(), r1_Retrieve161=r1_Expression()) == None


from python_code import r1_Expression
from python_code import r1_Query
from python_code import r1_ReturnClause

def test_r1_ReturnClause___init__():
    assert r1_ReturnClause.__init__(r1_ReturnClause('', r1_ReturnClause=r1_Query(), r1_ReturnClause164=r1_Expression()), '', r1_ReturnClause=r1_Query(), r1_ReturnClause164=r1_Expression()) == None


from python_code import r1_SameAs

def test_r1_SameAs___init__():
    assert r1_SameAs.__init__(r1_SameAs(''), '') == None


from python_code import r1_SameOrAfter

def test_r1_SameOrAfter___init__():
    assert r1_SameOrAfter.__init__(r1_SameOrAfter(''), '') == None


from python_code import r1_SameOrBefore

def test_r1_SameOrBefore___init__():
    assert r1_SameOrBefore.__init__(r1_SameOrBefore(''), '') == None


from python_code import r1_Sort
from python_code import r1_SortByItem
from python_code import r1_SortClause

def test_r1_SortByItem___init__():
    assert r1_SortByItem.__init__(r1_SortByItem('', r1_SortByItem=r1_Sort(), r1_SortByItem177=r1_SortClause()), '', r1_SortByItem=r1_Sort(), r1_SortByItem177=r1_SortClause()) == None


from python_code import r1_Starts

def test_r1_Starts___init__():
    assert r1_Starts.__init__(r1_Starts(''), '') == None


from python_code import r1_Expression
from python_code import r1_Tuple
from python_code import r1_TupleElement

def test_r1_TupleElement___init__():
    assert r1_TupleElement.__init__(r1_TupleElement('', r1_TupleElement=r1_Tuple(), r1_TupleElement209=r1_Expression()), '', r1_TupleElement=r1_Tuple(), r1_TupleElement209=r1_Expression()) == None


from python_code import r1_TupleElementDefinition
from python_code import r1_TupleTypeSpecifier
from python_code import r1_TypeSpecifier

def test_r1_TupleElementDefinition___init__():
    assert r1_TupleElementDefinition.__init__(r1_TupleElementDefinition('', r1_TupleElementDefinition=r1_TypeSpecifier(), r1_TupleElementDefinition214=r1_TupleTypeSpecifier()), '', r1_TupleElementDefinition=r1_TypeSpecifier(), r1_TupleElementDefinition214=r1_TupleTypeSpecifier()) == None


from python_code import r1_ValueSetDef

def test_r1_ValueSetDef___init__():
    assert r1_ValueSetDef.__init__(r1_ValueSetDef('', '', '', '', r1_ValueSetDef=set()), '', '', '', '', r1_ValueSetDef=set()) == None


from python_code import r1_InValueSet
from python_code import r1_ValueSetRef

def test_r1_ValueSetRef___init__():
    assert r1_ValueSetRef.__init__(r1_ValueSetRef('', '\x00', r1_ValueSetRef=r1_InValueSet()), '\x00\x00', '', r1_ValueSetRef=r1_InValueSet()) == None

