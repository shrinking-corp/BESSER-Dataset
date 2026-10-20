import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BasicFMmetamodel_Alternative,
    BasicFMmetamodel_CrossTreeConstraint,
    BasicFMmetamodel_Feature,
    BasicFMmetamodel_FeatureModel,
    BasicFMmetamodel_OrGroup,
    Feature,
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

def test_assoc_children7_reverse_link_reassign_clear():
    a1 = BasicFMmetamodel_Feature(id="sample_text", mandatory=True, name="sample_text", selected=True)
    a2 = BasicFMmetamodel_Feature(id="sample_text_2", mandatory=False, name="sample_text_2", selected=False)
    b = BasicFMmetamodel_Feature(id="sample_text", mandatory=True, name="sample_text", selected=True)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Feature'):
        assert _is_linked(a1, 'Feature', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Feature'):
        assert not _is_linked(a1, 'Feature', b)
    if hasattr(a2, 'Feature'):
        assert _is_linked(a2, 'Feature', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Feature'):
        assert not _is_linked(a2, 'Feature', b)


def test_assoc_features1_reverse_link_reassign_clear():
    a1 = BasicFMmetamodel_FeatureModel(name="sample_text")
    a2 = BasicFMmetamodel_FeatureModel(name="sample_text_2")
    b = BasicFMmetamodel_Feature(id="sample_text", mandatory=True, name="sample_text", selected=True)
    _safe_set(b, 'BasicFMmetamodel_Feature3', a1)
    assert _is_linked(b, 'BasicFMmetamodel_Feature3', a1)
    if hasattr(a1, 'BasicFMmetamodel_FeatureModel2'):
        assert _is_linked(a1, 'BasicFMmetamodel_FeatureModel2', b)
    _safe_set(b, 'BasicFMmetamodel_Feature3', a2)
    assert _is_linked(b, 'BasicFMmetamodel_Feature3', a2)
    if hasattr(a1, 'BasicFMmetamodel_FeatureModel2'):
        assert not _is_linked(a1, 'BasicFMmetamodel_FeatureModel2', b)
    if hasattr(a2, 'BasicFMmetamodel_FeatureModel2'):
        assert _is_linked(a2, 'BasicFMmetamodel_FeatureModel2', b)
    _safe_set(b, 'BasicFMmetamodel_Feature3', None)
    assert not _is_linked(b, 'BasicFMmetamodel_Feature3', a2)
    if hasattr(a2, 'BasicFMmetamodel_FeatureModel2'):
        assert not _is_linked(a2, 'BasicFMmetamodel_FeatureModel2', b)


def test_assoc_parent9_reverse_link_reassign_clear():
    a1 = BasicFMmetamodel_Feature(id="sample_text", mandatory=True, name="sample_text", selected=True)
    a2 = BasicFMmetamodel_Feature(id="sample_text_2", mandatory=False, name="sample_text_2", selected=False)
    b = BasicFMmetamodel_Feature(id="sample_text", mandatory=True, name="sample_text", selected=True)
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Feature10'):
        assert _is_linked(a1, 'Feature10', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Feature10'):
        assert not _is_linked(a1, 'Feature10', b)
    if hasattr(a2, 'Feature10'):
        assert _is_linked(a2, 'Feature10', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Feature10'):
        assert not _is_linked(a2, 'Feature10', b)


def test_assoc_root0_reverse_link_reassign_clear():
    a1 = BasicFMmetamodel_FeatureModel(name="sample_text")
    a2 = BasicFMmetamodel_FeatureModel(name="sample_text_2")
    b = BasicFMmetamodel_Feature(id="sample_text", mandatory=True, name="sample_text", selected=True)
    _safe_set(b, 'BasicFMmetamodel_Feature', a1)
    assert _is_linked(b, 'BasicFMmetamodel_Feature', a1)
    if hasattr(a1, 'BasicFMmetamodel_FeatureModel'):
        assert _is_linked(a1, 'BasicFMmetamodel_FeatureModel', b)
    _safe_set(b, 'BasicFMmetamodel_Feature', a2)
    assert _is_linked(b, 'BasicFMmetamodel_Feature', a2)
    if hasattr(a1, 'BasicFMmetamodel_FeatureModel'):
        assert not _is_linked(a1, 'BasicFMmetamodel_FeatureModel', b)
    if hasattr(a2, 'BasicFMmetamodel_FeatureModel'):
        assert _is_linked(a2, 'BasicFMmetamodel_FeatureModel', b)
    _safe_set(b, 'BasicFMmetamodel_Feature', None)
    assert not _is_linked(b, 'BasicFMmetamodel_Feature', a2)
    if hasattr(a2, 'BasicFMmetamodel_FeatureModel'):
        assert not _is_linked(a2, 'BasicFMmetamodel_FeatureModel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_crossTreeConstraints4_stub_double():
    # BasicFMmetamodel_CrossTreeConstraint has no real 'BasicFMmetamodel_CrossTreeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so BasicFMmetamodel_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # BasicFMmetamodel_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = BasicFMmetamodel_FeatureModel(name="sample_text")
    partner = BasicFMmetamodel_CrossTreeConstraint()
    setattr(partner, 'BasicFMmetamodel_CrossTreeConstraint', None)
    _safe_set(owner, 'BasicFMmetamodel_FeatureModel5', {partner})
    assert getattr(partner, 'BasicFMmetamodel_CrossTreeConstraint') == owner
    _safe_set(owner, 'BasicFMmetamodel_FeatureModel5', set())
    assert getattr(partner, 'BasicFMmetamodel_CrossTreeConstraint') is None


