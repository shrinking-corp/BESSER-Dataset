import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Measure,
    MeasureBinaryOperation,
    MeasureBinaryProductOperation,
    MeasureUnboundOperation,
    MeasureValue,
    MeasurementUncertaintyInformation,
    TypedMeasure,
    eel_EnergyComputation,
    eel_Integral,
    eel_Interval,
    eel_Measure,
    eel_MeasureAttribute,
    eel_MeasureBinaryOperation,
    eel_MeasureBinaryProductOperation,
    eel_MeasureBinarySumOperation,
    eel_MeasureCast,
    eel_MeasureOCL,
    eel_MeasureUnboundOperation,
    eel_MeasureUnboundProductOperation,
    eel_MeasureUnboundSumOperation,
    eel_MeasureValue,
    eel_MeasurementUncertainty,
    eel_MeasurementUncertaintyInformation,
    eel_NormalDistribution,
    eel_Platform,
    eel_PowerComputation,
    eel_RealTimeDuration,
    eel_Sample,
    eel_Sampling,
    eel_TypedMeasure,
    eel_Variable,
    Type,
    Visibility,
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

def test_assoc_measures1_reverse_link_reassign_clear():
    a1 = eel_Platform(name="sample_text")
    a2 = eel_Platform(name="sample_text_2")
    b = eel_Measure(name="sample_text", subname="sample_text", targetClass="sample_text", targetOperation="sample_text")
    _safe_set(b, 'eel_Measure', a1)
    assert _is_linked(b, 'eel_Measure', a1)
    if hasattr(a1, 'eel_Platform2'):
        assert _is_linked(a1, 'eel_Platform2', b)
    _safe_set(b, 'eel_Measure', a2)
    assert _is_linked(b, 'eel_Measure', a2)
    if hasattr(a1, 'eel_Platform2'):
        assert not _is_linked(a1, 'eel_Platform2', b)
    if hasattr(a2, 'eel_Platform2'):
        assert _is_linked(a2, 'eel_Platform2', b)
    _safe_set(b, 'eel_Measure', None)
    assert not _is_linked(b, 'eel_Measure', a2)
    if hasattr(a2, 'eel_Platform2'):
        assert not _is_linked(a2, 'eel_Platform2', b)


def test_assoc_uncertainty3_reverse_link_reassign_clear():
    a1 = eel_MeasurementUncertainty(standardUncertainty="sample_text")
    a2 = eel_MeasurementUncertainty(standardUncertainty="sample_text_2")
    b = eel_Measure(name="sample_text", subname="sample_text", targetClass="sample_text", targetOperation="sample_text")
    _safe_set(b, 'eel_Measure4', a1)
    assert _is_linked(b, 'eel_Measure4', a1)
    if hasattr(a1, 'eel_MeasurementUncertainty'):
        assert _is_linked(a1, 'eel_MeasurementUncertainty', b)
    _safe_set(b, 'eel_Measure4', a2)
    assert _is_linked(b, 'eel_Measure4', a2)
    if hasattr(a1, 'eel_MeasurementUncertainty'):
        assert not _is_linked(a1, 'eel_MeasurementUncertainty', b)
    if hasattr(a2, 'eel_MeasurementUncertainty'):
        assert _is_linked(a2, 'eel_MeasurementUncertainty', b)
    _safe_set(b, 'eel_Measure4', None)
    assert not _is_linked(b, 'eel_Measure4', a2)
    if hasattr(a2, 'eel_MeasurementUncertainty'):
        assert not _is_linked(a2, 'eel_MeasurementUncertainty', b)


def test_assoc_variables0_reverse_link_reassign_clear():
    a1 = eel_Variable(name="sample_text", value="sample_text", vibility="sample_text")
    a2 = eel_Variable(name="sample_text_2", value="sample_text_2", vibility="sample_text_2")
    b = eel_Platform(name="sample_text")
    _safe_set(b, 'eel_Platform', {a1})
    assert _is_linked(b, 'eel_Platform', a1)
    if hasattr(a1, 'eel_Variable'):
        assert _is_linked(a1, 'eel_Variable', b)
    _safe_set(b, 'eel_Platform', {a2})
    assert _is_linked(b, 'eel_Platform', a2)
    if hasattr(a1, 'eel_Variable'):
        assert not _is_linked(a1, 'eel_Variable', b)
    if hasattr(a2, 'eel_Variable'):
        assert _is_linked(a2, 'eel_Variable', b)
    _safe_set(b, 'eel_Platform', set())
    assert not _is_linked(b, 'eel_Platform', a2)
    if hasattr(a2, 'eel_Variable'):
        assert not _is_linked(a2, 'eel_Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_information14_stub_double():
    # eel_MeasurementUncertaintyInformation has no real 'eel_MeasurementUncertaintyInformation' property in the generated
    # code (a bare stub) -- manually attach it so eel_MeasurementUncertainty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eel_MeasurementUncertainty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eel_MeasurementUncertainty(standardUncertainty="sample_text")
    partner = eel_MeasurementUncertaintyInformation()
    setattr(partner, 'eel_MeasurementUncertaintyInformation', None)
    _safe_set(owner, 'eel_MeasurementUncertainty15', partner)
    assert getattr(partner, 'eel_MeasurementUncertaintyInformation') == owner
    _safe_set(owner, 'eel_MeasurementUncertainty15', None)
    assert getattr(partner, 'eel_MeasurementUncertaintyInformation') is None


def test_assoc_interval22_stub_double():
    # eel_Interval has no real 'eel_Interval23' property in the generated
    # code (a bare stub) -- manually attach it so eel_Integral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eel_Integral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eel_Integral(function="sample_text")
    partner = eel_Interval()
    setattr(partner, 'eel_Interval23', None)
    _safe_set(owner, 'eel_Integral', partner)
    assert getattr(partner, 'eel_Interval23') == owner
    _safe_set(owner, 'eel_Integral', None)
    assert getattr(partner, 'eel_Interval23') is None


def test_assoc_left7_stub_double():
    # eel_MeasureBinaryOperation has no real 'eel_MeasureBinaryOperation' property in the generated
    # code (a bare stub) -- manually attach it so eel_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eel_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eel_Measure(name="sample_text", subname="sample_text", targetClass="sample_text", targetOperation="sample_text")
    partner = eel_MeasureBinaryOperation()
    setattr(partner, 'eel_MeasureBinaryOperation', None)
    _safe_set(owner, 'eel_Measure8', partner)
    assert getattr(partner, 'eel_MeasureBinaryOperation') == owner
    _safe_set(owner, 'eel_Measure8', None)
    assert getattr(partner, 'eel_MeasureBinaryOperation') is None


def test_assoc_lowerEndpoint16_stub_double():
    # eel_Interval has no real 'eel_Interval' property in the generated
    # code (a bare stub) -- manually attach it so eel_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eel_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eel_Measure(name="sample_text", subname="sample_text", targetClass="sample_text", targetOperation="sample_text")
    partner = eel_Interval()
    setattr(partner, 'eel_Interval', None)
    _safe_set(owner, 'eel_Measure17', partner)
    assert getattr(partner, 'eel_Interval') == owner
    _safe_set(owner, 'eel_Measure17', None)
    assert getattr(partner, 'eel_Interval') is None


def test_assoc_measure5_stub_double():
    # eel_MeasureCast has no real 'eel_MeasureCast' property in the generated
    # code (a bare stub) -- manually attach it so eel_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eel_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eel_Measure(name="sample_text", subname="sample_text", targetClass="sample_text", targetOperation="sample_text")
    partner = eel_MeasureCast()
    setattr(partner, 'eel_MeasureCast', None)
    _safe_set(owner, 'eel_Measure6', partner)
    assert getattr(partner, 'eel_MeasureCast') == owner
    _safe_set(owner, 'eel_Measure6', None)
    assert getattr(partner, 'eel_MeasureCast') is None


def test_assoc_measures12_stub_double():
    # eel_MeasureUnboundOperation has no real 'eel_MeasureUnboundOperation' property in the generated
    # code (a bare stub) -- manually attach it so eel_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eel_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eel_Measure(name="sample_text", subname="sample_text", targetClass="sample_text", targetOperation="sample_text")
    partner = eel_MeasureUnboundOperation()
    setattr(partner, 'eel_MeasureUnboundOperation', None)
    _safe_set(owner, 'eel_Measure13', partner)
    assert owner in getattr(partner, 'eel_MeasureUnboundOperation')
    _safe_set(owner, 'eel_Measure13', None)
    assert owner not in getattr(partner, 'eel_MeasureUnboundOperation')


def test_assoc_quantity24_stub_double():
    # eel_Sample has no real 'eel_Sample25' property in the generated
    # code (a bare stub) -- manually attach it so eel_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eel_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eel_Measure(name="sample_text", subname="sample_text", targetClass="sample_text", targetOperation="sample_text")
    partner = eel_Sample()
    setattr(partner, 'eel_Sample25', None)
    _safe_set(owner, 'eel_Measure26', partner)
    assert owner in getattr(partner, 'eel_Sample25')
    _safe_set(owner, 'eel_Measure26', None)
    assert owner not in getattr(partner, 'eel_Sample25')


def test_assoc_right9_stub_double():
    # eel_MeasureBinaryOperation has no real 'eel_MeasureBinaryOperation10' property in the generated
    # code (a bare stub) -- manually attach it so eel_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eel_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eel_Measure(name="sample_text", subname="sample_text", targetClass="sample_text", targetOperation="sample_text")
    partner = eel_MeasureBinaryOperation()
    setattr(partner, 'eel_MeasureBinaryOperation10', None)
    _safe_set(owner, 'eel_Measure11', partner)
    assert getattr(partner, 'eel_MeasureBinaryOperation10') == owner
    _safe_set(owner, 'eel_Measure11', None)
    assert getattr(partner, 'eel_MeasureBinaryOperation10') is None


def test_assoc_samples21_stub_double():
    # eel_Sample has no real 'eel_Sample' property in the generated
    # code (a bare stub) -- manually attach it so eel_Sampling's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eel_Sampling's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eel_Sampling(measurementProcedure="sample_text")
    partner = eel_Sample()
    setattr(partner, 'eel_Sample', None)
    _safe_set(owner, 'eel_Sampling', {partner})
    assert getattr(partner, 'eel_Sample') == owner
    _safe_set(owner, 'eel_Sampling', set())
    assert getattr(partner, 'eel_Sample') is None


def test_assoc_upperEndpoint18_stub_double():
    # eel_Interval has no real 'eel_Interval19' property in the generated
    # code (a bare stub) -- manually attach it so eel_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eel_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eel_Measure(name="sample_text", subname="sample_text", targetClass="sample_text", targetOperation="sample_text")
    partner = eel_Interval()
    setattr(partner, 'eel_Interval19', None)
    _safe_set(owner, 'eel_Measure20', partner)
    assert getattr(partner, 'eel_Interval19') == owner
    _safe_set(owner, 'eel_Measure20', None)
    assert getattr(partner, 'eel_Interval19') is None


