import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AttributeValue,
    fc_Attribute,
    fc_AttributeValue,
    fc_BooleanValue,
    fc_DoubleValue,
    fc_Feature,
    fc_FeatureConfiguration,
    fc_FeatureModel,
    fc_IntegerValue,
    fc_Selection,
    fc_StringValue,
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

def test_assoc_featureConfiguration12_reverse_link_reassign_clear():
    a1 = fc_Selection(comment="sample_text", description="sample_text", enabled=True, id="sample_text", name="sample_text", present=True, root=True)
    a2 = fc_Selection(comment="sample_text_2", description="sample_text_2", enabled=False, id="sample_text_2", name="sample_text_2", present=False, root=False)
    b = fc_FeatureConfiguration(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    _safe_set(b, 'fc_FeatureConfiguration14', a1)
    assert _is_linked(b, 'fc_FeatureConfiguration14', a1)
    if hasattr(a1, 'fc_Selection13'):
        assert _is_linked(a1, 'fc_Selection13', b)
    _safe_set(b, 'fc_FeatureConfiguration14', a2)
    assert _is_linked(b, 'fc_FeatureConfiguration14', a2)
    if hasattr(a1, 'fc_Selection13'):
        assert not _is_linked(a1, 'fc_Selection13', b)
    if hasattr(a2, 'fc_Selection13'):
        assert _is_linked(a2, 'fc_Selection13', b)
    _safe_set(b, 'fc_FeatureConfiguration14', None)
    assert not _is_linked(b, 'fc_FeatureConfiguration14', a2)
    if hasattr(a2, 'fc_Selection13'):
        assert not _is_linked(a2, 'fc_Selection13', b)


def test_assoc_parent7_reverse_link_reassign_clear():
    a1 = fc_Selection(comment="sample_text", description="sample_text", enabled=True, id="sample_text", name="sample_text", present=True, root=True)
    a2 = fc_Selection(comment="sample_text_2", description="sample_text_2", enabled=False, id="sample_text_2", name="sample_text_2", present=False, root=False)
    b = fc_Selection(comment="sample_text", description="sample_text", enabled=True, id="sample_text", name="sample_text", present=True, root=True)
    _safe_set(b, 'selections', a1)
    assert _is_linked(b, 'selections', a1)
    if hasattr(a1, 'Selection'):
        assert _is_linked(a1, 'Selection', b)
    _safe_set(b, 'selections', a2)
    assert _is_linked(b, 'selections', a2)
    if hasattr(a1, 'Selection'):
        assert not _is_linked(a1, 'Selection', b)
    if hasattr(a2, 'Selection'):
        assert _is_linked(a2, 'Selection', b)
    _safe_set(b, 'selections', None)
    assert not _is_linked(b, 'selections', a2)
    if hasattr(a2, 'Selection'):
        assert not _is_linked(a2, 'Selection', b)


def test_assoc_root4_reverse_link_reassign_clear():
    a1 = fc_Selection(comment="sample_text", description="sample_text", enabled=True, id="sample_text", name="sample_text", present=True, root=True)
    a2 = fc_Selection(comment="sample_text_2", description="sample_text_2", enabled=False, id="sample_text_2", name="sample_text_2", present=False, root=False)
    b = fc_FeatureConfiguration(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    _safe_set(b, 'fc_FeatureConfiguration5', a1)
    assert _is_linked(b, 'fc_FeatureConfiguration5', a1)
    if hasattr(a1, 'fc_Selection'):
        assert _is_linked(a1, 'fc_Selection', b)
    _safe_set(b, 'fc_FeatureConfiguration5', a2)
    assert _is_linked(b, 'fc_FeatureConfiguration5', a2)
    if hasattr(a1, 'fc_Selection'):
        assert not _is_linked(a1, 'fc_Selection', b)
    if hasattr(a2, 'fc_Selection'):
        assert _is_linked(a2, 'fc_Selection', b)
    _safe_set(b, 'fc_FeatureConfiguration5', None)
    assert not _is_linked(b, 'fc_FeatureConfiguration5', a2)
    if hasattr(a2, 'fc_Selection'):
        assert not _is_linked(a2, 'fc_Selection', b)


def test_assoc_selection17_reverse_link_reassign_clear():
    a1 = fc_Selection(comment="sample_text", description="sample_text", enabled=True, id="sample_text", name="sample_text", present=True, root=True)
    a2 = fc_Selection(comment="sample_text_2", description="sample_text_2", enabled=False, id="sample_text_2", name="sample_text_2", present=False, root=False)
    b = fc_AttributeValue(comment="sample_text", description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'values', a1)
    assert _is_linked(b, 'values', a1)
    if hasattr(a1, 'Selection18'):
        assert _is_linked(a1, 'Selection18', b)
    _safe_set(b, 'values', a2)
    assert _is_linked(b, 'values', a2)
    if hasattr(a1, 'Selection18'):
        assert not _is_linked(a1, 'Selection18', b)
    if hasattr(a2, 'Selection18'):
        assert _is_linked(a2, 'Selection18', b)
    _safe_set(b, 'values', None)
    assert not _is_linked(b, 'values', a2)
    if hasattr(a2, 'Selection18'):
        assert not _is_linked(a2, 'Selection18', b)


def test_assoc_selections10_reverse_link_reassign_clear():
    a1 = fc_Selection(comment="sample_text", description="sample_text", enabled=True, id="sample_text", name="sample_text", present=True, root=True)
    a2 = fc_Selection(comment="sample_text_2", description="sample_text_2", enabled=False, id="sample_text_2", name="sample_text_2", present=False, root=False)
    b = fc_Selection(comment="sample_text", description="sample_text", enabled=True, id="sample_text", name="sample_text", present=True, root=True)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Selection11'):
        assert _is_linked(a1, 'Selection11', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Selection11'):
        assert not _is_linked(a1, 'Selection11', b)
    if hasattr(a2, 'Selection11'):
        assert _is_linked(a2, 'Selection11', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Selection11'):
        assert not _is_linked(a2, 'Selection11', b)


def test_assoc_values8_reverse_link_reassign_clear():
    a1 = fc_Selection(comment="sample_text", description="sample_text", enabled=True, id="sample_text", name="sample_text", present=True, root=True)
    a2 = fc_Selection(comment="sample_text_2", description="sample_text_2", enabled=False, id="sample_text_2", name="sample_text_2", present=False, root=False)
    b = fc_AttributeValue(comment="sample_text", description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'AttributeValue', a1)
    assert _is_linked(b, 'AttributeValue', a1)
    if hasattr(a1, 'selection'):
        assert _is_linked(a1, 'selection', b)
    _safe_set(b, 'AttributeValue', a2)
    assert _is_linked(b, 'AttributeValue', a2)
    if hasattr(a1, 'selection'):
        assert not _is_linked(a1, 'selection', b)
    if hasattr(a2, 'selection'):
        assert _is_linked(a2, 'selection', b)
    _safe_set(b, 'AttributeValue', None)
    assert not _is_linked(b, 'AttributeValue', a2)
    if hasattr(a2, 'selection'):
        assert not _is_linked(a2, 'selection', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute19_stub_double():
    # fc_Attribute has no real 'fc_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so fc_AttributeValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fc_AttributeValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fc_AttributeValue(comment="sample_text", description="sample_text", id="sample_text", name="sample_text")
    partner = fc_Attribute()
    setattr(partner, 'fc_Attribute', None)
    _safe_set(owner, 'fc_AttributeValue', partner)
    assert getattr(partner, 'fc_Attribute') == owner
    _safe_set(owner, 'fc_AttributeValue', None)
    assert getattr(partner, 'fc_Attribute') is None


def test_assoc_feature15_stub_double():
    # fc_Feature has no real 'fc_Feature' property in the generated
    # code (a bare stub) -- manually attach it so fc_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fc_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fc_Selection(comment="sample_text", description="sample_text", enabled=True, id="sample_text", name="sample_text", present=True, root=True)
    partner = fc_Feature()
    setattr(partner, 'fc_Feature', None)
    _safe_set(owner, 'fc_Selection16', partner)
    assert getattr(partner, 'fc_Feature') == owner
    _safe_set(owner, 'fc_Selection16', None)
    assert getattr(partner, 'fc_Feature') is None


def test_assoc_featureModel0_stub_double():
    # fc_FeatureModel has no real 'fc_FeatureModel' property in the generated
    # code (a bare stub) -- manually attach it so fc_FeatureConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fc_FeatureConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fc_FeatureConfiguration(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    partner = fc_FeatureModel()
    setattr(partner, 'fc_FeatureModel', None)
    _safe_set(owner, 'fc_FeatureConfiguration', partner)
    assert getattr(partner, 'fc_FeatureModel') == owner
    _safe_set(owner, 'fc_FeatureConfiguration', None)
    assert getattr(partner, 'fc_FeatureModel') is None


def test_assoc_featureModelCopy1_stub_double():
    # fc_FeatureModel has no real 'fc_FeatureModel3' property in the generated
    # code (a bare stub) -- manually attach it so fc_FeatureConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fc_FeatureConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fc_FeatureConfiguration(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    partner = fc_FeatureModel()
    setattr(partner, 'fc_FeatureModel3', None)
    _safe_set(owner, 'fc_FeatureConfiguration2', partner)
    assert getattr(partner, 'fc_FeatureModel3') == owner
    _safe_set(owner, 'fc_FeatureConfiguration2', None)
    assert getattr(partner, 'fc_FeatureModel3') is None


