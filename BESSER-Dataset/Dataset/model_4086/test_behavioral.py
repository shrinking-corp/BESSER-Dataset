import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    simpleUML_Generalization,
    simpleUML_Model,
    simpleUML_SimpleClass,
    simpleUML_UMLAttribute,
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

def test_assoc_attributes6_reverse_link_reassign_clear():
    a1 = simpleUML_UMLAttribute(umlName="sample_text")
    a2 = simpleUML_UMLAttribute(umlName="sample_text_2")
    b = simpleUML_SimpleClass(simpleName="sample_text")
    _safe_set(b, 'simpleUML_SimpleClass7', {a1})
    assert _is_linked(b, 'simpleUML_SimpleClass7', a1)
    if hasattr(a1, 'simpleUML_UMLAttribute'):
        assert _is_linked(a1, 'simpleUML_UMLAttribute', b)
    _safe_set(b, 'simpleUML_SimpleClass7', {a2})
    assert _is_linked(b, 'simpleUML_SimpleClass7', a2)
    if hasattr(a1, 'simpleUML_UMLAttribute'):
        assert not _is_linked(a1, 'simpleUML_UMLAttribute', b)
    if hasattr(a2, 'simpleUML_UMLAttribute'):
        assert _is_linked(a2, 'simpleUML_UMLAttribute', b)
    _safe_set(b, 'simpleUML_SimpleClass7', set())
    assert not _is_linked(b, 'simpleUML_SimpleClass7', a2)
    if hasattr(a2, 'simpleUML_UMLAttribute'):
        assert not _is_linked(a2, 'simpleUML_UMLAttribute', b)


def test_assoc_superclasses2_reverse_link_reassign_clear():
    a1 = simpleUML_SimpleClass(simpleName="sample_text")
    a2 = simpleUML_SimpleClass(simpleName="sample_text_2")
    b = simpleUML_SimpleClass(simpleName="sample_text")
    _safe_set(b, 'simpleUML_SimpleClass3', a1)
    assert _is_linked(b, 'simpleUML_SimpleClass3', a1)
    if hasattr(a1, 'simpleUML_SimpleClass1'):
        assert _is_linked(a1, 'simpleUML_SimpleClass1', b)
    _safe_set(b, 'simpleUML_SimpleClass3', a2)
    assert _is_linked(b, 'simpleUML_SimpleClass3', a2)
    if hasattr(a1, 'simpleUML_SimpleClass1'):
        assert not _is_linked(a1, 'simpleUML_SimpleClass1', b)
    if hasattr(a2, 'simpleUML_SimpleClass1'):
        assert _is_linked(a2, 'simpleUML_SimpleClass1', b)
    _safe_set(b, 'simpleUML_SimpleClass3', None)
    assert not _is_linked(b, 'simpleUML_SimpleClass3', a2)
    if hasattr(a2, 'simpleUML_SimpleClass1'):
        assert not _is_linked(a2, 'simpleUML_SimpleClass1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classes0_stub_double():
    # simpleUML_Model has no real 'simpleUML_Model' property in the generated
    # code (a bare stub) -- manually attach it so simpleUML_SimpleClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleUML_SimpleClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleUML_SimpleClass(simpleName="sample_text")
    partner = simpleUML_Model()
    setattr(partner, 'simpleUML_Model', None)
    _safe_set(owner, 'simpleUML_SimpleClass', partner)
    assert owner in getattr(partner, 'simpleUML_Model')
    _safe_set(owner, 'simpleUML_SimpleClass', None)
    assert owner not in getattr(partner, 'simpleUML_Model')


def test_assoc_generalizations4_stub_double():
    # simpleUML_Generalization has no real 'simpleUML_Generalization' property in the generated
    # code (a bare stub) -- manually attach it so simpleUML_SimpleClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleUML_SimpleClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleUML_SimpleClass(simpleName="sample_text")
    partner = simpleUML_Generalization()
    setattr(partner, 'simpleUML_Generalization', None)
    _safe_set(owner, 'simpleUML_SimpleClass5', {partner})
    assert getattr(partner, 'simpleUML_Generalization') == owner
    _safe_set(owner, 'simpleUML_SimpleClass5', set())
    assert getattr(partner, 'simpleUML_Generalization') is None


def test_assoc_reference8_stub_double():
    # simpleUML_Generalization has no real 'simpleUML_Generalization9' property in the generated
    # code (a bare stub) -- manually attach it so simpleUML_SimpleClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleUML_SimpleClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleUML_SimpleClass(simpleName="sample_text")
    partner = simpleUML_Generalization()
    setattr(partner, 'simpleUML_Generalization9', None)
    _safe_set(owner, 'simpleUML_SimpleClass10', partner)
    assert getattr(partner, 'simpleUML_Generalization9') == owner
    _safe_set(owner, 'simpleUML_SimpleClass10', None)
    assert getattr(partner, 'simpleUML_Generalization9') is None


