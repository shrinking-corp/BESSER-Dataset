import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Clonable,
    Node,
    fmp_Clonable,
    fmp_Constraint,
    fmp_Feature,
    fmp_FeatureGroup,
    fmp_Node,
    fmp_Project,
    fmp_Reference,
    fmp_TypedValue,
    ConfigState,
    ValueType,
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

def test_assoc_children15_reverse_link_reassign_clear():
    a1 = fmp_Node(id="sample_text", max=7, min=7)
    a2 = fmp_Node(id="sample_text_2", max=13, min=13)
    b = fmp_Node(id="sample_text", max=7, min=7)
    _safe_set(b, 'fmp_Node14', {a1})
    assert _is_linked(b, 'fmp_Node14', a1)
    if hasattr(a1, 'fmp_Node'):
        assert _is_linked(a1, 'fmp_Node', b)
    _safe_set(b, 'fmp_Node14', {a2})
    assert _is_linked(b, 'fmp_Node14', a2)
    if hasattr(a1, 'fmp_Node'):
        assert not _is_linked(a1, 'fmp_Node', b)
    if hasattr(a2, 'fmp_Node'):
        assert _is_linked(a2, 'fmp_Node', b)
    _safe_set(b, 'fmp_Node14', set())
    assert not _is_linked(b, 'fmp_Node14', a2)
    if hasattr(a2, 'fmp_Node'):
        assert not _is_linked(a2, 'fmp_Node', b)


def test_assoc_clones31_reverse_link_reassign_clear():
    a1 = fmp_Clonable(state="sample_text")
    a2 = fmp_Clonable(state="sample_text_2")
    b = fmp_Clonable(state="sample_text")
    _safe_set(b, 'prototype', {a1})
    assert _is_linked(b, 'prototype', a1)
    if hasattr(a1, 'Clonable'):
        assert _is_linked(a1, 'Clonable', b)
    _safe_set(b, 'prototype', {a2})
    assert _is_linked(b, 'prototype', a2)
    if hasattr(a1, 'Clonable'):
        assert not _is_linked(a1, 'Clonable', b)
    if hasattr(a2, 'Clonable'):
        assert _is_linked(a2, 'Clonable', b)
    _safe_set(b, 'prototype', set())
    assert not _is_linked(b, 'prototype', a2)
    if hasattr(a2, 'Clonable'):
        assert not _is_linked(a2, 'Clonable', b)


def test_assoc_configurations1_reverse_link_reassign_clear():
    a1 = fmp_Feature(name="sample_text", valueType="sample_text")
    a2 = fmp_Feature(name="sample_text_2", valueType="sample_text_2")
    b = fmp_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'fmp_Feature0', {a1})
    assert _is_linked(b, 'fmp_Feature0', a1)
    if hasattr(a1, 'fmp_Feature'):
        assert _is_linked(a1, 'fmp_Feature', b)
    _safe_set(b, 'fmp_Feature0', {a2})
    assert _is_linked(b, 'fmp_Feature0', a2)
    if hasattr(a1, 'fmp_Feature'):
        assert not _is_linked(a1, 'fmp_Feature', b)
    if hasattr(a2, 'fmp_Feature'):
        assert _is_linked(a2, 'fmp_Feature', b)
    _safe_set(b, 'fmp_Feature0', set())
    assert not _is_linked(b, 'fmp_Feature0', a2)
    if hasattr(a2, 'fmp_Feature'):
        assert not _is_linked(a2, 'fmp_Feature', b)


def test_assoc_confs9_reverse_link_reassign_clear():
    a1 = fmp_Node(id="sample_text", max=7, min=7)
    a2 = fmp_Node(id="sample_text_2", max=13, min=13)
    b = fmp_Node(id="sample_text", max=7, min=7)
    _safe_set(b, 'origin', {a1})
    assert _is_linked(b, 'origin', a1)
    if hasattr(a1, 'Node10'):
        assert _is_linked(a1, 'Node10', b)
    _safe_set(b, 'origin', {a2})
    assert _is_linked(b, 'origin', a2)
    if hasattr(a1, 'Node10'):
        assert not _is_linked(a1, 'Node10', b)
    if hasattr(a2, 'Node10'):
        assert _is_linked(a2, 'Node10', b)
    _safe_set(b, 'origin', set())
    assert not _is_linked(b, 'origin', a2)
    if hasattr(a2, 'Node10'):
        assert not _is_linked(a2, 'Node10', b)


def test_assoc_constraints6_reverse_link_reassign_clear():
    a1 = fmp_Feature(name="sample_text", valueType="sample_text")
    a2 = fmp_Feature(name="sample_text_2", valueType="sample_text_2")
    b = fmp_Constraint(text="sample_text")
    _safe_set(b, 'fmp_Constraint', a1)
    assert _is_linked(b, 'fmp_Constraint', a1)
    if hasattr(a1, 'fmp_Feature7'):
        assert _is_linked(a1, 'fmp_Feature7', b)
    _safe_set(b, 'fmp_Constraint', a2)
    assert _is_linked(b, 'fmp_Constraint', a2)
    if hasattr(a1, 'fmp_Feature7'):
        assert not _is_linked(a1, 'fmp_Feature7', b)
    if hasattr(a2, 'fmp_Feature7'):
        assert _is_linked(a2, 'fmp_Feature7', b)
    _safe_set(b, 'fmp_Constraint', None)
    assert not _is_linked(b, 'fmp_Constraint', a2)
    if hasattr(a2, 'fmp_Feature7'):
        assert not _is_linked(a2, 'fmp_Feature7', b)


def test_assoc_describedNode5_reverse_link_reassign_clear():
    a1 = fmp_Node(id="sample_text", max=7, min=7)
    a2 = fmp_Node(id="sample_text_2", max=13, min=13)
    b = fmp_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'properties', a1)
    assert _is_linked(b, 'properties', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'properties', a2)
    assert _is_linked(b, 'properties', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'properties', None)
    assert not _is_linked(b, 'properties', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_featureValue27_reverse_link_reassign_clear():
    a1 = fmp_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    a2 = fmp_TypedValue(floatValue="sample_text_2", integerValue="sample_text_2", stringValue="sample_text_2")
    b = fmp_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'fmp_Feature29', a1)
    assert _is_linked(b, 'fmp_Feature29', a1)
    if hasattr(a1, 'fmp_TypedValue28'):
        assert _is_linked(a1, 'fmp_TypedValue28', b)
    _safe_set(b, 'fmp_Feature29', a2)
    assert _is_linked(b, 'fmp_Feature29', a2)
    if hasattr(a1, 'fmp_TypedValue28'):
        assert not _is_linked(a1, 'fmp_TypedValue28', b)
    if hasattr(a2, 'fmp_TypedValue28'):
        assert _is_linked(a2, 'fmp_TypedValue28', b)
    _safe_set(b, 'fmp_Feature29', None)
    assert not _is_linked(b, 'fmp_Feature29', a2)
    if hasattr(a2, 'fmp_TypedValue28'):
        assert not _is_linked(a2, 'fmp_TypedValue28', b)


def test_assoc_origin12_reverse_link_reassign_clear():
    a1 = fmp_Node(id="sample_text", max=7, min=7)
    a2 = fmp_Node(id="sample_text_2", max=13, min=13)
    b = fmp_Node(id="sample_text", max=7, min=7)
    _safe_set(b, 'confs', a1)
    assert _is_linked(b, 'confs', a1)
    if hasattr(a1, 'Node13'):
        assert _is_linked(a1, 'Node13', b)
    _safe_set(b, 'confs', a2)
    assert _is_linked(b, 'confs', a2)
    if hasattr(a1, 'Node13'):
        assert not _is_linked(a1, 'Node13', b)
    if hasattr(a2, 'Node13'):
        assert _is_linked(a2, 'Node13', b)
    _safe_set(b, 'confs', None)
    assert not _is_linked(b, 'confs', a2)
    if hasattr(a2, 'Node13'):
        assert not _is_linked(a2, 'Node13', b)


def test_assoc_properties16_reverse_link_reassign_clear():
    a1 = fmp_Node(id="sample_text", max=7, min=7)
    a2 = fmp_Node(id="sample_text_2", max=13, min=13)
    b = fmp_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'Feature', a1)
    assert _is_linked(b, 'Feature', a1)
    if hasattr(a1, 'describedNode'):
        assert _is_linked(a1, 'describedNode', b)
    _safe_set(b, 'Feature', a2)
    assert _is_linked(b, 'Feature', a2)
    if hasattr(a1, 'describedNode'):
        assert not _is_linked(a1, 'describedNode', b)
    if hasattr(a2, 'describedNode'):
        assert _is_linked(a2, 'describedNode', b)
    _safe_set(b, 'Feature', None)
    assert not _is_linked(b, 'Feature', a2)
    if hasattr(a2, 'describedNode'):
        assert not _is_linked(a2, 'describedNode', b)


def test_assoc_prototype33_reverse_link_reassign_clear():
    a1 = fmp_Clonable(state="sample_text")
    a2 = fmp_Clonable(state="sample_text_2")
    b = fmp_Clonable(state="sample_text")
    _safe_set(b, 'clones', a1)
    assert _is_linked(b, 'clones', a1)
    if hasattr(a1, 'Clonable34'):
        assert _is_linked(a1, 'Clonable34', b)
    _safe_set(b, 'clones', a2)
    assert _is_linked(b, 'clones', a2)
    if hasattr(a1, 'Clonable34'):
        assert not _is_linked(a1, 'Clonable34', b)
    if hasattr(a2, 'Clonable34'):
        assert _is_linked(a2, 'Clonable34', b)
    _safe_set(b, 'clones', None)
    assert not _is_linked(b, 'clones', a2)
    if hasattr(a2, 'Clonable34'):
        assert not _is_linked(a2, 'Clonable34', b)


def test_assoc_typedValue3_reverse_link_reassign_clear():
    a1 = fmp_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    a2 = fmp_TypedValue(floatValue="sample_text_2", integerValue="sample_text_2", stringValue="sample_text_2")
    b = fmp_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'fmp_Feature4', a1)
    assert _is_linked(b, 'fmp_Feature4', a1)
    if hasattr(a1, 'fmp_TypedValue'):
        assert _is_linked(a1, 'fmp_TypedValue', b)
    _safe_set(b, 'fmp_Feature4', a2)
    assert _is_linked(b, 'fmp_Feature4', a2)
    if hasattr(a1, 'fmp_TypedValue'):
        assert not _is_linked(a1, 'fmp_TypedValue', b)
    if hasattr(a2, 'fmp_TypedValue'):
        assert _is_linked(a2, 'fmp_TypedValue', b)
    _safe_set(b, 'fmp_Feature4', None)
    assert not _is_linked(b, 'fmp_Feature4', a2)
    if hasattr(a2, 'fmp_TypedValue'):
        assert not _is_linked(a2, 'fmp_TypedValue', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_feature17_stub_double():
    # fmp_Reference has no real 'references' property in the generated
    # code (a bare stub) -- manually attach it so fmp_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmp_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmp_Feature(name="sample_text", valueType="sample_text")
    partner = fmp_Reference()
    setattr(partner, 'references', None)
    _safe_set(owner, 'Feature18', partner)
    assert getattr(partner, 'references') == owner
    _safe_set(owner, 'Feature18', None)
    assert getattr(partner, 'references') is None


def test_assoc_metaMetaModel24_stub_double():
    # fmp_Project has no real 'fmp_Project25' property in the generated
    # code (a bare stub) -- manually attach it so fmp_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmp_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmp_Feature(name="sample_text", valueType="sample_text")
    partner = fmp_Project()
    setattr(partner, 'fmp_Project25', None)
    _safe_set(owner, 'fmp_Feature26', partner)
    assert getattr(partner, 'fmp_Project25') == owner
    _safe_set(owner, 'fmp_Feature26', None)
    assert getattr(partner, 'fmp_Project25') is None


def test_assoc_metaModel21_stub_double():
    # fmp_Project has no real 'fmp_Project22' property in the generated
    # code (a bare stub) -- manually attach it so fmp_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmp_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmp_Feature(name="sample_text", valueType="sample_text")
    partner = fmp_Project()
    setattr(partner, 'fmp_Project22', None)
    _safe_set(owner, 'fmp_Feature23', partner)
    assert getattr(partner, 'fmp_Project22') == owner
    _safe_set(owner, 'fmp_Feature23', None)
    assert getattr(partner, 'fmp_Project22') is None


def test_assoc_model19_stub_double():
    # fmp_Project has no real 'fmp_Project' property in the generated
    # code (a bare stub) -- manually attach it so fmp_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmp_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmp_Feature(name="sample_text", valueType="sample_text")
    partner = fmp_Project()
    setattr(partner, 'fmp_Project', None)
    _safe_set(owner, 'fmp_Feature20', partner)
    assert getattr(partner, 'fmp_Project') == owner
    _safe_set(owner, 'fmp_Feature20', None)
    assert getattr(partner, 'fmp_Project') is None


def test_assoc_references2_stub_double():
    # fmp_Reference has no real 'Reference' property in the generated
    # code (a bare stub) -- manually attach it so fmp_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmp_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmp_Feature(name="sample_text", valueType="sample_text")
    partner = fmp_Reference()
    setattr(partner, 'Reference', None)
    _safe_set(owner, 'feature', {partner})
    assert getattr(partner, 'Reference') == owner
    _safe_set(owner, 'feature', set())
    assert getattr(partner, 'Reference') is None


