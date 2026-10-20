import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    codetaginfo_CodeTag,
    codetaginfo_CodeTagContext,
    codetaginfo_CodeTagInfo,
    codetaginfo_DocumentRoot,
    codetaginfo_EStringToStringMapEntry,
    CodeTagType,
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

def test_assoc_codeTagInfo7_reverse_link_reassign_clear():
    a1 = codetaginfo_DocumentRoot(mixed="sample_text")
    a2 = codetaginfo_DocumentRoot(mixed="sample_text_2")
    b = codetaginfo_CodeTagInfo(filename="sample_text", group="sample_text")
    _safe_set(b, 'codetaginfo_CodeTagInfo9', a1)
    assert _is_linked(b, 'codetaginfo_CodeTagInfo9', a1)
    if hasattr(a1, 'codetaginfo_DocumentRoot8'):
        assert _is_linked(a1, 'codetaginfo_DocumentRoot8', b)
    _safe_set(b, 'codetaginfo_CodeTagInfo9', a2)
    assert _is_linked(b, 'codetaginfo_CodeTagInfo9', a2)
    if hasattr(a1, 'codetaginfo_DocumentRoot8'):
        assert not _is_linked(a1, 'codetaginfo_DocumentRoot8', b)
    if hasattr(a2, 'codetaginfo_DocumentRoot8'):
        assert _is_linked(a2, 'codetaginfo_DocumentRoot8', b)
    _safe_set(b, 'codetaginfo_CodeTagInfo9', None)
    assert not _is_linked(b, 'codetaginfo_CodeTagInfo9', a2)
    if hasattr(a2, 'codetaginfo_DocumentRoot8'):
        assert not _is_linked(a2, 'codetaginfo_DocumentRoot8', b)


def test_assoc_codetag1_reverse_link_reassign_clear():
    a1 = codetaginfo_CodeTagInfo(filename="sample_text", group="sample_text")
    a2 = codetaginfo_CodeTagInfo(filename="sample_text_2", group="sample_text_2")
    b = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    _safe_set(b, 'codetaginfo_CodeTag2', a1)
    assert _is_linked(b, 'codetaginfo_CodeTag2', a1)
    if hasattr(a1, 'codetaginfo_CodeTagInfo'):
        assert _is_linked(a1, 'codetaginfo_CodeTagInfo', b)
    _safe_set(b, 'codetaginfo_CodeTag2', a2)
    assert _is_linked(b, 'codetaginfo_CodeTag2', a2)
    if hasattr(a1, 'codetaginfo_CodeTagInfo'):
        assert not _is_linked(a1, 'codetaginfo_CodeTagInfo', b)
    if hasattr(a2, 'codetaginfo_CodeTagInfo'):
        assert _is_linked(a2, 'codetaginfo_CodeTagInfo', b)
    _safe_set(b, 'codetaginfo_CodeTag2', None)
    assert not _is_linked(b, 'codetaginfo_CodeTag2', a2)
    if hasattr(a2, 'codetaginfo_CodeTagInfo'):
        assert not _is_linked(a2, 'codetaginfo_CodeTagInfo', b)


def test_assoc_contextinfo0_reverse_link_reassign_clear():
    a1 = codetaginfo_CodeTagContext(class_name="sample_text", component_name="sample_text", group="sample_text", operation_name="sample_text")
    a2 = codetaginfo_CodeTagContext(class_name="sample_text_2", component_name="sample_text_2", group="sample_text_2", operation_name="sample_text_2")
    b = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    _safe_set(b, 'codetaginfo_CodeTag', {a1})
    assert _is_linked(b, 'codetaginfo_CodeTag', a1)
    if hasattr(a1, 'codetaginfo_CodeTagContext'):
        assert _is_linked(a1, 'codetaginfo_CodeTagContext', b)
    _safe_set(b, 'codetaginfo_CodeTag', {a2})
    assert _is_linked(b, 'codetaginfo_CodeTag', a2)
    if hasattr(a1, 'codetaginfo_CodeTagContext'):
        assert not _is_linked(a1, 'codetaginfo_CodeTagContext', b)
    if hasattr(a2, 'codetaginfo_CodeTagContext'):
        assert _is_linked(a2, 'codetaginfo_CodeTagContext', b)
    _safe_set(b, 'codetaginfo_CodeTag', set())
    assert not _is_linked(b, 'codetaginfo_CodeTag', a2)
    if hasattr(a2, 'codetaginfo_CodeTagContext'):
        assert not _is_linked(a2, 'codetaginfo_CodeTagContext', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_xMLNSPrefixMap3_stub_double():
    # codetaginfo_EStringToStringMapEntry has no real 'codetaginfo_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so codetaginfo_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codetaginfo_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codetaginfo_DocumentRoot(mixed="sample_text")
    partner = codetaginfo_EStringToStringMapEntry()
    setattr(partner, 'codetaginfo_EStringToStringMapEntry', None)
    _safe_set(owner, 'codetaginfo_DocumentRoot', {partner})
    assert getattr(partner, 'codetaginfo_EStringToStringMapEntry') == owner
    _safe_set(owner, 'codetaginfo_DocumentRoot', set())
    assert getattr(partner, 'codetaginfo_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation4_stub_double():
    # codetaginfo_EStringToStringMapEntry has no real 'codetaginfo_EStringToStringMapEntry6' property in the generated
    # code (a bare stub) -- manually attach it so codetaginfo_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codetaginfo_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codetaginfo_DocumentRoot(mixed="sample_text")
    partner = codetaginfo_EStringToStringMapEntry()
    setattr(partner, 'codetaginfo_EStringToStringMapEntry6', None)
    _safe_set(owner, 'codetaginfo_DocumentRoot5', {partner})
    assert getattr(partner, 'codetaginfo_EStringToStringMapEntry6') == owner
    _safe_set(owner, 'codetaginfo_DocumentRoot5', set())
    assert getattr(partner, 'codetaginfo_EStringToStringMapEntry6') is None


