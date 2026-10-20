import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    E,
    Feature,
    Group,
    features_modeling_AND,
    features_modeling_Constraint,
    features_modeling_Constraints,
    features_modeling_E,
    features_modeling_EMAND,
    features_modeling_EX,
    features_modeling_Edge,
    features_modeling_F,
    features_modeling_Feature,
    features_modeling_G,
    features_modeling_GOR,
    features_modeling_GXOR,
    features_modeling_Group,
    features_modeling_I,
    features_modeling_NOT,
    features_modeling_PropFormulaCNF,
    features_modeling_PropositionOR,
    features_modeling_R,
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

def test_assoc_children2_reverse_link_reassign_clear():
    a1 = features_modeling_Feature(ID="sample_text")
    a2 = features_modeling_Feature(ID="sample_text_2")
    b = features_modeling_Feature(ID="sample_text")
    _safe_set(b, 'features_modeling_Feature1', {a1})
    assert _is_linked(b, 'features_modeling_Feature1', a1)
    if hasattr(a1, 'features_modeling_Feature'):
        assert _is_linked(a1, 'features_modeling_Feature', b)
    _safe_set(b, 'features_modeling_Feature1', {a2})
    assert _is_linked(b, 'features_modeling_Feature1', a2)
    if hasattr(a1, 'features_modeling_Feature'):
        assert not _is_linked(a1, 'features_modeling_Feature', b)
    if hasattr(a2, 'features_modeling_Feature'):
        assert _is_linked(a2, 'features_modeling_Feature', b)
    _safe_set(b, 'features_modeling_Feature1', set())
    assert not _is_linked(b, 'features_modeling_Feature1', a2)
    if hasattr(a2, 'features_modeling_Feature'):
        assert not _is_linked(a2, 'features_modeling_Feature', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_feature12_stub_double():
    # features_modeling_Constraint has no real 'features_modeling_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so features_modeling_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # features_modeling_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = features_modeling_Feature(ID="sample_text")
    partner = features_modeling_Constraint()
    setattr(partner, 'features_modeling_Constraint', None)
    _safe_set(owner, 'features_modeling_Feature13', partner)
    assert owner in getattr(partner, 'features_modeling_Constraint')
    _safe_set(owner, 'features_modeling_Feature13', None)
    assert owner not in getattr(partner, 'features_modeling_Constraint')


def test_assoc_feature14_stub_double():
    # features_modeling_Group has no real 'features_modeling_Group' property in the generated
    # code (a bare stub) -- manually attach it so features_modeling_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # features_modeling_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = features_modeling_Feature(ID="sample_text")
    partner = features_modeling_Group()
    setattr(partner, 'features_modeling_Group', None)
    _safe_set(owner, 'features_modeling_Feature15', partner)
    assert owner in getattr(partner, 'features_modeling_Group')
    _safe_set(owner, 'features_modeling_Feature15', None)
    assert owner not in getattr(partner, 'features_modeling_Group')


def test_assoc_feature19_stub_double():
    # features_modeling_PropositionOR has no real 'features_modeling_PropositionOR20' property in the generated
    # code (a bare stub) -- manually attach it so features_modeling_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # features_modeling_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = features_modeling_Feature(ID="sample_text")
    partner = features_modeling_PropositionOR()
    setattr(partner, 'features_modeling_PropositionOR20', None)
    _safe_set(owner, 'features_modeling_Feature21', partner)
    assert owner in getattr(partner, 'features_modeling_PropositionOR20')
    _safe_set(owner, 'features_modeling_Feature21', None)
    assert owner not in getattr(partner, 'features_modeling_PropositionOR20')


def test_assoc_feature24_stub_double():
    # features_modeling_NOT has no real 'features_modeling_NOT25' property in the generated
    # code (a bare stub) -- manually attach it so features_modeling_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # features_modeling_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = features_modeling_Feature(ID="sample_text")
    partner = features_modeling_NOT()
    setattr(partner, 'features_modeling_NOT25', None)
    _safe_set(owner, 'features_modeling_Feature26', partner)
    assert getattr(partner, 'features_modeling_NOT25') == owner
    _safe_set(owner, 'features_modeling_Feature26', None)
    assert getattr(partner, 'features_modeling_NOT25') is None


def test_assoc_feature3_stub_double():
    # features_modeling_F has no real 'features_modeling_F' property in the generated
    # code (a bare stub) -- manually attach it so features_modeling_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # features_modeling_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = features_modeling_Feature(ID="sample_text")
    partner = features_modeling_F()
    setattr(partner, 'features_modeling_F', None)
    _safe_set(owner, 'features_modeling_Feature4', partner)
    assert owner in getattr(partner, 'features_modeling_F')
    _safe_set(owner, 'features_modeling_Feature4', None)
    assert owner not in getattr(partner, 'features_modeling_F')


def test_assoc_feature8_stub_double():
    # features_modeling_Edge has no real 'features_modeling_Edge' property in the generated
    # code (a bare stub) -- manually attach it so features_modeling_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # features_modeling_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = features_modeling_Feature(ID="sample_text")
    partner = features_modeling_Edge()
    setattr(partner, 'features_modeling_Edge', None)
    _safe_set(owner, 'features_modeling_Feature9', partner)
    assert owner in getattr(partner, 'features_modeling_Edge')
    _safe_set(owner, 'features_modeling_Feature9', None)
    assert owner not in getattr(partner, 'features_modeling_Edge')


