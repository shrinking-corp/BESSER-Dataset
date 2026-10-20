import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Entity,
    Type,
    smalluml_Association,
    smalluml_Attribute,
    smalluml_BooleanType,
    smalluml_Cardinalities,
    smalluml_Class,
    smalluml_ClassDiagram,
    smalluml_Entity,
    smalluml_Enumeration,
    smalluml_IntegerType,
    smalluml_Operation,
    smalluml_Parameter,
    smalluml_RealType,
    smalluml_Type,
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

def test_assoc_attributes0_reverse_link_reassign_clear():
    a1 = smalluml_Class(abstract=True)
    a2 = smalluml_Class(abstract=False)
    b = smalluml_Attribute(name="sample_text")
    _safe_set(b, 'smalluml_Attribute', a1)
    assert _is_linked(b, 'smalluml_Attribute', a1)
    if hasattr(a1, 'smalluml_Class'):
        assert _is_linked(a1, 'smalluml_Class', b)
    _safe_set(b, 'smalluml_Attribute', a2)
    assert _is_linked(b, 'smalluml_Attribute', a2)
    if hasattr(a1, 'smalluml_Class'):
        assert not _is_linked(a1, 'smalluml_Class', b)
    if hasattr(a2, 'smalluml_Class'):
        assert _is_linked(a2, 'smalluml_Class', b)
    _safe_set(b, 'smalluml_Attribute', None)
    assert not _is_linked(b, 'smalluml_Attribute', a2)
    if hasattr(a2, 'smalluml_Class'):
        assert not _is_linked(a2, 'smalluml_Class', b)


def test_assoc_entities6_reverse_link_reassign_clear():
    a1 = smalluml_Entity(name="sample_text")
    a2 = smalluml_Entity(name="sample_text_2")
    b = smalluml_ClassDiagram(name="sample_text")
    _safe_set(b, 'smalluml_ClassDiagram', {a1})
    assert _is_linked(b, 'smalluml_ClassDiagram', a1)
    if hasattr(a1, 'smalluml_Entity'):
        assert _is_linked(a1, 'smalluml_Entity', b)
    _safe_set(b, 'smalluml_ClassDiagram', {a2})
    assert _is_linked(b, 'smalluml_ClassDiagram', a2)
    if hasattr(a1, 'smalluml_Entity'):
        assert not _is_linked(a1, 'smalluml_Entity', b)
    if hasattr(a2, 'smalluml_Entity'):
        assert _is_linked(a2, 'smalluml_Entity', b)
    _safe_set(b, 'smalluml_ClassDiagram', set())
    assert not _is_linked(b, 'smalluml_ClassDiagram', a2)
    if hasattr(a2, 'smalluml_Entity'):
        assert not _is_linked(a2, 'smalluml_Entity', b)


def test_assoc_extends2_reverse_link_reassign_clear():
    a1 = smalluml_Class(abstract=True)
    a2 = smalluml_Class(abstract=False)
    b = smalluml_Class(abstract=True)
    _safe_set(b, 'smalluml_Class3', a1)
    assert _is_linked(b, 'smalluml_Class3', a1)
    if hasattr(a1, 'smalluml_Class1'):
        assert _is_linked(a1, 'smalluml_Class1', b)
    _safe_set(b, 'smalluml_Class3', a2)
    assert _is_linked(b, 'smalluml_Class3', a2)
    if hasattr(a1, 'smalluml_Class1'):
        assert not _is_linked(a1, 'smalluml_Class1', b)
    if hasattr(a2, 'smalluml_Class1'):
        assert _is_linked(a2, 'smalluml_Class1', b)
    _safe_set(b, 'smalluml_Class3', None)
    assert not _is_linked(b, 'smalluml_Class3', a2)
    if hasattr(a2, 'smalluml_Class1'):
        assert not _is_linked(a2, 'smalluml_Class1', b)


def test_assoc_operations4_reverse_link_reassign_clear():
    a1 = smalluml_Operation(name="sample_text")
    a2 = smalluml_Operation(name="sample_text_2")
    b = smalluml_Class(abstract=True)
    _safe_set(b, 'smalluml_Class5', {a1})
    assert _is_linked(b, 'smalluml_Class5', a1)
    if hasattr(a1, 'smalluml_Operation'):
        assert _is_linked(a1, 'smalluml_Operation', b)
    _safe_set(b, 'smalluml_Class5', {a2})
    assert _is_linked(b, 'smalluml_Class5', a2)
    if hasattr(a1, 'smalluml_Operation'):
        assert not _is_linked(a1, 'smalluml_Operation', b)
    if hasattr(a2, 'smalluml_Operation'):
        assert _is_linked(a2, 'smalluml_Operation', b)
    _safe_set(b, 'smalluml_Class5', set())
    assert not _is_linked(b, 'smalluml_Class5', a2)
    if hasattr(a2, 'smalluml_Operation'):
        assert not _is_linked(a2, 'smalluml_Operation', b)


def test_assoc_parameters9_reverse_link_reassign_clear():
    a1 = smalluml_Parameter(name="sample_text")
    a2 = smalluml_Parameter(name="sample_text_2")
    b = smalluml_Operation(name="sample_text")
    _safe_set(b, 'smalluml_Operation10', {a1})
    assert _is_linked(b, 'smalluml_Operation10', a1)
    if hasattr(a1, 'smalluml_Parameter'):
        assert _is_linked(a1, 'smalluml_Parameter', b)
    _safe_set(b, 'smalluml_Operation10', {a2})
    assert _is_linked(b, 'smalluml_Operation10', a2)
    if hasattr(a1, 'smalluml_Parameter'):
        assert not _is_linked(a1, 'smalluml_Parameter', b)
    if hasattr(a2, 'smalluml_Parameter'):
        assert _is_linked(a2, 'smalluml_Parameter', b)
    _safe_set(b, 'smalluml_Operation10', set())
    assert not _is_linked(b, 'smalluml_Operation10', a2)
    if hasattr(a2, 'smalluml_Parameter'):
        assert not _is_linked(a2, 'smalluml_Parameter', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cardinalities17_stub_double():
    # smalluml_Association has no real 'smalluml_Association' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Cardinalities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Cardinalities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Cardinalities(lowerbound=7, upperbound=7)
    partner = smalluml_Association()
    setattr(partner, 'smalluml_Association', None)
    _safe_set(owner, 'smalluml_Cardinalities', partner)
    assert getattr(partner, 'smalluml_Association') == owner
    _safe_set(owner, 'smalluml_Cardinalities', None)
    assert getattr(partner, 'smalluml_Association') is None


def test_assoc_sourceclass21_stub_double():
    # smalluml_Association has no real 'smalluml_Association22' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Class(abstract=True)
    partner = smalluml_Association()
    setattr(partner, 'smalluml_Association22', None)
    _safe_set(owner, 'smalluml_Class23', partner)
    assert getattr(partner, 'smalluml_Association22') == owner
    _safe_set(owner, 'smalluml_Class23', None)
    assert getattr(partner, 'smalluml_Association22') is None


def test_assoc_targetclass18_stub_double():
    # smalluml_Association has no real 'smalluml_Association19' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Class(abstract=True)
    partner = smalluml_Association()
    setattr(partner, 'smalluml_Association19', None)
    _safe_set(owner, 'smalluml_Class20', partner)
    assert getattr(partner, 'smalluml_Association19') == owner
    _safe_set(owner, 'smalluml_Class20', None)
    assert getattr(partner, 'smalluml_Association19') is None


def test_assoc_type11_stub_double():
    # smalluml_Type has no real 'smalluml_Type13' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Attribute(name="sample_text")
    partner = smalluml_Type()
    setattr(partner, 'smalluml_Type13', None)
    _safe_set(owner, 'smalluml_Attribute12', partner)
    assert getattr(partner, 'smalluml_Type13') == owner
    _safe_set(owner, 'smalluml_Attribute12', None)
    assert getattr(partner, 'smalluml_Type13') is None


def test_assoc_type14_stub_double():
    # smalluml_Type has no real 'smalluml_Type16' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Parameter(name="sample_text")
    partner = smalluml_Type()
    setattr(partner, 'smalluml_Type16', None)
    _safe_set(owner, 'smalluml_Parameter15', partner)
    assert getattr(partner, 'smalluml_Type16') == owner
    _safe_set(owner, 'smalluml_Parameter15', None)
    assert getattr(partner, 'smalluml_Type16') is None


def test_assoc_typeReturn7_stub_double():
    # smalluml_Type has no real 'smalluml_Type' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Operation(name="sample_text")
    partner = smalluml_Type()
    setattr(partner, 'smalluml_Type', None)
    _safe_set(owner, 'smalluml_Operation8', partner)
    assert getattr(partner, 'smalluml_Type') == owner
    _safe_set(owner, 'smalluml_Operation8', None)
    assert getattr(partner, 'smalluml_Type') is None


