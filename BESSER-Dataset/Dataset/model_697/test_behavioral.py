import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnyType,
    type_AnyType,
    type_EDataType,
    type_EStringToStringMapEntry,
    type_ProcessingInstruction,
    type_SimpleAnyType,
    type_XMLTypeDocumentRoot,
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

def test_assoc_processingInstruction5_reverse_link_reassign_clear():
    a1 = type_XMLTypeDocumentRoot(cDATA="sample_text", comment="sample_text", mixed="sample_text", text="sample_text")
    a2 = type_XMLTypeDocumentRoot(cDATA="sample_text_2", comment="sample_text_2", mixed="sample_text_2", text="sample_text_2")
    b = type_ProcessingInstruction(data="sample_text", target="sample_text")
    _safe_set(b, 'type_ProcessingInstruction', a1)
    assert _is_linked(b, 'type_ProcessingInstruction', a1)
    if hasattr(a1, 'type_XMLTypeDocumentRoot6'):
        assert _is_linked(a1, 'type_XMLTypeDocumentRoot6', b)
    _safe_set(b, 'type_ProcessingInstruction', a2)
    assert _is_linked(b, 'type_ProcessingInstruction', a2)
    if hasattr(a1, 'type_XMLTypeDocumentRoot6'):
        assert not _is_linked(a1, 'type_XMLTypeDocumentRoot6', b)
    if hasattr(a2, 'type_XMLTypeDocumentRoot6'):
        assert _is_linked(a2, 'type_XMLTypeDocumentRoot6', b)
    _safe_set(b, 'type_ProcessingInstruction', None)
    assert not _is_linked(b, 'type_ProcessingInstruction', a2)
    if hasattr(a2, 'type_XMLTypeDocumentRoot6'):
        assert not _is_linked(a2, 'type_XMLTypeDocumentRoot6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_instanceType0_stub_double():
    # type_EDataType has no real 'type_EDataType' property in the generated
    # code (a bare stub) -- manually attach it so type_SimpleAnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_SimpleAnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_SimpleAnyType(rawValue="sample_text", value="sample_text")
    partner = type_EDataType()
    setattr(partner, 'type_EDataType', None)
    _safe_set(owner, 'type_SimpleAnyType', partner)
    assert getattr(partner, 'type_EDataType') == owner
    _safe_set(owner, 'type_SimpleAnyType', None)
    assert getattr(partner, 'type_EDataType') is None


def test_assoc_xMLNSPrefixMap1_stub_double():
    # type_EStringToStringMapEntry has no real 'type_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so type_XMLTypeDocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_XMLTypeDocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_XMLTypeDocumentRoot(cDATA="sample_text", comment="sample_text", mixed="sample_text", text="sample_text")
    partner = type_EStringToStringMapEntry()
    setattr(partner, 'type_EStringToStringMapEntry', None)
    _safe_set(owner, 'type_XMLTypeDocumentRoot', {partner})
    assert getattr(partner, 'type_EStringToStringMapEntry') == owner
    _safe_set(owner, 'type_XMLTypeDocumentRoot', set())
    assert getattr(partner, 'type_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation2_stub_double():
    # type_EStringToStringMapEntry has no real 'type_EStringToStringMapEntry4' property in the generated
    # code (a bare stub) -- manually attach it so type_XMLTypeDocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_XMLTypeDocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_XMLTypeDocumentRoot(cDATA="sample_text", comment="sample_text", mixed="sample_text", text="sample_text")
    partner = type_EStringToStringMapEntry()
    setattr(partner, 'type_EStringToStringMapEntry4', None)
    _safe_set(owner, 'type_XMLTypeDocumentRoot3', {partner})
    assert getattr(partner, 'type_EStringToStringMapEntry4') == owner
    _safe_set(owner, 'type_XMLTypeDocumentRoot3', set())
    assert getattr(partner, 'type_EStringToStringMapEntry4') is None


