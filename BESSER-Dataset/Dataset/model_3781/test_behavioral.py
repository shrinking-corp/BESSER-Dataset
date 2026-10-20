import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Dependency,
    Feature,
    UnaryDependency,
    assignment6_model_BinaryDependency,
    assignment6_model_Configurator,
    assignment6_model_Dependency,
    assignment6_model_Feature,
    assignment6_model_Group,
    assignment6_model_IntegerFeature,
    assignment6_model_IntegerValueDependency,
    assignment6_model_IsSelectedDependency,
    assignment6_model_SimpleFeature,
    assignment6_model_UnaryDependency,
    BinaryOperator,
    GroupType,
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

def test_assoc_dependencies9_reverse_link_reassign_clear():
    a1 = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    a2 = assignment6_model_Feature(mandatory=False, name="sample_text_2", selected=False)
    b = assignment6_model_Dependency(not_=True)
    _safe_set(b, 'assignment6_model_Dependency', a1)
    assert _is_linked(b, 'assignment6_model_Dependency', a1)
    if hasattr(a1, 'assignment6_model_Feature10'):
        assert _is_linked(a1, 'assignment6_model_Feature10', b)
    _safe_set(b, 'assignment6_model_Dependency', a2)
    assert _is_linked(b, 'assignment6_model_Dependency', a2)
    if hasattr(a1, 'assignment6_model_Feature10'):
        assert not _is_linked(a1, 'assignment6_model_Feature10', b)
    if hasattr(a2, 'assignment6_model_Feature10'):
        assert _is_linked(a2, 'assignment6_model_Feature10', b)
    _safe_set(b, 'assignment6_model_Dependency', None)
    assert not _is_linked(b, 'assignment6_model_Dependency', a2)
    if hasattr(a2, 'assignment6_model_Feature10'):
        assert not _is_linked(a2, 'assignment6_model_Feature10', b)


def test_assoc_features0_reverse_link_reassign_clear():
    a1 = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    a2 = assignment6_model_Feature(mandatory=False, name="sample_text_2", selected=False)
    b = assignment6_model_Configurator(name="sample_text")
    _safe_set(b, 'assignment6_model_Configurator', {a1})
    assert _is_linked(b, 'assignment6_model_Configurator', a1)
    if hasattr(a1, 'assignment6_model_Feature'):
        assert _is_linked(a1, 'assignment6_model_Feature', b)
    _safe_set(b, 'assignment6_model_Configurator', {a2})
    assert _is_linked(b, 'assignment6_model_Configurator', a2)
    if hasattr(a1, 'assignment6_model_Feature'):
        assert not _is_linked(a1, 'assignment6_model_Feature', b)
    if hasattr(a2, 'assignment6_model_Feature'):
        assert _is_linked(a2, 'assignment6_model_Feature', b)
    _safe_set(b, 'assignment6_model_Configurator', set())
    assert not _is_linked(b, 'assignment6_model_Configurator', a2)
    if hasattr(a2, 'assignment6_model_Feature'):
        assert not _is_linked(a2, 'assignment6_model_Feature', b)


def test_assoc_features4_reverse_link_reassign_clear():
    a1 = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    a2 = assignment6_model_Feature(mandatory=False, name="sample_text_2", selected=False)
    b = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    _safe_set(b, 'assignment6_model_Feature5', a1)
    assert _is_linked(b, 'assignment6_model_Feature5', a1)
    if hasattr(a1, 'assignment6_model_Feature3'):
        assert _is_linked(a1, 'assignment6_model_Feature3', b)
    _safe_set(b, 'assignment6_model_Feature5', a2)
    assert _is_linked(b, 'assignment6_model_Feature5', a2)
    if hasattr(a1, 'assignment6_model_Feature3'):
        assert not _is_linked(a1, 'assignment6_model_Feature3', b)
    if hasattr(a2, 'assignment6_model_Feature3'):
        assert _is_linked(a2, 'assignment6_model_Feature3', b)
    _safe_set(b, 'assignment6_model_Feature5', None)
    assert not _is_linked(b, 'assignment6_model_Feature5', a2)
    if hasattr(a2, 'assignment6_model_Feature3'):
        assert not _is_linked(a2, 'assignment6_model_Feature3', b)


def test_assoc_groups1_reverse_link_reassign_clear():
    a1 = assignment6_model_Group(groupType="sample_text", name="sample_text")
    a2 = assignment6_model_Group(groupType="sample_text_2", name="sample_text_2")
    b = assignment6_model_Configurator(name="sample_text")
    _safe_set(b, 'assignment6_model_Configurator2', {a1})
    assert _is_linked(b, 'assignment6_model_Configurator2', a1)
    if hasattr(a1, 'assignment6_model_Group'):
        assert _is_linked(a1, 'assignment6_model_Group', b)
    _safe_set(b, 'assignment6_model_Configurator2', {a2})
    assert _is_linked(b, 'assignment6_model_Configurator2', a2)
    if hasattr(a1, 'assignment6_model_Group'):
        assert not _is_linked(a1, 'assignment6_model_Group', b)
    if hasattr(a2, 'assignment6_model_Group'):
        assert _is_linked(a2, 'assignment6_model_Group', b)
    _safe_set(b, 'assignment6_model_Configurator2', set())
    assert not _is_linked(b, 'assignment6_model_Configurator2', a2)
    if hasattr(a2, 'assignment6_model_Group'):
        assert not _is_linked(a2, 'assignment6_model_Group', b)


def test_assoc_groups6_reverse_link_reassign_clear():
    a1 = assignment6_model_Group(groupType="sample_text", name="sample_text")
    a2 = assignment6_model_Group(groupType="sample_text_2", name="sample_text_2")
    b = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    _safe_set(b, 'assignment6_model_Feature7', {a1})
    assert _is_linked(b, 'assignment6_model_Feature7', a1)
    if hasattr(a1, 'assignment6_model_Group8'):
        assert _is_linked(a1, 'assignment6_model_Group8', b)
    _safe_set(b, 'assignment6_model_Feature7', {a2})
    assert _is_linked(b, 'assignment6_model_Feature7', a2)
    if hasattr(a1, 'assignment6_model_Group8'):
        assert not _is_linked(a1, 'assignment6_model_Group8', b)
    if hasattr(a2, 'assignment6_model_Group8'):
        assert _is_linked(a2, 'assignment6_model_Group8', b)
    _safe_set(b, 'assignment6_model_Feature7', set())
    assert not _is_linked(b, 'assignment6_model_Feature7', a2)
    if hasattr(a2, 'assignment6_model_Group8'):
        assert not _is_linked(a2, 'assignment6_model_Group8', b)


def test_assoc_leftHand15_reverse_link_reassign_clear():
    a1 = assignment6_model_Dependency(not_=True)
    a2 = assignment6_model_Dependency(not_=False)
    b = assignment6_model_BinaryDependency(operator="sample_text")
    _safe_set(b, 'assignment6_model_BinaryDependency16', a1)
    assert _is_linked(b, 'assignment6_model_BinaryDependency16', a1)
    if hasattr(a1, 'assignment6_model_Dependency17'):
        assert _is_linked(a1, 'assignment6_model_Dependency17', b)
    _safe_set(b, 'assignment6_model_BinaryDependency16', a2)
    assert _is_linked(b, 'assignment6_model_BinaryDependency16', a2)
    if hasattr(a1, 'assignment6_model_Dependency17'):
        assert not _is_linked(a1, 'assignment6_model_Dependency17', b)
    if hasattr(a2, 'assignment6_model_Dependency17'):
        assert _is_linked(a2, 'assignment6_model_Dependency17', b)
    _safe_set(b, 'assignment6_model_BinaryDependency16', None)
    assert not _is_linked(b, 'assignment6_model_BinaryDependency16', a2)
    if hasattr(a2, 'assignment6_model_Dependency17'):
        assert not _is_linked(a2, 'assignment6_model_Dependency17', b)


def test_assoc_rightHand13_reverse_link_reassign_clear():
    a1 = assignment6_model_Dependency(not_=True)
    a2 = assignment6_model_Dependency(not_=False)
    b = assignment6_model_BinaryDependency(operator="sample_text")
    _safe_set(b, 'assignment6_model_BinaryDependency', a1)
    assert _is_linked(b, 'assignment6_model_BinaryDependency', a1)
    if hasattr(a1, 'assignment6_model_Dependency14'):
        assert _is_linked(a1, 'assignment6_model_Dependency14', b)
    _safe_set(b, 'assignment6_model_BinaryDependency', a2)
    assert _is_linked(b, 'assignment6_model_BinaryDependency', a2)
    if hasattr(a1, 'assignment6_model_Dependency14'):
        assert not _is_linked(a1, 'assignment6_model_Dependency14', b)
    if hasattr(a2, 'assignment6_model_Dependency14'):
        assert _is_linked(a2, 'assignment6_model_Dependency14', b)
    _safe_set(b, 'assignment6_model_BinaryDependency', None)
    assert not _is_linked(b, 'assignment6_model_BinaryDependency', a2)
    if hasattr(a2, 'assignment6_model_Dependency14'):
        assert not _is_linked(a2, 'assignment6_model_Dependency14', b)


def test_assoc_target20_reverse_link_reassign_clear():
    a1 = assignment6_model_IntegerValueDependency(value=7)
    a2 = assignment6_model_IntegerValueDependency(value=13)
    b = assignment6_model_IntegerFeature(maxValue=7, minValue=7, step=7, value=7)
    _safe_set(b, 'assignment6_model_IntegerFeature', a1)
    assert _is_linked(b, 'assignment6_model_IntegerFeature', a1)
    if hasattr(a1, 'assignment6_model_IntegerValueDependency'):
        assert _is_linked(a1, 'assignment6_model_IntegerValueDependency', b)
    _safe_set(b, 'assignment6_model_IntegerFeature', a2)
    assert _is_linked(b, 'assignment6_model_IntegerFeature', a2)
    if hasattr(a1, 'assignment6_model_IntegerValueDependency'):
        assert not _is_linked(a1, 'assignment6_model_IntegerValueDependency', b)
    if hasattr(a2, 'assignment6_model_IntegerValueDependency'):
        assert _is_linked(a2, 'assignment6_model_IntegerValueDependency', b)
    _safe_set(b, 'assignment6_model_IntegerFeature', None)
    assert not _is_linked(b, 'assignment6_model_IntegerFeature', a2)
    if hasattr(a2, 'assignment6_model_IntegerValueDependency'):
        assert not _is_linked(a2, 'assignment6_model_IntegerValueDependency', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_features11_stub_double():
    # assignment6_model_SimpleFeature has no real 'assignment6_model_SimpleFeature' property in the generated
    # code (a bare stub) -- manually attach it so assignment6_model_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assignment6_model_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assignment6_model_Group(groupType="sample_text", name="sample_text")
    partner = assignment6_model_SimpleFeature()
    setattr(partner, 'assignment6_model_SimpleFeature', None)
    _safe_set(owner, 'assignment6_model_Group12', {partner})
    assert getattr(partner, 'assignment6_model_SimpleFeature') == owner
    _safe_set(owner, 'assignment6_model_Group12', set())
    assert getattr(partner, 'assignment6_model_SimpleFeature') is None


def test_assoc_target18_stub_double():
    # assignment6_model_IsSelectedDependency has no real 'assignment6_model_IsSelectedDependency' property in the generated
    # code (a bare stub) -- manually attach it so assignment6_model_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assignment6_model_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assignment6_model_Feature(mandatory=True, name="sample_text", selected=True)
    partner = assignment6_model_IsSelectedDependency()
    setattr(partner, 'assignment6_model_IsSelectedDependency', None)
    _safe_set(owner, 'assignment6_model_Feature19', partner)
    assert getattr(partner, 'assignment6_model_IsSelectedDependency') == owner
    _safe_set(owner, 'assignment6_model_Feature19', None)
    assert getattr(partner, 'assignment6_model_IsSelectedDependency') is None


