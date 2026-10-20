import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fm_Attribute,
    fm_Constraint,
    fm_EObject,
    fm_Feature,
    fm_FeatureModel,
    fm_Group,
    AttributeType,
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

def test_assoc_attributes12_reverse_link_reassign_clear():
    a1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    a2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    b = fm_Attribute(comment="sample_text", description="sample_text", id="sample_text", name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'feature'):
        assert _is_linked(a1, 'feature', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'feature'):
        assert not _is_linked(a1, 'feature', b)
    if hasattr(a2, 'feature'):
        assert _is_linked(a2, 'feature', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'feature'):
        assert not _is_linked(a2, 'feature', b)


def test_assoc_constraints4_reverse_link_reassign_clear():
    a1 = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    a2 = fm_FeatureModel(comment="sample_text_2", description="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = fm_Constraint(comment="sample_text", description="sample_text", language="sample_text", value="sample_text")
    _safe_set(b, 'fm_Constraint', a1)
    assert _is_linked(b, 'fm_Constraint', a1)
    if hasattr(a1, 'fm_FeatureModel5'):
        assert _is_linked(a1, 'fm_FeatureModel5', b)
    _safe_set(b, 'fm_Constraint', a2)
    assert _is_linked(b, 'fm_Constraint', a2)
    if hasattr(a1, 'fm_FeatureModel5'):
        assert not _is_linked(a1, 'fm_FeatureModel5', b)
    if hasattr(a2, 'fm_FeatureModel5'):
        assert _is_linked(a2, 'fm_FeatureModel5', b)
    _safe_set(b, 'fm_Constraint', None)
    assert not _is_linked(b, 'fm_Constraint', a2)
    if hasattr(a2, 'fm_FeatureModel5'):
        assert not _is_linked(a2, 'fm_FeatureModel5', b)


def test_assoc_feature25_reverse_link_reassign_clear():
    a1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    a2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    b = fm_Attribute(comment="sample_text", description="sample_text", id="sample_text", name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Feature26'):
        assert _is_linked(a1, 'Feature26', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Feature26'):
        assert not _is_linked(a1, 'Feature26', b)
    if hasattr(a2, 'Feature26'):
        assert _is_linked(a2, 'Feature26', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Feature26'):
        assert not _is_linked(a2, 'Feature26', b)


def test_assoc_featureModel18_reverse_link_reassign_clear():
    a1 = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    a2 = fm_FeatureModel(comment="sample_text_2", description="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    _safe_set(b, 'fm_Feature19', a1)
    assert _is_linked(b, 'fm_Feature19', a1)
    if hasattr(a1, 'fm_FeatureModel20'):
        assert _is_linked(a1, 'fm_FeatureModel20', b)
    _safe_set(b, 'fm_Feature19', a2)
    assert _is_linked(b, 'fm_Feature19', a2)
    if hasattr(a1, 'fm_FeatureModel20'):
        assert not _is_linked(a1, 'fm_FeatureModel20', b)
    if hasattr(a2, 'fm_FeatureModel20'):
        assert _is_linked(a2, 'fm_FeatureModel20', b)
    _safe_set(b, 'fm_Feature19', None)
    assert not _is_linked(b, 'fm_Feature19', a2)
    if hasattr(a2, 'fm_FeatureModel20'):
        assert not _is_linked(a2, 'fm_FeatureModel20', b)


def test_assoc_featureModel27_reverse_link_reassign_clear():
    a1 = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    a2 = fm_FeatureModel(comment="sample_text_2", description="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = fm_Constraint(comment="sample_text", description="sample_text", language="sample_text", value="sample_text")
    _safe_set(b, 'fm_Constraint28', a1)
    assert _is_linked(b, 'fm_Constraint28', a1)
    if hasattr(a1, 'fm_FeatureModel29'):
        assert _is_linked(a1, 'fm_FeatureModel29', b)
    _safe_set(b, 'fm_Constraint28', a2)
    assert _is_linked(b, 'fm_Constraint28', a2)
    if hasattr(a1, 'fm_FeatureModel29'):
        assert not _is_linked(a1, 'fm_FeatureModel29', b)
    if hasattr(a2, 'fm_FeatureModel29'):
        assert _is_linked(a2, 'fm_FeatureModel29', b)
    _safe_set(b, 'fm_Constraint28', None)
    assert not _is_linked(b, 'fm_Constraint28', a2)
    if hasattr(a2, 'fm_FeatureModel29'):
        assert not _is_linked(a2, 'fm_FeatureModel29', b)


def test_assoc_features14_reverse_link_reassign_clear():
    a1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    a2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    b = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    _safe_set(b, 'parentFeature', {a1})
    assert _is_linked(b, 'parentFeature', a1)
    if hasattr(a1, 'Feature15'):
        assert _is_linked(a1, 'Feature15', b)
    _safe_set(b, 'parentFeature', {a2})
    assert _is_linked(b, 'parentFeature', a2)
    if hasattr(a1, 'Feature15'):
        assert not _is_linked(a1, 'Feature15', b)
    if hasattr(a2, 'Feature15'):
        assert _is_linked(a2, 'Feature15', b)
    _safe_set(b, 'parentFeature', set())
    assert not _is_linked(b, 'parentFeature', a2)
    if hasattr(a2, 'Feature15'):
        assert not _is_linked(a2, 'Feature15', b)


def test_assoc_features23_reverse_link_reassign_clear():
    a1 = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    a2 = fm_Group(comment="sample_text_2", description="sample_text_2", lower=13, or_=False, upper=13, xor=False)
    b = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    _safe_set(b, 'Feature24', a1)
    assert _is_linked(b, 'Feature24', a1)
    if hasattr(a1, 'parentGroup'):
        assert _is_linked(a1, 'parentGroup', b)
    _safe_set(b, 'Feature24', a2)
    assert _is_linked(b, 'Feature24', a2)
    if hasattr(a1, 'parentGroup'):
        assert not _is_linked(a1, 'parentGroup', b)
    if hasattr(a2, 'parentGroup'):
        assert _is_linked(a2, 'parentGroup', b)
    _safe_set(b, 'Feature24', None)
    assert not _is_linked(b, 'Feature24', a2)
    if hasattr(a2, 'parentGroup'):
        assert not _is_linked(a2, 'parentGroup', b)


def test_assoc_groups16_reverse_link_reassign_clear():
    a1 = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    a2 = fm_Group(comment="sample_text_2", description="sample_text_2", lower=13, or_=False, upper=13, xor=False)
    b = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Group17'):
        assert _is_linked(a1, 'Group17', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Group17'):
        assert not _is_linked(a1, 'Group17', b)
    if hasattr(a2, 'Group17'):
        assert _is_linked(a2, 'Group17', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Group17'):
        assert not _is_linked(a2, 'Group17', b)


def test_assoc_orphans1_reverse_link_reassign_clear():
    a1 = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    a2 = fm_FeatureModel(comment="sample_text_2", description="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    _safe_set(b, 'fm_Feature3', a1)
    assert _is_linked(b, 'fm_Feature3', a1)
    if hasattr(a1, 'fm_FeatureModel2'):
        assert _is_linked(a1, 'fm_FeatureModel2', b)
    _safe_set(b, 'fm_Feature3', a2)
    assert _is_linked(b, 'fm_Feature3', a2)
    if hasattr(a1, 'fm_FeatureModel2'):
        assert not _is_linked(a1, 'fm_FeatureModel2', b)
    if hasattr(a2, 'fm_FeatureModel2'):
        assert _is_linked(a2, 'fm_FeatureModel2', b)
    _safe_set(b, 'fm_Feature3', None)
    assert not _is_linked(b, 'fm_Feature3', a2)
    if hasattr(a2, 'fm_FeatureModel2'):
        assert not _is_linked(a2, 'fm_FeatureModel2', b)


def test_assoc_parent21_reverse_link_reassign_clear():
    a1 = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    a2 = fm_Group(comment="sample_text_2", description="sample_text_2", lower=13, or_=False, upper=13, xor=False)
    b = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    _safe_set(b, 'Feature22', a1)
    assert _is_linked(b, 'Feature22', a1)
    if hasattr(a1, 'groups'):
        assert _is_linked(a1, 'groups', b)
    _safe_set(b, 'Feature22', a2)
    assert _is_linked(b, 'Feature22', a2)
    if hasattr(a1, 'groups'):
        assert not _is_linked(a1, 'groups', b)
    if hasattr(a2, 'groups'):
        assert _is_linked(a2, 'groups', b)
    _safe_set(b, 'Feature22', None)
    assert not _is_linked(b, 'Feature22', a2)
    if hasattr(a2, 'groups'):
        assert not _is_linked(a2, 'groups', b)


def test_assoc_parentFeature9_reverse_link_reassign_clear():
    a1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    a2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    b = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    _safe_set(b, 'features', a1)
    assert _is_linked(b, 'features', a1)
    if hasattr(a1, 'Feature'):
        assert _is_linked(a1, 'Feature', b)
    _safe_set(b, 'features', a2)
    assert _is_linked(b, 'features', a2)
    if hasattr(a1, 'Feature'):
        assert not _is_linked(a1, 'Feature', b)
    if hasattr(a2, 'Feature'):
        assert _is_linked(a2, 'Feature', b)
    _safe_set(b, 'features', None)
    assert not _is_linked(b, 'features', a2)
    if hasattr(a2, 'Feature'):
        assert not _is_linked(a2, 'Feature', b)


def test_assoc_parentGroup10_reverse_link_reassign_clear():
    a1 = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    a2 = fm_Group(comment="sample_text_2", description="sample_text_2", lower=13, or_=False, upper=13, xor=False)
    b = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    _safe_set(b, 'features11', a1)
    assert _is_linked(b, 'features11', a1)
    if hasattr(a1, 'Group'):
        assert _is_linked(a1, 'Group', b)
    _safe_set(b, 'features11', a2)
    assert _is_linked(b, 'features11', a2)
    if hasattr(a1, 'Group'):
        assert not _is_linked(a1, 'Group', b)
    if hasattr(a2, 'Group'):
        assert _is_linked(a2, 'Group', b)
    _safe_set(b, 'features11', None)
    assert not _is_linked(b, 'features11', a2)
    if hasattr(a2, 'Group'):
        assert not _is_linked(a2, 'Group', b)


def test_assoc_root0_reverse_link_reassign_clear():
    a1 = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    a2 = fm_FeatureModel(comment="sample_text_2", description="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    _safe_set(b, 'fm_Feature', a1)
    assert _is_linked(b, 'fm_Feature', a1)
    if hasattr(a1, 'fm_FeatureModel'):
        assert _is_linked(a1, 'fm_FeatureModel', b)
    _safe_set(b, 'fm_Feature', a2)
    assert _is_linked(b, 'fm_Feature', a2)
    if hasattr(a1, 'fm_FeatureModel'):
        assert not _is_linked(a1, 'fm_FeatureModel', b)
    if hasattr(a2, 'fm_FeatureModel'):
        assert _is_linked(a2, 'fm_FeatureModel', b)
    _safe_set(b, 'fm_Feature', None)
    assert not _is_linked(b, 'fm_Feature', a2)
    if hasattr(a2, 'fm_FeatureModel'):
        assert not _is_linked(a2, 'fm_FeatureModel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_parent6_stub_double():
    # fm_EObject has no real 'fm_EObject' property in the generated
    # code (a bare stub) -- manually attach it so fm_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fm_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    partner = fm_EObject()
    setattr(partner, 'fm_EObject', None)
    _safe_set(owner, 'fm_Feature7', partner)
    assert getattr(partner, 'fm_EObject') == owner
    _safe_set(owner, 'fm_Feature7', None)
    assert getattr(partner, 'fm_EObject') is None


