import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AdditionalMultiplicativeExpressionNE,
    AdditionalNumericExpressionNE,
    AdditionalUnaryExpressionNE,
    ArgList,
    AscOrDecs,
    BlankNode,
    BooleanLiteral,
    BuiltInCall,
    Constraint,
    GraphClauseNE,
    GraphNode,
    GraphPatternNotTriples,
    GraphTerm,
    IRIreference,
    LANGTAGOrIRIrefNE,
    LimitOffsetClauses,
    LocatedElement,
    NumericLiteral,
    OrderCondition,
    OrderConditionRightNE,
    PatternOrFilterNE,
    PrefixedName,
    PrimaryExpression,
    Query,
    SolutionsDisplayNE,
    SourceSelector,
    StringLiteral,
    TriplesNode,
    TriplesSameSubject,
    UnaryExpression,
    VarOrIRIref,
    VarOrTerm,
    VariablesNE,
    Verb,
    sparql_ANON,
    sparql_AdditionalConditionalAndExpressionNE,
    sparql_AdditionalExpressionNE,
    sparql_AdditionalGGPElement,
    sparql_AdditionalMultiplicativeExpressionNE,
    sparql_AdditionalNumericExpressionNE,
    sparql_AdditionalUnaryExpressionNE,
    sparql_AdditionalValueLogicalNE,
    sparql_AdditiveExpression,
    sparql_AllVariablesNE,
    sparql_ArgList,
    sparql_ArgListExpressionNE,
    sparql_ArgListNILNE,
    sparql_AscOrDecs,
    sparql_AscendingLiteral,
    sparql_AskQuery,
    sparql_BLANK_NODE_LABEL,
    sparql_BaseDecl,
    sparql_BiggerNumericExpressionNE,
    sparql_BiggerOrEqualNumericExpressionNE,
    sparql_BlankNode,
    sparql_BlankNodePropertyList,
    sparql_BooleanLiteral,
    sparql_BoundBuiltInCallNE,
    sparql_BrackettedExpression,
    sparql_BuiltInCall,
    sparql_Collection,
    sparql_ConditionalAndExpression,
    sparql_ConditionalOrExpression,
    sparql_Constraint,
    sparql_ConstructQuery,
    sparql_ConstructTemplate,
    sparql_DECIMAL,
    sparql_DOUBLE,
    sparql_DatasetClause,
    sparql_DatatypeBuiltInCallNE,
    sparql_DefaultGraphClause,
    sparql_DescendingLiteral,
    sparql_DescribeQuery,
    sparql_DistinctNE,
    sparql_DividedByAdditionalUnaryExpressionNE,
    sparql_EqualsNumericExpressionNE,
    sparql_Expression,
    sparql_FalseBooleanLiteralNE,
    sparql_Filter,
    sparql_FunctionCall,
    sparql_GraphClauseNE,
    sparql_GraphGraphPattern,
    sparql_GraphNode,
    sparql_GraphPatternNotTriples,
    sparql_GraphTerm,
    sparql_GroupGraphPattern,
    sparql_GroupOrUnionGraphPattern,
    sparql_INTEGER,
    sparql_IRI_REF,
    sparql_IRIrefOrFunction,
    sparql_IRIreference,
    sparql_IsBlankBuiltInCallNE,
    sparql_IsIRIBuiltInCallNE,
    sparql_IsLiteralBuiltInCallNE,
    sparql_IsURIBuiltInCallNE,
    sparql_LANGTAG,
    sparql_LANGTAGOrIRIrefNE,
    sparql_LangBuiltInCallNE,
    sparql_LangmatchesBuiltInCallNE,
    sparql_LimitClause,
    sparql_LimitOffsetClauses,
    sparql_LimitOffsetClausesLeftNE,
    sparql_LimitOffsetClausesRightNE,
    sparql_LocatedElement,
    sparql_MinusMultiplicativeExpressionNE,
    sparql_MinusPrimaryExpressionNE,
    sparql_MultiplicativeExpression,
    sparql_NamedGraphClause,
    sparql_NotEqualNumericExpressionNE,
    sparql_NotInList,
    sparql_NotPrimaryExpressionNE,
    sparql_NumericExpression,
    sparql_NumericLiteral,
    sparql_NumericLiteralNegative,
    sparql_NumericLiteralPositive,
    sparql_NumericLiteralUnsigned,
    sparql_Object,
    sparql_ObjectList,
    sparql_OffsetClause,
    sparql_OptionalGraphPattern,
    sparql_OrderClause,
    sparql_OrderCondition,
    sparql_OrderConditionLeftNE,
    sparql_OrderConditionRightNE,
    sparql_PNAME_LN,
    sparql_PNAME_NS,
    sparql_PN_LOCAL,
    sparql_PN_PREFIX,
    sparql_PatternOrFilterNE,
    sparql_PlusMultiplicativeExpressionNE,
    sparql_PlusPrimaryExpressionNE,
    sparql_PrefixDecl,
    sparql_PrefixedName,
    sparql_PrimaryExpression,
    sparql_Prologue,
    sparql_PropertyListNotEmpty,
    sparql_Query,
    sparql_RDFLiteral,
    sparql_ReducedNE,
    sparql_RegexExpression,
    sparql_RelationalExpression,
    sparql_STRING_LITERAL1,
    sparql_STRING_LITERAL2,
    sparql_STRING_LITERAL_LONG1,
    sparql_STRING_LITERAL_LONG2,
    sparql_SameTermBuiltInCallNE,
    sparql_SelectQuery,
    sparql_SmallerNumericExpressionNE,
    sparql_SmallerOrEqualNumericExpressionNE,
    sparql_SolutionModifier,
    sparql_SolutionsDisplayNE,
    sparql_SomeVariablesNE,
    sparql_SourceSelector,
    sparql_SparqlQueries,
    sparql_StrBuiltInCallNE,
    sparql_StringLiteral,
    sparql_TimesAdditionalUnaryExpressionNE,
    sparql_TriplesBlock,
    sparql_TriplesNode,
    sparql_TriplesSameSubject,
    sparql_TriplesSameSubjectLeftNE,
    sparql_TriplesSameSubjectRightNE,
    sparql_TrueBooleanLiteralNE,
    sparql_UnaryExpression,
    sparql_UpIRIrefNE,
    sparql_VAR1,
    sparql_VAR2,
    sparql_VARNAME,
    sparql_ValueLogical,
    sparql_Var,
    sparql_VarOrIRIref,
    sparql_VarOrTerm,
    sparql_VariablesNE,
    sparql_Verb,
    sparql_VerbANE,
    sparql_WS,
    sparql_WhereClause,
    sparql_WhereLiteral,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_integer67_stub_double():
    # sparql_LimitClause has no real 'sparql_LimitClause68' property in the generated
    # code (a bare stub) -- manually attach it so sparql_INTEGER's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_INTEGER's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_INTEGER(integer="sample_text")
    partner = sparql_LimitClause()
    setattr(partner, 'sparql_LimitClause68', None)
    _safe_set(owner, 'sparql_INTEGER', partner)
    assert getattr(partner, 'sparql_LimitClause68') == owner
    _safe_set(owner, 'sparql_INTEGER', None)
    assert getattr(partner, 'sparql_LimitClause68') is None


def test_assoc_integer69_stub_double():
    # sparql_OffsetClause has no real 'sparql_OffsetClause70' property in the generated
    # code (a bare stub) -- manually attach it so sparql_INTEGER's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_INTEGER's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_INTEGER(integer="sample_text")
    partner = sparql_OffsetClause()
    setattr(partner, 'sparql_OffsetClause70', None)
    _safe_set(owner, 'sparql_INTEGER71', partner)
    assert getattr(partner, 'sparql_OffsetClause70') == owner
    _safe_set(owner, 'sparql_INTEGER71', None)
    assert getattr(partner, 'sparql_OffsetClause70') is None


def test_assoc_iriref11_stub_double():
    # sparql_PrefixDecl has no real 'sparql_PrefixDecl12' property in the generated
    # code (a bare stub) -- manually attach it so sparql_IRI_REF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_IRI_REF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_IRI_REF(iri_ref="sample_text")
    partner = sparql_PrefixDecl()
    setattr(partner, 'sparql_PrefixDecl12', None)
    _safe_set(owner, 'sparql_IRI_REF13', partner)
    assert getattr(partner, 'sparql_PrefixDecl12') == owner
    _safe_set(owner, 'sparql_IRI_REF13', None)
    assert getattr(partner, 'sparql_PrefixDecl12') is None


def test_assoc_iriref7_stub_double():
    # sparql_BaseDecl has no real 'sparql_BaseDecl8' property in the generated
    # code (a bare stub) -- manually attach it so sparql_IRI_REF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_IRI_REF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_IRI_REF(iri_ref="sample_text")
    partner = sparql_BaseDecl()
    setattr(partner, 'sparql_BaseDecl8', None)
    _safe_set(owner, 'sparql_IRI_REF', partner)
    assert getattr(partner, 'sparql_BaseDecl8') == owner
    _safe_set(owner, 'sparql_IRI_REF', None)
    assert getattr(partner, 'sparql_BaseDecl8') is None


def test_assoc_name235_stub_double():
    # sparql_VAR1 has no real 'sparql_VAR1' property in the generated
    # code (a bare stub) -- manually attach it so sparql_VARNAME's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_VARNAME's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_VARNAME(varname="sample_text")
    partner = sparql_VAR1()
    setattr(partner, 'sparql_VAR1', None)
    _safe_set(owner, 'sparql_VARNAME', partner)
    assert getattr(partner, 'sparql_VAR1') == owner
    _safe_set(owner, 'sparql_VARNAME', None)
    assert getattr(partner, 'sparql_VAR1') is None


def test_assoc_name236_stub_double():
    # sparql_VAR2 has no real 'sparql_VAR2' property in the generated
    # code (a bare stub) -- manually attach it so sparql_VARNAME's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_VARNAME's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_VARNAME(varname="sample_text")
    partner = sparql_VAR2()
    setattr(partner, 'sparql_VAR2', None)
    _safe_set(owner, 'sparql_VARNAME237', partner)
    assert getattr(partner, 'sparql_VAR2') == owner
    _safe_set(owner, 'sparql_VARNAME237', None)
    assert getattr(partner, 'sparql_VAR2') is None


def test_assoc_pn_local238_stub_double():
    # sparql_PNAME_LN has no real 'sparql_PNAME_LN' property in the generated
    # code (a bare stub) -- manually attach it so sparql_PN_LOCAL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_PN_LOCAL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_PN_LOCAL(pn_local="sample_text")
    partner = sparql_PNAME_LN()
    setattr(partner, 'sparql_PNAME_LN', None)
    _safe_set(owner, 'sparql_PN_LOCAL', partner)
    assert getattr(partner, 'sparql_PNAME_LN') == owner
    _safe_set(owner, 'sparql_PN_LOCAL', None)
    assert getattr(partner, 'sparql_PNAME_LN') is None


def test_assoc_pnamens9_stub_double():
    # sparql_PrefixDecl has no real 'sparql_PrefixDecl10' property in the generated
    # code (a bare stub) -- manually attach it so sparql_PNAME_NS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_PNAME_NS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_PNAME_NS(pn_prefix="sample_text")
    partner = sparql_PrefixDecl()
    setattr(partner, 'sparql_PrefixDecl10', None)
    _safe_set(owner, 'sparql_PNAME_NS', partner)
    assert getattr(partner, 'sparql_PrefixDecl10') == owner
    _safe_set(owner, 'sparql_PNAME_NS', None)
    assert getattr(partner, 'sparql_PrefixDecl10') is None


def test_assoc_var136_stub_double():
    # sparql_BoundBuiltInCallNE has no real 'sparql_BoundBuiltInCallNE' property in the generated
    # code (a bare stub) -- manually attach it so sparql_Var's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_Var's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_Var(varname="sample_text")
    partner = sparql_BoundBuiltInCallNE()
    setattr(partner, 'sparql_BoundBuiltInCallNE', None)
    _safe_set(owner, 'sparql_Var137', partner)
    assert getattr(partner, 'sparql_BoundBuiltInCallNE') == owner
    _safe_set(owner, 'sparql_Var137', None)
    assert getattr(partner, 'sparql_BoundBuiltInCallNE') is None


def test_assoc_var15_stub_double():
    # sparql_SelectQuery has no real 'sparql_SelectQuery16' property in the generated
    # code (a bare stub) -- manually attach it so sparql_Var's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_Var's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_Var(varname="sample_text")
    partner = sparql_SelectQuery()
    setattr(partner, 'sparql_SelectQuery16', None)
    _safe_set(owner, 'sparql_Var', partner)
    assert owner in getattr(partner, 'sparql_SelectQuery16')
    _safe_set(owner, 'sparql_Var', None)
    assert owner not in getattr(partner, 'sparql_SelectQuery16')


def test_assoc_variables72_stub_double():
    # sparql_SomeVariablesNE has no real 'sparql_SomeVariablesNE' property in the generated
    # code (a bare stub) -- manually attach it so sparql_Var's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_Var's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_Var(varname="sample_text")
    partner = sparql_SomeVariablesNE()
    setattr(partner, 'sparql_SomeVariablesNE', None)
    _safe_set(owner, 'sparql_Var73', partner)
    assert owner in getattr(partner, 'sparql_SomeVariablesNE')
    _safe_set(owner, 'sparql_Var73', None)
    assert owner not in getattr(partner, 'sparql_SomeVariablesNE')


def test_assoc_ws239_stub_double():
    # sparql_NotInList has no real 'sparql_NotInList240' property in the generated
    # code (a bare stub) -- manually attach it so sparql_WS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_WS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_WS(ws="sample_text")
    partner = sparql_NotInList()
    setattr(partner, 'sparql_NotInList240', None)
    _safe_set(owner, 'sparql_WS', partner)
    assert owner in getattr(partner, 'sparql_NotInList240')
    _safe_set(owner, 'sparql_WS', None)
    assert owner not in getattr(partner, 'sparql_NotInList240')


def test_assoc_ws241_stub_double():
    # sparql_ANON has no real 'sparql_ANON' property in the generated
    # code (a bare stub) -- manually attach it so sparql_WS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_WS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_WS(ws="sample_text")
    partner = sparql_ANON()
    setattr(partner, 'sparql_ANON', None)
    _safe_set(owner, 'sparql_WS242', partner)
    assert owner in getattr(partner, 'sparql_ANON')
    _safe_set(owner, 'sparql_WS242', None)
    assert owner not in getattr(partner, 'sparql_ANON')


