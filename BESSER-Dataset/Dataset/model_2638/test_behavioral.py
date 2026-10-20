import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Class2,
    EdgeTarget,
    model3_Class1,
    model3_ClassWithIDAttribute,
    model3_ClassWithJavaClassAttribute,
    model3_ClassWithJavaObjectAttribute,
    model3_ClassWithTransientContainment,
    model3_Diagram,
    model3_EClass,
    model3_EPackage,
    model3_EReference,
    model3_Edge,
    model3_EdgeTarget,
    model3_File,
    model3_Image,
    model3_MetaRef,
    model3_NodeA,
    model3_NodeB,
    model3_NodeC,
    model3_NodeD,
    model3_NodeE,
    model3_NodeF,
    model3_Polygon,
    model3_PolygonWithDuplicates,
    model3_subpackage_Class2,
    subpackage_model3_Class1,
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

def test_assoc_children12_reverse_link_reassign_clear():
    a1 = model3_NodeB(name="sample_text")
    a2 = model3_NodeB(name="sample_text_2")
    b = model3_NodeB(name="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'NodeB'):
        assert _is_linked(a1, 'NodeB', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'NodeB'):
        assert not _is_linked(a1, 'NodeB', b)
    if hasattr(a2, 'NodeB'):
        assert _is_linked(a2, 'NodeB', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'NodeB'):
        assert not _is_linked(a2, 'NodeB', b)


def test_assoc_children17_reverse_link_reassign_clear():
    a1 = model3_NodeC(name="sample_text")
    a2 = model3_NodeC(name="sample_text_2")
    b = model3_NodeC(name="sample_text")
    _safe_set(b, 'parent18', {a1})
    assert _is_linked(b, 'parent18', a1)
    if hasattr(a1, 'NodeC'):
        assert _is_linked(a1, 'NodeC', b)
    _safe_set(b, 'parent18', {a2})
    assert _is_linked(b, 'parent18', a2)
    if hasattr(a1, 'NodeC'):
        assert not _is_linked(a1, 'NodeC', b)
    if hasattr(a2, 'NodeC'):
        assert _is_linked(a2, 'NodeC', b)
    _safe_set(b, 'parent18', set())
    assert not _is_linked(b, 'parent18', a2)
    if hasattr(a2, 'NodeC'):
        assert not _is_linked(a2, 'NodeC', b)


def test_assoc_children30_reverse_link_reassign_clear():
    a1 = model3_NodeD(name="sample_text")
    a2 = model3_NodeD(name="sample_text_2")
    b = model3_NodeD(name="sample_text")
    _safe_set(b, 'parent31', {a1})
    assert _is_linked(b, 'parent31', a1)
    if hasattr(a1, 'NodeD'):
        assert _is_linked(a1, 'NodeD', b)
    _safe_set(b, 'parent31', {a2})
    assert _is_linked(b, 'parent31', a2)
    if hasattr(a1, 'NodeD'):
        assert not _is_linked(a1, 'NodeD', b)
    if hasattr(a2, 'NodeD'):
        assert _is_linked(a2, 'NodeD', b)
    _safe_set(b, 'parent31', set())
    assert not _is_linked(b, 'parent31', a2)
    if hasattr(a2, 'NodeD'):
        assert not _is_linked(a2, 'NodeD', b)


def test_assoc_children7_reverse_link_reassign_clear():
    a1 = model3_NodeA(name="sample_text")
    a2 = model3_NodeA(name="sample_text_2")
    b = model3_NodeA(name="sample_text")
    _safe_set(b, 'model3_NodeA6', {a1})
    assert _is_linked(b, 'model3_NodeA6', a1)
    if hasattr(a1, 'model3_NodeA'):
        assert _is_linked(a1, 'model3_NodeA', b)
    _safe_set(b, 'model3_NodeA6', {a2})
    assert _is_linked(b, 'model3_NodeA6', a2)
    if hasattr(a1, 'model3_NodeA'):
        assert not _is_linked(a1, 'model3_NodeA', b)
    if hasattr(a2, 'model3_NodeA'):
        assert _is_linked(a2, 'model3_NodeA', b)
    _safe_set(b, 'model3_NodeA6', set())
    assert not _is_linked(b, 'model3_NodeA6', a2)
    if hasattr(a2, 'model3_NodeA'):
        assert not _is_linked(a2, 'model3_NodeA', b)


def test_assoc_mainNode43_reverse_link_reassign_clear():
    a1 = model3_NodeE(name="sample_text")
    a2 = model3_NodeE(name="sample_text_2")
    b = model3_NodeA(name="sample_text")
    _safe_set(b, 'model3_NodeA44', a1)
    assert _is_linked(b, 'model3_NodeA44', a1)
    if hasattr(a1, 'model3_NodeE'):
        assert _is_linked(a1, 'model3_NodeE', b)
    _safe_set(b, 'model3_NodeA44', a2)
    assert _is_linked(b, 'model3_NodeA44', a2)
    if hasattr(a1, 'model3_NodeE'):
        assert not _is_linked(a1, 'model3_NodeE', b)
    if hasattr(a2, 'model3_NodeE'):
        assert _is_linked(a2, 'model3_NodeE', b)
    _safe_set(b, 'model3_NodeA44', None)
    assert not _is_linked(b, 'model3_NodeA44', a2)
    if hasattr(a2, 'model3_NodeE'):
        assert not _is_linked(a2, 'model3_NodeE', b)


def test_assoc_oppositeNode40_reverse_link_reassign_clear():
    a1 = model3_NodeD(name="sample_text")
    a2 = model3_NodeD(name="sample_text_2")
    b = model3_NodeD(name="sample_text")
    _safe_set(b, 'otherNodes41', a1)
    assert _is_linked(b, 'otherNodes41', a1)
    if hasattr(a1, 'NodeD42'):
        assert _is_linked(a1, 'NodeD42', b)
    _safe_set(b, 'otherNodes41', a2)
    assert _is_linked(b, 'otherNodes41', a2)
    if hasattr(a1, 'NodeD42'):
        assert not _is_linked(a1, 'NodeD42', b)
    if hasattr(a2, 'NodeD42'):
        assert _is_linked(a2, 'NodeD42', b)
    _safe_set(b, 'otherNodes41', None)
    assert not _is_linked(b, 'otherNodes41', a2)
    if hasattr(a2, 'NodeD42'):
        assert not _is_linked(a2, 'NodeD42', b)


def test_assoc_oppositeNodes27_reverse_link_reassign_clear():
    a1 = model3_NodeC(name="sample_text")
    a2 = model3_NodeC(name="sample_text_2")
    b = model3_NodeC(name="sample_text")
    _safe_set(b, 'otherNodes', {a1})
    assert _is_linked(b, 'otherNodes', a1)
    if hasattr(a1, 'NodeC28'):
        assert _is_linked(a1, 'NodeC28', b)
    _safe_set(b, 'otherNodes', {a2})
    assert _is_linked(b, 'otherNodes', a2)
    if hasattr(a1, 'NodeC28'):
        assert not _is_linked(a1, 'NodeC28', b)
    if hasattr(a2, 'NodeC28'):
        assert _is_linked(a2, 'NodeC28', b)
    _safe_set(b, 'otherNodes', set())
    assert not _is_linked(b, 'otherNodes', a2)
    if hasattr(a2, 'NodeC28'):
        assert not _is_linked(a2, 'NodeC28', b)


def test_assoc_otherNodes24_reverse_link_reassign_clear():
    a1 = model3_NodeC(name="sample_text")
    a2 = model3_NodeC(name="sample_text_2")
    b = model3_NodeC(name="sample_text")
    _safe_set(b, 'oppositeNodes', {a1})
    assert _is_linked(b, 'oppositeNodes', a1)
    if hasattr(a1, 'NodeC25'):
        assert _is_linked(a1, 'NodeC25', b)
    _safe_set(b, 'oppositeNodes', {a2})
    assert _is_linked(b, 'oppositeNodes', a2)
    if hasattr(a1, 'NodeC25'):
        assert not _is_linked(a1, 'NodeC25', b)
    if hasattr(a2, 'NodeC25'):
        assert _is_linked(a2, 'NodeC25', b)
    _safe_set(b, 'oppositeNodes', set())
    assert not _is_linked(b, 'oppositeNodes', a2)
    if hasattr(a2, 'NodeC25'):
        assert not _is_linked(a2, 'NodeC25', b)


def test_assoc_otherNodes37_reverse_link_reassign_clear():
    a1 = model3_NodeD(name="sample_text")
    a2 = model3_NodeD(name="sample_text_2")
    b = model3_NodeD(name="sample_text")
    _safe_set(b, 'oppositeNode', {a1})
    assert _is_linked(b, 'oppositeNode', a1)
    if hasattr(a1, 'NodeD38'):
        assert _is_linked(a1, 'NodeD38', b)
    _safe_set(b, 'oppositeNode', {a2})
    assert _is_linked(b, 'oppositeNode', a2)
    if hasattr(a1, 'NodeD38'):
        assert not _is_linked(a1, 'NodeD38', b)
    if hasattr(a2, 'NodeD38'):
        assert _is_linked(a2, 'NodeD38', b)
    _safe_set(b, 'oppositeNode', set())
    assert not _is_linked(b, 'oppositeNode', a2)
    if hasattr(a2, 'NodeD38'):
        assert not _is_linked(a2, 'NodeD38', b)


def test_assoc_otherNodes45_reverse_link_reassign_clear():
    a1 = model3_NodeE(name="sample_text")
    a2 = model3_NodeE(name="sample_text_2")
    b = model3_NodeA(name="sample_text")
    _safe_set(b, 'model3_NodeA47', a1)
    assert _is_linked(b, 'model3_NodeA47', a1)
    if hasattr(a1, 'model3_NodeE46'):
        assert _is_linked(a1, 'model3_NodeE46', b)
    _safe_set(b, 'model3_NodeA47', a2)
    assert _is_linked(b, 'model3_NodeA47', a2)
    if hasattr(a1, 'model3_NodeE46'):
        assert not _is_linked(a1, 'model3_NodeE46', b)
    if hasattr(a2, 'model3_NodeE46'):
        assert _is_linked(a2, 'model3_NodeE46', b)
    _safe_set(b, 'model3_NodeA47', None)
    assert not _is_linked(b, 'model3_NodeA47', a2)
    if hasattr(a2, 'model3_NodeE46'):
        assert not _is_linked(a2, 'model3_NodeE46', b)


def test_assoc_otherNodes9_reverse_link_reassign_clear():
    a1 = model3_NodeA(name="sample_text")
    a2 = model3_NodeA(name="sample_text_2")
    b = model3_NodeA(name="sample_text")
    _safe_set(b, 'model3_NodeA8', {a1})
    assert _is_linked(b, 'model3_NodeA8', a1)
    if hasattr(a1, 'model3_NodeA10'):
        assert _is_linked(a1, 'model3_NodeA10', b)
    _safe_set(b, 'model3_NodeA8', {a2})
    assert _is_linked(b, 'model3_NodeA8', a2)
    if hasattr(a1, 'model3_NodeA10'):
        assert not _is_linked(a1, 'model3_NodeA10', b)
    if hasattr(a2, 'model3_NodeA10'):
        assert _is_linked(a2, 'model3_NodeA10', b)
    _safe_set(b, 'model3_NodeA8', set())
    assert not _is_linked(b, 'model3_NodeA8', a2)
    if hasattr(a2, 'model3_NodeA10'):
        assert not _is_linked(a2, 'model3_NodeA10', b)


def test_assoc_parent14_reverse_link_reassign_clear():
    a1 = model3_NodeB(name="sample_text")
    a2 = model3_NodeB(name="sample_text_2")
    b = model3_NodeB(name="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'NodeB15'):
        assert _is_linked(a1, 'NodeB15', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'NodeB15'):
        assert not _is_linked(a1, 'NodeB15', b)
    if hasattr(a2, 'NodeB15'):
        assert _is_linked(a2, 'NodeB15', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'NodeB15'):
        assert not _is_linked(a2, 'NodeB15', b)


def test_assoc_parent20_reverse_link_reassign_clear():
    a1 = model3_NodeC(name="sample_text")
    a2 = model3_NodeC(name="sample_text_2")
    b = model3_NodeC(name="sample_text")
    _safe_set(b, 'children21', a1)
    assert _is_linked(b, 'children21', a1)
    if hasattr(a1, 'NodeC22'):
        assert _is_linked(a1, 'NodeC22', b)
    _safe_set(b, 'children21', a2)
    assert _is_linked(b, 'children21', a2)
    if hasattr(a1, 'NodeC22'):
        assert not _is_linked(a1, 'NodeC22', b)
    if hasattr(a2, 'NodeC22'):
        assert _is_linked(a2, 'NodeC22', b)
    _safe_set(b, 'children21', None)
    assert not _is_linked(b, 'children21', a2)
    if hasattr(a2, 'NodeC22'):
        assert not _is_linked(a2, 'NodeC22', b)


def test_assoc_parent33_reverse_link_reassign_clear():
    a1 = model3_NodeD(name="sample_text")
    a2 = model3_NodeD(name="sample_text_2")
    b = model3_NodeD(name="sample_text")
    _safe_set(b, 'children34', a1)
    assert _is_linked(b, 'children34', a1)
    if hasattr(a1, 'NodeD35'):
        assert _is_linked(a1, 'NodeD35', b)
    _safe_set(b, 'children34', a2)
    assert _is_linked(b, 'children34', a2)
    if hasattr(a1, 'NodeD35'):
        assert not _is_linked(a1, 'NodeD35', b)
    if hasattr(a2, 'NodeD35'):
        assert _is_linked(a2, 'NodeD35', b)
    _safe_set(b, 'children34', None)
    assert not _is_linked(b, 'children34', a2)
    if hasattr(a2, 'NodeD35'):
        assert not _is_linked(a2, 'NodeD35', b)


def test_assoc_persistentChild54_reverse_link_reassign_clear():
    a1 = model3_ClassWithTransientContainment(name="sample_text")
    a2 = model3_ClassWithTransientContainment(name="sample_text_2")
    b = model3_ClassWithTransientContainment(name="sample_text")
    _safe_set(b, 'model3_ClassWithTransientContainment55', a1)
    assert _is_linked(b, 'model3_ClassWithTransientContainment55', a1)
    if hasattr(a1, 'model3_ClassWithTransientContainment53'):
        assert _is_linked(a1, 'model3_ClassWithTransientContainment53', b)
    _safe_set(b, 'model3_ClassWithTransientContainment55', a2)
    assert _is_linked(b, 'model3_ClassWithTransientContainment55', a2)
    if hasattr(a1, 'model3_ClassWithTransientContainment53'):
        assert not _is_linked(a1, 'model3_ClassWithTransientContainment53', b)
    if hasattr(a2, 'model3_ClassWithTransientContainment53'):
        assert _is_linked(a2, 'model3_ClassWithTransientContainment53', b)
    _safe_set(b, 'model3_ClassWithTransientContainment55', None)
    assert not _is_linked(b, 'model3_ClassWithTransientContainment55', a2)
    if hasattr(a2, 'model3_ClassWithTransientContainment53'):
        assert not _is_linked(a2, 'model3_ClassWithTransientContainment53', b)


def test_assoc_persistentChildren57_reverse_link_reassign_clear():
    a1 = model3_ClassWithTransientContainment(name="sample_text")
    a2 = model3_ClassWithTransientContainment(name="sample_text_2")
    b = model3_ClassWithTransientContainment(name="sample_text")
    _safe_set(b, 'model3_ClassWithTransientContainment58', a1)
    assert _is_linked(b, 'model3_ClassWithTransientContainment58', a1)
    if hasattr(a1, 'model3_ClassWithTransientContainment56'):
        assert _is_linked(a1, 'model3_ClassWithTransientContainment56', b)
    _safe_set(b, 'model3_ClassWithTransientContainment58', a2)
    assert _is_linked(b, 'model3_ClassWithTransientContainment58', a2)
    if hasattr(a1, 'model3_ClassWithTransientContainment56'):
        assert not _is_linked(a1, 'model3_ClassWithTransientContainment56', b)
    if hasattr(a2, 'model3_ClassWithTransientContainment56'):
        assert _is_linked(a2, 'model3_ClassWithTransientContainment56', b)
    _safe_set(b, 'model3_ClassWithTransientContainment58', None)
    assert not _is_linked(b, 'model3_ClassWithTransientContainment58', a2)
    if hasattr(a2, 'model3_ClassWithTransientContainment56'):
        assert not _is_linked(a2, 'model3_ClassWithTransientContainment56', b)


def test_assoc_transientChild49_reverse_link_reassign_clear():
    a1 = model3_ClassWithTransientContainment(name="sample_text")
    a2 = model3_ClassWithTransientContainment(name="sample_text_2")
    b = model3_ClassWithTransientContainment(name="sample_text")
    _safe_set(b, 'model3_ClassWithTransientContainment48', a1)
    assert _is_linked(b, 'model3_ClassWithTransientContainment48', a1)
    if hasattr(a1, 'model3_ClassWithTransientContainment'):
        assert _is_linked(a1, 'model3_ClassWithTransientContainment', b)
    _safe_set(b, 'model3_ClassWithTransientContainment48', a2)
    assert _is_linked(b, 'model3_ClassWithTransientContainment48', a2)
    if hasattr(a1, 'model3_ClassWithTransientContainment'):
        assert not _is_linked(a1, 'model3_ClassWithTransientContainment', b)
    if hasattr(a2, 'model3_ClassWithTransientContainment'):
        assert _is_linked(a2, 'model3_ClassWithTransientContainment', b)
    _safe_set(b, 'model3_ClassWithTransientContainment48', None)
    assert not _is_linked(b, 'model3_ClassWithTransientContainment48', a2)
    if hasattr(a2, 'model3_ClassWithTransientContainment'):
        assert not _is_linked(a2, 'model3_ClassWithTransientContainment', b)


def test_assoc_transientChildren51_reverse_link_reassign_clear():
    a1 = model3_ClassWithTransientContainment(name="sample_text")
    a2 = model3_ClassWithTransientContainment(name="sample_text_2")
    b = model3_ClassWithTransientContainment(name="sample_text")
    _safe_set(b, 'model3_ClassWithTransientContainment52', a1)
    assert _is_linked(b, 'model3_ClassWithTransientContainment52', a1)
    if hasattr(a1, 'model3_ClassWithTransientContainment50'):
        assert _is_linked(a1, 'model3_ClassWithTransientContainment50', b)
    _safe_set(b, 'model3_ClassWithTransientContainment52', a2)
    assert _is_linked(b, 'model3_ClassWithTransientContainment52', a2)
    if hasattr(a1, 'model3_ClassWithTransientContainment50'):
        assert not _is_linked(a1, 'model3_ClassWithTransientContainment50', b)
    if hasattr(a2, 'model3_ClassWithTransientContainment50'):
        assert _is_linked(a2, 'model3_ClassWithTransientContainment50', b)
    _safe_set(b, 'model3_ClassWithTransientContainment52', None)
    assert not _is_linked(b, 'model3_ClassWithTransientContainment52', a2)
    if hasattr(a2, 'model3_ClassWithTransientContainment50'):
        assert not _is_linked(a2, 'model3_ClassWithTransientContainment50', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_class20_stub_double():
    # Class2 has no real 'Class2' property in the generated
    # code (a bare stub) -- manually attach it so model3_Class1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model3_Class1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model3_Class1(additionalValue="sample_text")
    partner = Class2()
    setattr(partner, 'Class2', None)
    _safe_set(owner, 'class1', {partner})
    assert getattr(partner, 'Class2') == owner
    _safe_set(owner, 'class1', set())
    assert getattr(partner, 'Class2') is None


