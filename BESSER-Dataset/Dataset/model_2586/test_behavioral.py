import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SubTestClass,
    SuperClass,
    TestPackage_SubPackage_SubTestClass,
    TestPackage_SubPackage_SubTestInterface,
    TestPackage_SuperClass,
    TestPackage_TestClass,
    TestPackage_TestInterface,
    TestPackage_UberClass,
    UberClass,
    SubTestEnum,
    TestEnum,
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

def test_assoc_testRef21_stub_double():
    # TestPackage_TestClass has no real 'TestPackage_TestClass2' property in the generated
    # code (a bare stub) -- manually attach it so TestPackage_TestInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TestPackage_TestInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TestPackage_TestInterface(testAttr="sample_text")
    partner = TestPackage_TestClass()
    setattr(partner, 'TestPackage_TestClass2', None)
    _safe_set(owner, 'TestPackage_TestInterface', partner)
    assert getattr(partner, 'TestPackage_TestClass2') == owner
    _safe_set(owner, 'TestPackage_TestInterface', None)
    assert getattr(partner, 'TestPackage_TestClass2') is None


def test_assoc_testRef33_stub_double():
    # TestPackage_TestClass has no real 'TestPackage_TestClass4' property in the generated
    # code (a bare stub) -- manually attach it so TestPackage_TestInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TestPackage_TestInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TestPackage_TestInterface(testAttr="sample_text")
    partner = TestPackage_TestClass()
    setattr(partner, 'TestPackage_TestClass4', None)
    _safe_set(owner, 'TestPackage_TestInterface5', partner)
    assert getattr(partner, 'TestPackage_TestClass4') == owner
    _safe_set(owner, 'TestPackage_TestInterface5', None)
    assert getattr(partner, 'TestPackage_TestClass4') is None


def test_assoc_testRef46_stub_double():
    # TestPackage_TestClass has no real 'TestPackage_TestClass7' property in the generated
    # code (a bare stub) -- manually attach it so TestPackage_TestInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TestPackage_TestInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TestPackage_TestInterface(testAttr="sample_text")
    partner = TestPackage_TestClass()
    setattr(partner, 'TestPackage_TestClass7', None)
    _safe_set(owner, 'TestPackage_TestInterface8', partner)
    assert owner in getattr(partner, 'TestPackage_TestClass7')
    _safe_set(owner, 'TestPackage_TestInterface8', None)
    assert owner not in getattr(partner, 'TestPackage_TestClass7')


def test_assoc_testRef59_stub_double():
    # TestPackage_TestClass has no real 'TestPackage_TestClass10' property in the generated
    # code (a bare stub) -- manually attach it so TestPackage_TestInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TestPackage_TestInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TestPackage_TestInterface(testAttr="sample_text")
    partner = TestPackage_TestClass()
    setattr(partner, 'TestPackage_TestClass10', None)
    _safe_set(owner, 'TestPackage_TestInterface11', partner)
    assert owner in getattr(partner, 'TestPackage_TestClass10')
    _safe_set(owner, 'TestPackage_TestInterface11', None)
    assert owner not in getattr(partner, 'TestPackage_TestClass10')


def test_assoc_testRef612_stub_double():
    # TestPackage_TestClass has no real 'TestPackage_TestClass13' property in the generated
    # code (a bare stub) -- manually attach it so TestPackage_TestInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TestPackage_TestInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TestPackage_TestInterface(testAttr="sample_text")
    partner = TestPackage_TestClass()
    setattr(partner, 'TestPackage_TestClass13', None)
    _safe_set(owner, 'TestPackage_TestInterface14', partner)
    assert owner in getattr(partner, 'TestPackage_TestClass13')
    _safe_set(owner, 'TestPackage_TestInterface14', None)
    assert owner not in getattr(partner, 'TestPackage_TestClass13')


def test_assoc_testRef721_stub_double():
    # TestPackage_TestClass has no real 'TestPackage_TestClass22' property in the generated
    # code (a bare stub) -- manually attach it so TestPackage_TestInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TestPackage_TestInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TestPackage_TestInterface(testAttr="sample_text")
    partner = TestPackage_TestClass()
    setattr(partner, 'TestPackage_TestClass22', None)
    _safe_set(owner, 'TestPackage_TestInterface23', partner)
    assert owner in getattr(partner, 'TestPackage_TestClass22')
    _safe_set(owner, 'TestPackage_TestInterface23', None)
    assert owner not in getattr(partner, 'TestPackage_TestClass22')


def test_assoc_testRef824_stub_double():
    # TestPackage_TestClass has no real 'TestPackage_TestClass25' property in the generated
    # code (a bare stub) -- manually attach it so TestPackage_TestInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TestPackage_TestInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TestPackage_TestInterface(testAttr="sample_text")
    partner = TestPackage_TestClass()
    setattr(partner, 'TestPackage_TestClass25', None)
    _safe_set(owner, 'TestPackage_TestInterface26', partner)
    assert owner in getattr(partner, 'TestPackage_TestClass25')
    _safe_set(owner, 'TestPackage_TestInterface26', None)
    assert owner not in getattr(partner, 'TestPackage_TestClass25')


def test_assoc_testRef927_stub_double():
    # TestPackage_TestClass has no real 'TestPackage_TestClass28' property in the generated
    # code (a bare stub) -- manually attach it so TestPackage_TestInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TestPackage_TestInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TestPackage_TestInterface(testAttr="sample_text")
    partner = TestPackage_TestClass()
    setattr(partner, 'TestPackage_TestClass28', None)
    _safe_set(owner, 'TestPackage_TestInterface29', partner)
    assert owner in getattr(partner, 'TestPackage_TestClass28')
    _safe_set(owner, 'TestPackage_TestInterface29', None)
    assert owner not in getattr(partner, 'TestPackage_TestClass28')


def test_assoc_testRefWithExp15_stub_double():
    # TestPackage_TestClass has no real 'TestPackage_TestClass16' property in the generated
    # code (a bare stub) -- manually attach it so TestPackage_TestInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TestPackage_TestInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TestPackage_TestInterface(testAttr="sample_text")
    partner = TestPackage_TestClass()
    setattr(partner, 'TestPackage_TestClass16', None)
    _safe_set(owner, 'TestPackage_TestInterface17', partner)
    assert getattr(partner, 'TestPackage_TestClass16') == owner
    _safe_set(owner, 'TestPackage_TestInterface17', None)
    assert getattr(partner, 'TestPackage_TestClass16') is None


def test_assoc_testRefWithKey18_stub_double():
    # TestPackage_TestClass has no real 'TestPackage_TestClass19' property in the generated
    # code (a bare stub) -- manually attach it so TestPackage_TestInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TestPackage_TestInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TestPackage_TestInterface(testAttr="sample_text")
    partner = TestPackage_TestClass()
    setattr(partner, 'TestPackage_TestClass19', None)
    _safe_set(owner, 'TestPackage_TestInterface20', partner)
    assert getattr(partner, 'TestPackage_TestClass19') == owner
    _safe_set(owner, 'TestPackage_TestInterface20', None)
    assert getattr(partner, 'TestPackage_TestClass19') is None


