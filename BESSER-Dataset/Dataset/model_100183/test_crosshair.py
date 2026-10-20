from python_code import sparql_BlankNode

def test_sparql_BlankNode___init__():
    assert sparql_BlankNode.__init__(sparql_BlankNode(''), '') == None


from python_code import sparql_ClearGraphQuery

def test_sparql_ClearGraphQuery___init__():
    assert sparql_ClearGraphQuery.__init__(sparql_ClearGraphQuery('', False), '', False) == None


from python_code import sparql_CountAggregate
from python_code import sparql_Expression

def test_sparql_CountAggregate___init__():
    assert sparql_CountAggregate.__init__(sparql_CountAggregate(False, False, sparql_CountAggregate=sparql_Expression()), False, False, sparql_CountAggregate=sparql_Expression()) == None


from python_code import sparql_CreateGraphQuery

def test_sparql_CreateGraphQuery___init__():
    assert sparql_CreateGraphQuery.__init__(sparql_CreateGraphQuery('', '\x00'), '\x00\x00', '') == None


from python_code import sparql_DeleteDataQuery

def test_sparql_DeleteDataQuery___init__():
    assert sparql_DeleteDataQuery.__init__(sparql_DeleteDataQuery(''), '') == None


from python_code import sparql_DeleteQuery
from python_code import sparql_GroupGraphPattern
from python_code import sparql_WhereClause

def test_sparql_DeleteQuery___init__():
    assert sparql_DeleteQuery.__init__(sparql_DeleteQuery('', sparql_DeleteQuery25=sparql_WhereClause(), sparql_DeleteQuery=sparql_GroupGraphPattern()), '', sparql_DeleteQuery25=sparql_WhereClause(), sparql_DeleteQuery=sparql_GroupGraphPattern()) == None


from python_code import sparql_DropGraphQuery

def test_sparql_DropGraphQuery___init__():
    assert sparql_DropGraphQuery.__init__(sparql_DropGraphQuery('', '\x00'), '\x00\x00', '') == None


from python_code import sparql_AvgAggregate
from python_code import sparql_ExprAggArg
from python_code import sparql_Expression
from python_code import sparql_MaxAggregate
from python_code import sparql_MinAgregate
from python_code import sparql_SampleAggregate
from python_code import sparql_SumAggregate

def test_sparql_ExprAggArg___init__():
    assert sparql_ExprAggArg.__init__(sparql_ExprAggArg(True, sparql_ExprAggArg122=sparql_SumAggregate(), sparql_ExprAggArg124=sparql_MinAgregate(), sparql_ExprAggArg126=sparql_MaxAggregate(), sparql_ExprAggArg128=sparql_AvgAggregate(), sparql_ExprAggArg130=sparql_SampleAggregate(), sparql_ExprAggArg=sparql_Expression()), False, sparql_ExprAggArg122=sparql_SumAggregate(), sparql_ExprAggArg124=sparql_MinAgregate(), sparql_ExprAggArg126=sparql_MaxAggregate(), sparql_ExprAggArg128=sparql_AvgAggregate(), sparql_ExprAggArg130=sparql_SampleAggregate(), sparql_ExprAggArg=sparql_Expression()) == None


from python_code import sparql_ExpressionFilterExpression
from python_code import sparql_FilterNode

def test_sparql_ExpressionFilterExpression___init__():
    assert sparql_ExpressionFilterExpression.__init__(sparql_ExpressionFilterExpression('', sparql_ExpressionFilterExpression=sparql_FilterNode(), sparql_ExpressionFilterExpression82=sparql_FilterNode()), '', sparql_ExpressionFilterExpression=sparql_FilterNode(), sparql_ExpressionFilterExpression82=sparql_FilterNode()) == None


from python_code import sparql_Function

def test_sparql_Function___init__():
    assert sparql_Function.__init__(sparql_Function('', sparql_Function=set()), '', sparql_Function=set()) == None


from python_code import sparql_GroupAggregate

def test_sparql_GroupAggregate___init__():
    assert sparql_GroupAggregate.__init__(sparql_GroupAggregate(False, '\x00', sparql_GroupAggregate=set()), False, '', sparql_GroupAggregate=set()) == None


from python_code import sparql_Base
from python_code import sparql_DatasetClause
from python_code import sparql_IRI

def test_sparql_IRI___init__():
    assert sparql_IRI.__init__(sparql_IRI('', sparql_IRI29=sparql_DatasetClause(), sparql_IRI=sparql_Base()), '', sparql_IRI29=sparql_DatasetClause(), sparql_IRI=sparql_Base()) == None


from python_code import sparql_InsertDataQuery

def test_sparql_InsertDataQuery___init__():
    assert sparql_InsertDataQuery.__init__(sparql_InsertDataQuery(''), '') == None


from python_code import sparql_InsertQuery
from python_code import sparql_WhereClause

def test_sparql_InsertQuery___init__():
    assert sparql_InsertQuery.__init__(sparql_InsertQuery('', sparql_InsertQuery=sparql_WhereClause()), '', sparql_InsertQuery=sparql_WhereClause()) == None


from python_code import sparql_IntegerValue

def test_sparql_IntegerValue___init__():
    assert sparql_IntegerValue.__init__(sparql_IntegerValue(0), 0) == None


from python_code import sparql_LangTag

def test_sparql_LangTag___init__():
    assert sparql_LangTag.__init__(sparql_LangTag(''), '') == None


from python_code import sparql_LimitClause
from python_code import sparql_SelectionQuery

def test_sparql_LimitClause___init__():
    assert sparql_LimitClause.__init__(sparql_LimitClause(0, sparql_LimitClause=sparql_SelectionQuery()), 0, sparql_LimitClause=sparql_SelectionQuery()) == None


from python_code import sparql_LoadGraphQuery

def test_sparql_LoadGraphQuery___init__():
    assert sparql_LoadGraphQuery.__init__(sparql_LoadGraphQuery('', '\x00'), '\x00\x00', '') == None


from python_code import sparql_GroupGraphPattern
from python_code import sparql_ModifyQuery

def test_sparql_ModifyQuery___init__():
    assert sparql_ModifyQuery.__init__(sparql_ModifyQuery('', sparql_ModifyQuery=sparql_GroupGraphPattern()), '', sparql_ModifyQuery=sparql_GroupGraphPattern()) == None


from python_code import sparql_Parameter

def test_sparql_Parameter___init__():
    assert sparql_Parameter.__init__(sparql_Parameter(''), '') == None


from python_code import sparql_NamedFunction
from python_code import sparql_NamedVariable
from python_code import sparql_Prefix
from python_code import sparql_SPARQLQuery

def test_sparql_Prefix___init__():
    assert sparql_Prefix.__init__(sparql_Prefix('', '\x00', sparql_Prefix=sparql_SPARQLQuery(), sparql_Prefix87=sparql_NamedFunction(), sparql_Prefix111=sparql_NamedVariable()), '\x00\x00', '', sparql_Prefix=sparql_SPARQLQuery(), sparql_Prefix87=sparql_NamedFunction(), sparql_Prefix111=sparql_NamedVariable()) == None


from python_code import sparql_SelectQuery

def test_sparql_SelectQuery___init__():
    assert sparql_SelectQuery.__init__(sparql_SelectQuery(False, False, False, sparql_SelectQuery=set()), False, False, True, sparql_SelectQuery=set()) == None


from python_code import sparql_StringValue

def test_sparql_StringValue___init__():
    assert sparql_StringValue.__init__(sparql_StringValue(''), '') == None


from python_code import sparql_UsingGraph

def test_sparql_UsingGraph___init__():
    assert sparql_UsingGraph.__init__(sparql_UsingGraph(False, '\x00'), False, '\x00') == None

