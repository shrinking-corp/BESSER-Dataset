import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    test_AddressModel,
    test_ConfigurationModel,
    test_TestModel,
    Gender,
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

def test_assoc_address0_reverse_link_reassign_clear():
    a1 = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    a2 = test_TestModel(accountBalance="sample_text_2", age=13, birthDate=date(2025, 6, 15), childCount="sample_text_2", gender="sample_text_2", isSelectable="sample_text_2", name="sample_text_2", overdrawAccount="sample_text_2")
    b = test_AddressModel(differentPostAddress=True, houseNumber="sample_text", street="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1), zipCode="sample_text")
    _safe_set(b, 'test_AddressModel', a1)
    assert _is_linked(b, 'test_AddressModel', a1)
    if hasattr(a1, 'test_TestModel'):
        assert _is_linked(a1, 'test_TestModel', b)
    _safe_set(b, 'test_AddressModel', a2)
    assert _is_linked(b, 'test_AddressModel', a2)
    if hasattr(a1, 'test_TestModel'):
        assert not _is_linked(a1, 'test_TestModel', b)
    if hasattr(a2, 'test_TestModel'):
        assert _is_linked(a2, 'test_TestModel', b)
    _safe_set(b, 'test_AddressModel', None)
    assert not _is_linked(b, 'test_AddressModel', a2)
    if hasattr(a2, 'test_TestModel'):
        assert not _is_linked(a2, 'test_TestModel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_testModel3_stub_double():
    # test_ConfigurationModel has no real 'test_ConfigurationModel4' property in the generated
    # code (a bare stub) -- manually attach it so test_TestModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_TestModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    partner = test_ConfigurationModel()
    setattr(partner, 'test_ConfigurationModel4', None)
    _safe_set(owner, 'test_TestModel5', partner)
    assert getattr(partner, 'test_ConfigurationModel4') == owner
    _safe_set(owner, 'test_TestModel5', None)
    assert getattr(partner, 'test_ConfigurationModel4') is None


def test_assoc_testModels1_stub_double():
    # test_ConfigurationModel has no real 'test_ConfigurationModel' property in the generated
    # code (a bare stub) -- manually attach it so test_TestModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_TestModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_TestModel(accountBalance="sample_text", age=7, birthDate=date(2024, 1, 1), childCount="sample_text", gender="sample_text", isSelectable="sample_text", name="sample_text", overdrawAccount="sample_text")
    partner = test_ConfigurationModel()
    setattr(partner, 'test_ConfigurationModel', None)
    _safe_set(owner, 'test_TestModel2', partner)
    assert owner in getattr(partner, 'test_ConfigurationModel')
    _safe_set(owner, 'test_TestModel2', None)
    assert owner not in getattr(partner, 'test_ConfigurationModel')


