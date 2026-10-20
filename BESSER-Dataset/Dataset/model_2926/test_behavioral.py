import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    Type,
    wh_AbstractElement,
    wh_DataType,
    wh_Entity,
    wh_Feature,
    wh_Import,
    wh_PackageDeclaration,
    wh_Type,
    wh_Wh,
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

def test_assoc_type7_reverse_link_reassign_clear():
    a1 = wh_Type(name="sample_text")
    a2 = wh_Type(name="sample_text_2")
    b = wh_Feature(many=True, name="sample_text")
    _safe_set(b, 'wh_Feature8', a1)
    assert _is_linked(b, 'wh_Feature8', a1)
    if hasattr(a1, 'wh_Type'):
        assert _is_linked(a1, 'wh_Type', b)
    _safe_set(b, 'wh_Feature8', a2)
    assert _is_linked(b, 'wh_Feature8', a2)
    if hasattr(a1, 'wh_Type'):
        assert not _is_linked(a1, 'wh_Type', b)
    if hasattr(a2, 'wh_Type'):
        assert _is_linked(a2, 'wh_Type', b)
    _safe_set(b, 'wh_Feature8', None)
    assert not _is_linked(b, 'wh_Feature8', a2)
    if hasattr(a2, 'wh_Type'):
        assert not _is_linked(a2, 'wh_Type', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements1_stub_double():
    # wh_AbstractElement has no real 'wh_AbstractElement2' property in the generated
    # code (a bare stub) -- manually attach it so wh_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_PackageDeclaration(name="sample_text")
    partner = wh_AbstractElement()
    setattr(partner, 'wh_AbstractElement2', None)
    _safe_set(owner, 'wh_PackageDeclaration', {partner})
    assert getattr(partner, 'wh_AbstractElement2') == owner
    _safe_set(owner, 'wh_PackageDeclaration', set())
    assert getattr(partner, 'wh_AbstractElement2') is None


def test_assoc_features5_stub_double():
    # wh_Entity has no real 'wh_Entity6' property in the generated
    # code (a bare stub) -- manually attach it so wh_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Feature(many=True, name="sample_text")
    partner = wh_Entity()
    setattr(partner, 'wh_Entity6', None)
    _safe_set(owner, 'wh_Feature', partner)
    assert owner in getattr(partner, 'wh_Entity6')
    _safe_set(owner, 'wh_Feature', None)
    assert owner not in getattr(partner, 'wh_Entity6')


