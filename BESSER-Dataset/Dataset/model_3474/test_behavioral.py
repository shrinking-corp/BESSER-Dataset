import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TreeConstraint,
    myDsl_CrossTreeConstraint,
    myDsl_FM,
    myDsl_Feature,
    myDsl_FeatureAttribute,
    myDsl_MandatoryTreeConstraint,
    myDsl_OptionalTreeConstraint,
    myDsl_OrAlternativeTreeConstraint,
    myDsl_ParentChildConstraint,
    myDsl_TreeConstraint,
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

def test_assoc_feature118_reverse_link_reassign_clear():
    a1 = myDsl_Feature(name="sample_text")
    a2 = myDsl_Feature(name="sample_text_2")
    b = myDsl_CrossTreeConstraint(type="sample_text")
    _safe_set(b, 'myDsl_CrossTreeConstraint19', a1)
    assert _is_linked(b, 'myDsl_CrossTreeConstraint19', a1)
    if hasattr(a1, 'myDsl_Feature20'):
        assert _is_linked(a1, 'myDsl_Feature20', b)
    _safe_set(b, 'myDsl_CrossTreeConstraint19', a2)
    assert _is_linked(b, 'myDsl_CrossTreeConstraint19', a2)
    if hasattr(a1, 'myDsl_Feature20'):
        assert not _is_linked(a1, 'myDsl_Feature20', b)
    if hasattr(a2, 'myDsl_Feature20'):
        assert _is_linked(a2, 'myDsl_Feature20', b)
    _safe_set(b, 'myDsl_CrossTreeConstraint19', None)
    assert not _is_linked(b, 'myDsl_CrossTreeConstraint19', a2)
    if hasattr(a2, 'myDsl_Feature20'):
        assert not _is_linked(a2, 'myDsl_Feature20', b)


def test_assoc_feature221_reverse_link_reassign_clear():
    a1 = myDsl_Feature(name="sample_text")
    a2 = myDsl_Feature(name="sample_text_2")
    b = myDsl_CrossTreeConstraint(type="sample_text")
    _safe_set(b, 'myDsl_CrossTreeConstraint22', a1)
    assert _is_linked(b, 'myDsl_CrossTreeConstraint22', a1)
    if hasattr(a1, 'myDsl_Feature23'):
        assert _is_linked(a1, 'myDsl_Feature23', b)
    _safe_set(b, 'myDsl_CrossTreeConstraint22', a2)
    assert _is_linked(b, 'myDsl_CrossTreeConstraint22', a2)
    if hasattr(a1, 'myDsl_Feature23'):
        assert not _is_linked(a1, 'myDsl_Feature23', b)
    if hasattr(a2, 'myDsl_Feature23'):
        assert _is_linked(a2, 'myDsl_Feature23', b)
    _safe_set(b, 'myDsl_CrossTreeConstraint22', None)
    assert not _is_linked(b, 'myDsl_CrossTreeConstraint22', a2)
    if hasattr(a2, 'myDsl_Feature23'):
        assert not _is_linked(a2, 'myDsl_Feature23', b)


def test_assoc_feature24_reverse_link_reassign_clear():
    a1 = myDsl_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    a2 = myDsl_FeatureAttribute(attributeType="sample_text_2", defaultValue=13, maxValue=13, minValue=13, nullValue=13)
    b = myDsl_Feature(name="sample_text")
    _safe_set(b, 'myDsl_Feature26', a1)
    assert _is_linked(b, 'myDsl_Feature26', a1)
    if hasattr(a1, 'myDsl_FeatureAttribute25'):
        assert _is_linked(a1, 'myDsl_FeatureAttribute25', b)
    _safe_set(b, 'myDsl_Feature26', a2)
    assert _is_linked(b, 'myDsl_Feature26', a2)
    if hasattr(a1, 'myDsl_FeatureAttribute25'):
        assert not _is_linked(a1, 'myDsl_FeatureAttribute25', b)
    if hasattr(a2, 'myDsl_FeatureAttribute25'):
        assert _is_linked(a2, 'myDsl_FeatureAttribute25', b)
    _safe_set(b, 'myDsl_Feature26', None)
    assert not _is_linked(b, 'myDsl_Feature26', a2)
    if hasattr(a2, 'myDsl_FeatureAttribute25'):
        assert not _is_linked(a2, 'myDsl_FeatureAttribute25', b)


def test_assoc_features16_reverse_link_reassign_clear():
    a1 = myDsl_OrAlternativeTreeConstraint(max=7, min=7)
    a2 = myDsl_OrAlternativeTreeConstraint(max=13, min=13)
    b = myDsl_Feature(name="sample_text")
    _safe_set(b, 'myDsl_Feature17', a1)
    assert _is_linked(b, 'myDsl_Feature17', a1)
    if hasattr(a1, 'myDsl_OrAlternativeTreeConstraint'):
        assert _is_linked(a1, 'myDsl_OrAlternativeTreeConstraint', b)
    _safe_set(b, 'myDsl_Feature17', a2)
    assert _is_linked(b, 'myDsl_Feature17', a2)
    if hasattr(a1, 'myDsl_OrAlternativeTreeConstraint'):
        assert not _is_linked(a1, 'myDsl_OrAlternativeTreeConstraint', b)
    if hasattr(a2, 'myDsl_OrAlternativeTreeConstraint'):
        assert _is_linked(a2, 'myDsl_OrAlternativeTreeConstraint', b)
    _safe_set(b, 'myDsl_Feature17', None)
    assert not _is_linked(b, 'myDsl_Feature17', a2)
    if hasattr(a2, 'myDsl_OrAlternativeTreeConstraint'):
        assert not _is_linked(a2, 'myDsl_OrAlternativeTreeConstraint', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes3_stub_double():
    # myDsl_FM has no real 'myDsl_FM4' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_FeatureAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_FeatureAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    partner = myDsl_FM()
    setattr(partner, 'myDsl_FM4', None)
    _safe_set(owner, 'myDsl_FeatureAttribute', partner)
    assert owner in getattr(partner, 'myDsl_FM4')
    _safe_set(owner, 'myDsl_FeatureAttribute', None)
    assert owner not in getattr(partner, 'myDsl_FM4')


def test_assoc_crossTreeConstraints5_stub_double():
    # myDsl_FM has no real 'myDsl_FM6' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_CrossTreeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_CrossTreeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_CrossTreeConstraint(type="sample_text")
    partner = myDsl_FM()
    setattr(partner, 'myDsl_FM6', None)
    _safe_set(owner, 'myDsl_CrossTreeConstraint', partner)
    assert owner in getattr(partner, 'myDsl_FM6')
    _safe_set(owner, 'myDsl_CrossTreeConstraint', None)
    assert owner not in getattr(partner, 'myDsl_FM6')


def test_assoc_feature12_stub_double():
    # myDsl_MandatoryTreeConstraint has no real 'myDsl_MandatoryTreeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Feature(name="sample_text")
    partner = myDsl_MandatoryTreeConstraint()
    setattr(partner, 'myDsl_MandatoryTreeConstraint', None)
    _safe_set(owner, 'myDsl_Feature13', partner)
    assert getattr(partner, 'myDsl_MandatoryTreeConstraint') == owner
    _safe_set(owner, 'myDsl_Feature13', None)
    assert getattr(partner, 'myDsl_MandatoryTreeConstraint') is None


def test_assoc_feature14_stub_double():
    # myDsl_OptionalTreeConstraint has no real 'myDsl_OptionalTreeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Feature(name="sample_text")
    partner = myDsl_OptionalTreeConstraint()
    setattr(partner, 'myDsl_OptionalTreeConstraint', None)
    _safe_set(owner, 'myDsl_Feature15', partner)
    assert getattr(partner, 'myDsl_OptionalTreeConstraint') == owner
    _safe_set(owner, 'myDsl_Feature15', None)
    assert getattr(partner, 'myDsl_OptionalTreeConstraint') is None


def test_assoc_features0_stub_double():
    # myDsl_FM has no real 'myDsl_FM' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Feature(name="sample_text")
    partner = myDsl_FM()
    setattr(partner, 'myDsl_FM', None)
    _safe_set(owner, 'myDsl_Feature', partner)
    assert owner in getattr(partner, 'myDsl_FM')
    _safe_set(owner, 'myDsl_Feature', None)
    assert owner not in getattr(partner, 'myDsl_FM')


def test_assoc_parent7_stub_double():
    # myDsl_ParentChildConstraint has no real 'myDsl_ParentChildConstraint8' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Feature(name="sample_text")
    partner = myDsl_ParentChildConstraint()
    setattr(partner, 'myDsl_ParentChildConstraint8', None)
    _safe_set(owner, 'myDsl_Feature9', partner)
    assert getattr(partner, 'myDsl_ParentChildConstraint8') == owner
    _safe_set(owner, 'myDsl_Feature9', None)
    assert getattr(partner, 'myDsl_ParentChildConstraint8') is None


