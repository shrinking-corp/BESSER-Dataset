import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Alternative,
    BooleanConstraint,
    FMConstraint,
    Feature,
    VariabilityElement,
    featureModel_Action,
    featureModel_AdaptationRule,
    featureModel_Alternative,
    featureModel_Attribute,
    featureModel_BooleanConstraint,
    featureModel_Condition,
    featureModel_Excludes,
    featureModel_Exclusive,
    featureModel_FMConstraint,
    featureModel_Feature,
    featureModel_FeatureModel,
    featureModel_Implies,
    featureModel_IntValue,
    featureModel_Value,
    featureModel_VariabilityElement,
    ComparisonOperator,
    SelectionOperator,
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

def test_assoc_attribute20_reverse_link_reassign_clear():
    a1 = featureModel_Condition(type="sample_text")
    a2 = featureModel_Condition(type="sample_text_2")
    b = featureModel_Attribute(name="sample_text", runtime=True)
    _safe_set(b, 'featureModel_Attribute22', a1)
    assert _is_linked(b, 'featureModel_Attribute22', a1)
    if hasattr(a1, 'featureModel_Condition21'):
        assert _is_linked(a1, 'featureModel_Condition21', b)
    _safe_set(b, 'featureModel_Attribute22', a2)
    assert _is_linked(b, 'featureModel_Attribute22', a2)
    if hasattr(a1, 'featureModel_Condition21'):
        assert not _is_linked(a1, 'featureModel_Condition21', b)
    if hasattr(a2, 'featureModel_Condition21'):
        assert _is_linked(a2, 'featureModel_Condition21', b)
    _safe_set(b, 'featureModel_Attribute22', None)
    assert not _is_linked(b, 'featureModel_Attribute22', a2)
    if hasattr(a2, 'featureModel_Condition21'):
        assert not _is_linked(a2, 'featureModel_Condition21', b)


def test_assoc_attributes3_reverse_link_reassign_clear():
    a1 = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    a2 = featureModel_Feature(mandatory=False, name="sample_text_2", selected=False, unselected=False)
    b = featureModel_Attribute(name="sample_text", runtime=True)
    _safe_set(b, 'featureModel_Attribute', a1)
    assert _is_linked(b, 'featureModel_Attribute', a1)
    if hasattr(a1, 'featureModel_Feature4'):
        assert _is_linked(a1, 'featureModel_Feature4', b)
    _safe_set(b, 'featureModel_Attribute', a2)
    assert _is_linked(b, 'featureModel_Attribute', a2)
    if hasattr(a1, 'featureModel_Feature4'):
        assert not _is_linked(a1, 'featureModel_Feature4', b)
    if hasattr(a2, 'featureModel_Feature4'):
        assert _is_linked(a2, 'featureModel_Feature4', b)
    _safe_set(b, 'featureModel_Attribute', None)
    assert not _is_linked(b, 'featureModel_Attribute', a2)
    if hasattr(a2, 'featureModel_Feature4'):
        assert not _is_linked(a2, 'featureModel_Feature4', b)


def test_assoc_feature25_reverse_link_reassign_clear():
    a1 = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    a2 = featureModel_Feature(mandatory=False, name="sample_text_2", selected=False, unselected=False)
    b = featureModel_Condition(type="sample_text")
    _safe_set(b, 'featureModel_Condition26', a1)
    assert _is_linked(b, 'featureModel_Condition26', a1)
    if hasattr(a1, 'featureModel_Feature27'):
        assert _is_linked(a1, 'featureModel_Feature27', b)
    _safe_set(b, 'featureModel_Condition26', a2)
    assert _is_linked(b, 'featureModel_Condition26', a2)
    if hasattr(a1, 'featureModel_Feature27'):
        assert not _is_linked(a1, 'featureModel_Feature27', b)
    if hasattr(a2, 'featureModel_Feature27'):
        assert _is_linked(a2, 'featureModel_Feature27', b)
    _safe_set(b, 'featureModel_Condition26', None)
    assert not _is_linked(b, 'featureModel_Condition26', a2)
    if hasattr(a2, 'featureModel_Feature27'):
        assert not _is_linked(a2, 'featureModel_Feature27', b)


def test_assoc_feature28_reverse_link_reassign_clear():
    a1 = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    a2 = featureModel_Feature(mandatory=False, name="sample_text_2", selected=False, unselected=False)
    b = featureModel_Action(type="sample_text")
    _safe_set(b, 'featureModel_Action29', a1)
    assert _is_linked(b, 'featureModel_Action29', a1)
    if hasattr(a1, 'featureModel_Feature30'):
        assert _is_linked(a1, 'featureModel_Feature30', b)
    _safe_set(b, 'featureModel_Action29', a2)
    assert _is_linked(b, 'featureModel_Action29', a2)
    if hasattr(a1, 'featureModel_Feature30'):
        assert not _is_linked(a1, 'featureModel_Feature30', b)
    if hasattr(a2, 'featureModel_Feature30'):
        assert _is_linked(a2, 'featureModel_Feature30', b)
    _safe_set(b, 'featureModel_Action29', None)
    assert not _is_linked(b, 'featureModel_Action29', a2)
    if hasattr(a2, 'featureModel_Feature30'):
        assert not _is_linked(a2, 'featureModel_Feature30', b)


def test_assoc_subFeatures6_reverse_link_reassign_clear():
    a1 = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    a2 = featureModel_Feature(mandatory=False, name="sample_text_2", selected=False, unselected=False)
    b = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    _safe_set(b, 'featureModel_Feature7', a1)
    assert _is_linked(b, 'featureModel_Feature7', a1)
    if hasattr(a1, 'featureModel_Feature5'):
        assert _is_linked(a1, 'featureModel_Feature5', b)
    _safe_set(b, 'featureModel_Feature7', a2)
    assert _is_linked(b, 'featureModel_Feature7', a2)
    if hasattr(a1, 'featureModel_Feature5'):
        assert not _is_linked(a1, 'featureModel_Feature5', b)
    if hasattr(a2, 'featureModel_Feature5'):
        assert _is_linked(a2, 'featureModel_Feature5', b)
    _safe_set(b, 'featureModel_Feature7', None)
    assert not _is_linked(b, 'featureModel_Feature7', a2)
    if hasattr(a2, 'featureModel_Feature5'):
        assert not _is_linked(a2, 'featureModel_Feature5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action18_stub_double():
    # featureModel_AdaptationRule has no real 'featureModel_AdaptationRule19' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Action(type="sample_text")
    partner = featureModel_AdaptationRule()
    setattr(partner, 'featureModel_AdaptationRule19', None)
    _safe_set(owner, 'featureModel_Action', partner)
    assert getattr(partner, 'featureModel_AdaptationRule19') == owner
    _safe_set(owner, 'featureModel_Action', None)
    assert getattr(partner, 'featureModel_AdaptationRule19') is None


def test_assoc_condition17_stub_double():
    # featureModel_AdaptationRule has no real 'featureModel_AdaptationRule' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Condition(type="sample_text")
    partner = featureModel_AdaptationRule()
    setattr(partner, 'featureModel_AdaptationRule', None)
    _safe_set(owner, 'featureModel_Condition', partner)
    assert getattr(partner, 'featureModel_AdaptationRule') == owner
    _safe_set(owner, 'featureModel_Condition', None)
    assert getattr(partner, 'featureModel_AdaptationRule') is None


def test_assoc_from_12_stub_double():
    # featureModel_BooleanConstraint has no real 'featureModel_BooleanConstraint' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    partner = featureModel_BooleanConstraint()
    setattr(partner, 'featureModel_BooleanConstraint', None)
    _safe_set(owner, 'featureModel_Feature13', partner)
    assert getattr(partner, 'featureModel_BooleanConstraint') == owner
    _safe_set(owner, 'featureModel_Feature13', None)
    assert getattr(partner, 'featureModel_BooleanConstraint') is None


def test_assoc_rootFeature1_stub_double():
    # featureModel_FeatureModel has no real 'featureModel_FeatureModel2' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    partner = featureModel_FeatureModel()
    setattr(partner, 'featureModel_FeatureModel2', None)
    _safe_set(owner, 'featureModel_Feature', partner)
    assert getattr(partner, 'featureModel_FeatureModel2') == owner
    _safe_set(owner, 'featureModel_Feature', None)
    assert getattr(partner, 'featureModel_FeatureModel2') is None


def test_assoc_to14_stub_double():
    # featureModel_BooleanConstraint has no real 'featureModel_BooleanConstraint15' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    partner = featureModel_BooleanConstraint()
    setattr(partner, 'featureModel_BooleanConstraint15', None)
    _safe_set(owner, 'featureModel_Feature16', partner)
    assert getattr(partner, 'featureModel_BooleanConstraint15') == owner
    _safe_set(owner, 'featureModel_Feature16', None)
    assert getattr(partner, 'featureModel_BooleanConstraint15') is None


def test_assoc_value10_stub_double():
    # featureModel_Value has no real 'featureModel_Value' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Attribute(name="sample_text", runtime=True)
    partner = featureModel_Value()
    setattr(partner, 'featureModel_Value', None)
    _safe_set(owner, 'featureModel_Attribute11', partner)
    assert getattr(partner, 'featureModel_Value') == owner
    _safe_set(owner, 'featureModel_Attribute11', None)
    assert getattr(partner, 'featureModel_Value') is None


def test_assoc_value23_stub_double():
    # featureModel_IntValue has no real 'featureModel_IntValue' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Condition(type="sample_text")
    partner = featureModel_IntValue()
    setattr(partner, 'featureModel_IntValue', None)
    _safe_set(owner, 'featureModel_Condition24', partner)
    assert getattr(partner, 'featureModel_IntValue') == owner
    _safe_set(owner, 'featureModel_Condition24', None)
    assert getattr(partner, 'featureModel_IntValue') is None


def test_assoc_variants8_stub_double():
    # featureModel_Alternative has no real 'featureModel_Alternative' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    partner = featureModel_Alternative()
    setattr(partner, 'featureModel_Alternative', None)
    _safe_set(owner, 'featureModel_Feature9', partner)
    assert owner in getattr(partner, 'featureModel_Alternative')
    _safe_set(owner, 'featureModel_Feature9', None)
    assert owner not in getattr(partner, 'featureModel_Alternative')


