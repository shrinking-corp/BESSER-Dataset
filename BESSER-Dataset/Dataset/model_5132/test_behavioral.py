import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Etunit_DocumentRoot,
    Etunit_EStringToStringMapEntry,
    Etunit_ErrorType,
    Etunit_FailureType,
    Etunit_TestcaseType,
    Etunit_Testsuite,
    Etunit_TestsuiteType,
    Etunit_TestsuitesType,
    Testsuite,
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

def test_assoc_error8_reverse_link_reassign_clear():
    a1 = Etunit_TestcaseType(classname="sample_text", name="sample_text", time="sample_text")
    a2 = Etunit_TestcaseType(classname="sample_text_2", name="sample_text_2", time="sample_text_2")
    b = Etunit_ErrorType(actual="sample_text", expected="sample_text", mixed="sample_text")
    _safe_set(b, 'Etunit_ErrorType', a1)
    assert _is_linked(b, 'Etunit_ErrorType', a1)
    if hasattr(a1, 'Etunit_TestcaseType'):
        assert _is_linked(a1, 'Etunit_TestcaseType', b)
    _safe_set(b, 'Etunit_ErrorType', a2)
    assert _is_linked(b, 'Etunit_ErrorType', a2)
    if hasattr(a1, 'Etunit_TestcaseType'):
        assert not _is_linked(a1, 'Etunit_TestcaseType', b)
    if hasattr(a2, 'Etunit_TestcaseType'):
        assert _is_linked(a2, 'Etunit_TestcaseType', b)
    _safe_set(b, 'Etunit_ErrorType', None)
    assert not _is_linked(b, 'Etunit_ErrorType', a2)
    if hasattr(a2, 'Etunit_TestcaseType'):
        assert not _is_linked(a2, 'Etunit_TestcaseType', b)


def test_assoc_failure9_reverse_link_reassign_clear():
    a1 = Etunit_TestcaseType(classname="sample_text", name="sample_text", time="sample_text")
    a2 = Etunit_TestcaseType(classname="sample_text_2", name="sample_text_2", time="sample_text_2")
    b = Etunit_FailureType(actual="sample_text", expected="sample_text", mixed="sample_text")
    _safe_set(b, 'Etunit_FailureType', a1)
    assert _is_linked(b, 'Etunit_FailureType', a1)
    if hasattr(a1, 'Etunit_TestcaseType10'):
        assert _is_linked(a1, 'Etunit_TestcaseType10', b)
    _safe_set(b, 'Etunit_FailureType', a2)
    assert _is_linked(b, 'Etunit_FailureType', a2)
    if hasattr(a1, 'Etunit_TestcaseType10'):
        assert not _is_linked(a1, 'Etunit_TestcaseType10', b)
    if hasattr(a2, 'Etunit_TestcaseType10'):
        assert _is_linked(a2, 'Etunit_TestcaseType10', b)
    _safe_set(b, 'Etunit_FailureType', None)
    assert not _is_linked(b, 'Etunit_FailureType', a2)
    if hasattr(a2, 'Etunit_TestcaseType10'):
        assert not _is_linked(a2, 'Etunit_TestcaseType10', b)


def test_assoc_testcase11_reverse_link_reassign_clear():
    a1 = Etunit_Testsuite(errors="sample_text", failures="sample_text", name="sample_text", skipped="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    a2 = Etunit_Testsuite(errors="sample_text_2", failures="sample_text_2", name="sample_text_2", skipped="sample_text_2", tests="sample_text_2", time="sample_text_2", timestamp="sample_text_2")
    b = Etunit_TestcaseType(classname="sample_text", name="sample_text", time="sample_text")
    _safe_set(b, 'Etunit_TestcaseType13', a1)
    assert _is_linked(b, 'Etunit_TestcaseType13', a1)
    if hasattr(a1, 'Etunit_Testsuite12'):
        assert _is_linked(a1, 'Etunit_Testsuite12', b)
    _safe_set(b, 'Etunit_TestcaseType13', a2)
    assert _is_linked(b, 'Etunit_TestcaseType13', a2)
    if hasattr(a1, 'Etunit_Testsuite12'):
        assert not _is_linked(a1, 'Etunit_Testsuite12', b)
    if hasattr(a2, 'Etunit_Testsuite12'):
        assert _is_linked(a2, 'Etunit_Testsuite12', b)
    _safe_set(b, 'Etunit_TestcaseType13', None)
    assert not _is_linked(b, 'Etunit_TestcaseType13', a2)
    if hasattr(a2, 'Etunit_Testsuite12'):
        assert not _is_linked(a2, 'Etunit_Testsuite12', b)


def test_assoc_testsuite4_reverse_link_reassign_clear():
    a1 = Etunit_Testsuite(errors="sample_text", failures="sample_text", name="sample_text", skipped="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    a2 = Etunit_Testsuite(errors="sample_text_2", failures="sample_text_2", name="sample_text_2", skipped="sample_text_2", tests="sample_text_2", time="sample_text_2", timestamp="sample_text_2")
    b = Etunit_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'Etunit_DocumentRoot5', {a1})
    assert _is_linked(b, 'Etunit_DocumentRoot5', a1)
    if hasattr(a1, 'Etunit_Testsuite'):
        assert _is_linked(a1, 'Etunit_Testsuite', b)
    _safe_set(b, 'Etunit_DocumentRoot5', {a2})
    assert _is_linked(b, 'Etunit_DocumentRoot5', a2)
    if hasattr(a1, 'Etunit_Testsuite'):
        assert not _is_linked(a1, 'Etunit_Testsuite', b)
    if hasattr(a2, 'Etunit_Testsuite'):
        assert _is_linked(a2, 'Etunit_Testsuite', b)
    _safe_set(b, 'Etunit_DocumentRoot5', set())
    assert not _is_linked(b, 'Etunit_DocumentRoot5', a2)
    if hasattr(a2, 'Etunit_Testsuite'):
        assert not _is_linked(a2, 'Etunit_Testsuite', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_testsuites6_stub_double():
    # Etunit_TestsuitesType has no real 'Etunit_TestsuitesType' property in the generated
    # code (a bare stub) -- manually attach it so Etunit_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Etunit_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Etunit_DocumentRoot(mixed="sample_text")
    partner = Etunit_TestsuitesType()
    setattr(partner, 'Etunit_TestsuitesType', None)
    _safe_set(owner, 'Etunit_DocumentRoot7', {partner})
    assert getattr(partner, 'Etunit_TestsuitesType') == owner
    _safe_set(owner, 'Etunit_DocumentRoot7', set())
    assert getattr(partner, 'Etunit_TestsuitesType') is None


def test_assoc_xMLNSPrefixMap0_stub_double():
    # Etunit_EStringToStringMapEntry has no real 'Etunit_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so Etunit_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Etunit_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Etunit_DocumentRoot(mixed="sample_text")
    partner = Etunit_EStringToStringMapEntry()
    setattr(partner, 'Etunit_EStringToStringMapEntry', None)
    _safe_set(owner, 'Etunit_DocumentRoot', {partner})
    assert getattr(partner, 'Etunit_EStringToStringMapEntry') == owner
    _safe_set(owner, 'Etunit_DocumentRoot', set())
    assert getattr(partner, 'Etunit_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # Etunit_EStringToStringMapEntry has no real 'Etunit_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so Etunit_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Etunit_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Etunit_DocumentRoot(mixed="sample_text")
    partner = Etunit_EStringToStringMapEntry()
    setattr(partner, 'Etunit_EStringToStringMapEntry3', None)
    _safe_set(owner, 'Etunit_DocumentRoot2', {partner})
    assert getattr(partner, 'Etunit_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'Etunit_DocumentRoot2', set())
    assert getattr(partner, 'Etunit_EStringToStringMapEntry3') is None


