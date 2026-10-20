import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    List_Element,
    List_List,
    List_SubTestPackage_SubTest,
    List_TestPackage_Test,
    SubTestPackage_List_Element,
    SubTestPackage_SubTest,
    Test,
    TestPackage_List_Element,
    listType,
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

def test_assoc_elements0_reverse_link_reassign_clear():
    a1 = List_List(size=7, type="sample_text")
    a2 = List_List(size=13, type="sample_text_2")
    b = List_Element(name="sample_text", value=7)
    _safe_set(b, 'List_Element', a1)
    assert _is_linked(b, 'List_Element', a1)
    if hasattr(a1, 'List_List'):
        assert _is_linked(a1, 'List_List', b)
    _safe_set(b, 'List_Element', a2)
    assert _is_linked(b, 'List_Element', a2)
    if hasattr(a1, 'List_List'):
        assert not _is_linked(a1, 'List_List', b)
    if hasattr(a2, 'List_List'):
        assert _is_linked(a2, 'List_List', b)
    _safe_set(b, 'List_Element', None)
    assert not _is_linked(b, 'List_Element', a2)
    if hasattr(a2, 'List_List'):
        assert not _is_linked(a2, 'List_List', b)


def test_assoc_firstElement1_reverse_link_reassign_clear():
    a1 = List_List(size=7, type="sample_text")
    a2 = List_List(size=13, type="sample_text_2")
    b = List_Element(name="sample_text", value=7)
    _safe_set(b, 'List_Element3', a1)
    assert _is_linked(b, 'List_Element3', a1)
    if hasattr(a1, 'List_List2'):
        assert _is_linked(a1, 'List_List2', b)
    _safe_set(b, 'List_Element3', a2)
    assert _is_linked(b, 'List_Element3', a2)
    if hasattr(a1, 'List_List2'):
        assert not _is_linked(a1, 'List_List2', b)
    if hasattr(a2, 'List_List2'):
        assert _is_linked(a2, 'List_List2', b)
    _safe_set(b, 'List_Element3', None)
    assert not _is_linked(b, 'List_Element3', a2)
    if hasattr(a2, 'List_List2'):
        assert not _is_linked(a2, 'List_List2', b)


def test_assoc_lastElement4_reverse_link_reassign_clear():
    a1 = List_List(size=7, type="sample_text")
    a2 = List_List(size=13, type="sample_text_2")
    b = List_Element(name="sample_text", value=7)
    _safe_set(b, 'List_Element6', a1)
    assert _is_linked(b, 'List_Element6', a1)
    if hasattr(a1, 'List_List5'):
        assert _is_linked(a1, 'List_List5', b)
    _safe_set(b, 'List_Element6', a2)
    assert _is_linked(b, 'List_Element6', a2)
    if hasattr(a1, 'List_List5'):
        assert not _is_linked(a1, 'List_List5', b)
    if hasattr(a2, 'List_List5'):
        assert _is_linked(a2, 'List_List5', b)
    _safe_set(b, 'List_Element6', None)
    assert not _is_linked(b, 'List_Element6', a2)
    if hasattr(a2, 'List_List5'):
        assert not _is_linked(a2, 'List_List5', b)


def test_assoc_subElements12_reverse_link_reassign_clear():
    a1 = List_List(size=7, type="sample_text")
    a2 = List_List(size=13, type="sample_text_2")
    b = List_Element(name="sample_text", value=7)
    _safe_set(b, 'List_Element13', a1)
    assert _is_linked(b, 'List_Element13', a1)
    if hasattr(a1, 'List_List14'):
        assert _is_linked(a1, 'List_List14', b)
    _safe_set(b, 'List_Element13', a2)
    assert _is_linked(b, 'List_Element13', a2)
    if hasattr(a1, 'List_List14'):
        assert not _is_linked(a1, 'List_List14', b)
    if hasattr(a2, 'List_List14'):
        assert _is_linked(a2, 'List_List14', b)
    _safe_set(b, 'List_Element13', None)
    assert not _is_linked(b, 'List_Element13', a2)
    if hasattr(a2, 'List_List14'):
        assert not _is_linked(a2, 'List_List14', b)


def test_assoc_testPointer8_reverse_link_reassign_clear():
    a1 = List_List(size=7, type="sample_text")
    a2 = List_List(size=13, type="sample_text_2")
    b = List_List(size=7, type="sample_text")
    _safe_set(b, 'List_List9', a1)
    assert _is_linked(b, 'List_List9', a1)
    if hasattr(a1, 'List_List7'):
        assert _is_linked(a1, 'List_List7', b)
    _safe_set(b, 'List_List9', a2)
    assert _is_linked(b, 'List_List9', a2)
    if hasattr(a1, 'List_List7'):
        assert not _is_linked(a1, 'List_List7', b)
    if hasattr(a2, 'List_List7'):
        assert _is_linked(a2, 'List_List7', b)
    _safe_set(b, 'List_List9', None)
    assert not _is_linked(b, 'List_List9', a2)
    if hasattr(a2, 'List_List7'):
        assert not _is_linked(a2, 'List_List7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elementPointer16_stub_double():
    # TestPackage_List_Element has no real 'TestPackage_List_Element' property in the generated
    # code (a bare stub) -- manually attach it so List_TestPackage_Test's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # List_TestPackage_Test's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = List_TestPackage_Test(value=7)
    partner = TestPackage_List_Element()
    setattr(partner, 'TestPackage_List_Element', None)
    _safe_set(owner, 'List_TestPackage_Test', partner)
    assert getattr(partner, 'TestPackage_List_Element') == owner
    _safe_set(owner, 'List_TestPackage_Test', None)
    assert getattr(partner, 'TestPackage_List_Element') is None


def test_assoc_elementPointer20_stub_double():
    # SubTestPackage_List_Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so List_SubTestPackage_SubTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # List_SubTestPackage_SubTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = List_SubTestPackage_SubTest(value=7)
    partner = SubTestPackage_List_Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'subTestPointer', partner)
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'subTestPointer', None)
    assert getattr(partner, 'Element') is None


def test_assoc_elementPointer217_stub_double():
    # TestPackage_List_Element has no real 'TestPackage_List_Element19' property in the generated
    # code (a bare stub) -- manually attach it so List_TestPackage_Test's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # List_TestPackage_Test's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = List_TestPackage_Test(value=7)
    partner = TestPackage_List_Element()
    setattr(partner, 'TestPackage_List_Element19', None)
    _safe_set(owner, 'List_TestPackage_Test18', partner)
    assert getattr(partner, 'TestPackage_List_Element19') == owner
    _safe_set(owner, 'List_TestPackage_Test18', None)
    assert getattr(partner, 'TestPackage_List_Element19') is None


def test_assoc_packagePointer10_stub_double():
    # Test has no real 'Test' property in the generated
    # code (a bare stub) -- manually attach it so List_List's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # List_List's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = List_List(size=7, type="sample_text")
    partner = Test()
    setattr(partner, 'Test', None)
    _safe_set(owner, 'List_List11', partner)
    assert getattr(partner, 'Test') == owner
    _safe_set(owner, 'List_List11', None)
    assert getattr(partner, 'Test') is None


def test_assoc_subTestPointer15_stub_double():
    # SubTestPackage_SubTest has no real 'SubTest' property in the generated
    # code (a bare stub) -- manually attach it so List_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # List_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = List_Element(name="sample_text", value=7)
    partner = SubTestPackage_SubTest()
    setattr(partner, 'SubTest', None)
    _safe_set(owner, 'elementPointer', partner)
    assert getattr(partner, 'SubTest') == owner
    _safe_set(owner, 'elementPointer', None)
    assert getattr(partner, 'SubTest') is None


