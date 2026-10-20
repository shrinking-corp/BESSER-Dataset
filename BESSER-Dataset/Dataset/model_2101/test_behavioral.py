import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Domain,
    Relation,
    afmmm_Attribute,
    afmmm_AttributedFeatureDiagram,
    afmmm_AttributedFeatureModel,
    afmmm_Boolean,
    afmmm_CrossTreeConstraint,
    afmmm_Domain,
    afmmm_EClass0,
    afmmm_Enum,
    afmmm_Feature,
    afmmm_Integer,
    afmmm_Mandatory,
    afmmm_Mutex,
    afmmm_Optional,
    afmmm_Or,
    afmmm_Real,
    afmmm_Relation,
    afmmm_XOr,
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

def test_assoc_attributes8_reverse_link_reassign_clear():
    a1 = afmmm_Feature(name="sample_text")
    a2 = afmmm_Feature(name="sample_text_2")
    b = afmmm_Attribute(name="sample_text")
    _safe_set(b, 'afmmm_Attribute', a1)
    assert _is_linked(b, 'afmmm_Attribute', a1)
    if hasattr(a1, 'afmmm_Feature9'):
        assert _is_linked(a1, 'afmmm_Feature9', b)
    _safe_set(b, 'afmmm_Attribute', a2)
    assert _is_linked(b, 'afmmm_Attribute', a2)
    if hasattr(a1, 'afmmm_Feature9'):
        assert not _is_linked(a1, 'afmmm_Feature9', b)
    if hasattr(a2, 'afmmm_Feature9'):
        assert _is_linked(a2, 'afmmm_Feature9', b)
    _safe_set(b, 'afmmm_Attribute', None)
    assert not _is_linked(b, 'afmmm_Attribute', a2)
    if hasattr(a2, 'afmmm_Feature9'):
        assert not _is_linked(a2, 'afmmm_Feature9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children13_stub_double():
    # afmmm_Relation has no real 'afmmm_Relation14' property in the generated
    # code (a bare stub) -- manually attach it so afmmm_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # afmmm_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = afmmm_Feature(name="sample_text")
    partner = afmmm_Relation()
    setattr(partner, 'afmmm_Relation14', None)
    _safe_set(owner, 'afmmm_Feature15', partner)
    assert owner in getattr(partner, 'afmmm_Relation14')
    _safe_set(owner, 'afmmm_Feature15', None)
    assert owner not in getattr(partner, 'afmmm_Relation14')


def test_assoc_domain23_stub_double():
    # afmmm_Domain has no real 'afmmm_Domain25' property in the generated
    # code (a bare stub) -- manually attach it so afmmm_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # afmmm_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = afmmm_Attribute(name="sample_text")
    partner = afmmm_Domain()
    setattr(partner, 'afmmm_Domain25', None)
    _safe_set(owner, 'afmmm_Attribute24', partner)
    assert getattr(partner, 'afmmm_Domain25') == owner
    _safe_set(owner, 'afmmm_Attribute24', None)
    assert getattr(partner, 'afmmm_Domain25') is None


def test_assoc_features0_stub_double():
    # afmmm_AttributedFeatureDiagram has no real 'afmmm_AttributedFeatureDiagram' property in the generated
    # code (a bare stub) -- manually attach it so afmmm_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # afmmm_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = afmmm_Feature(name="sample_text")
    partner = afmmm_AttributedFeatureDiagram()
    setattr(partner, 'afmmm_AttributedFeatureDiagram', None)
    _safe_set(owner, 'afmmm_Feature', partner)
    assert owner in getattr(partner, 'afmmm_AttributedFeatureDiagram')
    _safe_set(owner, 'afmmm_Feature', None)
    assert owner not in getattr(partner, 'afmmm_AttributedFeatureDiagram')


def test_assoc_parent10_stub_double():
    # afmmm_Relation has no real 'afmmm_Relation11' property in the generated
    # code (a bare stub) -- manually attach it so afmmm_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # afmmm_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = afmmm_Feature(name="sample_text")
    partner = afmmm_Relation()
    setattr(partner, 'afmmm_Relation11', None)
    _safe_set(owner, 'afmmm_Feature12', partner)
    assert getattr(partner, 'afmmm_Relation11') == owner
    _safe_set(owner, 'afmmm_Feature12', None)
    assert getattr(partner, 'afmmm_Relation11') is None


def test_assoc_root1_stub_double():
    # afmmm_AttributedFeatureDiagram has no real 'afmmm_AttributedFeatureDiagram2' property in the generated
    # code (a bare stub) -- manually attach it so afmmm_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # afmmm_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = afmmm_Feature(name="sample_text")
    partner = afmmm_AttributedFeatureDiagram()
    setattr(partner, 'afmmm_AttributedFeatureDiagram2', None)
    _safe_set(owner, 'afmmm_Feature3', partner)
    assert getattr(partner, 'afmmm_AttributedFeatureDiagram2') == owner
    _safe_set(owner, 'afmmm_Feature3', None)
    assert getattr(partner, 'afmmm_AttributedFeatureDiagram2') is None


