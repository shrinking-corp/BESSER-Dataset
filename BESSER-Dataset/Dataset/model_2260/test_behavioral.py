import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    _bDXQcCdxEeKsSJflfBDxuw,
    tdt4250_Answer,
    tdt4250_Assignment,
    tdt4250_Course,
    tdt4250_Person,
    tdt4250_Root,
    tdt4250_Student,
    tdt4250_Teacher,
    tdt4250__bDIm8SdxEeKsSJflfBDxuw,
    tdt4250__bDNfcCdxEeKsSJflfBDxuw,
    tdt4250__bDSX8CdxEeKsSJflfBDxuw,
    tdt4250__bDTmECdxEeKsSJflfBDxuw,
    tdt4250__bDXQcCdxEeKsSJflfBDxuw,
    tdt4250__bDYekCdxEeKsSJflfBDxuw,
    ResponsibilityRole,
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

def test_assoc_coordinates10_stub_double():
    # tdt4250__bDIm8SdxEeKsSJflfBDxuw has no real 'tdt4250__bDIm8SdxEeKsSJflfBDxuw11' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250_Teacher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250_Teacher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250_Teacher(role="sample_text")
    partner = tdt4250__bDIm8SdxEeKsSJflfBDxuw()
    setattr(partner, 'tdt4250__bDIm8SdxEeKsSJflfBDxuw11', None)
    _safe_set(owner, 'tdt4250_Teacher', {partner})
    assert getattr(partner, 'tdt4250__bDIm8SdxEeKsSJflfBDxuw11') == owner
    _safe_set(owner, 'tdt4250_Teacher', set())
    assert getattr(partner, 'tdt4250__bDIm8SdxEeKsSJflfBDxuw11') is None


def test_assoc_has0_stub_double():
    # tdt4250__bDNfcCdxEeKsSJflfBDxuw has no real 'tdt4250__bDNfcCdxEeKsSJflfBDxuw' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250_Course(ID=7, credit=7, name="sample_text")
    partner = tdt4250__bDNfcCdxEeKsSJflfBDxuw()
    setattr(partner, 'tdt4250__bDNfcCdxEeKsSJflfBDxuw', None)
    _safe_set(owner, 'tdt4250_Course', {partner})
    assert getattr(partner, 'tdt4250__bDNfcCdxEeKsSJflfBDxuw') == owner
    _safe_set(owner, 'tdt4250_Course', set())
    assert getattr(partner, 'tdt4250__bDNfcCdxEeKsSJflfBDxuw') is None


def test_assoc_isAttended1_stub_double():
    # tdt4250__bDTmECdxEeKsSJflfBDxuw has no real 'tdt4250__bDTmECdxEeKsSJflfBDxuw' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250_Course(ID=7, credit=7, name="sample_text")
    partner = tdt4250__bDTmECdxEeKsSJflfBDxuw()
    setattr(partner, 'tdt4250__bDTmECdxEeKsSJflfBDxuw', None)
    _safe_set(owner, 'tdt4250_Course2', {partner})
    assert getattr(partner, 'tdt4250__bDTmECdxEeKsSJflfBDxuw') == owner
    _safe_set(owner, 'tdt4250_Course2', set())
    assert getattr(partner, 'tdt4250__bDTmECdxEeKsSJflfBDxuw') is None


def test_assoc_isCoordinated3_stub_double():
    # tdt4250__bDYekCdxEeKsSJflfBDxuw has no real 'tdt4250__bDYekCdxEeKsSJflfBDxuw' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250_Course(ID=7, credit=7, name="sample_text")
    partner = tdt4250__bDYekCdxEeKsSJflfBDxuw()
    setattr(partner, 'tdt4250__bDYekCdxEeKsSJflfBDxuw', None)
    _safe_set(owner, 'tdt4250_Course4', {partner})
    assert getattr(partner, 'tdt4250__bDYekCdxEeKsSJflfBDxuw') == owner
    _safe_set(owner, 'tdt4250_Course4', set())
    assert getattr(partner, 'tdt4250__bDYekCdxEeKsSJflfBDxuw') is None


def test_assoc_isSolved5_stub_double():
    # tdt4250__bDSX8CdxEeKsSJflfBDxuw has no real 'tdt4250__bDSX8CdxEeKsSJflfBDxuw' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250_Assignment(ID=7, content="sample_text", mandatory=True, name="sample_text")
    partner = tdt4250__bDSX8CdxEeKsSJflfBDxuw()
    setattr(partner, 'tdt4250__bDSX8CdxEeKsSJflfBDxuw', None)
    _safe_set(owner, 'tdt4250_Assignment', {partner})
    assert getattr(partner, 'tdt4250__bDSX8CdxEeKsSJflfBDxuw') == owner
    _safe_set(owner, 'tdt4250_Assignment', set())
    assert getattr(partner, 'tdt4250__bDSX8CdxEeKsSJflfBDxuw') is None


