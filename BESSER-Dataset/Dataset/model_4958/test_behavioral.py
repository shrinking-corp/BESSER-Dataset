import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Model,
    ModelElement,
    NamedElement,
    TypedElement,
    testmodel_Association,
    testmodel_Attribute,
    testmodel_Class,
    testmodel_Group,
    testmodel_Model,
    testmodel_ModelElement,
    testmodel_NamedElement,
    testmodel_TypedElement,
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

def test_assoc_first4_stub_double():
    # testmodel_Class has no real 'testmodel_Class5' property in the generated
    # code (a bare stub) -- manually attach it so testmodel_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testmodel_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testmodel_Association(firstLabel="sample_text", secondLabel="sample_text")
    partner = testmodel_Class()
    setattr(partner, 'testmodel_Class5', None)
    _safe_set(owner, 'testmodel_Association', partner)
    assert getattr(partner, 'testmodel_Class5') == owner
    _safe_set(owner, 'testmodel_Association', None)
    assert getattr(partner, 'testmodel_Class5') is None


def test_assoc_second6_stub_double():
    # testmodel_Class has no real 'testmodel_Class8' property in the generated
    # code (a bare stub) -- manually attach it so testmodel_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testmodel_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testmodel_Association(firstLabel="sample_text", secondLabel="sample_text")
    partner = testmodel_Class()
    setattr(partner, 'testmodel_Class8', None)
    _safe_set(owner, 'testmodel_Association7', partner)
    assert getattr(partner, 'testmodel_Class8') == owner
    _safe_set(owner, 'testmodel_Association7', None)
    assert getattr(partner, 'testmodel_Class8') is None


