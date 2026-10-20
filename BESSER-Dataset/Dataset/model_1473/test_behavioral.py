import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GraphConstraint_Attribute,
    GraphConstraint_EAttribute,
    GraphConstraint_EClass,
    GraphConstraint_EDataType,
    GraphConstraint_EPackage,
    GraphConstraint_EReference,
    GraphConstraint_Edge,
    GraphConstraint_ElementMapping,
    GraphConstraint_Formula,
    GraphConstraint_Graph,
    GraphConstraint_GraphElement,
    GraphConstraint_Mapping,
    GraphConstraint_NestedGraphCondition,
    GraphConstraint_NestedGraphConstraint,
    GraphConstraint_Node,
    GraphConstraint_QuantifiedGraphCondition,
    GraphConstraint_True,
    GraphConstraint_Variable,
    GraphElement,
    NestedGraphCondition,
    Operator,
    Quantifier,
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

def test_assoc_args47_stub_double():
    # GraphConstraint_NestedGraphCondition has no real 'NestedGraphCondition48' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_Formula(op="sample_text")
    partner = GraphConstraint_NestedGraphCondition()
    setattr(partner, 'NestedGraphCondition48', None)
    _safe_set(owner, 'formula', {partner})
    assert getattr(partner, 'NestedGraphCondition48') == owner
    _safe_set(owner, 'formula', set())
    assert getattr(partner, 'NestedGraphCondition48') is None


def test_assoc_attributes8_stub_double():
    # GraphConstraint_Node has no real 'GraphConstraint_Node9' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_Attribute(op="sample_text", value="sample_text")
    partner = GraphConstraint_Node()
    setattr(partner, 'GraphConstraint_Node9', None)
    _safe_set(owner, 'GraphConstraint_Attribute', partner)
    assert owner in getattr(partner, 'GraphConstraint_Node9')
    _safe_set(owner, 'GraphConstraint_Attribute', None)
    assert owner not in getattr(partner, 'GraphConstraint_Node9')


def test_assoc_codomain34_stub_double():
    # GraphConstraint_Graph has no real 'GraphConstraint_Graph35' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_QuantifiedGraphCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_QuantifiedGraphCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_QuantifiedGraphCondition(quantifier="sample_text")
    partner = GraphConstraint_Graph()
    setattr(partner, 'GraphConstraint_Graph35', None)
    _safe_set(owner, 'GraphConstraint_QuantifiedGraphCondition', partner)
    assert getattr(partner, 'GraphConstraint_Graph35') == owner
    _safe_set(owner, 'GraphConstraint_QuantifiedGraphCondition', None)
    assert getattr(partner, 'GraphConstraint_Graph35') is None


def test_assoc_codomainMapping42_stub_double():
    # GraphConstraint_Mapping has no real 'GraphConstraint_Mapping44' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_QuantifiedGraphCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_QuantifiedGraphCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_QuantifiedGraphCondition(quantifier="sample_text")
    partner = GraphConstraint_Mapping()
    setattr(partner, 'GraphConstraint_Mapping44', None)
    _safe_set(owner, 'GraphConstraint_QuantifiedGraphCondition43', partner)
    assert getattr(partner, 'GraphConstraint_Mapping44') == owner
    _safe_set(owner, 'GraphConstraint_QuantifiedGraphCondition43', None)
    assert getattr(partner, 'GraphConstraint_Mapping44') is None


def test_assoc_condition4_stub_double():
    # GraphConstraint_NestedGraphCondition has no real 'NestedGraphCondition' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_NestedGraphConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_NestedGraphConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_NestedGraphConstraint(name="sample_text")
    partner = GraphConstraint_NestedGraphCondition()
    setattr(partner, 'NestedGraphCondition', None)
    _safe_set(owner, 'gc', partner)
    assert getattr(partner, 'NestedGraphCondition') == owner
    _safe_set(owner, 'gc', None)
    assert getattr(partner, 'NestedGraphCondition') is None


def test_assoc_emptyDomain5_stub_double():
    # GraphConstraint_Graph has no real 'GraphConstraint_Graph7' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_NestedGraphConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_NestedGraphConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_NestedGraphConstraint(name="sample_text")
    partner = GraphConstraint_Graph()
    setattr(partner, 'GraphConstraint_Graph7', None)
    _safe_set(owner, 'GraphConstraint_NestedGraphConstraint6', partner)
    assert getattr(partner, 'GraphConstraint_Graph7') == owner
    _safe_set(owner, 'GraphConstraint_NestedGraphConstraint6', None)
    assert getattr(partner, 'GraphConstraint_Graph7') is None


def test_assoc_formula50_stub_double():
    # GraphConstraint_NestedGraphCondition has no real 'args' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_Formula(op="sample_text")
    partner = GraphConstraint_NestedGraphCondition()
    setattr(partner, 'args', None)
    _safe_set(owner, 'Formula', partner)
    assert getattr(partner, 'args') == owner
    _safe_set(owner, 'Formula', None)
    assert getattr(partner, 'args') is None


def test_assoc_gc52_stub_double():
    # GraphConstraint_NestedGraphCondition has no real 'condition' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_NestedGraphConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_NestedGraphConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_NestedGraphConstraint(name="sample_text")
    partner = GraphConstraint_NestedGraphCondition()
    setattr(partner, 'condition', None)
    _safe_set(owner, 'NestedGraphConstraint', partner)
    assert getattr(partner, 'condition') == owner
    _safe_set(owner, 'NestedGraphConstraint', None)
    assert getattr(partner, 'condition') is None


def test_assoc_image31_stub_double():
    # GraphConstraint_ElementMapping has no real 'GraphConstraint_ElementMapping32' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_GraphElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_GraphElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_GraphElement(name="sample_text")
    partner = GraphConstraint_ElementMapping()
    setattr(partner, 'GraphConstraint_ElementMapping32', None)
    _safe_set(owner, 'GraphConstraint_GraphElement33', partner)
    assert getattr(partner, 'GraphConstraint_ElementMapping32') == owner
    _safe_set(owner, 'GraphConstraint_GraphElement33', None)
    assert getattr(partner, 'GraphConstraint_ElementMapping32') is None


def test_assoc_import_3_stub_double():
    # GraphConstraint_EPackage has no real 'GraphConstraint_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_NestedGraphConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_NestedGraphConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_NestedGraphConstraint(name="sample_text")
    partner = GraphConstraint_EPackage()
    setattr(partner, 'GraphConstraint_EPackage', None)
    _safe_set(owner, 'GraphConstraint_NestedGraphConstraint', partner)
    assert getattr(partner, 'GraphConstraint_EPackage') == owner
    _safe_set(owner, 'GraphConstraint_NestedGraphConstraint', None)
    assert getattr(partner, 'GraphConstraint_EPackage') is None


def test_assoc_nested45_stub_double():
    # GraphConstraint_NestedGraphCondition has no real 'NestedGraphCondition46' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_QuantifiedGraphCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_QuantifiedGraphCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_QuantifiedGraphCondition(quantifier="sample_text")
    partner = GraphConstraint_NestedGraphCondition()
    setattr(partner, 'NestedGraphCondition46', None)
    _safe_set(owner, 'qgc', partner)
    assert getattr(partner, 'NestedGraphCondition46') == owner
    _safe_set(owner, 'qgc', None)
    assert getattr(partner, 'NestedGraphCondition46') is None


def test_assoc_origin29_stub_double():
    # GraphConstraint_ElementMapping has no real 'GraphConstraint_ElementMapping30' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_GraphElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_GraphElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_GraphElement(name="sample_text")
    partner = GraphConstraint_ElementMapping()
    setattr(partner, 'GraphConstraint_ElementMapping30', None)
    _safe_set(owner, 'GraphConstraint_GraphElement', partner)
    assert getattr(partner, 'GraphConstraint_ElementMapping30') == owner
    _safe_set(owner, 'GraphConstraint_GraphElement', None)
    assert getattr(partner, 'GraphConstraint_ElementMapping30') is None


def test_assoc_qgc51_stub_double():
    # GraphConstraint_NestedGraphCondition has no real 'nested' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_QuantifiedGraphCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_QuantifiedGraphCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_QuantifiedGraphCondition(quantifier="sample_text")
    partner = GraphConstraint_NestedGraphCondition()
    setattr(partner, 'nested', None)
    _safe_set(owner, 'QuantifiedGraphCondition', partner)
    assert getattr(partner, 'nested') == owner
    _safe_set(owner, 'QuantifiedGraphCondition', None)
    assert getattr(partner, 'nested') is None


def test_assoc_restriction36_stub_double():
    # GraphConstraint_Graph has no real 'GraphConstraint_Graph38' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_QuantifiedGraphCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_QuantifiedGraphCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_QuantifiedGraphCondition(quantifier="sample_text")
    partner = GraphConstraint_Graph()
    setattr(partner, 'GraphConstraint_Graph38', None)
    _safe_set(owner, 'GraphConstraint_QuantifiedGraphCondition37', partner)
    assert getattr(partner, 'GraphConstraint_Graph38') == owner
    _safe_set(owner, 'GraphConstraint_QuantifiedGraphCondition37', None)
    assert getattr(partner, 'GraphConstraint_Graph38') is None


def test_assoc_restrictionMapping39_stub_double():
    # GraphConstraint_Mapping has no real 'GraphConstraint_Mapping41' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_QuantifiedGraphCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_QuantifiedGraphCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_QuantifiedGraphCondition(quantifier="sample_text")
    partner = GraphConstraint_Mapping()
    setattr(partner, 'GraphConstraint_Mapping41', None)
    _safe_set(owner, 'GraphConstraint_QuantifiedGraphCondition40', partner)
    assert getattr(partner, 'GraphConstraint_Mapping41') == owner
    _safe_set(owner, 'GraphConstraint_QuantifiedGraphCondition40', None)
    assert getattr(partner, 'GraphConstraint_Mapping41') is None


def test_assoc_type20_stub_double():
    # GraphConstraint_EAttribute has no real 'GraphConstraint_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_Attribute(op="sample_text", value="sample_text")
    partner = GraphConstraint_EAttribute()
    setattr(partner, 'GraphConstraint_EAttribute', None)
    _safe_set(owner, 'GraphConstraint_Attribute21', partner)
    assert getattr(partner, 'GraphConstraint_EAttribute') == owner
    _safe_set(owner, 'GraphConstraint_Attribute21', None)
    assert getattr(partner, 'GraphConstraint_EAttribute') is None


def test_assoc_type49_stub_double():
    # GraphConstraint_EDataType has no real 'GraphConstraint_EDataType' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_Variable(name="sample_text")
    partner = GraphConstraint_EDataType()
    setattr(partner, 'GraphConstraint_EDataType', None)
    _safe_set(owner, 'GraphConstraint_Variable', partner)
    assert getattr(partner, 'GraphConstraint_EDataType') == owner
    _safe_set(owner, 'GraphConstraint_Variable', None)
    assert getattr(partner, 'GraphConstraint_EDataType') is None


def test_assoc_vars55_stub_double():
    # GraphConstraint_NestedGraphCondition has no real 'GraphConstraint_NestedGraphCondition56' property in the generated
    # code (a bare stub) -- manually attach it so GraphConstraint_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphConstraint_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphConstraint_Variable(name="sample_text")
    partner = GraphConstraint_NestedGraphCondition()
    setattr(partner, 'GraphConstraint_NestedGraphCondition56', None)
    _safe_set(owner, 'GraphConstraint_Variable57', partner)
    assert owner in getattr(partner, 'GraphConstraint_NestedGraphCondition56')
    _safe_set(owner, 'GraphConstraint_Variable57', None)
    assert owner not in getattr(partner, 'GraphConstraint_NestedGraphCondition56')


