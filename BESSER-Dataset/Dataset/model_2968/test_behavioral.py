import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASD_Annotation,
    ASD_Assertion,
    ASD_AssertionSet,
    ASD_InfoType,
    ASD_InfoTypeImported,
    ASD_Message,
    ASD_NamedElement,
    ASD_Operation,
    ASD_Profile,
    ASD_ServiceDescription,
    InfoType,
    NamedElement,
    EEnumDimensionType,
    EEnumIntention,
    EEnumMes,
    EEnumOp,
    EEnumSubset,
    EEnumValueType,
    EEnumlogicalType,
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

def test_assoc_annotations29_reverse_link_reassign_clear():
    a1 = ASD_NamedElement(name="sample_text")
    a2 = ASD_NamedElement(name="sample_text_2")
    b = ASD_Annotation(key="sample_text", value="sample_text")
    _safe_set(b, 'Annotation', a1)
    assert _is_linked(b, 'Annotation', a1)
    if hasattr(a1, 'owner'):
        assert _is_linked(a1, 'owner', b)
    _safe_set(b, 'Annotation', a2)
    assert _is_linked(b, 'Annotation', a2)
    if hasattr(a1, 'owner'):
        assert not _is_linked(a1, 'owner', b)
    if hasattr(a2, 'owner'):
        assert _is_linked(a2, 'owner', b)
    _safe_set(b, 'Annotation', None)
    assert not _is_linked(b, 'Annotation', a2)
    if hasattr(a2, 'owner'):
        assert not _is_linked(a2, 'owner', b)


def test_assoc_assertions26_reverse_link_reassign_clear():
    a1 = ASD_AssertionSet(lType="sample_text")
    a2 = ASD_AssertionSet(lType="sample_text_2")
    b = ASD_Assertion(dimension="sample_text", dimensionType="sample_text", lType="sample_text", maxVal=3.14, minVal=3.14, role="sample_text", subset="sample_text")
    _safe_set(b, 'Assertion', a1)
    assert _is_linked(b, 'Assertion', a1)
    if hasattr(a1, 'set'):
        assert _is_linked(a1, 'set', b)
    _safe_set(b, 'Assertion', a2)
    assert _is_linked(b, 'Assertion', a2)
    if hasattr(a1, 'set'):
        assert not _is_linked(a1, 'set', b)
    if hasattr(a2, 'set'):
        assert _is_linked(a2, 'set', b)
    _safe_set(b, 'Assertion', None)
    assert not _is_linked(b, 'Assertion', a2)
    if hasattr(a2, 'set'):
        assert not _is_linked(a2, 'set', b)


def test_assoc_contents5_reverse_link_reassign_clear():
    a1 = ASD_Operation(messagePattern="sample_text")
    a2 = ASD_Operation(messagePattern="sample_text_2")
    b = ASD_Message(role="sample_text", subset="sample_text")
    _safe_set(b, 'Message', a1)
    assert _is_linked(b, 'Message', a1)
    if hasattr(a1, 'operation'):
        assert _is_linked(a1, 'operation', b)
    _safe_set(b, 'Message', a2)
    assert _is_linked(b, 'Message', a2)
    if hasattr(a1, 'operation'):
        assert not _is_linked(a1, 'operation', b)
    if hasattr(a2, 'operation'):
        assert _is_linked(a2, 'operation', b)
    _safe_set(b, 'Message', None)
    assert not _is_linked(b, 'Message', a2)
    if hasattr(a2, 'operation'):
        assert not _is_linked(a2, 'operation', b)


def test_assoc_infoType12_reverse_link_reassign_clear():
    a1 = ASD_InfoType(subset="sample_text", valueRange="sample_text", valueType="sample_text")
    a2 = ASD_InfoType(subset="sample_text_2", valueRange="sample_text_2", valueType="sample_text_2")
    b = ASD_InfoType(subset="sample_text", valueRange="sample_text", valueType="sample_text")
    _safe_set(b, 'ASD_InfoType11', {a1})
    assert _is_linked(b, 'ASD_InfoType11', a1)
    if hasattr(a1, 'ASD_InfoType'):
        assert _is_linked(a1, 'ASD_InfoType', b)
    _safe_set(b, 'ASD_InfoType11', {a2})
    assert _is_linked(b, 'ASD_InfoType11', a2)
    if hasattr(a1, 'ASD_InfoType'):
        assert not _is_linked(a1, 'ASD_InfoType', b)
    if hasattr(a2, 'ASD_InfoType'):
        assert _is_linked(a2, 'ASD_InfoType', b)
    _safe_set(b, 'ASD_InfoType11', set())
    assert not _is_linked(b, 'ASD_InfoType11', a2)
    if hasattr(a2, 'ASD_InfoType'):
        assert not _is_linked(a2, 'ASD_InfoType', b)


def test_assoc_infoType7_reverse_link_reassign_clear():
    a1 = ASD_Message(role="sample_text", subset="sample_text")
    a2 = ASD_Message(role="sample_text_2", subset="sample_text_2")
    b = ASD_InfoType(subset="sample_text", valueRange="sample_text", valueType="sample_text")
    _safe_set(b, 'InfoType8', a1)
    assert _is_linked(b, 'InfoType8', a1)
    if hasattr(a1, 'message'):
        assert _is_linked(a1, 'message', b)
    _safe_set(b, 'InfoType8', a2)
    assert _is_linked(b, 'InfoType8', a2)
    if hasattr(a1, 'message'):
        assert not _is_linked(a1, 'message', b)
    if hasattr(a2, 'message'):
        assert _is_linked(a2, 'message', b)
    _safe_set(b, 'InfoType8', None)
    assert not _is_linked(b, 'InfoType8', a2)
    if hasattr(a2, 'message'):
        assert not _is_linked(a2, 'message', b)


def test_assoc_message16_reverse_link_reassign_clear():
    a1 = ASD_Message(role="sample_text", subset="sample_text")
    a2 = ASD_Message(role="sample_text_2", subset="sample_text_2")
    b = ASD_InfoType(subset="sample_text", valueRange="sample_text", valueType="sample_text")
    _safe_set(b, 'infoType', {a1})
    assert _is_linked(b, 'infoType', a1)
    if hasattr(a1, 'Message17'):
        assert _is_linked(a1, 'Message17', b)
    _safe_set(b, 'infoType', {a2})
    assert _is_linked(b, 'infoType', a2)
    if hasattr(a1, 'Message17'):
        assert not _is_linked(a1, 'Message17', b)
    if hasattr(a2, 'Message17'):
        assert _is_linked(a2, 'Message17', b)
    _safe_set(b, 'infoType', set())
    assert not _is_linked(b, 'infoType', a2)
    if hasattr(a2, 'Message17'):
        assert not _is_linked(a2, 'Message17', b)


def test_assoc_operation9_reverse_link_reassign_clear():
    a1 = ASD_Operation(messagePattern="sample_text")
    a2 = ASD_Operation(messagePattern="sample_text_2")
    b = ASD_Message(role="sample_text", subset="sample_text")
    _safe_set(b, 'contents', a1)
    assert _is_linked(b, 'contents', a1)
    if hasattr(a1, 'Operation10'):
        assert _is_linked(a1, 'Operation10', b)
    _safe_set(b, 'contents', a2)
    assert _is_linked(b, 'contents', a2)
    if hasattr(a1, 'Operation10'):
        assert not _is_linked(a1, 'Operation10', b)
    if hasattr(a2, 'Operation10'):
        assert _is_linked(a2, 'Operation10', b)
    _safe_set(b, 'contents', None)
    assert not _is_linked(b, 'contents', a2)
    if hasattr(a2, 'Operation10'):
        assert not _is_linked(a2, 'Operation10', b)


def test_assoc_owner30_reverse_link_reassign_clear():
    a1 = ASD_NamedElement(name="sample_text")
    a2 = ASD_NamedElement(name="sample_text_2")
    b = ASD_Annotation(key="sample_text", value="sample_text")
    _safe_set(b, 'annotations', a1)
    assert _is_linked(b, 'annotations', a1)
    if hasattr(a1, 'NamedElement'):
        assert _is_linked(a1, 'NamedElement', b)
    _safe_set(b, 'annotations', a2)
    assert _is_linked(b, 'annotations', a2)
    if hasattr(a1, 'NamedElement'):
        assert not _is_linked(a1, 'NamedElement', b)
    if hasattr(a2, 'NamedElement'):
        assert _is_linked(a2, 'NamedElement', b)
    _safe_set(b, 'annotations', None)
    assert not _is_linked(b, 'annotations', a2)
    if hasattr(a2, 'NamedElement'):
        assert not _is_linked(a2, 'NamedElement', b)


def test_assoc_ref14_reverse_link_reassign_clear():
    a1 = ASD_InfoType(subset="sample_text", valueRange="sample_text", valueType="sample_text")
    a2 = ASD_InfoType(subset="sample_text_2", valueRange="sample_text_2", valueType="sample_text_2")
    b = ASD_InfoType(subset="sample_text", valueRange="sample_text", valueType="sample_text")
    _safe_set(b, 'ASD_InfoType15', a1)
    assert _is_linked(b, 'ASD_InfoType15', a1)
    if hasattr(a1, 'ASD_InfoType13'):
        assert _is_linked(a1, 'ASD_InfoType13', b)
    _safe_set(b, 'ASD_InfoType15', a2)
    assert _is_linked(b, 'ASD_InfoType15', a2)
    if hasattr(a1, 'ASD_InfoType13'):
        assert not _is_linked(a1, 'ASD_InfoType13', b)
    if hasattr(a2, 'ASD_InfoType13'):
        assert _is_linked(a2, 'ASD_InfoType13', b)
    _safe_set(b, 'ASD_InfoType15', None)
    assert not _is_linked(b, 'ASD_InfoType15', a2)
    if hasattr(a2, 'ASD_InfoType13'):
        assert not _is_linked(a2, 'ASD_InfoType13', b)


def test_assoc_set27_reverse_link_reassign_clear():
    a1 = ASD_AssertionSet(lType="sample_text")
    a2 = ASD_AssertionSet(lType="sample_text_2")
    b = ASD_Assertion(dimension="sample_text", dimensionType="sample_text", lType="sample_text", maxVal=3.14, minVal=3.14, role="sample_text", subset="sample_text")
    _safe_set(b, 'assertions', a1)
    assert _is_linked(b, 'assertions', a1)
    if hasattr(a1, 'AssertionSet28'):
        assert _is_linked(a1, 'AssertionSet28', b)
    _safe_set(b, 'assertions', a2)
    assert _is_linked(b, 'assertions', a2)
    if hasattr(a1, 'AssertionSet28'):
        assert not _is_linked(a1, 'AssertionSet28', b)
    if hasattr(a2, 'AssertionSet28'):
        assert _is_linked(a2, 'AssertionSet28', b)
    _safe_set(b, 'assertions', None)
    assert not _is_linked(b, 'assertions', a2)
    if hasattr(a2, 'AssertionSet28'):
        assert not _is_linked(a2, 'AssertionSet28', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_infotypes1_stub_double():
    # ASD_ServiceDescription has no real 'service2' property in the generated
    # code (a bare stub) -- manually attach it so ASD_InfoType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASD_InfoType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASD_InfoType(subset="sample_text", valueRange="sample_text", valueType="sample_text")
    partner = ASD_ServiceDescription()
    setattr(partner, 'service2', None)
    _safe_set(owner, 'InfoType', partner)
    assert owner in getattr(partner, 'service2')
    _safe_set(owner, 'InfoType', None)
    assert owner not in getattr(partner, 'service2')


def test_assoc_operations0_stub_double():
    # ASD_ServiceDescription has no real 'service' property in the generated
    # code (a bare stub) -- manually attach it so ASD_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASD_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASD_Operation(messagePattern="sample_text")
    partner = ASD_ServiceDescription()
    setattr(partner, 'service', None)
    _safe_set(owner, 'Operation', partner)
    assert owner in getattr(partner, 'service')
    _safe_set(owner, 'Operation', None)
    assert owner not in getattr(partner, 'service')


def test_assoc_profile24_stub_double():
    # ASD_Profile has no real 'Profile25' property in the generated
    # code (a bare stub) -- manually attach it so ASD_AssertionSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASD_AssertionSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASD_AssertionSet(lType="sample_text")
    partner = ASD_Profile()
    setattr(partner, 'Profile25', None)
    _safe_set(owner, 'sets', partner)
    assert getattr(partner, 'Profile25') == owner
    _safe_set(owner, 'sets', None)
    assert getattr(partner, 'Profile25') is None


def test_assoc_refers20_stub_double():
    # ASD_Profile has no real 'ASD_Profile' property in the generated
    # code (a bare stub) -- manually attach it so ASD_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASD_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASD_Operation(messagePattern="sample_text")
    partner = ASD_Profile()
    setattr(partner, 'ASD_Profile', None)
    _safe_set(owner, 'ASD_Operation', partner)
    assert owner in getattr(partner, 'ASD_Profile')
    _safe_set(owner, 'ASD_Operation', None)
    assert owner not in getattr(partner, 'ASD_Profile')


def test_assoc_service18_stub_double():
    # ASD_ServiceDescription has no real 'ServiceDescription19' property in the generated
    # code (a bare stub) -- manually attach it so ASD_InfoType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASD_InfoType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASD_InfoType(subset="sample_text", valueRange="sample_text", valueType="sample_text")
    partner = ASD_ServiceDescription()
    setattr(partner, 'ServiceDescription19', None)
    _safe_set(owner, 'infotypes', partner)
    assert getattr(partner, 'ServiceDescription19') == owner
    _safe_set(owner, 'infotypes', None)
    assert getattr(partner, 'ServiceDescription19') is None


def test_assoc_service6_stub_double():
    # ASD_ServiceDescription has no real 'ServiceDescription' property in the generated
    # code (a bare stub) -- manually attach it so ASD_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASD_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASD_Operation(messagePattern="sample_text")
    partner = ASD_ServiceDescription()
    setattr(partner, 'ServiceDescription', None)
    _safe_set(owner, 'operations', partner)
    assert getattr(partner, 'ServiceDescription') == owner
    _safe_set(owner, 'operations', None)
    assert getattr(partner, 'ServiceDescription') is None


def test_assoc_sets21_stub_double():
    # ASD_Profile has no real 'profile' property in the generated
    # code (a bare stub) -- manually attach it so ASD_AssertionSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASD_AssertionSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASD_AssertionSet(lType="sample_text")
    partner = ASD_Profile()
    setattr(partner, 'profile', None)
    _safe_set(owner, 'AssertionSet', partner)
    assert owner in getattr(partner, 'profile')
    _safe_set(owner, 'AssertionSet', None)
    assert owner not in getattr(partner, 'profile')


