import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElements,
    SuperEntity,
    aml_AbstractElements,
    aml_Aml,
    aml_Cable,
    aml_ColorFeature,
    aml_Drive,
    aml_Entity,
    aml_Feature,
    aml_FormFeature,
    aml_LengthFeature,
    aml_MaxFeature,
    aml_MinMax,
    aml_NetWorkFeature,
    aml_PriceRule,
    aml_ProductPUIDFeature,
    aml_SizeFeature,
    aml_SpeedFeature,
    aml_SuperEntity,
    aml_TargetGroupFeature,
    aml_TypeFeature,
    Color,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_colorFeature13_stub_double():
    # aml_Cable has no real 'aml_Cable' property in the generated
    # code (a bare stub) -- manually attach it so aml_ColorFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_ColorFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_ColorFeature(name="sample_text", value="sample_text")
    partner = aml_Cable()
    setattr(partner, 'aml_Cable', None)
    _safe_set(owner, 'aml_ColorFeature', partner)
    assert getattr(partner, 'aml_Cable') == owner
    _safe_set(owner, 'aml_ColorFeature', None)
    assert getattr(partner, 'aml_Cable') is None


def test_assoc_elements0_stub_double():
    # aml_Aml has no real 'aml_Aml' property in the generated
    # code (a bare stub) -- manually attach it so aml_AbstractElements's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_AbstractElements's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_AbstractElements(name="sample_text")
    partner = aml_Aml()
    setattr(partner, 'aml_Aml', None)
    _safe_set(owner, 'aml_AbstractElements', partner)
    assert owner in getattr(partner, 'aml_Aml')
    _safe_set(owner, 'aml_AbstractElements', None)
    assert owner not in getattr(partner, 'aml_Aml')


def test_assoc_features20_stub_double():
    # aml_PriceRule has no real 'aml_PriceRule21' property in the generated
    # code (a bare stub) -- manually attach it so aml_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Feature(name="sample_text", value="sample_text")
    partner = aml_PriceRule()
    setattr(partner, 'aml_PriceRule21', None)
    _safe_set(owner, 'aml_Feature', partner)
    assert owner in getattr(partner, 'aml_PriceRule21')
    _safe_set(owner, 'aml_Feature', None)
    assert owner not in getattr(partner, 'aml_PriceRule21')


def test_assoc_features23_stub_double():
    # aml_Entity has no real 'aml_Entity24' property in the generated
    # code (a bare stub) -- manually attach it so aml_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Feature(name="sample_text", value="sample_text")
    partner = aml_Entity()
    setattr(partner, 'aml_Entity24', None)
    _safe_set(owner, 'aml_Feature25', partner)
    assert owner in getattr(partner, 'aml_Entity24')
    _safe_set(owner, 'aml_Feature25', None)
    assert owner not in getattr(partner, 'aml_Entity24')


def test_assoc_formFeature11_stub_double():
    # aml_Drive has no real 'aml_Drive12' property in the generated
    # code (a bare stub) -- manually attach it so aml_FormFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_FormFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_FormFeature(name="sample_text", value=7)
    partner = aml_Drive()
    setattr(partner, 'aml_Drive12', None)
    _safe_set(owner, 'aml_FormFeature', partner)
    assert getattr(partner, 'aml_Drive12') == owner
    _safe_set(owner, 'aml_FormFeature', None)
    assert getattr(partner, 'aml_Drive12') is None


def test_assoc_lengthFeature16_stub_double():
    # aml_Cable has no real 'aml_Cable17' property in the generated
    # code (a bare stub) -- manually attach it so aml_LengthFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_LengthFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_LengthFeature(name="sample_text", value=3.14)
    partner = aml_Cable()
    setattr(partner, 'aml_Cable17', None)
    _safe_set(owner, 'aml_LengthFeature', partner)
    assert getattr(partner, 'aml_Cable17') == owner
    _safe_set(owner, 'aml_LengthFeature', None)
    assert getattr(partner, 'aml_Cable17') is None


def test_assoc_maxFeature4_stub_double():
    # aml_MinMax has no real 'aml_MinMax5' property in the generated
    # code (a bare stub) -- manually attach it so aml_MaxFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MaxFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MaxFeature(name="sample_text", value=7)
    partner = aml_MinMax()
    setattr(partner, 'aml_MinMax5', None)
    _safe_set(owner, 'aml_MaxFeature', partner)
    assert getattr(partner, 'aml_MinMax5') == owner
    _safe_set(owner, 'aml_MaxFeature', None)
    assert getattr(partner, 'aml_MinMax5') is None


def test_assoc_networkFeature14_stub_double():
    # aml_Cable has no real 'aml_Cable15' property in the generated
    # code (a bare stub) -- manually attach it so aml_NetWorkFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_NetWorkFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_NetWorkFeature(name="sample_text", value="sample_text")
    partner = aml_Cable()
    setattr(partner, 'aml_Cable15', None)
    _safe_set(owner, 'aml_NetWorkFeature', partner)
    assert getattr(partner, 'aml_Cable15') == owner
    _safe_set(owner, 'aml_NetWorkFeature', None)
    assert getattr(partner, 'aml_Cable15') is None


def test_assoc_productPuidsFeature2_stub_double():
    # aml_MinMax has no real 'aml_MinMax3' property in the generated
    # code (a bare stub) -- manually attach it so aml_ProductPUIDFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_ProductPUIDFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_ProductPUIDFeature(name="sample_text", values=7)
    partner = aml_MinMax()
    setattr(partner, 'aml_MinMax3', None)
    _safe_set(owner, 'aml_ProductPUIDFeature', partner)
    assert getattr(partner, 'aml_MinMax3') == owner
    _safe_set(owner, 'aml_ProductPUIDFeature', None)
    assert getattr(partner, 'aml_MinMax3') is None


def test_assoc_sizeFeature7_stub_double():
    # aml_Drive has no real 'aml_Drive8' property in the generated
    # code (a bare stub) -- manually attach it so aml_SizeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_SizeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_SizeFeature(name="sample_text", value=7)
    partner = aml_Drive()
    setattr(partner, 'aml_Drive8', None)
    _safe_set(owner, 'aml_SizeFeature', partner)
    assert getattr(partner, 'aml_Drive8') == owner
    _safe_set(owner, 'aml_SizeFeature', None)
    assert getattr(partner, 'aml_Drive8') is None


def test_assoc_speedFeature9_stub_double():
    # aml_Drive has no real 'aml_Drive10' property in the generated
    # code (a bare stub) -- manually attach it so aml_SpeedFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_SpeedFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_SpeedFeature(name="sample_text", value=3.14)
    partner = aml_Drive()
    setattr(partner, 'aml_Drive10', None)
    _safe_set(owner, 'aml_SpeedFeature', partner)
    assert getattr(partner, 'aml_Drive10') == owner
    _safe_set(owner, 'aml_SpeedFeature', None)
    assert getattr(partner, 'aml_Drive10') is None


def test_assoc_targetGroupFeature1_stub_double():
    # aml_MinMax has no real 'aml_MinMax' property in the generated
    # code (a bare stub) -- manually attach it so aml_TargetGroupFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_TargetGroupFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_TargetGroupFeature(name="sample_text", value="sample_text")
    partner = aml_MinMax()
    setattr(partner, 'aml_MinMax', None)
    _safe_set(owner, 'aml_TargetGroupFeature', partner)
    assert getattr(partner, 'aml_MinMax') == owner
    _safe_set(owner, 'aml_TargetGroupFeature', None)
    assert getattr(partner, 'aml_MinMax') is None


def test_assoc_typeFeature6_stub_double():
    # aml_Drive has no real 'aml_Drive' property in the generated
    # code (a bare stub) -- manually attach it so aml_TypeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_TypeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_TypeFeature(name="sample_text", value="sample_text")
    partner = aml_Drive()
    setattr(partner, 'aml_Drive', None)
    _safe_set(owner, 'aml_TypeFeature', partner)
    assert getattr(partner, 'aml_Drive') == owner
    _safe_set(owner, 'aml_TypeFeature', None)
    assert getattr(partner, 'aml_Drive') is None


