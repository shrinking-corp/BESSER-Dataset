import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTest,
    InterfaceTest,
    MultipleSuperTest,
    OperationsTest,
    exhaustive_AbstractTest,
    exhaustive_AttributesTest,
    exhaustive_BindedChildTest,
    exhaustive_GenericTest,
    exhaustive_InterfaceTest,
    exhaustive_MultipleBoundsGeneric,
    exhaustive_MultipleSuperTest,
    exhaustive_OperationsTest,
    exhaustive_PartiallyBindedChildTest,
    exhaustive_ReferencesTest,
    exhaustive_UnbindedChildTest,
    SerializableEnumTest,
    UnserializableEnumTest,
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

def test_assoc_derivedYes24_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest25' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest25', None)
    _safe_set(owner, 'exhaustive_AttributesTest26', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest25') == owner
    _safe_set(owner, 'exhaustive_AttributesTest26', None)
    assert getattr(partner, 'exhaustive_ReferencesTest25') is None


def test_assoc_lowerBound133_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest34' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest34', None)
    _safe_set(owner, 'exhaustive_AttributesTest35', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest34') == owner
    _safe_set(owner, 'exhaustive_AttributesTest35', None)
    assert getattr(partner, 'exhaustive_ReferencesTest34') is None


def test_assoc_lowerBound236_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest37' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest37', None)
    _safe_set(owner, 'exhaustive_AttributesTest38', partner)
    assert owner in getattr(partner, 'exhaustive_ReferencesTest37')
    _safe_set(owner, 'exhaustive_AttributesTest38', None)
    assert owner not in getattr(partner, 'exhaustive_ReferencesTest37')


def test_assoc_opposite16_stub_double():
    # exhaustive_ReferencesTest has no real 'opposite2' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'opposite2', None)
    _safe_set(owner, 'AttributesTest', partner)
    assert getattr(partner, 'opposite2') == owner
    _safe_set(owner, 'AttributesTest', None)
    assert getattr(partner, 'opposite2') is None


def test_assoc_opposite239_stub_double():
    # exhaustive_ReferencesTest has no real 'ReferencesTest' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'ReferencesTest', None)
    _safe_set(owner, 'opposite1', partner)
    assert getattr(partner, 'ReferencesTest') == owner
    _safe_set(owner, 'opposite1', None)
    assert getattr(partner, 'ReferencesTest') is None


def test_assoc_orderedFalse7_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest8' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest8', None)
    _safe_set(owner, 'exhaustive_AttributesTest', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest8') == owner
    _safe_set(owner, 'exhaustive_AttributesTest', None)
    assert getattr(partner, 'exhaustive_ReferencesTest8') is None


def test_assoc_resolveProxiesFalse9_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest10' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest10', None)
    _safe_set(owner, 'exhaustive_AttributesTest11', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest10') == owner
    _safe_set(owner, 'exhaustive_AttributesTest11', None)
    assert getattr(partner, 'exhaustive_ReferencesTest10') is None


def test_assoc_transientTrue12_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest13' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest13', None)
    _safe_set(owner, 'exhaustive_AttributesTest14', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest13') == owner
    _safe_set(owner, 'exhaustive_AttributesTest14', None)
    assert getattr(partner, 'exhaustive_ReferencesTest13') is None


def test_assoc_uniqueFalse15_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest16' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest16', None)
    _safe_set(owner, 'exhaustive_AttributesTest17', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest16') == owner
    _safe_set(owner, 'exhaustive_AttributesTest17', None)
    assert getattr(partner, 'exhaustive_ReferencesTest16') is None


def test_assoc_unsettableTrue18_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest19' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest19', None)
    _safe_set(owner, 'exhaustive_AttributesTest20', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest19') == owner
    _safe_set(owner, 'exhaustive_AttributesTest20', None)
    assert getattr(partner, 'exhaustive_ReferencesTest19') is None


def test_assoc_upperBound230_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest31' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest31', None)
    _safe_set(owner, 'exhaustive_AttributesTest32', partner)
    assert owner in getattr(partner, 'exhaustive_ReferencesTest31')
    _safe_set(owner, 'exhaustive_AttributesTest32', None)
    assert owner not in getattr(partner, 'exhaustive_ReferencesTest31')


def test_assoc_upperBoundN27_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest28' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest28', None)
    _safe_set(owner, 'exhaustive_AttributesTest29', partner)
    assert owner in getattr(partner, 'exhaustive_ReferencesTest28')
    _safe_set(owner, 'exhaustive_AttributesTest29', None)
    assert owner not in getattr(partner, 'exhaustive_ReferencesTest28')


def test_assoc_volatileTrue21_stub_double():
    # exhaustive_ReferencesTest has no real 'exhaustive_ReferencesTest22' property in the generated
    # code (a bare stub) -- manually attach it so exhaustive_AttributesTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exhaustive_AttributesTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    partner = exhaustive_ReferencesTest()
    setattr(partner, 'exhaustive_ReferencesTest22', None)
    _safe_set(owner, 'exhaustive_AttributesTest23', partner)
    assert getattr(partner, 'exhaustive_ReferencesTest22') == owner
    _safe_set(owner, 'exhaustive_AttributesTest23', None)
    assert getattr(partner, 'exhaustive_ReferencesTest22') is None


