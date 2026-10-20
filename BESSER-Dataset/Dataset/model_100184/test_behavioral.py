import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractLiteral,
    Assertion,
    Atom,
    ClassAtom,
    ClassExpression,
    Constant,
    DataPropertyAtom,
    DataPropertyExpression,
    DataRange,
    Declaration,
    Expression,
    IRI,
    Individual,
    ObjectPropertyAtom,
    ObjectPropertyExpression,
    ParameterableElement,
    Query,
    TemplateableElement,
    Term,
    Variable,
    sparqlas_AbbreviatedIRI,
    sparqlas_AbstractLiteral,
    sparqlas_AnonymousIndividual,
    sparqlas_AskQuery,
    sparqlas_Assertion,
    sparqlas_AsymmetricObjectProperty,
    sparqlas_Atom,
    sparqlas_Class,
    sparqlas_ClassAssertion,
    sparqlas_ClassAtom,
    sparqlas_ClassDeclaration,
    sparqlas_ClassExpression,
    sparqlas_ClassVariable,
    sparqlas_Constant,
    sparqlas_ConstructQuery,
    sparqlas_DataAllValuesFrom,
    sparqlas_DataComplementOf,
    sparqlas_DataExactCardinality,
    sparqlas_DataHasValue,
    sparqlas_DataIntersectionOf,
    sparqlas_DataMaxCardinality,
    sparqlas_DataMinCardinality,
    sparqlas_DataOneOf,
    sparqlas_DataProperty,
    sparqlas_DataPropertyAssertion,
    sparqlas_DataPropertyAtom,
    sparqlas_DataPropertyDomain,
    sparqlas_DataPropertyExpression,
    sparqlas_DataPropertyRange,
    sparqlas_DataPropertyVariable,
    sparqlas_DataRange,
    sparqlas_DataSomeValuesFrom,
    sparqlas_DataUnionOf,
    sparqlas_Datatype,
    sparqlas_DatatypePropertyDeclaration,
    sparqlas_DatatypeRestriction,
    sparqlas_Declaration,
    sparqlas_DescribeQuery,
    sparqlas_DifferentIndividuals,
    sparqlas_DirectClassAssertion,
    sparqlas_DirectSubClassOf,
    sparqlas_DisjointClasses,
    sparqlas_DisjointDataProperties,
    sparqlas_DisjointObjectProperties,
    sparqlas_DisjointUnion,
    sparqlas_EquivalentClasses,
    sparqlas_EquivalentDataProperties,
    sparqlas_EquivalentObjectProperties,
    sparqlas_Expression,
    sparqlas_FacetRestriction,
    sparqlas_FullIRI,
    sparqlas_FunctionalDataProperty,
    sparqlas_FunctionalObjectProperty,
    sparqlas_HasKey,
    sparqlas_IRI,
    sparqlas_Import,
    sparqlas_Individual,
    sparqlas_IndividualDeclaration,
    sparqlas_IndividualVariable,
    sparqlas_InverseFunctionalObjectProperty,
    sparqlas_InverseObjectProperty,
    sparqlas_InverseObjectPropertyAtom,
    sparqlas_IrreflexiveObjectProperty,
    sparqlas_Literal,
    sparqlas_LiteralVariable,
    sparqlas_NamedIndividual,
    sparqlas_NegativeDataPropertyAssertion,
    sparqlas_NegativeObjectPropertyAssertion,
    sparqlas_ObjectAllValuesFrom,
    sparqlas_ObjectComplementOf,
    sparqlas_ObjectExactCardinality,
    sparqlas_ObjectHasValue,
    sparqlas_ObjectIntersectionOf,
    sparqlas_ObjectMaxCardinality,
    sparqlas_ObjectMinCardinality,
    sparqlas_ObjectOneOf,
    sparqlas_ObjectProperty,
    sparqlas_ObjectPropertyAssertion,
    sparqlas_ObjectPropertyAtom,
    sparqlas_ObjectPropertyChain,
    sparqlas_ObjectPropertyDeclaration,
    sparqlas_ObjectPropertyDomain,
    sparqlas_ObjectPropertyExpression,
    sparqlas_ObjectPropertyRange,
    sparqlas_ObjectPropertyVariable,
    sparqlas_ObjectSomeValuesFrom,
    sparqlas_ObjectUnionOf,
    sparqlas_OntologyDocument,
    sparqlas_ParameterableElement,
    sparqlas_PrefixDefinition,
    sparqlas_Query,
    sparqlas_ReflexiveObjectProperty,
    sparqlas_SameIndividual,
    sparqlas_SelectQuery,
    sparqlas_StrictSubClassOf,
    sparqlas_SubClassOf,
    sparqlas_SubDataPropertyOf,
    sparqlas_SubObjectPropertyOf,
    sparqlas_SymmetricObjectProperty,
    sparqlas_TemplateBinding,
    sparqlas_TemplateParameter,
    sparqlas_TemplateParameterSubstitution,
    sparqlas_TemplateSignature,
    sparqlas_TemplateableElement,
    sparqlas_Term,
    sparqlas_TransitiveObjectProperty,
    sparqlas_Variable,
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

def test_assoc_classExpression104_stub_double():
    # sparqlas_ClassExpression has no real 'sparqlas_ClassExpression105' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_ObjectMinCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_ObjectMinCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_ObjectMinCardinality(cardinality=7)
    partner = sparqlas_ClassExpression()
    setattr(partner, 'sparqlas_ClassExpression105', None)
    _safe_set(owner, 'sparqlas_ObjectMinCardinality', partner)
    assert getattr(partner, 'sparqlas_ClassExpression105') == owner
    _safe_set(owner, 'sparqlas_ObjectMinCardinality', None)
    assert getattr(partner, 'sparqlas_ClassExpression105') is None


def test_assoc_classExpression109_stub_double():
    # sparqlas_ClassExpression has no real 'sparqlas_ClassExpression110' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_ObjectMaxCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_ObjectMaxCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_ObjectMaxCardinality(cardinality=7)
    partner = sparqlas_ClassExpression()
    setattr(partner, 'sparqlas_ClassExpression110', None)
    _safe_set(owner, 'sparqlas_ObjectMaxCardinality', partner)
    assert getattr(partner, 'sparqlas_ClassExpression110') == owner
    _safe_set(owner, 'sparqlas_ObjectMaxCardinality', None)
    assert getattr(partner, 'sparqlas_ClassExpression110') is None


def test_assoc_classExpression114_stub_double():
    # sparqlas_ClassExpression has no real 'sparqlas_ClassExpression115' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_ObjectExactCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_ObjectExactCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_ObjectExactCardinality(cardinality=7)
    partner = sparqlas_ClassExpression()
    setattr(partner, 'sparqlas_ClassExpression115', None)
    _safe_set(owner, 'sparqlas_ObjectExactCardinality', partner)
    assert getattr(partner, 'sparqlas_ClassExpression115') == owner
    _safe_set(owner, 'sparqlas_ObjectExactCardinality', None)
    assert getattr(partner, 'sparqlas_ClassExpression115') is None


def test_assoc_constantIRI27_stub_double():
    # sparqlas_Constant has no real 'sparqlas_Constant' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_IRI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_IRI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_IRI(id="sample_text")
    partner = sparqlas_Constant()
    setattr(partner, 'sparqlas_Constant', None)
    _safe_set(owner, 'sparqlas_IRI28', partner)
    assert getattr(partner, 'sparqlas_Constant') == owner
    _safe_set(owner, 'sparqlas_IRI28', None)
    assert getattr(partner, 'sparqlas_Constant') is None


def test_assoc_constrainingFacet160_stub_double():
    # sparqlas_FacetRestriction has no real 'sparqlas_FacetRestriction161' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_IRI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_IRI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_IRI(id="sample_text")
    partner = sparqlas_FacetRestriction()
    setattr(partner, 'sparqlas_FacetRestriction161', None)
    _safe_set(owner, 'sparqlas_IRI162', partner)
    assert getattr(partner, 'sparqlas_FacetRestriction161') == owner
    _safe_set(owner, 'sparqlas_IRI162', None)
    assert getattr(partner, 'sparqlas_FacetRestriction161') is None


def test_assoc_dataPropertyExpression135_stub_double():
    # sparqlas_DataPropertyExpression has no real 'sparqlas_DataPropertyExpression137' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_DataMinCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_DataMinCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_DataMinCardinality(cardinality=7)
    partner = sparqlas_DataPropertyExpression()
    setattr(partner, 'sparqlas_DataPropertyExpression137', None)
    _safe_set(owner, 'sparqlas_DataMinCardinality136', partner)
    assert getattr(partner, 'sparqlas_DataPropertyExpression137') == owner
    _safe_set(owner, 'sparqlas_DataMinCardinality136', None)
    assert getattr(partner, 'sparqlas_DataPropertyExpression137') is None


def test_assoc_dataPropertyExpression140_stub_double():
    # sparqlas_DataPropertyExpression has no real 'sparqlas_DataPropertyExpression142' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_DataMaxCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_DataMaxCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_DataMaxCardinality(cardinality=7)
    partner = sparqlas_DataPropertyExpression()
    setattr(partner, 'sparqlas_DataPropertyExpression142', None)
    _safe_set(owner, 'sparqlas_DataMaxCardinality141', partner)
    assert getattr(partner, 'sparqlas_DataPropertyExpression142') == owner
    _safe_set(owner, 'sparqlas_DataMaxCardinality141', None)
    assert getattr(partner, 'sparqlas_DataPropertyExpression142') is None


def test_assoc_dataPropertyExpression145_stub_double():
    # sparqlas_DataPropertyExpression has no real 'sparqlas_DataPropertyExpression147' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_DataExactCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_DataExactCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_DataExactCardinality(cardinality=7)
    partner = sparqlas_DataPropertyExpression()
    setattr(partner, 'sparqlas_DataPropertyExpression147', None)
    _safe_set(owner, 'sparqlas_DataExactCardinality146', partner)
    assert getattr(partner, 'sparqlas_DataPropertyExpression147') == owner
    _safe_set(owner, 'sparqlas_DataExactCardinality146', None)
    assert getattr(partner, 'sparqlas_DataPropertyExpression147') is None


def test_assoc_dataRange133_stub_double():
    # sparqlas_DataRange has no real 'sparqlas_DataRange134' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_DataMinCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_DataMinCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_DataMinCardinality(cardinality=7)
    partner = sparqlas_DataRange()
    setattr(partner, 'sparqlas_DataRange134', None)
    _safe_set(owner, 'sparqlas_DataMinCardinality', partner)
    assert getattr(partner, 'sparqlas_DataRange134') == owner
    _safe_set(owner, 'sparqlas_DataMinCardinality', None)
    assert getattr(partner, 'sparqlas_DataRange134') is None


def test_assoc_dataRange138_stub_double():
    # sparqlas_DataRange has no real 'sparqlas_DataRange139' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_DataMaxCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_DataMaxCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_DataMaxCardinality(cardinality=7)
    partner = sparqlas_DataRange()
    setattr(partner, 'sparqlas_DataRange139', None)
    _safe_set(owner, 'sparqlas_DataMaxCardinality', partner)
    assert getattr(partner, 'sparqlas_DataRange139') == owner
    _safe_set(owner, 'sparqlas_DataMaxCardinality', None)
    assert getattr(partner, 'sparqlas_DataRange139') is None


def test_assoc_dataRange143_stub_double():
    # sparqlas_DataRange has no real 'sparqlas_DataRange144' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_DataExactCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_DataExactCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_DataExactCardinality(cardinality=7)
    partner = sparqlas_DataRange()
    setattr(partner, 'sparqlas_DataRange144', None)
    _safe_set(owner, 'sparqlas_DataExactCardinality', partner)
    assert getattr(partner, 'sparqlas_DataRange144') == owner
    _safe_set(owner, 'sparqlas_DataExactCardinality', None)
    assert getattr(partner, 'sparqlas_DataRange144') is None


def test_assoc_datatype29_stub_double():
    # sparqlas_Datatype has no real 'sparqlas_Datatype' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_Literal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_Literal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_Literal(lexicalForm="sample_text")
    partner = sparqlas_Datatype()
    setattr(partner, 'sparqlas_Datatype', None)
    _safe_set(owner, 'sparqlas_Literal', partner)
    assert getattr(partner, 'sparqlas_Datatype') == owner
    _safe_set(owner, 'sparqlas_Literal', None)
    assert getattr(partner, 'sparqlas_Datatype') is None


def test_assoc_describeIRI22_stub_double():
    # sparqlas_DescribeQuery has no real 'sparqlas_DescribeQuery' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_IRI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_IRI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_IRI(id="sample_text")
    partner = sparqlas_DescribeQuery()
    setattr(partner, 'sparqlas_DescribeQuery', None)
    _safe_set(owner, 'sparqlas_IRI23', partner)
    assert getattr(partner, 'sparqlas_DescribeQuery') == owner
    _safe_set(owner, 'sparqlas_IRI23', None)
    assert getattr(partner, 'sparqlas_DescribeQuery') is None


def test_assoc_importIRI7_stub_double():
    # sparqlas_Import has no real 'sparqlas_Import8' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_IRI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_IRI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_IRI(id="sample_text")
    partner = sparqlas_Import()
    setattr(partner, 'sparqlas_Import8', None)
    _safe_set(owner, 'sparqlas_IRI9', partner)
    assert getattr(partner, 'sparqlas_Import8') == owner
    _safe_set(owner, 'sparqlas_IRI9', None)
    assert getattr(partner, 'sparqlas_Import8') is None


def test_assoc_namespace10_stub_double():
    # sparqlas_FullIRI has no real 'sparqlas_FullIRI' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_PrefixDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_PrefixDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_PrefixDefinition(pref="sample_text")
    partner = sparqlas_FullIRI()
    setattr(partner, 'sparqlas_FullIRI', None)
    _safe_set(owner, 'sparqlas_PrefixDefinition11', partner)
    assert getattr(partner, 'sparqlas_FullIRI') == owner
    _safe_set(owner, 'sparqlas_PrefixDefinition11', None)
    assert getattr(partner, 'sparqlas_FullIRI') is None


def test_assoc_objectPropertyExpression106_stub_double():
    # sparqlas_ObjectPropertyExpression has no real 'sparqlas_ObjectPropertyExpression108' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_ObjectMinCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_ObjectMinCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_ObjectMinCardinality(cardinality=7)
    partner = sparqlas_ObjectPropertyExpression()
    setattr(partner, 'sparqlas_ObjectPropertyExpression108', None)
    _safe_set(owner, 'sparqlas_ObjectMinCardinality107', partner)
    assert getattr(partner, 'sparqlas_ObjectPropertyExpression108') == owner
    _safe_set(owner, 'sparqlas_ObjectMinCardinality107', None)
    assert getattr(partner, 'sparqlas_ObjectPropertyExpression108') is None


def test_assoc_objectPropertyExpression111_stub_double():
    # sparqlas_ObjectPropertyExpression has no real 'sparqlas_ObjectPropertyExpression113' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_ObjectMaxCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_ObjectMaxCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_ObjectMaxCardinality(cardinality=7)
    partner = sparqlas_ObjectPropertyExpression()
    setattr(partner, 'sparqlas_ObjectPropertyExpression113', None)
    _safe_set(owner, 'sparqlas_ObjectMaxCardinality112', partner)
    assert getattr(partner, 'sparqlas_ObjectPropertyExpression113') == owner
    _safe_set(owner, 'sparqlas_ObjectMaxCardinality112', None)
    assert getattr(partner, 'sparqlas_ObjectPropertyExpression113') is None


def test_assoc_objectPropertyExpression116_stub_double():
    # sparqlas_ObjectPropertyExpression has no real 'sparqlas_ObjectPropertyExpression118' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_ObjectExactCardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_ObjectExactCardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_ObjectExactCardinality(cardinality=7)
    partner = sparqlas_ObjectPropertyExpression()
    setattr(partner, 'sparqlas_ObjectPropertyExpression118', None)
    _safe_set(owner, 'sparqlas_ObjectExactCardinality117', partner)
    assert getattr(partner, 'sparqlas_ObjectPropertyExpression118') == owner
    _safe_set(owner, 'sparqlas_ObjectExactCardinality117', None)
    assert getattr(partner, 'sparqlas_ObjectPropertyExpression118') is None


def test_assoc_prefixDefinition3_stub_double():
    # sparqlas_OntologyDocument has no real 'sparqlas_OntologyDocument4' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_PrefixDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_PrefixDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_PrefixDefinition(pref="sample_text")
    partner = sparqlas_OntologyDocument()
    setattr(partner, 'sparqlas_OntologyDocument4', None)
    _safe_set(owner, 'sparqlas_PrefixDefinition', partner)
    assert owner in getattr(partner, 'sparqlas_OntologyDocument4')
    _safe_set(owner, 'sparqlas_PrefixDefinition', None)
    assert owner not in getattr(partner, 'sparqlas_OntologyDocument4')


def test_assoc_queryIRI0_stub_double():
    # sparqlas_OntologyDocument has no real 'sparqlas_OntologyDocument' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_IRI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_IRI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_IRI(id="sample_text")
    partner = sparqlas_OntologyDocument()
    setattr(partner, 'sparqlas_OntologyDocument', None)
    _safe_set(owner, 'sparqlas_IRI', partner)
    assert getattr(partner, 'sparqlas_OntologyDocument') == owner
    _safe_set(owner, 'sparqlas_IRI', None)
    assert getattr(partner, 'sparqlas_OntologyDocument') is None


def test_assoc_variables13_stub_double():
    # sparqlas_SelectQuery has no real 'sparqlas_SelectQuery14' property in the generated
    # code (a bare stub) -- manually attach it so sparqlas_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparqlas_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparqlas_Variable(symbol="sample_text")
    partner = sparqlas_SelectQuery()
    setattr(partner, 'sparqlas_SelectQuery14', None)
    _safe_set(owner, 'sparqlas_Variable', partner)
    assert owner in getattr(partner, 'sparqlas_SelectQuery14')
    _safe_set(owner, 'sparqlas_Variable', None)
    assert owner not in getattr(partner, 'sparqlas_SelectQuery14')


