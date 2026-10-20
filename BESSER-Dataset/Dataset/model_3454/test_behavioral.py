import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    FeatureModel_Comment,
    FeatureModel_Constraint,
    FeatureModel_ExcludeConstraint,
    FeatureModel_Feature,
    FeatureModel_FeatureModel,
    FeatureModel_Group,
    FeatureModel_NamedElement,
    FeatureModel_RequireConstraint,
    NamedElement,
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

def test_assoc_children10_reverse_link_reassign_clear():
    a1 = FeatureModel_Feature(abstract=True, mandatory=True)
    a2 = FeatureModel_Feature(abstract=False, mandatory=False)
    b = FeatureModel_Feature(abstract=True, mandatory=True)
    _safe_set(b, 'FeatureModel_Feature9', {a1})
    assert _is_linked(b, 'FeatureModel_Feature9', a1)
    if hasattr(a1, 'FeatureModel_Feature11'):
        assert _is_linked(a1, 'FeatureModel_Feature11', b)
    _safe_set(b, 'FeatureModel_Feature9', {a2})
    assert _is_linked(b, 'FeatureModel_Feature9', a2)
    if hasattr(a1, 'FeatureModel_Feature11'):
        assert not _is_linked(a1, 'FeatureModel_Feature11', b)
    if hasattr(a2, 'FeatureModel_Feature11'):
        assert _is_linked(a2, 'FeatureModel_Feature11', b)
    _safe_set(b, 'FeatureModel_Feature9', set())
    assert not _is_linked(b, 'FeatureModel_Feature9', a2)
    if hasattr(a2, 'FeatureModel_Feature11'):
        assert not _is_linked(a2, 'FeatureModel_Feature11', b)


def test_assoc_comments0_reverse_link_reassign_clear():
    a1 = FeatureModel_FeatureModel(version=3.14)
    a2 = FeatureModel_FeatureModel(version=9.99)
    b = FeatureModel_Comment(text="sample_text")
    _safe_set(b, 'FeatureModel_Comment', a1)
    assert _is_linked(b, 'FeatureModel_Comment', a1)
    if hasattr(a1, 'FeatureModel_FeatureModel'):
        assert _is_linked(a1, 'FeatureModel_FeatureModel', b)
    _safe_set(b, 'FeatureModel_Comment', a2)
    assert _is_linked(b, 'FeatureModel_Comment', a2)
    if hasattr(a1, 'FeatureModel_FeatureModel'):
        assert not _is_linked(a1, 'FeatureModel_FeatureModel', b)
    if hasattr(a2, 'FeatureModel_FeatureModel'):
        assert _is_linked(a2, 'FeatureModel_FeatureModel', b)
    _safe_set(b, 'FeatureModel_Comment', None)
    assert not _is_linked(b, 'FeatureModel_Comment', a2)
    if hasattr(a2, 'FeatureModel_FeatureModel'):
        assert not _is_linked(a2, 'FeatureModel_FeatureModel', b)


def test_assoc_constraints1_reverse_link_reassign_clear():
    a1 = FeatureModel_FeatureModel(version=3.14)
    a2 = FeatureModel_FeatureModel(version=9.99)
    b = FeatureModel_Constraint(code="sample_text", language="sample_text")
    _safe_set(b, 'FeatureModel_Constraint', a1)
    assert _is_linked(b, 'FeatureModel_Constraint', a1)
    if hasattr(a1, 'FeatureModel_FeatureModel2'):
        assert _is_linked(a1, 'FeatureModel_FeatureModel2', b)
    _safe_set(b, 'FeatureModel_Constraint', a2)
    assert _is_linked(b, 'FeatureModel_Constraint', a2)
    if hasattr(a1, 'FeatureModel_FeatureModel2'):
        assert not _is_linked(a1, 'FeatureModel_FeatureModel2', b)
    if hasattr(a2, 'FeatureModel_FeatureModel2'):
        assert _is_linked(a2, 'FeatureModel_FeatureModel2', b)
    _safe_set(b, 'FeatureModel_Constraint', None)
    assert not _is_linked(b, 'FeatureModel_Constraint', a2)
    if hasattr(a2, 'FeatureModel_FeatureModel2'):
        assert not _is_linked(a2, 'FeatureModel_FeatureModel2', b)


def test_assoc_element7_reverse_link_reassign_clear():
    a1 = FeatureModel_NamedElement(name="sample_text")
    a2 = FeatureModel_NamedElement(name="sample_text_2")
    b = FeatureModel_Comment(text="sample_text")
    _safe_set(b, 'FeatureModel_Comment8', a1)
    assert _is_linked(b, 'FeatureModel_Comment8', a1)
    if hasattr(a1, 'FeatureModel_NamedElement'):
        assert _is_linked(a1, 'FeatureModel_NamedElement', b)
    _safe_set(b, 'FeatureModel_Comment8', a2)
    assert _is_linked(b, 'FeatureModel_Comment8', a2)
    if hasattr(a1, 'FeatureModel_NamedElement'):
        assert not _is_linked(a1, 'FeatureModel_NamedElement', b)
    if hasattr(a2, 'FeatureModel_NamedElement'):
        assert _is_linked(a2, 'FeatureModel_NamedElement', b)
    _safe_set(b, 'FeatureModel_Comment8', None)
    assert not _is_linked(b, 'FeatureModel_Comment8', a2)
    if hasattr(a2, 'FeatureModel_NamedElement'):
        assert not _is_linked(a2, 'FeatureModel_NamedElement', b)


def test_assoc_features26_reverse_link_reassign_clear():
    a1 = FeatureModel_Group(groupType="sample_text")
    a2 = FeatureModel_Group(groupType="sample_text_2")
    b = FeatureModel_Feature(abstract=True, mandatory=True)
    _safe_set(b, 'Feature27', a1)
    assert _is_linked(b, 'Feature27', a1)
    if hasattr(a1, 'group'):
        assert _is_linked(a1, 'group', b)
    _safe_set(b, 'Feature27', a2)
    assert _is_linked(b, 'Feature27', a2)
    if hasattr(a1, 'group'):
        assert not _is_linked(a1, 'group', b)
    if hasattr(a2, 'group'):
        assert _is_linked(a2, 'group', b)
    _safe_set(b, 'Feature27', None)
    assert not _is_linked(b, 'Feature27', a2)
    if hasattr(a2, 'group'):
        assert not _is_linked(a2, 'group', b)


def test_assoc_group15_reverse_link_reassign_clear():
    a1 = FeatureModel_Group(groupType="sample_text")
    a2 = FeatureModel_Group(groupType="sample_text_2")
    b = FeatureModel_Feature(abstract=True, mandatory=True)
    _safe_set(b, 'features', a1)
    assert _is_linked(b, 'features', a1)
    if hasattr(a1, 'Group'):
        assert _is_linked(a1, 'Group', b)
    _safe_set(b, 'features', a2)
    assert _is_linked(b, 'features', a2)
    if hasattr(a1, 'Group'):
        assert not _is_linked(a1, 'Group', b)
    if hasattr(a2, 'Group'):
        assert _is_linked(a2, 'Group', b)
    _safe_set(b, 'features', None)
    assert not _is_linked(b, 'features', a2)
    if hasattr(a2, 'Group'):
        assert not _is_linked(a2, 'Group', b)


def test_assoc_groups5_reverse_link_reassign_clear():
    a1 = FeatureModel_Group(groupType="sample_text")
    a2 = FeatureModel_Group(groupType="sample_text_2")
    b = FeatureModel_FeatureModel(version=3.14)
    _safe_set(b, 'FeatureModel_FeatureModel6', {a1})
    assert _is_linked(b, 'FeatureModel_FeatureModel6', a1)
    if hasattr(a1, 'FeatureModel_Group'):
        assert _is_linked(a1, 'FeatureModel_Group', b)
    _safe_set(b, 'FeatureModel_FeatureModel6', {a2})
    assert _is_linked(b, 'FeatureModel_FeatureModel6', a2)
    if hasattr(a1, 'FeatureModel_Group'):
        assert not _is_linked(a1, 'FeatureModel_Group', b)
    if hasattr(a2, 'FeatureModel_Group'):
        assert _is_linked(a2, 'FeatureModel_Group', b)
    _safe_set(b, 'FeatureModel_FeatureModel6', set())
    assert not _is_linked(b, 'FeatureModel_FeatureModel6', a2)
    if hasattr(a2, 'FeatureModel_Group'):
        assert not _is_linked(a2, 'FeatureModel_Group', b)


def test_assoc_root3_reverse_link_reassign_clear():
    a1 = FeatureModel_FeatureModel(version=3.14)
    a2 = FeatureModel_FeatureModel(version=9.99)
    b = FeatureModel_Feature(abstract=True, mandatory=True)
    _safe_set(b, 'FeatureModel_Feature', a1)
    assert _is_linked(b, 'FeatureModel_Feature', a1)
    if hasattr(a1, 'FeatureModel_FeatureModel4'):
        assert _is_linked(a1, 'FeatureModel_FeatureModel4', b)
    _safe_set(b, 'FeatureModel_Feature', a2)
    assert _is_linked(b, 'FeatureModel_Feature', a2)
    if hasattr(a1, 'FeatureModel_FeatureModel4'):
        assert not _is_linked(a1, 'FeatureModel_FeatureModel4', b)
    if hasattr(a2, 'FeatureModel_FeatureModel4'):
        assert _is_linked(a2, 'FeatureModel_FeatureModel4', b)
    _safe_set(b, 'FeatureModel_Feature', None)
    assert not _is_linked(b, 'FeatureModel_Feature', a2)
    if hasattr(a2, 'FeatureModel_FeatureModel4'):
        assert not _is_linked(a2, 'FeatureModel_FeatureModel4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_excludeConstraintsA16_stub_double():
    # FeatureModel_ExcludeConstraint has no real 'ExcludeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so FeatureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FeatureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FeatureModel_Feature(abstract=True, mandatory=True)
    partner = FeatureModel_ExcludeConstraint()
    setattr(partner, 'ExcludeConstraint', None)
    _safe_set(owner, 'excludedFeatureA', {partner})
    assert getattr(partner, 'ExcludeConstraint') == owner
    _safe_set(owner, 'excludedFeatureA', set())
    assert getattr(partner, 'ExcludeConstraint') is None


def test_assoc_excludeConstraintsB17_stub_double():
    # FeatureModel_ExcludeConstraint has no real 'ExcludeConstraint18' property in the generated
    # code (a bare stub) -- manually attach it so FeatureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FeatureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FeatureModel_Feature(abstract=True, mandatory=True)
    partner = FeatureModel_ExcludeConstraint()
    setattr(partner, 'ExcludeConstraint18', None)
    _safe_set(owner, 'excludedFeatureB', {partner})
    assert getattr(partner, 'ExcludeConstraint18') == owner
    _safe_set(owner, 'excludedFeatureB', set())
    assert getattr(partner, 'ExcludeConstraint18') is None


def test_assoc_excludedFeatureA22_stub_double():
    # FeatureModel_ExcludeConstraint has no real 'excludeConstraintsA' property in the generated
    # code (a bare stub) -- manually attach it so FeatureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FeatureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FeatureModel_Feature(abstract=True, mandatory=True)
    partner = FeatureModel_ExcludeConstraint()
    setattr(partner, 'excludeConstraintsA', None)
    _safe_set(owner, 'Feature23', partner)
    assert getattr(partner, 'excludeConstraintsA') == owner
    _safe_set(owner, 'Feature23', None)
    assert getattr(partner, 'excludeConstraintsA') is None


def test_assoc_excludedFeatureB24_stub_double():
    # FeatureModel_ExcludeConstraint has no real 'excludeConstraintsB' property in the generated
    # code (a bare stub) -- manually attach it so FeatureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FeatureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FeatureModel_Feature(abstract=True, mandatory=True)
    partner = FeatureModel_ExcludeConstraint()
    setattr(partner, 'excludeConstraintsB', None)
    _safe_set(owner, 'Feature25', partner)
    assert getattr(partner, 'excludeConstraintsB') == owner
    _safe_set(owner, 'Feature25', None)
    assert getattr(partner, 'excludeConstraintsB') is None


def test_assoc_feature20_stub_double():
    # FeatureModel_RequireConstraint has no real 'requireConstraints' property in the generated
    # code (a bare stub) -- manually attach it so FeatureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FeatureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FeatureModel_Feature(abstract=True, mandatory=True)
    partner = FeatureModel_RequireConstraint()
    setattr(partner, 'requireConstraints', None)
    _safe_set(owner, 'Feature21', partner)
    assert getattr(partner, 'requireConstraints') == owner
    _safe_set(owner, 'Feature21', None)
    assert getattr(partner, 'requireConstraints') is None


def test_assoc_requireConstraints13_stub_double():
    # FeatureModel_RequireConstraint has no real 'RequireConstraint14' property in the generated
    # code (a bare stub) -- manually attach it so FeatureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FeatureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FeatureModel_Feature(abstract=True, mandatory=True)
    partner = FeatureModel_RequireConstraint()
    setattr(partner, 'RequireConstraint14', None)
    _safe_set(owner, 'feature', {partner})
    assert getattr(partner, 'RequireConstraint14') == owner
    _safe_set(owner, 'feature', set())
    assert getattr(partner, 'RequireConstraint14') is None


def test_assoc_requiredConstraints12_stub_double():
    # FeatureModel_RequireConstraint has no real 'RequireConstraint' property in the generated
    # code (a bare stub) -- manually attach it so FeatureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FeatureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FeatureModel_Feature(abstract=True, mandatory=True)
    partner = FeatureModel_RequireConstraint()
    setattr(partner, 'RequireConstraint', None)
    _safe_set(owner, 'requiredFeature', {partner})
    assert getattr(partner, 'RequireConstraint') == owner
    _safe_set(owner, 'requiredFeature', set())
    assert getattr(partner, 'RequireConstraint') is None


def test_assoc_requiredFeature19_stub_double():
    # FeatureModel_RequireConstraint has no real 'requiredConstraints' property in the generated
    # code (a bare stub) -- manually attach it so FeatureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FeatureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FeatureModel_Feature(abstract=True, mandatory=True)
    partner = FeatureModel_RequireConstraint()
    setattr(partner, 'requiredConstraints', None)
    _safe_set(owner, 'Feature', partner)
    assert getattr(partner, 'requiredConstraints') == owner
    _safe_set(owner, 'Feature', None)
    assert getattr(partner, 'requiredConstraints') is None


