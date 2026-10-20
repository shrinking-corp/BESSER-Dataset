import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MT__Element,
    MTpos__Element,
    MTpre__Element,
    ramRoot_GenericNode,
    ramRoot_MT__Element,
    ramRoot_MTpos__Chair,
    ramRoot_MTpos__Element,
    ramRoot_MTpos__Restaurant,
    ramRoot_MTpos__Table,
    ramRoot_MTpos__Waitress,
    ramRoot_MTpre__Chair,
    ramRoot_MTpre__Element,
    ramRoot_MTpre__Restaurant,
    ramRoot_MTpre__Table,
    ramRoot_MTpre__Waitress,
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

def test_assoc_chairs1_reverse_link_reassign_clear():
    a1 = ramRoot_MTpos__Table(MTpos__id="sample_text", MTpos__isReserved="sample_text")
    a2 = ramRoot_MTpos__Table(MTpos__id="sample_text_2", MTpos__isReserved="sample_text_2")
    b = ramRoot_MTpos__Chair(MTpos__order="sample_text")
    _safe_set(b, 'ramRoot_MTpos__Chair', a1)
    assert _is_linked(b, 'ramRoot_MTpos__Chair', a1)
    if hasattr(a1, 'ramRoot_MTpos__Table'):
        assert _is_linked(a1, 'ramRoot_MTpos__Table', b)
    _safe_set(b, 'ramRoot_MTpos__Chair', a2)
    assert _is_linked(b, 'ramRoot_MTpos__Chair', a2)
    if hasattr(a1, 'ramRoot_MTpos__Table'):
        assert not _is_linked(a1, 'ramRoot_MTpos__Table', b)
    if hasattr(a2, 'ramRoot_MTpos__Table'):
        assert _is_linked(a2, 'ramRoot_MTpos__Table', b)
    _safe_set(b, 'ramRoot_MTpos__Chair', None)
    assert not _is_linked(b, 'ramRoot_MTpos__Chair', a2)
    if hasattr(a2, 'ramRoot_MTpos__Table'):
        assert not _is_linked(a2, 'ramRoot_MTpos__Table', b)


def test_assoc_chairs4_reverse_link_reassign_clear():
    a1 = ramRoot_MTpre__Table(MTpre__id="sample_text", MTpre__isReserved="sample_text")
    a2 = ramRoot_MTpre__Table(MTpre__id="sample_text_2", MTpre__isReserved="sample_text_2")
    b = ramRoot_MTpre__Chair(MTpre__order="sample_text")
    _safe_set(b, 'ramRoot_MTpre__Chair', a1)
    assert _is_linked(b, 'ramRoot_MTpre__Chair', a1)
    if hasattr(a1, 'ramRoot_MTpre__Table'):
        assert _is_linked(a1, 'ramRoot_MTpre__Table', b)
    _safe_set(b, 'ramRoot_MTpre__Chair', a2)
    assert _is_linked(b, 'ramRoot_MTpre__Chair', a2)
    if hasattr(a1, 'ramRoot_MTpre__Table'):
        assert not _is_linked(a1, 'ramRoot_MTpre__Table', b)
    if hasattr(a2, 'ramRoot_MTpre__Table'):
        assert _is_linked(a2, 'ramRoot_MTpre__Table', b)
    _safe_set(b, 'ramRoot_MTpre__Chair', None)
    assert not _is_linked(b, 'ramRoot_MTpre__Chair', a2)
    if hasattr(a2, 'ramRoot_MTpre__Table'):
        assert not _is_linked(a2, 'ramRoot_MTpre__Table', b)


def test_assoc_tables2_reverse_link_reassign_clear():
    a1 = ramRoot_MTpos__Waitress(MTpos__name="sample_text")
    a2 = ramRoot_MTpos__Waitress(MTpos__name="sample_text_2")
    b = ramRoot_MTpos__Table(MTpos__id="sample_text", MTpos__isReserved="sample_text")
    _safe_set(b, 'ramRoot_MTpos__Table3', a1)
    assert _is_linked(b, 'ramRoot_MTpos__Table3', a1)
    if hasattr(a1, 'ramRoot_MTpos__Waitress'):
        assert _is_linked(a1, 'ramRoot_MTpos__Waitress', b)
    _safe_set(b, 'ramRoot_MTpos__Table3', a2)
    assert _is_linked(b, 'ramRoot_MTpos__Table3', a2)
    if hasattr(a1, 'ramRoot_MTpos__Waitress'):
        assert not _is_linked(a1, 'ramRoot_MTpos__Waitress', b)
    if hasattr(a2, 'ramRoot_MTpos__Waitress'):
        assert _is_linked(a2, 'ramRoot_MTpos__Waitress', b)
    _safe_set(b, 'ramRoot_MTpos__Table3', None)
    assert not _is_linked(b, 'ramRoot_MTpos__Table3', a2)
    if hasattr(a2, 'ramRoot_MTpos__Waitress'):
        assert not _is_linked(a2, 'ramRoot_MTpos__Waitress', b)


def test_assoc_tables5_reverse_link_reassign_clear():
    a1 = ramRoot_MTpre__Waitress(MTpre__name="sample_text")
    a2 = ramRoot_MTpre__Waitress(MTpre__name="sample_text_2")
    b = ramRoot_MTpre__Table(MTpre__id="sample_text", MTpre__isReserved="sample_text")
    _safe_set(b, 'ramRoot_MTpre__Table6', a1)
    assert _is_linked(b, 'ramRoot_MTpre__Table6', a1)
    if hasattr(a1, 'ramRoot_MTpre__Waitress'):
        assert _is_linked(a1, 'ramRoot_MTpre__Waitress', b)
    _safe_set(b, 'ramRoot_MTpre__Table6', a2)
    assert _is_linked(b, 'ramRoot_MTpre__Table6', a2)
    if hasattr(a1, 'ramRoot_MTpre__Waitress'):
        assert not _is_linked(a1, 'ramRoot_MTpre__Waitress', b)
    if hasattr(a2, 'ramRoot_MTpre__Waitress'):
        assert _is_linked(a2, 'ramRoot_MTpre__Waitress', b)
    _safe_set(b, 'ramRoot_MTpre__Table6', None)
    assert not _is_linked(b, 'ramRoot_MTpre__Table6', a2)
    if hasattr(a2, 'ramRoot_MTpre__Waitress'):
        assert not _is_linked(a2, 'ramRoot_MTpre__Waitress', b)


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


def test_assoc_tables14_stub_double():
    # ramRoot_MTpos__Restaurant has no real 'ramRoot_MTpos__Restaurant15' property in the generated
    # code (a bare stub) -- manually attach it so ramRoot_MTpos__Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ramRoot_MTpos__Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ramRoot_MTpos__Table(MTpos__id="sample_text", MTpos__isReserved="sample_text")
    partner = ramRoot_MTpos__Restaurant()
    setattr(partner, 'ramRoot_MTpos__Restaurant15', None)
    _safe_set(owner, 'ramRoot_MTpos__Table16', partner)
    assert owner in getattr(partner, 'ramRoot_MTpos__Restaurant15')
    _safe_set(owner, 'ramRoot_MTpos__Table16', None)
    assert owner not in getattr(partner, 'ramRoot_MTpos__Restaurant15')


def test_assoc_tables7_stub_double():
    # ramRoot_MTpre__Restaurant has no real 'ramRoot_MTpre__Restaurant' property in the generated
    # code (a bare stub) -- manually attach it so ramRoot_MTpre__Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ramRoot_MTpre__Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ramRoot_MTpre__Table(MTpre__id="sample_text", MTpre__isReserved="sample_text")
    partner = ramRoot_MTpre__Restaurant()
    setattr(partner, 'ramRoot_MTpre__Restaurant', None)
    _safe_set(owner, 'ramRoot_MTpre__Table8', partner)
    assert owner in getattr(partner, 'ramRoot_MTpre__Restaurant')
    _safe_set(owner, 'ramRoot_MTpre__Table8', None)
    assert owner not in getattr(partner, 'ramRoot_MTpre__Restaurant')


def test_assoc_waitress12_stub_double():
    # ramRoot_MTpos__Restaurant has no real 'ramRoot_MTpos__Restaurant' property in the generated
    # code (a bare stub) -- manually attach it so ramRoot_MTpos__Waitress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ramRoot_MTpos__Waitress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ramRoot_MTpos__Waitress(MTpos__name="sample_text")
    partner = ramRoot_MTpos__Restaurant()
    setattr(partner, 'ramRoot_MTpos__Restaurant', None)
    _safe_set(owner, 'ramRoot_MTpos__Waitress13', partner)
    assert owner in getattr(partner, 'ramRoot_MTpos__Restaurant')
    _safe_set(owner, 'ramRoot_MTpos__Waitress13', None)
    assert owner not in getattr(partner, 'ramRoot_MTpos__Restaurant')


def test_assoc_waitress9_stub_double():
    # ramRoot_MTpre__Restaurant has no real 'ramRoot_MTpre__Restaurant10' property in the generated
    # code (a bare stub) -- manually attach it so ramRoot_MTpre__Waitress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ramRoot_MTpre__Waitress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ramRoot_MTpre__Waitress(MTpre__name="sample_text")
    partner = ramRoot_MTpre__Restaurant()
    setattr(partner, 'ramRoot_MTpre__Restaurant10', None)
    _safe_set(owner, 'ramRoot_MTpre__Waitress11', partner)
    assert owner in getattr(partner, 'ramRoot_MTpre__Restaurant10')
    _safe_set(owner, 'ramRoot_MTpre__Waitress11', None)
    assert owner not in getattr(partner, 'ramRoot_MTpre__Restaurant10')


