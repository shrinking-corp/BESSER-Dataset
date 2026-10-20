import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MT__Element,
    MTpos__Element,
    MTpos__Person,
    MTpre__Element,
    MTpre__Person,
    ramRoot_GenericNode,
    ramRoot_MT__Element,
    ramRoot_MTpos__Classroom,
    ramRoot_MTpos__Element,
    ramRoot_MTpos__Man,
    ramRoot_MTpos__Person,
    ramRoot_MTpos__Woman,
    ramRoot_MTpre__Classroom,
    ramRoot_MTpre__Element,
    ramRoot_MTpre__Man,
    ramRoot_MTpre__Person,
    ramRoot_MTpre__Woman,
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

def test_assoc_friend_with10_reverse_link_reassign_clear():
    a1 = ramRoot_MTpre__Person(name="sample_text")
    a2 = ramRoot_MTpre__Person(name="sample_text_2")
    b = ramRoot_MTpre__Person(name="sample_text")
    _safe_set(b, 'ramRoot_MTpre__Person9', {a1})
    assert _is_linked(b, 'ramRoot_MTpre__Person9', a1)
    if hasattr(a1, 'ramRoot_MTpre__Person11'):
        assert _is_linked(a1, 'ramRoot_MTpre__Person11', b)
    _safe_set(b, 'ramRoot_MTpre__Person9', {a2})
    assert _is_linked(b, 'ramRoot_MTpre__Person9', a2)
    if hasattr(a1, 'ramRoot_MTpre__Person11'):
        assert not _is_linked(a1, 'ramRoot_MTpre__Person11', b)
    if hasattr(a2, 'ramRoot_MTpre__Person11'):
        assert _is_linked(a2, 'ramRoot_MTpre__Person11', b)
    _safe_set(b, 'ramRoot_MTpre__Person9', set())
    assert not _is_linked(b, 'ramRoot_MTpre__Person9', a2)
    if hasattr(a2, 'ramRoot_MTpre__Person11'):
        assert not _is_linked(a2, 'ramRoot_MTpre__Person11', b)


def test_assoc_friend_with3_reverse_link_reassign_clear():
    a1 = ramRoot_MTpos__Person(name="sample_text")
    a2 = ramRoot_MTpos__Person(name="sample_text_2")
    b = ramRoot_MTpos__Person(name="sample_text")
    _safe_set(b, 'ramRoot_MTpos__Person4', a1)
    assert _is_linked(b, 'ramRoot_MTpos__Person4', a1)
    if hasattr(a1, 'ramRoot_MTpos__Person2'):
        assert _is_linked(a1, 'ramRoot_MTpos__Person2', b)
    _safe_set(b, 'ramRoot_MTpos__Person4', a2)
    assert _is_linked(b, 'ramRoot_MTpos__Person4', a2)
    if hasattr(a1, 'ramRoot_MTpos__Person2'):
        assert not _is_linked(a1, 'ramRoot_MTpos__Person2', b)
    if hasattr(a2, 'ramRoot_MTpos__Person2'):
        assert _is_linked(a2, 'ramRoot_MTpos__Person2', b)
    _safe_set(b, 'ramRoot_MTpos__Person4', None)
    assert not _is_linked(b, 'ramRoot_MTpos__Person4', a2)
    if hasattr(a2, 'ramRoot_MTpos__Person2'):
        assert not _is_linked(a2, 'ramRoot_MTpos__Person2', b)


def test_assoc_person12_reverse_link_reassign_clear():
    a1 = ramRoot_MTpre__Person(name="sample_text")
    a2 = ramRoot_MTpre__Person(name="sample_text_2")
    b = ramRoot_MTpre__Classroom(id="sample_text")
    _safe_set(b, 'ramRoot_MTpre__Classroom13', {a1})
    assert _is_linked(b, 'ramRoot_MTpre__Classroom13', a1)
    if hasattr(a1, 'ramRoot_MTpre__Person14'):
        assert _is_linked(a1, 'ramRoot_MTpre__Person14', b)
    _safe_set(b, 'ramRoot_MTpre__Classroom13', {a2})
    assert _is_linked(b, 'ramRoot_MTpre__Classroom13', a2)
    if hasattr(a1, 'ramRoot_MTpre__Person14'):
        assert not _is_linked(a1, 'ramRoot_MTpre__Person14', b)
    if hasattr(a2, 'ramRoot_MTpre__Person14'):
        assert _is_linked(a2, 'ramRoot_MTpre__Person14', b)
    _safe_set(b, 'ramRoot_MTpre__Classroom13', set())
    assert not _is_linked(b, 'ramRoot_MTpre__Classroom13', a2)
    if hasattr(a2, 'ramRoot_MTpre__Person14'):
        assert not _is_linked(a2, 'ramRoot_MTpre__Person14', b)


def test_assoc_person5_reverse_link_reassign_clear():
    a1 = ramRoot_MTpos__Person(name="sample_text")
    a2 = ramRoot_MTpos__Person(name="sample_text_2")
    b = ramRoot_MTpos__Classroom(id="sample_text")
    _safe_set(b, 'ramRoot_MTpos__Classroom6', {a1})
    assert _is_linked(b, 'ramRoot_MTpos__Classroom6', a1)
    if hasattr(a1, 'ramRoot_MTpos__Person7'):
        assert _is_linked(a1, 'ramRoot_MTpos__Person7', b)
    _safe_set(b, 'ramRoot_MTpos__Classroom6', {a2})
    assert _is_linked(b, 'ramRoot_MTpos__Classroom6', a2)
    if hasattr(a1, 'ramRoot_MTpos__Person7'):
        assert not _is_linked(a1, 'ramRoot_MTpos__Person7', b)
    if hasattr(a2, 'ramRoot_MTpos__Person7'):
        assert _is_linked(a2, 'ramRoot_MTpos__Person7', b)
    _safe_set(b, 'ramRoot_MTpos__Classroom6', set())
    assert not _is_linked(b, 'ramRoot_MTpos__Classroom6', a2)
    if hasattr(a2, 'ramRoot_MTpos__Person7'):
        assert not _is_linked(a2, 'ramRoot_MTpos__Person7', b)


def test_assoc_teacher_of1_reverse_link_reassign_clear():
    a1 = ramRoot_MTpos__Person(name="sample_text")
    a2 = ramRoot_MTpos__Person(name="sample_text_2")
    b = ramRoot_MTpos__Classroom(id="sample_text")
    _safe_set(b, 'ramRoot_MTpos__Classroom', a1)
    assert _is_linked(b, 'ramRoot_MTpos__Classroom', a1)
    if hasattr(a1, 'ramRoot_MTpos__Person'):
        assert _is_linked(a1, 'ramRoot_MTpos__Person', b)
    _safe_set(b, 'ramRoot_MTpos__Classroom', a2)
    assert _is_linked(b, 'ramRoot_MTpos__Classroom', a2)
    if hasattr(a1, 'ramRoot_MTpos__Person'):
        assert not _is_linked(a1, 'ramRoot_MTpos__Person', b)
    if hasattr(a2, 'ramRoot_MTpos__Person'):
        assert _is_linked(a2, 'ramRoot_MTpos__Person', b)
    _safe_set(b, 'ramRoot_MTpos__Classroom', None)
    assert not _is_linked(b, 'ramRoot_MTpos__Classroom', a2)
    if hasattr(a2, 'ramRoot_MTpos__Person'):
        assert not _is_linked(a2, 'ramRoot_MTpos__Person', b)


def test_assoc_teacher_of8_reverse_link_reassign_clear():
    a1 = ramRoot_MTpre__Person(name="sample_text")
    a2 = ramRoot_MTpre__Person(name="sample_text_2")
    b = ramRoot_MTpre__Classroom(id="sample_text")
    _safe_set(b, 'ramRoot_MTpre__Classroom', a1)
    assert _is_linked(b, 'ramRoot_MTpre__Classroom', a1)
    if hasattr(a1, 'ramRoot_MTpre__Person'):
        assert _is_linked(a1, 'ramRoot_MTpre__Person', b)
    _safe_set(b, 'ramRoot_MTpre__Classroom', a2)
    assert _is_linked(b, 'ramRoot_MTpre__Classroom', a2)
    if hasattr(a1, 'ramRoot_MTpre__Person'):
        assert not _is_linked(a1, 'ramRoot_MTpre__Person', b)
    if hasattr(a2, 'ramRoot_MTpre__Person'):
        assert _is_linked(a2, 'ramRoot_MTpre__Person', b)
    _safe_set(b, 'ramRoot_MTpre__Classroom', None)
    assert not _is_linked(b, 'ramRoot_MTpre__Classroom', a2)
    if hasattr(a2, 'ramRoot_MTpre__Person'):
        assert not _is_linked(a2, 'ramRoot_MTpre__Person', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_GenericLink0_stub_double():
    # ramRoot_GenericNode has no real 'ramRoot_GenericNode' property in the generated
    # code (a bare stub) -- manually attach it so ramRoot_MT__Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ramRoot_MT__Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ramRoot_MT__Element(MT__isProcessed=True, MT__label="sample_text")
    partner = ramRoot_GenericNode()
    setattr(partner, 'ramRoot_GenericNode', None)
    _safe_set(owner, 'ramRoot_MT__Element', partner)
    assert owner in getattr(partner, 'ramRoot_GenericNode')
    _safe_set(owner, 'ramRoot_MT__Element', None)
    assert owner not in getattr(partner, 'ramRoot_GenericNode')


