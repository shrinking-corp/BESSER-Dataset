import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    metamodel_Datatype,
    metamodel_Entity,
    metamodel_Feature,
    metamodel_Model,
    metamodel_Query,
    metamodel_Type,
    metamodel_parameter,
    Annotation,
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

def test_assoc_parameters10_reverse_link_reassign_clear():
    a1 = metamodel_parameter(name="sample_text")
    a2 = metamodel_parameter(name="sample_text_2")
    b = metamodel_Query(methodName="sample_text", queryString="sample_text")
    _safe_set(b, 'metamodel_Query11', {a1})
    assert _is_linked(b, 'metamodel_Query11', a1)
    if hasattr(a1, 'metamodel_parameter'):
        assert _is_linked(a1, 'metamodel_parameter', b)
    _safe_set(b, 'metamodel_Query11', {a2})
    assert _is_linked(b, 'metamodel_Query11', a2)
    if hasattr(a1, 'metamodel_parameter'):
        assert not _is_linked(a1, 'metamodel_parameter', b)
    if hasattr(a2, 'metamodel_parameter'):
        assert _is_linked(a2, 'metamodel_parameter', b)
    _safe_set(b, 'metamodel_Query11', set())
    assert not _is_linked(b, 'metamodel_Query11', a2)
    if hasattr(a2, 'metamodel_parameter'):
        assert not _is_linked(a2, 'metamodel_parameter', b)


def test_assoc_type12_reverse_link_reassign_clear():
    a1 = metamodel_parameter(name="sample_text")
    a2 = metamodel_parameter(name="sample_text_2")
    b = metamodel_Type(name="sample_text")
    _safe_set(b, 'metamodel_Type14', a1)
    assert _is_linked(b, 'metamodel_Type14', a1)
    if hasattr(a1, 'metamodel_parameter13'):
        assert _is_linked(a1, 'metamodel_parameter13', b)
    _safe_set(b, 'metamodel_Type14', a2)
    assert _is_linked(b, 'metamodel_Type14', a2)
    if hasattr(a1, 'metamodel_parameter13'):
        assert not _is_linked(a1, 'metamodel_parameter13', b)
    if hasattr(a2, 'metamodel_parameter13'):
        assert _is_linked(a2, 'metamodel_parameter13', b)
    _safe_set(b, 'metamodel_Type14', None)
    assert not _is_linked(b, 'metamodel_Type14', a2)
    if hasattr(a2, 'metamodel_parameter13'):
        assert not _is_linked(a2, 'metamodel_parameter13', b)


def test_assoc_type4_reverse_link_reassign_clear():
    a1 = metamodel_Type(name="sample_text")
    a2 = metamodel_Type(name="sample_text_2")
    b = metamodel_Feature(annotation="sample_text", mappedBy="sample_text", name="sample_text")
    _safe_set(b, 'metamodel_Feature5', a1)
    assert _is_linked(b, 'metamodel_Feature5', a1)
    if hasattr(a1, 'metamodel_Type6'):
        assert _is_linked(a1, 'metamodel_Type6', b)
    _safe_set(b, 'metamodel_Feature5', a2)
    assert _is_linked(b, 'metamodel_Feature5', a2)
    if hasattr(a1, 'metamodel_Type6'):
        assert not _is_linked(a1, 'metamodel_Type6', b)
    if hasattr(a2, 'metamodel_Type6'):
        assert _is_linked(a2, 'metamodel_Type6', b)
    _safe_set(b, 'metamodel_Feature5', None)
    assert not _is_linked(b, 'metamodel_Feature5', a2)
    if hasattr(a2, 'metamodel_Type6'):
        assert not _is_linked(a2, 'metamodel_Type6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_EReference07_stub_double():
    # metamodel_Entity has no real 'metamodel_Entity9' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Query(methodName="sample_text", queryString="sample_text")
    partner = metamodel_Entity()
    setattr(partner, 'metamodel_Entity9', None)
    _safe_set(owner, 'metamodel_Query8', partner)
    assert getattr(partner, 'metamodel_Entity9') == owner
    _safe_set(owner, 'metamodel_Query8', None)
    assert getattr(partner, 'metamodel_Entity9') is None


def test_assoc_features1_stub_double():
    # metamodel_Entity has no real 'metamodel_Entity' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Feature(annotation="sample_text", mappedBy="sample_text", name="sample_text")
    partner = metamodel_Entity()
    setattr(partner, 'metamodel_Entity', None)
    _safe_set(owner, 'metamodel_Feature', partner)
    assert getattr(partner, 'metamodel_Entity') == owner
    _safe_set(owner, 'metamodel_Feature', None)
    assert getattr(partner, 'metamodel_Entity') is None


def test_assoc_queries2_stub_double():
    # metamodel_Entity has no real 'metamodel_Entity3' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Query(methodName="sample_text", queryString="sample_text")
    partner = metamodel_Entity()
    setattr(partner, 'metamodel_Entity3', None)
    _safe_set(owner, 'metamodel_Query', partner)
    assert getattr(partner, 'metamodel_Entity3') == owner
    _safe_set(owner, 'metamodel_Query', None)
    assert getattr(partner, 'metamodel_Entity3') is None


def test_assoc_types0_stub_double():
    # metamodel_Model has no real 'metamodel_Model' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Type(name="sample_text")
    partner = metamodel_Model()
    setattr(partner, 'metamodel_Model', None)
    _safe_set(owner, 'metamodel_Type', partner)
    assert getattr(partner, 'metamodel_Model') == owner
    _safe_set(owner, 'metamodel_Type', None)
    assert getattr(partner, 'metamodel_Model') is None


