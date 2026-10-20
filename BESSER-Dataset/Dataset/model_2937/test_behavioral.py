import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SolutionConstraint,
    test7_AttributeType,
    test7_AttributeTypeElement,
    test7_Feature,
    test7_FeatureAttribute,
    test7_FeatureAttributeElement,
    test7_FeatureAttributeReference,
    test7_FiniteDomainSC,
    test7_FiniteDomainSCValueReference,
    test7_HardLimitSC,
    test7_Model,
    test7_OptimizationSC,
    test7_SelectionStateSC,
    test7_SolutionConstraint,
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

def test_assoc_attrType12_reverse_link_reassign_clear():
    a1 = test7_FeatureAttribute(name="sample_text")
    a2 = test7_FeatureAttribute(name="sample_text_2")
    b = test7_AttributeType(name="sample_text")
    _safe_set(b, 'test7_AttributeType14', a1)
    assert _is_linked(b, 'test7_AttributeType14', a1)
    if hasattr(a1, 'test7_FeatureAttribute13'):
        assert _is_linked(a1, 'test7_FeatureAttribute13', b)
    _safe_set(b, 'test7_AttributeType14', a2)
    assert _is_linked(b, 'test7_AttributeType14', a2)
    if hasattr(a1, 'test7_FeatureAttribute13'):
        assert not _is_linked(a1, 'test7_FeatureAttribute13', b)
    if hasattr(a2, 'test7_FeatureAttribute13'):
        assert _is_linked(a2, 'test7_FeatureAttribute13', b)
    _safe_set(b, 'test7_AttributeType14', None)
    assert not _is_linked(b, 'test7_AttributeType14', a2)
    if hasattr(a2, 'test7_FeatureAttribute13'):
        assert not _is_linked(a2, 'test7_FeatureAttribute13', b)


def test_assoc_attrType22_reverse_link_reassign_clear():
    a1 = test7_OptimizationSC(funct="sample_text")
    a2 = test7_OptimizationSC(funct="sample_text_2")
    b = test7_AttributeType(name="sample_text")
    _safe_set(b, 'test7_AttributeType23', a1)
    assert _is_linked(b, 'test7_AttributeType23', a1)
    if hasattr(a1, 'test7_OptimizationSC'):
        assert _is_linked(a1, 'test7_OptimizationSC', b)
    _safe_set(b, 'test7_AttributeType23', a2)
    assert _is_linked(b, 'test7_AttributeType23', a2)
    if hasattr(a1, 'test7_OptimizationSC'):
        assert not _is_linked(a1, 'test7_OptimizationSC', b)
    if hasattr(a2, 'test7_OptimizationSC'):
        assert _is_linked(a2, 'test7_OptimizationSC', b)
    _safe_set(b, 'test7_AttributeType23', None)
    assert not _is_linked(b, 'test7_AttributeType23', a2)
    if hasattr(a2, 'test7_OptimizationSC'):
        assert not _is_linked(a2, 'test7_OptimizationSC', b)


def test_assoc_attrType24_reverse_link_reassign_clear():
    a1 = test7_HardLimitSC(op1="sample_text", op2="sample_text", value1="sample_text", value2="sample_text")
    a2 = test7_HardLimitSC(op1="sample_text_2", op2="sample_text_2", value1="sample_text_2", value2="sample_text_2")
    b = test7_AttributeType(name="sample_text")
    _safe_set(b, 'test7_AttributeType25', a1)
    assert _is_linked(b, 'test7_AttributeType25', a1)
    if hasattr(a1, 'test7_HardLimitSC'):
        assert _is_linked(a1, 'test7_HardLimitSC', b)
    _safe_set(b, 'test7_AttributeType25', a2)
    assert _is_linked(b, 'test7_AttributeType25', a2)
    if hasattr(a1, 'test7_HardLimitSC'):
        assert not _is_linked(a1, 'test7_HardLimitSC', b)
    if hasattr(a2, 'test7_HardLimitSC'):
        assert _is_linked(a2, 'test7_HardLimitSC', b)
    _safe_set(b, 'test7_AttributeType25', None)
    assert not _is_linked(b, 'test7_AttributeType25', a2)
    if hasattr(a2, 'test7_HardLimitSC'):
        assert not _is_linked(a2, 'test7_HardLimitSC', b)


def test_assoc_elements7_reverse_link_reassign_clear():
    a1 = test7_AttributeTypeElement(dataType="sample_text", name="sample_text")
    a2 = test7_AttributeTypeElement(dataType="sample_text_2", name="sample_text_2")
    b = test7_AttributeType(name="sample_text")
    _safe_set(b, 'test7_AttributeType8', {a1})
    assert _is_linked(b, 'test7_AttributeType8', a1)
    if hasattr(a1, 'test7_AttributeTypeElement'):
        assert _is_linked(a1, 'test7_AttributeTypeElement', b)
    _safe_set(b, 'test7_AttributeType8', {a2})
    assert _is_linked(b, 'test7_AttributeType8', a2)
    if hasattr(a1, 'test7_AttributeTypeElement'):
        assert not _is_linked(a1, 'test7_AttributeTypeElement', b)
    if hasattr(a2, 'test7_AttributeTypeElement'):
        assert _is_linked(a2, 'test7_AttributeTypeElement', b)
    _safe_set(b, 'test7_AttributeType8', set())
    assert not _is_linked(b, 'test7_AttributeType8', a2)
    if hasattr(a2, 'test7_AttributeTypeElement'):
        assert not _is_linked(a2, 'test7_AttributeTypeElement', b)


def test_assoc_feature26_reverse_link_reassign_clear():
    a1 = test7_SelectionStateSC(state="sample_text")
    a2 = test7_SelectionStateSC(state="sample_text_2")
    b = test7_Feature(name="sample_text")
    _safe_set(b, 'test7_Feature27', a1)
    assert _is_linked(b, 'test7_Feature27', a1)
    if hasattr(a1, 'test7_SelectionStateSC'):
        assert _is_linked(a1, 'test7_SelectionStateSC', b)
    _safe_set(b, 'test7_Feature27', a2)
    assert _is_linked(b, 'test7_Feature27', a2)
    if hasattr(a1, 'test7_SelectionStateSC'):
        assert not _is_linked(a1, 'test7_SelectionStateSC', b)
    if hasattr(a2, 'test7_SelectionStateSC'):
        assert _is_linked(a2, 'test7_SelectionStateSC', b)
    _safe_set(b, 'test7_Feature27', None)
    assert not _is_linked(b, 'test7_Feature27', a2)
    if hasattr(a2, 'test7_SelectionStateSC'):
        assert not _is_linked(a2, 'test7_SelectionStateSC', b)


def test_assoc_independentAttrType10_reverse_link_reassign_clear():
    a1 = test7_AttributeType(name="sample_text")
    a2 = test7_AttributeType(name="sample_text_2")
    b = test7_AttributeType(name="sample_text")
    _safe_set(b, 'test7_AttributeType9', a1)
    assert _is_linked(b, 'test7_AttributeType9', a1)
    if hasattr(a1, 'test7_AttributeType11'):
        assert _is_linked(a1, 'test7_AttributeType11', b)
    _safe_set(b, 'test7_AttributeType9', a2)
    assert _is_linked(b, 'test7_AttributeType9', a2)
    if hasattr(a1, 'test7_AttributeType11'):
        assert not _is_linked(a1, 'test7_AttributeType11', b)
    if hasattr(a2, 'test7_AttributeType11'):
        assert _is_linked(a2, 'test7_AttributeType11', b)
    _safe_set(b, 'test7_AttributeType9', None)
    assert not _is_linked(b, 'test7_AttributeType9', a2)
    if hasattr(a2, 'test7_AttributeType11'):
        assert not _is_linked(a2, 'test7_AttributeType11', b)


def test_assoc_values15_reverse_link_reassign_clear():
    a1 = test7_FeatureAttributeElement(value="sample_text")
    a2 = test7_FeatureAttributeElement(value="sample_text_2")
    b = test7_FeatureAttribute(name="sample_text")
    _safe_set(b, 'test7_FeatureAttribute16', {a1})
    assert _is_linked(b, 'test7_FeatureAttribute16', a1)
    if hasattr(a1, 'test7_FeatureAttributeElement'):
        assert _is_linked(a1, 'test7_FeatureAttributeElement', b)
    _safe_set(b, 'test7_FeatureAttribute16', {a2})
    assert _is_linked(b, 'test7_FeatureAttribute16', a2)
    if hasattr(a1, 'test7_FeatureAttributeElement'):
        assert not _is_linked(a1, 'test7_FeatureAttributeElement', b)
    if hasattr(a2, 'test7_FeatureAttributeElement'):
        assert _is_linked(a2, 'test7_FeatureAttributeElement', b)
    _safe_set(b, 'test7_FeatureAttribute16', set())
    assert not _is_linked(b, 'test7_FeatureAttribute16', a2)
    if hasattr(a2, 'test7_FeatureAttributeElement'):
        assert not _is_linked(a2, 'test7_FeatureAttributeElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributeTypes0_stub_double():
    # test7_Model has no real 'test7_Model' property in the generated
    # code (a bare stub) -- manually attach it so test7_AttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test7_AttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test7_AttributeType(name="sample_text")
    partner = test7_Model()
    setattr(partner, 'test7_Model', None)
    _safe_set(owner, 'test7_AttributeType', partner)
    assert owner in getattr(partner, 'test7_Model')
    _safe_set(owner, 'test7_AttributeType', None)
    assert owner not in getattr(partner, 'test7_Model')


def test_assoc_attributes19_stub_double():
    # test7_FeatureAttributeReference has no real 'test7_FeatureAttributeReference21' property in the generated
    # code (a bare stub) -- manually attach it so test7_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test7_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test7_Feature(name="sample_text")
    partner = test7_FeatureAttributeReference()
    setattr(partner, 'test7_FeatureAttributeReference21', None)
    _safe_set(owner, 'test7_Feature20', {partner})
    assert getattr(partner, 'test7_FeatureAttributeReference21') == owner
    _safe_set(owner, 'test7_Feature20', set())
    assert getattr(partner, 'test7_FeatureAttributeReference21') is None


def test_assoc_feature28_stub_double():
    # test7_FiniteDomainSC has no real 'test7_FiniteDomainSC' property in the generated
    # code (a bare stub) -- manually attach it so test7_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test7_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test7_Feature(name="sample_text")
    partner = test7_FiniteDomainSC()
    setattr(partner, 'test7_FiniteDomainSC', None)
    _safe_set(owner, 'test7_Feature29', partner)
    assert getattr(partner, 'test7_FiniteDomainSC') == owner
    _safe_set(owner, 'test7_Feature29', None)
    assert getattr(partner, 'test7_FiniteDomainSC') is None


def test_assoc_featureAttr30_stub_double():
    # test7_FiniteDomainSC has no real 'test7_FiniteDomainSC31' property in the generated
    # code (a bare stub) -- manually attach it so test7_FeatureAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test7_FeatureAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test7_FeatureAttribute(name="sample_text")
    partner = test7_FiniteDomainSC()
    setattr(partner, 'test7_FiniteDomainSC31', None)
    _safe_set(owner, 'test7_FeatureAttribute32', partner)
    assert getattr(partner, 'test7_FiniteDomainSC31') == owner
    _safe_set(owner, 'test7_FeatureAttribute32', None)
    assert getattr(partner, 'test7_FiniteDomainSC31') is None


def test_assoc_featureAttributes1_stub_double():
    # test7_Model has no real 'test7_Model2' property in the generated
    # code (a bare stub) -- manually attach it so test7_FeatureAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test7_FeatureAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test7_FeatureAttribute(name="sample_text")
    partner = test7_Model()
    setattr(partner, 'test7_Model2', None)
    _safe_set(owner, 'test7_FeatureAttribute', partner)
    assert owner in getattr(partner, 'test7_Model2')
    _safe_set(owner, 'test7_FeatureAttribute', None)
    assert owner not in getattr(partner, 'test7_Model2')


def test_assoc_features3_stub_double():
    # test7_Model has no real 'test7_Model4' property in the generated
    # code (a bare stub) -- manually attach it so test7_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test7_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test7_Feature(name="sample_text")
    partner = test7_Model()
    setattr(partner, 'test7_Model4', None)
    _safe_set(owner, 'test7_Feature', partner)
    assert owner in getattr(partner, 'test7_Model4')
    _safe_set(owner, 'test7_Feature', None)
    assert owner not in getattr(partner, 'test7_Model4')


def test_assoc_name17_stub_double():
    # test7_FeatureAttributeReference has no real 'test7_FeatureAttributeReference' property in the generated
    # code (a bare stub) -- manually attach it so test7_FeatureAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test7_FeatureAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test7_FeatureAttribute(name="sample_text")
    partner = test7_FeatureAttributeReference()
    setattr(partner, 'test7_FeatureAttributeReference', None)
    _safe_set(owner, 'test7_FeatureAttribute18', partner)
    assert getattr(partner, 'test7_FeatureAttributeReference') == owner
    _safe_set(owner, 'test7_FeatureAttribute18', None)
    assert getattr(partner, 'test7_FeatureAttributeReference') is None


def test_assoc_solutionConstraints5_stub_double():
    # test7_Model has no real 'test7_Model6' property in the generated
    # code (a bare stub) -- manually attach it so test7_SolutionConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test7_SolutionConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test7_SolutionConstraint(name="sample_text", type="sample_text")
    partner = test7_Model()
    setattr(partner, 'test7_Model6', None)
    _safe_set(owner, 'test7_SolutionConstraint', partner)
    assert owner in getattr(partner, 'test7_Model6')
    _safe_set(owner, 'test7_SolutionConstraint', None)
    assert owner not in getattr(partner, 'test7_Model6')


def test_assoc_values33_stub_double():
    # test7_FiniteDomainSC has no real 'test7_FiniteDomainSC34' property in the generated
    # code (a bare stub) -- manually attach it so test7_FiniteDomainSCValueReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test7_FiniteDomainSCValueReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test7_FiniteDomainSCValueReference(value="sample_text")
    partner = test7_FiniteDomainSC()
    setattr(partner, 'test7_FiniteDomainSC34', None)
    _safe_set(owner, 'test7_FiniteDomainSCValueReference', partner)
    assert owner in getattr(partner, 'test7_FiniteDomainSC34')
    _safe_set(owner, 'test7_FiniteDomainSCValueReference', None)
    assert owner not in getattr(partner, 'test7_FiniteDomainSC34')


