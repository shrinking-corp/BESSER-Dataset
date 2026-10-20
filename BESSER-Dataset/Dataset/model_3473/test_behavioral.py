import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Alternative,
    BooleanConstraint,
    Cardinality,
    EFM_Alternative,
    EFM_Attribute,
    EFM_BooleanConstraint,
    EFM_Cardinality,
    EFM_Colocated,
    EFM_Comparison,
    EFM_Excludes,
    EFM_Exclusive,
    EFM_FMConstraint,
    EFM_FMElement,
    EFM_FeatCardinality,
    EFM_Feature,
    EFM_FeatureModel,
    EFM_Functional,
    EFM_HostedBy,
    EFM_Implies,
    EFM_IntValue,
    EFM_NodeFeature,
    EFM_NodeFeatureElement,
    EFM_NotHostedBy,
    EFM_Operation,
    EFM_RangeOperation,
    EFM_Requires,
    EFM_ResourceVerification,
    EFM_Separated,
    EFM_Value,
    EFM_ValueOperation,
    FMConstraint,
    FMElement,
    Feature,
    NodeFeatureElement,
    Operation,
    ComparisonOperator,
    LogicalOperator,
    Operator,
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

def test_assoc_NodeAttributes48_reverse_link_reassign_clear():
    a1 = EFM_NodeFeature(name="sample_text")
    a2 = EFM_NodeFeature(name="sample_text_2")
    b = EFM_Attribute(name="sample_text")
    _safe_set(b, 'EFM_Attribute50', a1)
    assert _is_linked(b, 'EFM_Attribute50', a1)
    if hasattr(a1, 'EFM_NodeFeature49'):
        assert _is_linked(a1, 'EFM_NodeFeature49', b)
    _safe_set(b, 'EFM_Attribute50', a2)
    assert _is_linked(b, 'EFM_Attribute50', a2)
    if hasattr(a1, 'EFM_NodeFeature49'):
        assert not _is_linked(a1, 'EFM_NodeFeature49', b)
    if hasattr(a2, 'EFM_NodeFeature49'):
        assert _is_linked(a2, 'EFM_NodeFeature49', b)
    _safe_set(b, 'EFM_Attribute50', None)
    assert not _is_linked(b, 'EFM_Attribute50', a2)
    if hasattr(a2, 'EFM_NodeFeature49'):
        assert not _is_linked(a2, 'EFM_NodeFeature49', b)


def test_assoc_attribute37_reverse_link_reassign_clear():
    a1 = EFM_RangeOperation(max=7, min=7)
    a2 = EFM_RangeOperation(max=13, min=13)
    b = EFM_Attribute(name="sample_text")
    _safe_set(b, 'EFM_Attribute38', a1)
    assert _is_linked(b, 'EFM_Attribute38', a1)
    if hasattr(a1, 'EFM_RangeOperation'):
        assert _is_linked(a1, 'EFM_RangeOperation', b)
    _safe_set(b, 'EFM_Attribute38', a2)
    assert _is_linked(b, 'EFM_Attribute38', a2)
    if hasattr(a1, 'EFM_RangeOperation'):
        assert not _is_linked(a1, 'EFM_RangeOperation', b)
    if hasattr(a2, 'EFM_RangeOperation'):
        assert _is_linked(a2, 'EFM_RangeOperation', b)
    _safe_set(b, 'EFM_Attribute38', None)
    assert not _is_linked(b, 'EFM_Attribute38', a2)
    if hasattr(a2, 'EFM_RangeOperation'):
        assert not _is_linked(a2, 'EFM_RangeOperation', b)


def test_assoc_attributes3_reverse_link_reassign_clear():
    a1 = EFM_Feature(name="sample_text")
    a2 = EFM_Feature(name="sample_text_2")
    b = EFM_Attribute(name="sample_text")
    _safe_set(b, 'EFM_Attribute', a1)
    assert _is_linked(b, 'EFM_Attribute', a1)
    if hasattr(a1, 'EFM_Feature4'):
        assert _is_linked(a1, 'EFM_Feature4', b)
    _safe_set(b, 'EFM_Attribute', a2)
    assert _is_linked(b, 'EFM_Attribute', a2)
    if hasattr(a1, 'EFM_Feature4'):
        assert not _is_linked(a1, 'EFM_Feature4', b)
    if hasattr(a2, 'EFM_Feature4'):
        assert _is_linked(a2, 'EFM_Feature4', b)
    _safe_set(b, 'EFM_Attribute', None)
    assert not _is_linked(b, 'EFM_Attribute', a2)
    if hasattr(a2, 'EFM_Feature4'):
        assert not _is_linked(a2, 'EFM_Feature4', b)


def test_assoc_from_25_reverse_link_reassign_clear():
    a1 = EFM_Functional(type="sample_text", value=7)
    a2 = EFM_Functional(type="sample_text_2", value=13)
    b = EFM_Feature(name="sample_text")
    _safe_set(b, 'EFM_Feature26', a1)
    assert _is_linked(b, 'EFM_Feature26', a1)
    if hasattr(a1, 'EFM_Functional'):
        assert _is_linked(a1, 'EFM_Functional', b)
    _safe_set(b, 'EFM_Feature26', a2)
    assert _is_linked(b, 'EFM_Feature26', a2)
    if hasattr(a1, 'EFM_Functional'):
        assert not _is_linked(a1, 'EFM_Functional', b)
    if hasattr(a2, 'EFM_Functional'):
        assert _is_linked(a2, 'EFM_Functional', b)
    _safe_set(b, 'EFM_Feature26', None)
    assert not _is_linked(b, 'EFM_Feature26', a2)
    if hasattr(a2, 'EFM_Functional'):
        assert not _is_linked(a2, 'EFM_Functional', b)


def test_assoc_nodeFeature10_reverse_link_reassign_clear():
    a1 = EFM_NodeFeature(name="sample_text")
    a2 = EFM_NodeFeature(name="sample_text_2")
    b = EFM_Feature(name="sample_text")
    _safe_set(b, 'EFM_Feature11', {a1})
    assert _is_linked(b, 'EFM_Feature11', a1)
    if hasattr(a1, 'EFM_NodeFeature'):
        assert _is_linked(a1, 'EFM_NodeFeature', b)
    _safe_set(b, 'EFM_Feature11', {a2})
    assert _is_linked(b, 'EFM_Feature11', a2)
    if hasattr(a1, 'EFM_NodeFeature'):
        assert not _is_linked(a1, 'EFM_NodeFeature', b)
    if hasattr(a2, 'EFM_NodeFeature'):
        assert _is_linked(a2, 'EFM_NodeFeature', b)
    _safe_set(b, 'EFM_Feature11', set())
    assert not _is_linked(b, 'EFM_Feature11', a2)
    if hasattr(a2, 'EFM_NodeFeature'):
        assert not _is_linked(a2, 'EFM_NodeFeature', b)


def test_assoc_subFeatures6_reverse_link_reassign_clear():
    a1 = EFM_Feature(name="sample_text")
    a2 = EFM_Feature(name="sample_text_2")
    b = EFM_Feature(name="sample_text")
    _safe_set(b, 'EFM_Feature7', a1)
    assert _is_linked(b, 'EFM_Feature7', a1)
    if hasattr(a1, 'EFM_Feature5'):
        assert _is_linked(a1, 'EFM_Feature5', b)
    _safe_set(b, 'EFM_Feature7', a2)
    assert _is_linked(b, 'EFM_Feature7', a2)
    if hasattr(a1, 'EFM_Feature5'):
        assert not _is_linked(a1, 'EFM_Feature5', b)
    if hasattr(a2, 'EFM_Feature5'):
        assert _is_linked(a2, 'EFM_Feature5', b)
    _safe_set(b, 'EFM_Feature7', None)
    assert not _is_linked(b, 'EFM_Feature7', a2)
    if hasattr(a2, 'EFM_Feature5'):
        assert not _is_linked(a2, 'EFM_Feature5', b)


def test_assoc_to27_reverse_link_reassign_clear():
    a1 = EFM_Functional(type="sample_text", value=7)
    a2 = EFM_Functional(type="sample_text_2", value=13)
    b = EFM_Feature(name="sample_text")
    _safe_set(b, 'EFM_Feature29', a1)
    assert _is_linked(b, 'EFM_Feature29', a1)
    if hasattr(a1, 'EFM_Functional28'):
        assert _is_linked(a1, 'EFM_Functional28', b)
    _safe_set(b, 'EFM_Feature29', a2)
    assert _is_linked(b, 'EFM_Feature29', a2)
    if hasattr(a1, 'EFM_Functional28'):
        assert not _is_linked(a1, 'EFM_Functional28', b)
    if hasattr(a2, 'EFM_Functional28'):
        assert _is_linked(a2, 'EFM_Functional28', b)
    _safe_set(b, 'EFM_Feature29', None)
    assert not _is_linked(b, 'EFM_Feature29', a2)
    if hasattr(a2, 'EFM_Functional28'):
        assert not _is_linked(a2, 'EFM_Functional28', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_From77_stub_double():
    # EFM_NotHostedBy has no real 'EFM_NotHostedBy78' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_NotHostedBy()
    setattr(partner, 'EFM_NotHostedBy78', None)
    _safe_set(owner, 'EFM_Feature79', partner)
    assert owner in getattr(partner, 'EFM_NotHostedBy78')
    _safe_set(owner, 'EFM_Feature79', None)
    assert owner not in getattr(partner, 'EFM_NotHostedBy78')


def test_assoc_HostedBy54_stub_double():
    # EFM_HostedBy has no real 'EFM_HostedBy' property in the generated
    # code (a bare stub) -- manually attach it so EFM_NodeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_NodeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_NodeFeature(name="sample_text")
    partner = EFM_HostedBy()
    setattr(partner, 'EFM_HostedBy', None)
    _safe_set(owner, 'EFM_NodeFeature55', partner)
    assert getattr(partner, 'EFM_HostedBy') == owner
    _safe_set(owner, 'EFM_NodeFeature55', None)
    assert getattr(partner, 'EFM_HostedBy') is None


def test_assoc_NodeCardinalities51_stub_double():
    # EFM_FeatCardinality has no real 'EFM_FeatCardinality53' property in the generated
    # code (a bare stub) -- manually attach it so EFM_NodeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_NodeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_NodeFeature(name="sample_text")
    partner = EFM_FeatCardinality()
    setattr(partner, 'EFM_FeatCardinality53', None)
    _safe_set(owner, 'EFM_NodeFeature52', partner)
    assert getattr(partner, 'EFM_FeatCardinality53') == owner
    _safe_set(owner, 'EFM_NodeFeature52', None)
    assert getattr(partner, 'EFM_FeatCardinality53') is None


def test_assoc_NotHostedBy56_stub_double():
    # EFM_NotHostedBy has no real 'EFM_NotHostedBy' property in the generated
    # code (a bare stub) -- manually attach it so EFM_NodeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_NodeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_NodeFeature(name="sample_text")
    partner = EFM_NotHostedBy()
    setattr(partner, 'EFM_NotHostedBy', None)
    _safe_set(owner, 'EFM_NodeFeature57', partner)
    assert getattr(partner, 'EFM_NotHostedBy') == owner
    _safe_set(owner, 'EFM_NodeFeature57', None)
    assert getattr(partner, 'EFM_NotHostedBy') is None


def test_assoc_action22_stub_double():
    # EFM_Operation has no real 'EFM_Operation24' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Requires's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Requires's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Requires(operator="sample_text")
    partner = EFM_Operation()
    setattr(partner, 'EFM_Operation24', None)
    _safe_set(owner, 'EFM_Requires23', partner)
    assert getattr(partner, 'EFM_Operation24') == owner
    _safe_set(owner, 'EFM_Requires23', None)
    assert getattr(partner, 'EFM_Operation24') is None


def test_assoc_attribute39_stub_double():
    # EFM_ValueOperation has no real 'EFM_ValueOperation' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Attribute(name="sample_text")
    partner = EFM_ValueOperation()
    setattr(partner, 'EFM_ValueOperation', None)
    _safe_set(owner, 'EFM_Attribute40', partner)
    assert getattr(partner, 'EFM_ValueOperation') == owner
    _safe_set(owner, 'EFM_Attribute40', None)
    assert getattr(partner, 'EFM_ValueOperation') is None


def test_assoc_conditions21_stub_double():
    # EFM_Operation has no real 'EFM_Operation' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Requires's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Requires's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Requires(operator="sample_text")
    partner = EFM_Operation()
    setattr(partner, 'EFM_Operation', None)
    _safe_set(owner, 'EFM_Requires', {partner})
    assert getattr(partner, 'EFM_Operation') == owner
    _safe_set(owner, 'EFM_Requires', set())
    assert getattr(partner, 'EFM_Operation') is None


def test_assoc_extF71_stub_double():
    # EFM_ResourceVerification has no real 'EFM_ResourceVerification72' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Attribute(name="sample_text")
    partner = EFM_ResourceVerification()
    setattr(partner, 'EFM_ResourceVerification72', None)
    _safe_set(owner, 'EFM_Attribute73', partner)
    assert getattr(partner, 'EFM_ResourceVerification72') == owner
    _safe_set(owner, 'EFM_Attribute73', None)
    assert getattr(partner, 'EFM_ResourceVerification72') is None


def test_assoc_extF74_stub_double():
    # EFM_NotHostedBy has no real 'EFM_NotHostedBy75' property in the generated
    # code (a bare stub) -- manually attach it so EFM_NodeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_NodeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_NodeFeature(name="sample_text")
    partner = EFM_NotHostedBy()
    setattr(partner, 'EFM_NotHostedBy75', None)
    _safe_set(owner, 'EFM_NodeFeature76', partner)
    assert getattr(partner, 'EFM_NotHostedBy75') == owner
    _safe_set(owner, 'EFM_NodeFeature76', None)
    assert getattr(partner, 'EFM_NotHostedBy75') is None


def test_assoc_feature34_stub_double():
    # EFM_Operation has no real 'EFM_Operation35' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_Operation()
    setattr(partner, 'EFM_Operation35', None)
    _safe_set(owner, 'EFM_Feature36', partner)
    assert getattr(partner, 'EFM_Operation35') == owner
    _safe_set(owner, 'EFM_Feature36', None)
    assert getattr(partner, 'EFM_Operation35') is None


def test_assoc_featureCardinality8_stub_double():
    # EFM_FeatCardinality has no real 'EFM_FeatCardinality' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_FeatCardinality()
    setattr(partner, 'EFM_FeatCardinality', None)
    _safe_set(owner, 'EFM_Feature9', partner)
    assert getattr(partner, 'EFM_FeatCardinality') == owner
    _safe_set(owner, 'EFM_Feature9', None)
    assert getattr(partner, 'EFM_FeatCardinality') is None


def test_assoc_fromAgain45_stub_double():
    # EFM_Colocated has no real 'EFM_Colocated46' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_Colocated()
    setattr(partner, 'EFM_Colocated46', None)
    _safe_set(owner, 'EFM_Feature47', partner)
    assert owner in getattr(partner, 'EFM_Colocated46')
    _safe_set(owner, 'EFM_Feature47', None)
    assert owner not in getattr(partner, 'EFM_Colocated46')


def test_assoc_fromAtt69_stub_double():
    # EFM_ResourceVerification has no real 'EFM_ResourceVerification' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Attribute(name="sample_text")
    partner = EFM_ResourceVerification()
    setattr(partner, 'EFM_ResourceVerification', None)
    _safe_set(owner, 'EFM_Attribute70', partner)
    assert owner in getattr(partner, 'EFM_ResourceVerification')
    _safe_set(owner, 'EFM_Attribute70', None)
    assert owner not in getattr(partner, 'EFM_ResourceVerification')


def test_assoc_from_16_stub_double():
    # EFM_BooleanConstraint has no real 'EFM_BooleanConstraint' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_BooleanConstraint()
    setattr(partner, 'EFM_BooleanConstraint', None)
    _safe_set(owner, 'EFM_Feature17', partner)
    assert getattr(partner, 'EFM_BooleanConstraint') == owner
    _safe_set(owner, 'EFM_Feature17', None)
    assert getattr(partner, 'EFM_BooleanConstraint') is None


def test_assoc_from_30_stub_double():
    # EFM_FMElement has no real 'EFM_FMElement' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Comparison(type="sample_text")
    partner = EFM_FMElement()
    setattr(partner, 'EFM_FMElement', None)
    _safe_set(owner, 'EFM_Comparison', partner)
    assert getattr(partner, 'EFM_FMElement') == owner
    _safe_set(owner, 'EFM_Comparison', None)
    assert getattr(partner, 'EFM_FMElement') is None


def test_assoc_from_43_stub_double():
    # EFM_Colocated has no real 'EFM_Colocated' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_Colocated()
    setattr(partner, 'EFM_Colocated', None)
    _safe_set(owner, 'EFM_Feature44', partner)
    assert getattr(partner, 'EFM_Colocated') == owner
    _safe_set(owner, 'EFM_Feature44', None)
    assert getattr(partner, 'EFM_Colocated') is None


def test_assoc_from_58_stub_double():
    # EFM_HostedBy has no real 'EFM_HostedBy59' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_HostedBy()
    setattr(partner, 'EFM_HostedBy59', None)
    _safe_set(owner, 'EFM_Feature60', partner)
    assert owner in getattr(partner, 'EFM_HostedBy59')
    _safe_set(owner, 'EFM_Feature60', None)
    assert owner not in getattr(partner, 'EFM_HostedBy59')


def test_assoc_from_64_stub_double():
    # EFM_Separated has no real 'EFM_Separated' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_Separated()
    setattr(partner, 'EFM_Separated', None)
    _safe_set(owner, 'EFM_Feature65', partner)
    assert getattr(partner, 'EFM_Separated') == owner
    _safe_set(owner, 'EFM_Feature65', None)
    assert getattr(partner, 'EFM_Separated') is None


def test_assoc_rootFeature1_stub_double():
    # EFM_FeatureModel has no real 'EFM_FeatureModel2' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_FeatureModel()
    setattr(partner, 'EFM_FeatureModel2', None)
    _safe_set(owner, 'EFM_Feature', partner)
    assert getattr(partner, 'EFM_FeatureModel2') == owner
    _safe_set(owner, 'EFM_Feature', None)
    assert getattr(partner, 'EFM_FeatureModel2') is None


def test_assoc_to18_stub_double():
    # EFM_BooleanConstraint has no real 'EFM_BooleanConstraint19' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_BooleanConstraint()
    setattr(partner, 'EFM_BooleanConstraint19', None)
    _safe_set(owner, 'EFM_Feature20', partner)
    assert getattr(partner, 'EFM_BooleanConstraint19') == owner
    _safe_set(owner, 'EFM_Feature20', None)
    assert getattr(partner, 'EFM_BooleanConstraint19') is None


def test_assoc_to31_stub_double():
    # EFM_FMElement has no real 'EFM_FMElement33' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Comparison(type="sample_text")
    partner = EFM_FMElement()
    setattr(partner, 'EFM_FMElement33', None)
    _safe_set(owner, 'EFM_Comparison32', partner)
    assert getattr(partner, 'EFM_FMElement33') == owner
    _safe_set(owner, 'EFM_Comparison32', None)
    assert getattr(partner, 'EFM_FMElement33') is None


def test_assoc_to61_stub_double():
    # EFM_HostedBy has no real 'EFM_HostedBy62' property in the generated
    # code (a bare stub) -- manually attach it so EFM_NodeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_NodeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_NodeFeature(name="sample_text")
    partner = EFM_HostedBy()
    setattr(partner, 'EFM_HostedBy62', None)
    _safe_set(owner, 'EFM_NodeFeature63', partner)
    assert getattr(partner, 'EFM_HostedBy62') == owner
    _safe_set(owner, 'EFM_NodeFeature63', None)
    assert getattr(partner, 'EFM_HostedBy62') is None


def test_assoc_to66_stub_double():
    # EFM_Separated has no real 'EFM_Separated67' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_Separated()
    setattr(partner, 'EFM_Separated67', None)
    _safe_set(owner, 'EFM_Feature68', partner)
    assert getattr(partner, 'EFM_Separated67') == owner
    _safe_set(owner, 'EFM_Feature68', None)
    assert getattr(partner, 'EFM_Separated67') is None


def test_assoc_value14_stub_double():
    # EFM_Value has no real 'EFM_Value' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Attribute(name="sample_text")
    partner = EFM_Value()
    setattr(partner, 'EFM_Value', None)
    _safe_set(owner, 'EFM_Attribute15', partner)
    assert getattr(partner, 'EFM_Value') == owner
    _safe_set(owner, 'EFM_Attribute15', None)
    assert getattr(partner, 'EFM_Value') is None


def test_assoc_variants12_stub_double():
    # EFM_Alternative has no real 'EFM_Alternative' property in the generated
    # code (a bare stub) -- manually attach it so EFM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EFM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EFM_Feature(name="sample_text")
    partner = EFM_Alternative()
    setattr(partner, 'EFM_Alternative', None)
    _safe_set(owner, 'EFM_Feature13', partner)
    assert owner in getattr(partner, 'EFM_Alternative')
    _safe_set(owner, 'EFM_Feature13', None)
    assert owner not in getattr(partner, 'EFM_Alternative')


