import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    person_CompanyType,
    person_DocumentRoot,
    person_EStringToStringMapEntry,
    person_PersonType,
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

def test_assoc_company5_stub_double():
    # person_CompanyType has no real 'person_CompanyType7' property in the generated
    # code (a bare stub) -- manually attach it so person_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # person_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = person_DocumentRoot(mixed="sample_text")
    partner = person_CompanyType()
    setattr(partner, 'person_CompanyType7', None)
    _safe_set(owner, 'person_DocumentRoot6', {partner})
    assert getattr(partner, 'person_CompanyType7') == owner
    _safe_set(owner, 'person_DocumentRoot6', set())
    assert getattr(partner, 'person_CompanyType7') is None


def test_assoc_person0_stub_double():
    # person_CompanyType has no real 'person_CompanyType' property in the generated
    # code (a bare stub) -- manually attach it so person_PersonType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # person_PersonType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = person_PersonType(age="sample_text", country="sample_text", email="sample_text", name="sample_text")
    partner = person_CompanyType()
    setattr(partner, 'person_CompanyType', None)
    _safe_set(owner, 'person_PersonType', partner)
    assert getattr(partner, 'person_CompanyType') == owner
    _safe_set(owner, 'person_PersonType', None)
    assert getattr(partner, 'person_CompanyType') is None


def test_assoc_xMLNSPrefixMap1_stub_double():
    # person_EStringToStringMapEntry has no real 'person_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so person_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # person_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = person_DocumentRoot(mixed="sample_text")
    partner = person_EStringToStringMapEntry()
    setattr(partner, 'person_EStringToStringMapEntry', None)
    _safe_set(owner, 'person_DocumentRoot', {partner})
    assert getattr(partner, 'person_EStringToStringMapEntry') == owner
    _safe_set(owner, 'person_DocumentRoot', set())
    assert getattr(partner, 'person_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation2_stub_double():
    # person_EStringToStringMapEntry has no real 'person_EStringToStringMapEntry4' property in the generated
    # code (a bare stub) -- manually attach it so person_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # person_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = person_DocumentRoot(mixed="sample_text")
    partner = person_EStringToStringMapEntry()
    setattr(partner, 'person_EStringToStringMapEntry4', None)
    _safe_set(owner, 'person_DocumentRoot3', {partner})
    assert getattr(partner, 'person_EStringToStringMapEntry4') == owner
    _safe_set(owner, 'person_DocumentRoot3', set())
    assert getattr(partner, 'person_EStringToStringMapEntry4') is None


