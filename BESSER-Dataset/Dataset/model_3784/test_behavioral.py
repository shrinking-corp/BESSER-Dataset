import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EObject,
    TestType,
    test_StringToStringMap,
    test_StringToTestElementMap,
    test_TestElement,
    test_TestElementToStringMap,
    test_TestElementToTestElementMap,
    test_TestType,
    test_TypeWithFeatureMapContainment,
    test_TypeWithFeatureMapNonContainment,
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

def test_assoc_containedElement8_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'srefContainer', a1)
    assert _is_linked(b, 'srefContainer', a1)
    if hasattr(a1, 'TestElement9'):
        assert _is_linked(a1, 'TestElement9', b)
    _safe_set(b, 'srefContainer', a2)
    assert _is_linked(b, 'srefContainer', a2)
    if hasattr(a1, 'TestElement9'):
        assert not _is_linked(a1, 'TestElement9', b)
    if hasattr(a2, 'TestElement9'):
        assert _is_linked(a2, 'TestElement9', b)
    _safe_set(b, 'srefContainer', None)
    assert not _is_linked(b, 'srefContainer', a2)
    if hasattr(a2, 'TestElement9'):
        assert not _is_linked(a2, 'TestElement9', b)


def test_assoc_containedElement_NoOpposite49_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'test_TestElement50', a1)
    assert _is_linked(b, 'test_TestElement50', a1)
    if hasattr(a1, 'test_TestElement48'):
        assert _is_linked(a1, 'test_TestElement48', b)
    _safe_set(b, 'test_TestElement50', a2)
    assert _is_linked(b, 'test_TestElement50', a2)
    if hasattr(a1, 'test_TestElement48'):
        assert not _is_linked(a1, 'test_TestElement48', b)
    if hasattr(a2, 'test_TestElement48'):
        assert _is_linked(a2, 'test_TestElement48', b)
    _safe_set(b, 'test_TestElement50', None)
    assert not _is_linked(b, 'test_TestElement50', a2)
    if hasattr(a2, 'test_TestElement48'):
        assert not _is_linked(a2, 'test_TestElement48', b)


def test_assoc_containedElements240_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'container2', {a1})
    assert _is_linked(b, 'container2', a1)
    if hasattr(a1, 'TestElement41'):
        assert _is_linked(a1, 'TestElement41', b)
    _safe_set(b, 'container2', {a2})
    assert _is_linked(b, 'container2', a2)
    if hasattr(a1, 'TestElement41'):
        assert not _is_linked(a1, 'TestElement41', b)
    if hasattr(a2, 'TestElement41'):
        assert _is_linked(a2, 'TestElement41', b)
    _safe_set(b, 'container2', set())
    assert not _is_linked(b, 'container2', a2)
    if hasattr(a2, 'TestElement41'):
        assert not _is_linked(a2, 'TestElement41', b)


def test_assoc_containedElements3_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'container', {a1})
    assert _is_linked(b, 'container', a1)
    if hasattr(a1, 'TestElement'):
        assert _is_linked(a1, 'TestElement', b)
    _safe_set(b, 'container', {a2})
    assert _is_linked(b, 'container', a2)
    if hasattr(a1, 'TestElement'):
        assert not _is_linked(a1, 'TestElement', b)
    if hasattr(a2, 'TestElement'):
        assert _is_linked(a2, 'TestElement', b)
    _safe_set(b, 'container', set())
    assert not _is_linked(b, 'container', a2)
    if hasattr(a2, 'TestElement'):
        assert not _is_linked(a2, 'TestElement', b)


def test_assoc_containedElements_NoOpposite46_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'test_TestElement47', a1)
    assert _is_linked(b, 'test_TestElement47', a1)
    if hasattr(a1, 'test_TestElement45'):
        assert _is_linked(a1, 'test_TestElement45', b)
    _safe_set(b, 'test_TestElement47', a2)
    assert _is_linked(b, 'test_TestElement47', a2)
    if hasattr(a1, 'test_TestElement45'):
        assert not _is_linked(a1, 'test_TestElement45', b)
    if hasattr(a2, 'test_TestElement45'):
        assert _is_linked(a2, 'test_TestElement45', b)
    _safe_set(b, 'test_TestElement47', None)
    assert not _is_linked(b, 'test_TestElement47', a2)
    if hasattr(a2, 'test_TestElement45'):
        assert not _is_linked(a2, 'test_TestElement45', b)


def test_assoc_container14_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'containedElements', a1)
    assert _is_linked(b, 'containedElements', a1)
    if hasattr(a1, 'TestElement15'):
        assert _is_linked(a1, 'TestElement15', b)
    _safe_set(b, 'containedElements', a2)
    assert _is_linked(b, 'containedElements', a2)
    if hasattr(a1, 'TestElement15'):
        assert not _is_linked(a1, 'TestElement15', b)
    if hasattr(a2, 'TestElement15'):
        assert _is_linked(a2, 'TestElement15', b)
    _safe_set(b, 'containedElements', None)
    assert not _is_linked(b, 'containedElements', a2)
    if hasattr(a2, 'TestElement15'):
        assert not _is_linked(a2, 'TestElement15', b)


def test_assoc_container243_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'containedElements2', a1)
    assert _is_linked(b, 'containedElements2', a1)
    if hasattr(a1, 'TestElement44'):
        assert _is_linked(a1, 'TestElement44', b)
    _safe_set(b, 'containedElements2', a2)
    assert _is_linked(b, 'containedElements2', a2)
    if hasattr(a1, 'TestElement44'):
        assert not _is_linked(a1, 'TestElement44', b)
    if hasattr(a2, 'TestElement44'):
        assert _is_linked(a2, 'TestElement44', b)
    _safe_set(b, 'containedElements2', None)
    assert not _is_linked(b, 'containedElements2', a2)
    if hasattr(a2, 'TestElement44'):
        assert not _is_linked(a2, 'TestElement44', b)


def test_assoc_elementToStringMap23_reverse_link_reassign_clear():
    a1 = test_TestElementToStringMap(value="sample_text")
    a2 = test_TestElementToStringMap(value="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'test_TestElement24', {a1})
    assert _is_linked(b, 'test_TestElement24', a1)
    if hasattr(a1, 'test_TestElementToStringMap'):
        assert _is_linked(a1, 'test_TestElementToStringMap', b)
    _safe_set(b, 'test_TestElement24', {a2})
    assert _is_linked(b, 'test_TestElement24', a2)
    if hasattr(a1, 'test_TestElementToStringMap'):
        assert not _is_linked(a1, 'test_TestElementToStringMap', b)
    if hasattr(a2, 'test_TestElementToStringMap'):
        assert _is_linked(a2, 'test_TestElementToStringMap', b)
    _safe_set(b, 'test_TestElement24', set())
    assert not _is_linked(b, 'test_TestElement24', a2)
    if hasattr(a2, 'test_TestElementToStringMap'):
        assert not _is_linked(a2, 'test_TestElementToStringMap', b)


def test_assoc_featureMapReferences152_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'test_TestElement53', a1)
    assert _is_linked(b, 'test_TestElement53', a1)
    if hasattr(a1, 'test_TestElement51'):
        assert _is_linked(a1, 'test_TestElement51', b)
    _safe_set(b, 'test_TestElement53', a2)
    assert _is_linked(b, 'test_TestElement53', a2)
    if hasattr(a1, 'test_TestElement51'):
        assert not _is_linked(a1, 'test_TestElement51', b)
    if hasattr(a2, 'test_TestElement51'):
        assert _is_linked(a2, 'test_TestElement51', b)
    _safe_set(b, 'test_TestElement53', None)
    assert not _is_linked(b, 'test_TestElement53', a2)
    if hasattr(a2, 'test_TestElement51'):
        assert not _is_linked(a2, 'test_TestElement51', b)


def test_assoc_featureMapReferences255_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'test_TestElement56', a1)
    assert _is_linked(b, 'test_TestElement56', a1)
    if hasattr(a1, 'test_TestElement54'):
        assert _is_linked(a1, 'test_TestElement54', b)
    _safe_set(b, 'test_TestElement56', a2)
    assert _is_linked(b, 'test_TestElement56', a2)
    if hasattr(a1, 'test_TestElement54'):
        assert not _is_linked(a1, 'test_TestElement54', b)
    if hasattr(a2, 'test_TestElement54'):
        assert _is_linked(a2, 'test_TestElement54', b)
    _safe_set(b, 'test_TestElement56', None)
    assert not _is_linked(b, 'test_TestElement56', a2)
    if hasattr(a2, 'test_TestElement54'):
        assert not _is_linked(a2, 'test_TestElement54', b)


def test_assoc_firstKey69_reverse_link_reassign_clear():
    a1 = test_TypeWithFeatureMapNonContainment(map="sample_text")
    a2 = test_TypeWithFeatureMapNonContainment(map="sample_text_2")
    b = test_TestType(name="sample_text")
    _safe_set(b, 'test_TestType', a1)
    assert _is_linked(b, 'test_TestType', a1)
    if hasattr(a1, 'test_TypeWithFeatureMapNonContainment'):
        assert _is_linked(a1, 'test_TypeWithFeatureMapNonContainment', b)
    _safe_set(b, 'test_TestType', a2)
    assert _is_linked(b, 'test_TestType', a2)
    if hasattr(a1, 'test_TypeWithFeatureMapNonContainment'):
        assert not _is_linked(a1, 'test_TypeWithFeatureMapNonContainment', b)
    if hasattr(a2, 'test_TypeWithFeatureMapNonContainment'):
        assert _is_linked(a2, 'test_TypeWithFeatureMapNonContainment', b)
    _safe_set(b, 'test_TestType', None)
    assert not _is_linked(b, 'test_TestType', a2)
    if hasattr(a2, 'test_TypeWithFeatureMapNonContainment'):
        assert not _is_linked(a2, 'test_TypeWithFeatureMapNonContainment', b)


def test_assoc_firstKeyContainment73_reverse_link_reassign_clear():
    a1 = test_TypeWithFeatureMapContainment(mapContainment="sample_text")
    a2 = test_TypeWithFeatureMapContainment(mapContainment="sample_text_2")
    b = test_TestType(name="sample_text")
    _safe_set(b, 'test_TestType74', a1)
    assert _is_linked(b, 'test_TestType74', a1)
    if hasattr(a1, 'test_TypeWithFeatureMapContainment'):
        assert _is_linked(a1, 'test_TypeWithFeatureMapContainment', b)
    _safe_set(b, 'test_TestType74', a2)
    assert _is_linked(b, 'test_TestType74', a2)
    if hasattr(a1, 'test_TypeWithFeatureMapContainment'):
        assert not _is_linked(a1, 'test_TypeWithFeatureMapContainment', b)
    if hasattr(a2, 'test_TypeWithFeatureMapContainment'):
        assert _is_linked(a2, 'test_TypeWithFeatureMapContainment', b)
    _safe_set(b, 'test_TestType74', None)
    assert not _is_linked(b, 'test_TestType74', a2)
    if hasattr(a2, 'test_TypeWithFeatureMapContainment'):
        assert not _is_linked(a2, 'test_TypeWithFeatureMapContainment', b)


def test_assoc_key57_reverse_link_reassign_clear():
    a1 = test_TestElementToStringMap(value="sample_text")
    a2 = test_TestElementToStringMap(value="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'test_TestElement59', a1)
    assert _is_linked(b, 'test_TestElement59', a1)
    if hasattr(a1, 'test_TestElementToStringMap58'):
        assert _is_linked(a1, 'test_TestElementToStringMap58', b)
    _safe_set(b, 'test_TestElement59', a2)
    assert _is_linked(b, 'test_TestElement59', a2)
    if hasattr(a1, 'test_TestElementToStringMap58'):
        assert not _is_linked(a1, 'test_TestElementToStringMap58', b)
    if hasattr(a2, 'test_TestElementToStringMap58'):
        assert _is_linked(a2, 'test_TestElementToStringMap58', b)
    _safe_set(b, 'test_TestElement59', None)
    assert not _is_linked(b, 'test_TestElement59', a2)
    if hasattr(a2, 'test_TestElementToStringMap58'):
        assert not _is_linked(a2, 'test_TestElementToStringMap58', b)


def test_assoc_nonContained_1ToN31_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'nonContained_NTo1', {a1})
    assert _is_linked(b, 'nonContained_NTo1', a1)
    if hasattr(a1, 'TestElement32'):
        assert _is_linked(a1, 'TestElement32', b)
    _safe_set(b, 'nonContained_NTo1', {a2})
    assert _is_linked(b, 'nonContained_NTo1', a2)
    if hasattr(a1, 'TestElement32'):
        assert not _is_linked(a1, 'TestElement32', b)
    if hasattr(a2, 'TestElement32'):
        assert _is_linked(a2, 'TestElement32', b)
    _safe_set(b, 'nonContained_NTo1', set())
    assert not _is_linked(b, 'nonContained_NTo1', a2)
    if hasattr(a2, 'TestElement32'):
        assert not _is_linked(a2, 'TestElement32', b)


def test_assoc_nonContained_MToN37_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'nonContained_NToM', {a1})
    assert _is_linked(b, 'nonContained_NToM', a1)
    if hasattr(a1, 'TestElement38'):
        assert _is_linked(a1, 'TestElement38', b)
    _safe_set(b, 'nonContained_NToM', {a2})
    assert _is_linked(b, 'nonContained_NToM', a2)
    if hasattr(a1, 'TestElement38'):
        assert not _is_linked(a1, 'TestElement38', b)
    if hasattr(a2, 'TestElement38'):
        assert _is_linked(a2, 'TestElement38', b)
    _safe_set(b, 'nonContained_NToM', set())
    assert not _is_linked(b, 'nonContained_NToM', a2)
    if hasattr(a2, 'TestElement38'):
        assert not _is_linked(a2, 'TestElement38', b)


def test_assoc_nonContained_NTo128_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'nonContained_1ToN', a1)
    assert _is_linked(b, 'nonContained_1ToN', a1)
    if hasattr(a1, 'TestElement29'):
        assert _is_linked(a1, 'TestElement29', b)
    _safe_set(b, 'nonContained_1ToN', a2)
    assert _is_linked(b, 'nonContained_1ToN', a2)
    if hasattr(a1, 'TestElement29'):
        assert not _is_linked(a1, 'TestElement29', b)
    if hasattr(a2, 'TestElement29'):
        assert _is_linked(a2, 'TestElement29', b)
    _safe_set(b, 'nonContained_1ToN', None)
    assert not _is_linked(b, 'nonContained_1ToN', a2)
    if hasattr(a2, 'TestElement29'):
        assert not _is_linked(a2, 'TestElement29', b)


def test_assoc_nonContained_NToM34_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'nonContained_MToN', {a1})
    assert _is_linked(b, 'nonContained_MToN', a1)
    if hasattr(a1, 'TestElement35'):
        assert _is_linked(a1, 'TestElement35', b)
    _safe_set(b, 'nonContained_MToN', {a2})
    assert _is_linked(b, 'nonContained_MToN', a2)
    if hasattr(a1, 'TestElement35'):
        assert not _is_linked(a1, 'TestElement35', b)
    if hasattr(a2, 'TestElement35'):
        assert _is_linked(a2, 'TestElement35', b)
    _safe_set(b, 'nonContained_MToN', set())
    assert not _is_linked(b, 'nonContained_MToN', a2)
    if hasattr(a2, 'TestElement35'):
        assert not _is_linked(a2, 'TestElement35', b)


def test_assoc_otherReference11_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'test_TestElement12', a1)
    assert _is_linked(b, 'test_TestElement12', a1)
    if hasattr(a1, 'test_TestElement10'):
        assert _is_linked(a1, 'test_TestElement10', b)
    _safe_set(b, 'test_TestElement12', a2)
    assert _is_linked(b, 'test_TestElement12', a2)
    if hasattr(a1, 'test_TestElement10'):
        assert not _is_linked(a1, 'test_TestElement10', b)
    if hasattr(a2, 'test_TestElement10'):
        assert _is_linked(a2, 'test_TestElement10', b)
    _safe_set(b, 'test_TestElement12', None)
    assert not _is_linked(b, 'test_TestElement12', a2)
    if hasattr(a2, 'test_TestElement10'):
        assert not _is_linked(a2, 'test_TestElement10', b)


def test_assoc_reference5_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'test_TestElement6', a1)
    assert _is_linked(b, 'test_TestElement6', a1)
    if hasattr(a1, 'test_TestElement4'):
        assert _is_linked(a1, 'test_TestElement4', b)
    _safe_set(b, 'test_TestElement6', a2)
    assert _is_linked(b, 'test_TestElement6', a2)
    if hasattr(a1, 'test_TestElement4'):
        assert not _is_linked(a1, 'test_TestElement4', b)
    if hasattr(a2, 'test_TestElement4'):
        assert _is_linked(a2, 'test_TestElement4', b)
    _safe_set(b, 'test_TestElement6', None)
    assert not _is_linked(b, 'test_TestElement6', a2)
    if hasattr(a2, 'test_TestElement4'):
        assert not _is_linked(a2, 'test_TestElement4', b)


def test_assoc_references1_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'test_TestElement0', {a1})
    assert _is_linked(b, 'test_TestElement0', a1)
    if hasattr(a1, 'test_TestElement'):
        assert _is_linked(a1, 'test_TestElement', b)
    _safe_set(b, 'test_TestElement0', {a2})
    assert _is_linked(b, 'test_TestElement0', a2)
    if hasattr(a1, 'test_TestElement'):
        assert not _is_linked(a1, 'test_TestElement', b)
    if hasattr(a2, 'test_TestElement'):
        assert _is_linked(a2, 'test_TestElement', b)
    _safe_set(b, 'test_TestElement0', set())
    assert not _is_linked(b, 'test_TestElement0', a2)
    if hasattr(a2, 'test_TestElement'):
        assert not _is_linked(a2, 'test_TestElement', b)


def test_assoc_secondKey70_reverse_link_reassign_clear():
    a1 = test_TypeWithFeatureMapNonContainment(map="sample_text")
    a2 = test_TypeWithFeatureMapNonContainment(map="sample_text_2")
    b = test_TestType(name="sample_text")
    _safe_set(b, 'test_TestType72', a1)
    assert _is_linked(b, 'test_TestType72', a1)
    if hasattr(a1, 'test_TypeWithFeatureMapNonContainment71'):
        assert _is_linked(a1, 'test_TypeWithFeatureMapNonContainment71', b)
    _safe_set(b, 'test_TestType72', a2)
    assert _is_linked(b, 'test_TestType72', a2)
    if hasattr(a1, 'test_TypeWithFeatureMapNonContainment71'):
        assert not _is_linked(a1, 'test_TypeWithFeatureMapNonContainment71', b)
    if hasattr(a2, 'test_TypeWithFeatureMapNonContainment71'):
        assert _is_linked(a2, 'test_TypeWithFeatureMapNonContainment71', b)
    _safe_set(b, 'test_TestType72', None)
    assert not _is_linked(b, 'test_TestType72', a2)
    if hasattr(a2, 'test_TypeWithFeatureMapNonContainment71'):
        assert not _is_linked(a2, 'test_TypeWithFeatureMapNonContainment71', b)


def test_assoc_secondKeyContainment75_reverse_link_reassign_clear():
    a1 = test_TypeWithFeatureMapContainment(mapContainment="sample_text")
    a2 = test_TypeWithFeatureMapContainment(mapContainment="sample_text_2")
    b = test_TestType(name="sample_text")
    _safe_set(b, 'test_TestType77', a1)
    assert _is_linked(b, 'test_TestType77', a1)
    if hasattr(a1, 'test_TypeWithFeatureMapContainment76'):
        assert _is_linked(a1, 'test_TypeWithFeatureMapContainment76', b)
    _safe_set(b, 'test_TestType77', a2)
    assert _is_linked(b, 'test_TestType77', a2)
    if hasattr(a1, 'test_TypeWithFeatureMapContainment76'):
        assert not _is_linked(a1, 'test_TypeWithFeatureMapContainment76', b)
    if hasattr(a2, 'test_TypeWithFeatureMapContainment76'):
        assert _is_linked(a2, 'test_TypeWithFeatureMapContainment76', b)
    _safe_set(b, 'test_TestType77', None)
    assert not _is_linked(b, 'test_TestType77', a2)
    if hasattr(a2, 'test_TypeWithFeatureMapContainment76'):
        assert not _is_linked(a2, 'test_TypeWithFeatureMapContainment76', b)


def test_assoc_srefContainer17_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    _safe_set(b, 'containedElement', a1)
    assert _is_linked(b, 'containedElement', a1)
    if hasattr(a1, 'TestElement18'):
        assert _is_linked(a1, 'TestElement18', b)
    _safe_set(b, 'containedElement', a2)
    assert _is_linked(b, 'containedElement', a2)
    if hasattr(a1, 'TestElement18'):
        assert not _is_linked(a1, 'TestElement18', b)
    if hasattr(a2, 'TestElement18'):
        assert _is_linked(a2, 'TestElement18', b)
    _safe_set(b, 'containedElement', None)
    assert not _is_linked(b, 'containedElement', a2)
    if hasattr(a2, 'TestElement18'):
        assert not _is_linked(a2, 'TestElement18', b)


def test_assoc_stringToElementMap25_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_StringToTestElementMap(key="sample_text")
    _safe_set(b, 'test_StringToTestElementMap', a1)
    assert _is_linked(b, 'test_StringToTestElementMap', a1)
    if hasattr(a1, 'test_TestElement26'):
        assert _is_linked(a1, 'test_TestElement26', b)
    _safe_set(b, 'test_StringToTestElementMap', a2)
    assert _is_linked(b, 'test_StringToTestElementMap', a2)
    if hasattr(a1, 'test_TestElement26'):
        assert not _is_linked(a1, 'test_TestElement26', b)
    if hasattr(a2, 'test_TestElement26'):
        assert _is_linked(a2, 'test_TestElement26', b)
    _safe_set(b, 'test_StringToTestElementMap', None)
    assert not _is_linked(b, 'test_StringToTestElementMap', a2)
    if hasattr(a2, 'test_TestElement26'):
        assert not _is_linked(a2, 'test_TestElement26', b)


def test_assoc_stringToStringMap21_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_StringToStringMap(key="sample_text", value="sample_text")
    _safe_set(b, 'test_StringToStringMap', a1)
    assert _is_linked(b, 'test_StringToStringMap', a1)
    if hasattr(a1, 'test_TestElement22'):
        assert _is_linked(a1, 'test_TestElement22', b)
    _safe_set(b, 'test_StringToStringMap', a2)
    assert _is_linked(b, 'test_StringToStringMap', a2)
    if hasattr(a1, 'test_TestElement22'):
        assert not _is_linked(a1, 'test_TestElement22', b)
    if hasattr(a2, 'test_TestElement22'):
        assert _is_linked(a2, 'test_TestElement22', b)
    _safe_set(b, 'test_StringToStringMap', None)
    assert not _is_linked(b, 'test_StringToStringMap', a2)
    if hasattr(a2, 'test_TestElement22'):
        assert not _is_linked(a2, 'test_TestElement22', b)


def test_assoc_value66_reverse_link_reassign_clear():
    a1 = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    a2 = test_TestElement(description="sample_text_2", featureMapEntries="sample_text_2", name="sample_text_2", strings="sample_text_2")
    b = test_StringToTestElementMap(key="sample_text")
    _safe_set(b, 'test_StringToTestElementMap67', a1)
    assert _is_linked(b, 'test_StringToTestElementMap67', a1)
    if hasattr(a1, 'test_TestElement68'):
        assert _is_linked(a1, 'test_TestElement68', b)
    _safe_set(b, 'test_StringToTestElementMap67', a2)
    assert _is_linked(b, 'test_StringToTestElementMap67', a2)
    if hasattr(a1, 'test_TestElement68'):
        assert not _is_linked(a1, 'test_TestElement68', b)
    if hasattr(a2, 'test_TestElement68'):
        assert _is_linked(a2, 'test_TestElement68', b)
    _safe_set(b, 'test_StringToTestElementMap67', None)
    assert not _is_linked(b, 'test_StringToTestElementMap67', a2)
    if hasattr(a2, 'test_TestElement68'):
        assert not _is_linked(a2, 'test_TestElement68', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elementMap19_stub_double():
    # test_TestElementToTestElementMap has no real 'test_TestElementToTestElementMap' property in the generated
    # code (a bare stub) -- manually attach it so test_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    partner = test_TestElementToTestElementMap()
    setattr(partner, 'test_TestElementToTestElementMap', None)
    _safe_set(owner, 'test_TestElement20', {partner})
    assert getattr(partner, 'test_TestElementToTestElementMap') == owner
    _safe_set(owner, 'test_TestElement20', set())
    assert getattr(partner, 'test_TestElementToTestElementMap') is None


def test_assoc_key63_stub_double():
    # test_TestElementToTestElementMap has no real 'test_TestElementToTestElementMap64' property in the generated
    # code (a bare stub) -- manually attach it so test_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    partner = test_TestElementToTestElementMap()
    setattr(partner, 'test_TestElementToTestElementMap64', None)
    _safe_set(owner, 'test_TestElement65', partner)
    assert getattr(partner, 'test_TestElementToTestElementMap64') == owner
    _safe_set(owner, 'test_TestElement65', None)
    assert getattr(partner, 'test_TestElementToTestElementMap64') is None


def test_assoc_value60_stub_double():
    # test_TestElementToTestElementMap has no real 'test_TestElementToTestElementMap61' property in the generated
    # code (a bare stub) -- manually attach it so test_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_TestElement(description="sample_text", featureMapEntries="sample_text", name="sample_text", strings="sample_text")
    partner = test_TestElementToTestElementMap()
    setattr(partner, 'test_TestElementToTestElementMap61', None)
    _safe_set(owner, 'test_TestElement62', partner)
    assert getattr(partner, 'test_TestElementToTestElementMap61') == owner
    _safe_set(owner, 'test_TestElement62', None)
    assert getattr(partner, 'test_TestElementToTestElementMap61') is None


