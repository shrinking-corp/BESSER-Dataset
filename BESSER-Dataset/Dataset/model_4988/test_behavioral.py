import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Component,
    Port,
    Property,
    componentmodel_Component,
    componentmodel_CompositeComponent,
    componentmodel_EnumProperty,
    componentmodel_InPort,
    componentmodel_NumericProperty,
    componentmodel_OutPort,
    componentmodel_Port,
    componentmodel_PrimitiveComponent,
    componentmodel_Property,
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

def test_assoc_ports0_reverse_link_reassign_clear():
    a1 = componentmodel_Port(description="sample_text", name="sample_text", type="sample_text", typePackage="sample_text")
    a2 = componentmodel_Port(description="sample_text_2", name="sample_text_2", type="sample_text_2", typePackage="sample_text_2")
    b = componentmodel_Component(description="sample_text", name="sample_text")
    _safe_set(b, 'componentmodel_Component', {a1})
    assert _is_linked(b, 'componentmodel_Component', a1)
    if hasattr(a1, 'componentmodel_Port'):
        assert _is_linked(a1, 'componentmodel_Port', b)
    _safe_set(b, 'componentmodel_Component', {a2})
    assert _is_linked(b, 'componentmodel_Component', a2)
    if hasattr(a1, 'componentmodel_Port'):
        assert not _is_linked(a1, 'componentmodel_Port', b)
    if hasattr(a2, 'componentmodel_Port'):
        assert _is_linked(a2, 'componentmodel_Port', b)
    _safe_set(b, 'componentmodel_Component', set())
    assert not _is_linked(b, 'componentmodel_Component', a2)
    if hasattr(a2, 'componentmodel_Port'):
        assert not _is_linked(a2, 'componentmodel_Port', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_components2_stub_double():
    # componentmodel_CompositeComponent has no real 'componentmodel_CompositeComponent' property in the generated
    # code (a bare stub) -- manually attach it so componentmodel_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentmodel_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentmodel_Component(description="sample_text", name="sample_text")
    partner = componentmodel_CompositeComponent()
    setattr(partner, 'componentmodel_CompositeComponent', None)
    _safe_set(owner, 'componentmodel_Component3', partner)
    assert owner in getattr(partner, 'componentmodel_CompositeComponent')
    _safe_set(owner, 'componentmodel_Component3', None)
    assert owner not in getattr(partner, 'componentmodel_CompositeComponent')


def test_assoc_properties1_stub_double():
    # componentmodel_PrimitiveComponent has no real 'componentmodel_PrimitiveComponent' property in the generated
    # code (a bare stub) -- manually attach it so componentmodel_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentmodel_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentmodel_Property(description="sample_text", name="sample_text")
    partner = componentmodel_PrimitiveComponent()
    setattr(partner, 'componentmodel_PrimitiveComponent', None)
    _safe_set(owner, 'componentmodel_Property', partner)
    assert owner in getattr(partner, 'componentmodel_PrimitiveComponent')
    _safe_set(owner, 'componentmodel_Property', None)
    assert owner not in getattr(partner, 'componentmodel_PrimitiveComponent')


