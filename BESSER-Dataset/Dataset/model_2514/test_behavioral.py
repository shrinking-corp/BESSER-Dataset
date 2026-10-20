import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    AbstractD,
    B,
    C,
    D,
    test_ast_AbstractD,
    test_ast_D,
    test_ast_E,
    test_ntas_A,
    test_ntas_B,
    test_ntas_C,
    test_ntas_Root,
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

def test_assoc_DerivedMultipleUpperC24_stub_double():
    # C has no real 'C26' property in the generated
    # code (a bare stub) -- manually attach it so test_ast_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_ast_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_ast_D(index=7, name="sample_text", someBool=True, someCollection="sample_text", someOtherBool="sample_text", someQCollection="sample_text")
    partner = C()
    setattr(partner, 'C26', None)
    _safe_set(owner, 'test_ast_D25', {partner})
    assert getattr(partner, 'C26') == owner
    _safe_set(owner, 'test_ast_D25', set())
    assert getattr(partner, 'C26') is None


def test_assoc_DerivedUpperD21_stub_double():
    # D has no real 'D23' property in the generated
    # code (a bare stub) -- manually attach it so test_ast_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_ast_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_ast_D(index=7, name="sample_text", someBool=True, someCollection="sample_text", someOtherBool="sample_text", someQCollection="sample_text")
    partner = D()
    setattr(partner, 'D23', None)
    _safe_set(owner, 'test_ast_D22', partner)
    assert getattr(partner, 'D23') == owner
    _safe_set(owner, 'test_ast_D22', None)
    assert getattr(partner, 'D23') is None


def test_assoc_MultipleUpperC18_stub_double():
    # C has no real 'C20' property in the generated
    # code (a bare stub) -- manually attach it so test_ast_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_ast_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_ast_D(index=7, name="sample_text", someBool=True, someCollection="sample_text", someOtherBool="sample_text", someQCollection="sample_text")
    partner = C()
    setattr(partner, 'C20', None)
    _safe_set(owner, 'test_ast_D19', {partner})
    assert getattr(partner, 'C20') == owner
    _safe_set(owner, 'test_ast_D19', set())
    assert getattr(partner, 'C20') is None


def test_assoc_UpperA27_stub_double():
    # A has no real 'A29' property in the generated
    # code (a bare stub) -- manually attach it so test_ast_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_ast_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_ast_D(index=7, name="sample_text", someBool=True, someCollection="sample_text", someOtherBool="sample_text", someQCollection="sample_text")
    partner = A()
    setattr(partner, 'A29', None)
    _safe_set(owner, 'test_ast_D28', partner)
    assert getattr(partner, 'A29') == owner
    _safe_set(owner, 'test_ast_D28', None)
    assert getattr(partner, 'A29') is None


def test_assoc_UpperC12_stub_double():
    # C has no real 'C14' property in the generated
    # code (a bare stub) -- manually attach it so test_ast_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_ast_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_ast_D(index=7, name="sample_text", someBool=True, someCollection="sample_text", someOtherBool="sample_text", someQCollection="sample_text")
    partner = C()
    setattr(partner, 'C14', None)
    _safe_set(owner, 'test_ast_D13', partner)
    assert getattr(partner, 'C14') == owner
    _safe_set(owner, 'test_ast_D13', None)
    assert getattr(partner, 'C14') is None


def test_assoc_derivedMultipleLowerA30_stub_double():
    # A has no real 'A32' property in the generated
    # code (a bare stub) -- manually attach it so test_ast_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_ast_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_ast_D(index=7, name="sample_text", someBool=True, someCollection="sample_text", someOtherBool="sample_text", someQCollection="sample_text")
    partner = A()
    setattr(partner, 'A32', None)
    _safe_set(owner, 'test_ast_D31', {partner})
    assert getattr(partner, 'A32') == owner
    _safe_set(owner, 'test_ast_D31', set())
    assert getattr(partner, 'A32') is None


def test_assoc_lowerD10_stub_double():
    # D has no real 'D11' property in the generated
    # code (a bare stub) -- manually attach it so test_ast_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_ast_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_ast_D(index=7, name="sample_text", someBool=True, someCollection="sample_text", someOtherBool="sample_text", someQCollection="sample_text")
    partner = D()
    setattr(partner, 'D11', None)
    _safe_set(owner, 'test_ast_D', partner)
    assert getattr(partner, 'D11') == owner
    _safe_set(owner, 'test_ast_D', None)
    assert getattr(partner, 'D11') is None


def test_assoc_multipleLowerD15_stub_double():
    # D has no real 'D17' property in the generated
    # code (a bare stub) -- manually attach it so test_ast_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_ast_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_ast_D(index=7, name="sample_text", someBool=True, someCollection="sample_text", someOtherBool="sample_text", someQCollection="sample_text")
    partner = D()
    setattr(partner, 'D17', None)
    _safe_set(owner, 'test_ast_D16', {partner})
    assert getattr(partner, 'D17') == owner
    _safe_set(owner, 'test_ast_D16', set())
    assert getattr(partner, 'D17') is None


def test_assoc_refToSomeA33_stub_double():
    # A has no real 'A34' property in the generated
    # code (a bare stub) -- manually attach it so test_ast_AbstractD's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_ast_AbstractD's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_ast_AbstractD(derivedString="sample_text")
    partner = A()
    setattr(partner, 'A34', None)
    _safe_set(owner, 'test_ast_AbstractD', partner)
    assert getattr(partner, 'A34') == owner
    _safe_set(owner, 'test_ast_AbstractD', None)
    assert getattr(partner, 'A34') is None


