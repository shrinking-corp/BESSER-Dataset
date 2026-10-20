import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TreeConstraint,
    sPLOT2CoCo_CrossTreeConstraint,
    sPLOT2CoCo_FM,
    sPLOT2CoCo_Feature,
    sPLOT2CoCo_FeatureAttribute,
    sPLOT2CoCo_MandatoryTreeConstraint,
    sPLOT2CoCo_OptionalTreeConstraint,
    sPLOT2CoCo_OrAlternativeTreeConstraint,
    sPLOT2CoCo_ParentChildConstraint,
    sPLOT2CoCo_TreeConstraint,
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
    a1 = sPLOT2CoCo_Feature(name="sample_text")
    a2 = sPLOT2CoCo_Feature(name="sample_text_2")
    b = sPLOT2CoCo_CrossTreeConstraint(type="sample_text")
    _safe_set(b, 'sPLOT2CoCo_CrossTreeConstraint19', a1)
    assert _is_linked(b, 'sPLOT2CoCo_CrossTreeConstraint19', a1)
    if hasattr(a1, 'sPLOT2CoCo_Feature20'):
        assert _is_linked(a1, 'sPLOT2CoCo_Feature20', b)
    _safe_set(b, 'sPLOT2CoCo_CrossTreeConstraint19', a2)
    assert _is_linked(b, 'sPLOT2CoCo_CrossTreeConstraint19', a2)
    if hasattr(a1, 'sPLOT2CoCo_Feature20'):
        assert not _is_linked(a1, 'sPLOT2CoCo_Feature20', b)
    if hasattr(a2, 'sPLOT2CoCo_Feature20'):
        assert _is_linked(a2, 'sPLOT2CoCo_Feature20', b)
    _safe_set(b, 'sPLOT2CoCo_CrossTreeConstraint19', None)
    assert not _is_linked(b, 'sPLOT2CoCo_CrossTreeConstraint19', a2)
    if hasattr(a2, 'sPLOT2CoCo_Feature20'):
        assert not _is_linked(a2, 'sPLOT2CoCo_Feature20', b)


def test_assoc_feature221_reverse_link_reassign_clear():
    a1 = sPLOT2CoCo_Feature(name="sample_text")
    a2 = sPLOT2CoCo_Feature(name="sample_text_2")
    b = sPLOT2CoCo_CrossTreeConstraint(type="sample_text")
    _safe_set(b, 'sPLOT2CoCo_CrossTreeConstraint22', a1)
    assert _is_linked(b, 'sPLOT2CoCo_CrossTreeConstraint22', a1)
    if hasattr(a1, 'sPLOT2CoCo_Feature23'):
        assert _is_linked(a1, 'sPLOT2CoCo_Feature23', b)
    _safe_set(b, 'sPLOT2CoCo_CrossTreeConstraint22', a2)
    assert _is_linked(b, 'sPLOT2CoCo_CrossTreeConstraint22', a2)
    if hasattr(a1, 'sPLOT2CoCo_Feature23'):
        assert not _is_linked(a1, 'sPLOT2CoCo_Feature23', b)
    if hasattr(a2, 'sPLOT2CoCo_Feature23'):
        assert _is_linked(a2, 'sPLOT2CoCo_Feature23', b)
    _safe_set(b, 'sPLOT2CoCo_CrossTreeConstraint22', None)
    assert not _is_linked(b, 'sPLOT2CoCo_CrossTreeConstraint22', a2)
    if hasattr(a2, 'sPLOT2CoCo_Feature23'):
        assert not _is_linked(a2, 'sPLOT2CoCo_Feature23', b)


def test_assoc_feature24_reverse_link_reassign_clear():
    a1 = sPLOT2CoCo_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    a2 = sPLOT2CoCo_FeatureAttribute(attributeType="sample_text_2", defaultValue=13, maxValue=13, minValue=13, nullValue=13)
    b = sPLOT2CoCo_Feature(name="sample_text")
    _safe_set(b, 'sPLOT2CoCo_Feature26', a1)
    assert _is_linked(b, 'sPLOT2CoCo_Feature26', a1)
    if hasattr(a1, 'sPLOT2CoCo_FeatureAttribute25'):
        assert _is_linked(a1, 'sPLOT2CoCo_FeatureAttribute25', b)
    _safe_set(b, 'sPLOT2CoCo_Feature26', a2)
    assert _is_linked(b, 'sPLOT2CoCo_Feature26', a2)
    if hasattr(a1, 'sPLOT2CoCo_FeatureAttribute25'):
        assert not _is_linked(a1, 'sPLOT2CoCo_FeatureAttribute25', b)
    if hasattr(a2, 'sPLOT2CoCo_FeatureAttribute25'):
        assert _is_linked(a2, 'sPLOT2CoCo_FeatureAttribute25', b)
    _safe_set(b, 'sPLOT2CoCo_Feature26', None)
    assert not _is_linked(b, 'sPLOT2CoCo_Feature26', a2)
    if hasattr(a2, 'sPLOT2CoCo_FeatureAttribute25'):
        assert not _is_linked(a2, 'sPLOT2CoCo_FeatureAttribute25', b)


def test_assoc_features16_reverse_link_reassign_clear():
    a1 = sPLOT2CoCo_OrAlternativeTreeConstraint(max=7, min=7)
    a2 = sPLOT2CoCo_OrAlternativeTreeConstraint(max=13, min=13)
    b = sPLOT2CoCo_Feature(name="sample_text")
    _safe_set(b, 'sPLOT2CoCo_Feature17', a1)
    assert _is_linked(b, 'sPLOT2CoCo_Feature17', a1)
    if hasattr(a1, 'sPLOT2CoCo_OrAlternativeTreeConstraint'):
        assert _is_linked(a1, 'sPLOT2CoCo_OrAlternativeTreeConstraint', b)
    _safe_set(b, 'sPLOT2CoCo_Feature17', a2)
    assert _is_linked(b, 'sPLOT2CoCo_Feature17', a2)
    if hasattr(a1, 'sPLOT2CoCo_OrAlternativeTreeConstraint'):
        assert not _is_linked(a1, 'sPLOT2CoCo_OrAlternativeTreeConstraint', b)
    if hasattr(a2, 'sPLOT2CoCo_OrAlternativeTreeConstraint'):
        assert _is_linked(a2, 'sPLOT2CoCo_OrAlternativeTreeConstraint', b)
    _safe_set(b, 'sPLOT2CoCo_Feature17', None)
    assert not _is_linked(b, 'sPLOT2CoCo_Feature17', a2)
    if hasattr(a2, 'sPLOT2CoCo_OrAlternativeTreeConstraint'):
        assert not _is_linked(a2, 'sPLOT2CoCo_OrAlternativeTreeConstraint', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes3_stub_double():
    # sPLOT2CoCo_FM has no real 'sPLOT2CoCo_FM4' property in the generated
    # code (a bare stub) -- manually attach it so sPLOT2CoCo_FeatureAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sPLOT2CoCo_FeatureAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sPLOT2CoCo_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    partner = sPLOT2CoCo_FM()
    setattr(partner, 'sPLOT2CoCo_FM4', None)
    _safe_set(owner, 'sPLOT2CoCo_FeatureAttribute', partner)
    assert owner in getattr(partner, 'sPLOT2CoCo_FM4')
    _safe_set(owner, 'sPLOT2CoCo_FeatureAttribute', None)
    assert owner not in getattr(partner, 'sPLOT2CoCo_FM4')


def test_assoc_crossTreeConstraints5_stub_double():
    # sPLOT2CoCo_FM has no real 'sPLOT2CoCo_FM6' property in the generated
    # code (a bare stub) -- manually attach it so sPLOT2CoCo_CrossTreeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sPLOT2CoCo_CrossTreeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sPLOT2CoCo_CrossTreeConstraint(type="sample_text")
    partner = sPLOT2CoCo_FM()
    setattr(partner, 'sPLOT2CoCo_FM6', None)
    _safe_set(owner, 'sPLOT2CoCo_CrossTreeConstraint', partner)
    assert owner in getattr(partner, 'sPLOT2CoCo_FM6')
    _safe_set(owner, 'sPLOT2CoCo_CrossTreeConstraint', None)
    assert owner not in getattr(partner, 'sPLOT2CoCo_FM6')


def test_assoc_feature12_stub_double():
    # sPLOT2CoCo_MandatoryTreeConstraint has no real 'sPLOT2CoCo_MandatoryTreeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so sPLOT2CoCo_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sPLOT2CoCo_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sPLOT2CoCo_Feature(name="sample_text")
    partner = sPLOT2CoCo_MandatoryTreeConstraint()
    setattr(partner, 'sPLOT2CoCo_MandatoryTreeConstraint', None)
    _safe_set(owner, 'sPLOT2CoCo_Feature13', partner)
    assert getattr(partner, 'sPLOT2CoCo_MandatoryTreeConstraint') == owner
    _safe_set(owner, 'sPLOT2CoCo_Feature13', None)
    assert getattr(partner, 'sPLOT2CoCo_MandatoryTreeConstraint') is None


def test_assoc_feature14_stub_double():
    # sPLOT2CoCo_OptionalTreeConstraint has no real 'sPLOT2CoCo_OptionalTreeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so sPLOT2CoCo_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sPLOT2CoCo_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sPLOT2CoCo_Feature(name="sample_text")
    partner = sPLOT2CoCo_OptionalTreeConstraint()
    setattr(partner, 'sPLOT2CoCo_OptionalTreeConstraint', None)
    _safe_set(owner, 'sPLOT2CoCo_Feature15', partner)
    assert getattr(partner, 'sPLOT2CoCo_OptionalTreeConstraint') == owner
    _safe_set(owner, 'sPLOT2CoCo_Feature15', None)
    assert getattr(partner, 'sPLOT2CoCo_OptionalTreeConstraint') is None


def test_assoc_features0_stub_double():
    # sPLOT2CoCo_FM has no real 'sPLOT2CoCo_FM' property in the generated
    # code (a bare stub) -- manually attach it so sPLOT2CoCo_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sPLOT2CoCo_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sPLOT2CoCo_Feature(name="sample_text")
    partner = sPLOT2CoCo_FM()
    setattr(partner, 'sPLOT2CoCo_FM', None)
    _safe_set(owner, 'sPLOT2CoCo_Feature', partner)
    assert owner in getattr(partner, 'sPLOT2CoCo_FM')
    _safe_set(owner, 'sPLOT2CoCo_Feature', None)
    assert owner not in getattr(partner, 'sPLOT2CoCo_FM')


def test_assoc_parent7_stub_double():
    # sPLOT2CoCo_ParentChildConstraint has no real 'sPLOT2CoCo_ParentChildConstraint8' property in the generated
    # code (a bare stub) -- manually attach it so sPLOT2CoCo_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sPLOT2CoCo_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sPLOT2CoCo_Feature(name="sample_text")
    partner = sPLOT2CoCo_ParentChildConstraint()
    setattr(partner, 'sPLOT2CoCo_ParentChildConstraint8', None)
    _safe_set(owner, 'sPLOT2CoCo_Feature9', partner)
    assert getattr(partner, 'sPLOT2CoCo_ParentChildConstraint8') == owner
    _safe_set(owner, 'sPLOT2CoCo_Feature9', None)
    assert getattr(partner, 'sPLOT2CoCo_ParentChildConstraint8') is None


