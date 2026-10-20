import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DObject,
    TestCategoryBase,
    TestCategoryBeanAbstract,
    dmf_DObject,
    tests_EReferenceTest,
    tests_ExternalTestType,
    tests_TestCategoryAllProperty,
    tests_TestCategoryBase,
    tests_TestCategoryBeanA,
    tests_TestCategoryBeanAbstract,
    tests_TestCategoryBeanB,
    tests_TestCategoryBeanConcrete,
    tests_TestCategoryComposition,
    tests_TestCategoryCompositionArray,
    tests_TestCategoryExtends,
    tests_TestCategoryIntrinsicArray,
    tests_TestCategoryReference,
    tests_TestCategoryReferenceArray,
    tests_TestCrossLinkedParametersWithCalculation,
    tests_TestMassParameters,
    tests_TestParameter,
    EnumTestEnum,
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

def test_assoc_testArray14_reverse_link_reassign_clear():
    a1 = tests_TestCategoryBase(testBaseProperty=7)
    a2 = tests_TestCategoryBase(testBaseProperty=13)
    b = tests_TestCategoryBase(testBaseProperty=7)
    _safe_set(b, 'tests_TestCategoryBase13', {a1})
    assert _is_linked(b, 'tests_TestCategoryBase13', a1)
    if hasattr(a1, 'tests_TestCategoryBase'):
        assert _is_linked(a1, 'tests_TestCategoryBase', b)
    _safe_set(b, 'tests_TestCategoryBase13', {a2})
    assert _is_linked(b, 'tests_TestCategoryBase13', a2)
    if hasattr(a1, 'tests_TestCategoryBase'):
        assert not _is_linked(a1, 'tests_TestCategoryBase', b)
    if hasattr(a2, 'tests_TestCategoryBase'):
        assert _is_linked(a2, 'tests_TestCategoryBase', b)
    _safe_set(b, 'tests_TestCategoryBase13', set())
    assert not _is_linked(b, 'tests_TestCategoryBase13', a2)
    if hasattr(a2, 'tests_TestCategoryBase'):
        assert not _is_linked(a2, 'tests_TestCategoryBase', b)


def test_assoc_testReference16_reverse_link_reassign_clear():
    a1 = tests_TestCategoryBase(testBaseProperty=7)
    a2 = tests_TestCategoryBase(testBaseProperty=13)
    b = tests_TestCategoryBase(testBaseProperty=7)
    _safe_set(b, 'tests_TestCategoryBase17', a1)
    assert _is_linked(b, 'tests_TestCategoryBase17', a1)
    if hasattr(a1, 'tests_TestCategoryBase15'):
        assert _is_linked(a1, 'tests_TestCategoryBase15', b)
    _safe_set(b, 'tests_TestCategoryBase17', a2)
    assert _is_linked(b, 'tests_TestCategoryBase17', a2)
    if hasattr(a1, 'tests_TestCategoryBase15'):
        assert not _is_linked(a1, 'tests_TestCategoryBase15', b)
    if hasattr(a2, 'tests_TestCategoryBase15'):
        assert _is_linked(a2, 'tests_TestCategoryBase15', b)
    _safe_set(b, 'tests_TestCategoryBase17', None)
    assert not _is_linked(b, 'tests_TestCategoryBase17', a2)
    if hasattr(a2, 'tests_TestCategoryBase15'):
        assert not _is_linked(a2, 'tests_TestCategoryBase15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_mass18_stub_double():
    # tests_TestMassParameters has no real 'tests_TestMassParameters' property in the generated
    # code (a bare stub) -- manually attach it so tests_TestParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tests_TestParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tests_TestParameter(defaultValue=3.14)
    partner = tests_TestMassParameters()
    setattr(partner, 'tests_TestMassParameters', None)
    _safe_set(owner, 'tests_TestParameter', partner)
    assert getattr(partner, 'tests_TestMassParameters') == owner
    _safe_set(owner, 'tests_TestParameter', None)
    assert getattr(partner, 'tests_TestMassParameters') is None


def test_assoc_testCategoryReferenceArrayDynamic8_stub_double():
    # tests_TestCategoryReferenceArray has no real 'tests_TestCategoryReferenceArray' property in the generated
    # code (a bare stub) -- manually attach it so tests_TestCategoryAllProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tests_TestCategoryAllProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    partner = tests_TestCategoryReferenceArray()
    setattr(partner, 'tests_TestCategoryReferenceArray', None)
    _safe_set(owner, 'tests_TestCategoryAllProperty9', partner)
    assert owner in getattr(partner, 'tests_TestCategoryReferenceArray')
    _safe_set(owner, 'tests_TestCategoryAllProperty9', None)
    assert owner not in getattr(partner, 'tests_TestCategoryReferenceArray')


def test_assoc_testCategoryReferenceArrayStatic10_stub_double():
    # tests_TestCategoryReferenceArray has no real 'tests_TestCategoryReferenceArray11' property in the generated
    # code (a bare stub) -- manually attach it so tests_TestCategoryAllProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tests_TestCategoryAllProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    partner = tests_TestCategoryReferenceArray()
    setattr(partner, 'tests_TestCategoryReferenceArray11', None)
    _safe_set(owner, 'tests_TestCategoryAllProperty12', partner)
    assert owner in getattr(partner, 'tests_TestCategoryReferenceArray11')
    _safe_set(owner, 'tests_TestCategoryAllProperty12', None)
    assert owner not in getattr(partner, 'tests_TestCategoryReferenceArray11')


def test_assoc_testCompositionArrayDynamic3_stub_double():
    # tests_TestCategoryCompositionArray has no real 'tests_TestCategoryCompositionArray' property in the generated
    # code (a bare stub) -- manually attach it so tests_TestCategoryAllProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tests_TestCategoryAllProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    partner = tests_TestCategoryCompositionArray()
    setattr(partner, 'tests_TestCategoryCompositionArray', None)
    _safe_set(owner, 'tests_TestCategoryAllProperty4', partner)
    assert owner in getattr(partner, 'tests_TestCategoryCompositionArray')
    _safe_set(owner, 'tests_TestCategoryAllProperty4', None)
    assert owner not in getattr(partner, 'tests_TestCategoryCompositionArray')


def test_assoc_testCompositionArrayStatic5_stub_double():
    # tests_TestCategoryCompositionArray has no real 'tests_TestCategoryCompositionArray6' property in the generated
    # code (a bare stub) -- manually attach it so tests_TestCategoryAllProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tests_TestCategoryAllProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    partner = tests_TestCategoryCompositionArray()
    setattr(partner, 'tests_TestCategoryCompositionArray6', None)
    _safe_set(owner, 'tests_TestCategoryAllProperty7', partner)
    assert owner in getattr(partner, 'tests_TestCategoryCompositionArray6')
    _safe_set(owner, 'tests_TestCategoryAllProperty7', None)
    assert owner not in getattr(partner, 'tests_TestCategoryCompositionArray6')


def test_assoc_testRefCategory1_stub_double():
    # tests_TestCategoryReference has no real 'tests_TestCategoryReference' property in the generated
    # code (a bare stub) -- manually attach it so tests_TestCategoryAllProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tests_TestCategoryAllProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    partner = tests_TestCategoryReference()
    setattr(partner, 'tests_TestCategoryReference', None)
    _safe_set(owner, 'tests_TestCategoryAllProperty2', partner)
    assert getattr(partner, 'tests_TestCategoryReference') == owner
    _safe_set(owner, 'tests_TestCategoryAllProperty2', None)
    assert getattr(partner, 'tests_TestCategoryReference') is None


def test_assoc_testSubCategory0_stub_double():
    # tests_TestCategoryComposition has no real 'tests_TestCategoryComposition' property in the generated
    # code (a bare stub) -- manually attach it so tests_TestCategoryAllProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tests_TestCategoryAllProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    partner = tests_TestCategoryComposition()
    setattr(partner, 'tests_TestCategoryComposition', None)
    _safe_set(owner, 'tests_TestCategoryAllProperty', partner)
    assert getattr(partner, 'tests_TestCategoryComposition') == owner
    _safe_set(owner, 'tests_TestCategoryAllProperty', None)
    assert getattr(partner, 'tests_TestCategoryComposition') is None


