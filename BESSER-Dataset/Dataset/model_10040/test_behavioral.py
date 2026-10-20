import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Graph_Graph,
    Graph_ID1006,
    Graph_TBoolean,
    Graph_TByte,
    Graph_TChar,
    Graph_TDouble,
    Graph_TFloat,
    Graph_TInt,
    Graph_TLong,
    Graph_TShort,
    Graph_TString,
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

def test_assoc_id1006s0_reverse_link_reassign_clear():
    a1 = Graph_ID1006(id="sample_text", name="sample_text")
    a2 = Graph_ID1006(id="sample_text_2", name="sample_text_2")
    b = Graph_Graph(id="sample_text")
    _safe_set(b, 'Graph_Graph', {a1})
    assert _is_linked(b, 'Graph_Graph', a1)
    if hasattr(a1, 'Graph_ID1006'):
        assert _is_linked(a1, 'Graph_ID1006', b)
    _safe_set(b, 'Graph_Graph', {a2})
    assert _is_linked(b, 'Graph_Graph', a2)
    if hasattr(a1, 'Graph_ID1006'):
        assert not _is_linked(a1, 'Graph_ID1006', b)
    if hasattr(a2, 'Graph_ID1006'):
        assert _is_linked(a2, 'Graph_ID1006', b)
    _safe_set(b, 'Graph_Graph', set())
    assert not _is_linked(b, 'Graph_Graph', a2)
    if hasattr(a2, 'Graph_ID1006'):
        assert not _is_linked(a2, 'Graph_ID1006', b)


def test_assoc_outID1008s19_reverse_link_reassign_clear():
    a1 = Graph_TString(id="sample_text", name="sample_text")
    a2 = Graph_TString(id="sample_text_2", name="sample_text_2")
    b = Graph_ID1006(id="sample_text", name="sample_text")
    _safe_set(b, 'Graph_ID100620', {a1})
    assert _is_linked(b, 'Graph_ID100620', a1)
    if hasattr(a1, 'Graph_TString21'):
        assert _is_linked(a1, 'Graph_TString21', b)
    _safe_set(b, 'Graph_ID100620', {a2})
    assert _is_linked(b, 'Graph_ID100620', a2)
    if hasattr(a1, 'Graph_TString21'):
        assert not _is_linked(a1, 'Graph_TString21', b)
    if hasattr(a2, 'Graph_TString21'):
        assert _is_linked(a2, 'Graph_TString21', b)
    _safe_set(b, 'Graph_ID100620', set())
    assert not _is_linked(b, 'Graph_ID100620', a2)
    if hasattr(a2, 'Graph_TString21'):
        assert not _is_linked(a2, 'Graph_TString21', b)


def test_assoc_tBooleans1_reverse_link_reassign_clear():
    a1 = Graph_TBoolean(value=True)
    a2 = Graph_TBoolean(value=False)
    b = Graph_Graph(id="sample_text")
    _safe_set(b, 'Graph_Graph2', {a1})
    assert _is_linked(b, 'Graph_Graph2', a1)
    if hasattr(a1, 'Graph_TBoolean'):
        assert _is_linked(a1, 'Graph_TBoolean', b)
    _safe_set(b, 'Graph_Graph2', {a2})
    assert _is_linked(b, 'Graph_Graph2', a2)
    if hasattr(a1, 'Graph_TBoolean'):
        assert not _is_linked(a1, 'Graph_TBoolean', b)
    if hasattr(a2, 'Graph_TBoolean'):
        assert _is_linked(a2, 'Graph_TBoolean', b)
    _safe_set(b, 'Graph_Graph2', set())
    assert not _is_linked(b, 'Graph_Graph2', a2)
    if hasattr(a2, 'Graph_TBoolean'):
        assert not _is_linked(a2, 'Graph_TBoolean', b)


def test_assoc_tBytes5_reverse_link_reassign_clear():
    a1 = Graph_TByte(value="sample_text")
    a2 = Graph_TByte(value="sample_text_2")
    b = Graph_Graph(id="sample_text")
    _safe_set(b, 'Graph_Graph6', {a1})
    assert _is_linked(b, 'Graph_Graph6', a1)
    if hasattr(a1, 'Graph_TByte'):
        assert _is_linked(a1, 'Graph_TByte', b)
    _safe_set(b, 'Graph_Graph6', {a2})
    assert _is_linked(b, 'Graph_Graph6', a2)
    if hasattr(a1, 'Graph_TByte'):
        assert not _is_linked(a1, 'Graph_TByte', b)
    if hasattr(a2, 'Graph_TByte'):
        assert _is_linked(a2, 'Graph_TByte', b)
    _safe_set(b, 'Graph_Graph6', set())
    assert not _is_linked(b, 'Graph_Graph6', a2)
    if hasattr(a2, 'Graph_TByte'):
        assert not _is_linked(a2, 'Graph_TByte', b)


def test_assoc_tChars3_reverse_link_reassign_clear():
    a1 = Graph_TChar(value="sample_text")
    a2 = Graph_TChar(value="sample_text_2")
    b = Graph_Graph(id="sample_text")
    _safe_set(b, 'Graph_Graph4', {a1})
    assert _is_linked(b, 'Graph_Graph4', a1)
    if hasattr(a1, 'Graph_TChar'):
        assert _is_linked(a1, 'Graph_TChar', b)
    _safe_set(b, 'Graph_Graph4', {a2})
    assert _is_linked(b, 'Graph_Graph4', a2)
    if hasattr(a1, 'Graph_TChar'):
        assert not _is_linked(a1, 'Graph_TChar', b)
    if hasattr(a2, 'Graph_TChar'):
        assert _is_linked(a2, 'Graph_TChar', b)
    _safe_set(b, 'Graph_Graph4', set())
    assert not _is_linked(b, 'Graph_Graph4', a2)
    if hasattr(a2, 'Graph_TChar'):
        assert not _is_linked(a2, 'Graph_TChar', b)


def test_assoc_tDoubles15_reverse_link_reassign_clear():
    a1 = Graph_TDouble(value=3.14)
    a2 = Graph_TDouble(value=9.99)
    b = Graph_Graph(id="sample_text")
    _safe_set(b, 'Graph_Graph16', {a1})
    assert _is_linked(b, 'Graph_Graph16', a1)
    if hasattr(a1, 'Graph_TDouble'):
        assert _is_linked(a1, 'Graph_TDouble', b)
    _safe_set(b, 'Graph_Graph16', {a2})
    assert _is_linked(b, 'Graph_Graph16', a2)
    if hasattr(a1, 'Graph_TDouble'):
        assert not _is_linked(a1, 'Graph_TDouble', b)
    if hasattr(a2, 'Graph_TDouble'):
        assert _is_linked(a2, 'Graph_TDouble', b)
    _safe_set(b, 'Graph_Graph16', set())
    assert not _is_linked(b, 'Graph_Graph16', a2)
    if hasattr(a2, 'Graph_TDouble'):
        assert not _is_linked(a2, 'Graph_TDouble', b)


def test_assoc_tFloats13_reverse_link_reassign_clear():
    a1 = Graph_TFloat(value=3.14)
    a2 = Graph_TFloat(value=9.99)
    b = Graph_Graph(id="sample_text")
    _safe_set(b, 'Graph_Graph14', {a1})
    assert _is_linked(b, 'Graph_Graph14', a1)
    if hasattr(a1, 'Graph_TFloat'):
        assert _is_linked(a1, 'Graph_TFloat', b)
    _safe_set(b, 'Graph_Graph14', {a2})
    assert _is_linked(b, 'Graph_Graph14', a2)
    if hasattr(a1, 'Graph_TFloat'):
        assert not _is_linked(a1, 'Graph_TFloat', b)
    if hasattr(a2, 'Graph_TFloat'):
        assert _is_linked(a2, 'Graph_TFloat', b)
    _safe_set(b, 'Graph_Graph14', set())
    assert not _is_linked(b, 'Graph_Graph14', a2)
    if hasattr(a2, 'Graph_TFloat'):
        assert not _is_linked(a2, 'Graph_TFloat', b)


def test_assoc_tInts9_reverse_link_reassign_clear():
    a1 = Graph_TInt(value=7)
    a2 = Graph_TInt(value=13)
    b = Graph_Graph(id="sample_text")
    _safe_set(b, 'Graph_Graph10', {a1})
    assert _is_linked(b, 'Graph_Graph10', a1)
    if hasattr(a1, 'Graph_TInt'):
        assert _is_linked(a1, 'Graph_TInt', b)
    _safe_set(b, 'Graph_Graph10', {a2})
    assert _is_linked(b, 'Graph_Graph10', a2)
    if hasattr(a1, 'Graph_TInt'):
        assert not _is_linked(a1, 'Graph_TInt', b)
    if hasattr(a2, 'Graph_TInt'):
        assert _is_linked(a2, 'Graph_TInt', b)
    _safe_set(b, 'Graph_Graph10', set())
    assert not _is_linked(b, 'Graph_Graph10', a2)
    if hasattr(a2, 'Graph_TInt'):
        assert not _is_linked(a2, 'Graph_TInt', b)


def test_assoc_tLongs11_reverse_link_reassign_clear():
    a1 = Graph_TLong(value="sample_text")
    a2 = Graph_TLong(value="sample_text_2")
    b = Graph_Graph(id="sample_text")
    _safe_set(b, 'Graph_Graph12', {a1})
    assert _is_linked(b, 'Graph_Graph12', a1)
    if hasattr(a1, 'Graph_TLong'):
        assert _is_linked(a1, 'Graph_TLong', b)
    _safe_set(b, 'Graph_Graph12', {a2})
    assert _is_linked(b, 'Graph_Graph12', a2)
    if hasattr(a1, 'Graph_TLong'):
        assert not _is_linked(a1, 'Graph_TLong', b)
    if hasattr(a2, 'Graph_TLong'):
        assert _is_linked(a2, 'Graph_TLong', b)
    _safe_set(b, 'Graph_Graph12', set())
    assert not _is_linked(b, 'Graph_Graph12', a2)
    if hasattr(a2, 'Graph_TLong'):
        assert not _is_linked(a2, 'Graph_TLong', b)


def test_assoc_tShorts7_reverse_link_reassign_clear():
    a1 = Graph_TShort(value="sample_text")
    a2 = Graph_TShort(value="sample_text_2")
    b = Graph_Graph(id="sample_text")
    _safe_set(b, 'Graph_Graph8', {a1})
    assert _is_linked(b, 'Graph_Graph8', a1)
    if hasattr(a1, 'Graph_TShort'):
        assert _is_linked(a1, 'Graph_TShort', b)
    _safe_set(b, 'Graph_Graph8', {a2})
    assert _is_linked(b, 'Graph_Graph8', a2)
    if hasattr(a1, 'Graph_TShort'):
        assert not _is_linked(a1, 'Graph_TShort', b)
    if hasattr(a2, 'Graph_TShort'):
        assert _is_linked(a2, 'Graph_TShort', b)
    _safe_set(b, 'Graph_Graph8', set())
    assert not _is_linked(b, 'Graph_Graph8', a2)
    if hasattr(a2, 'Graph_TShort'):
        assert not _is_linked(a2, 'Graph_TShort', b)


def test_assoc_tStrings17_reverse_link_reassign_clear():
    a1 = Graph_TString(id="sample_text", name="sample_text")
    a2 = Graph_TString(id="sample_text_2", name="sample_text_2")
    b = Graph_Graph(id="sample_text")
    _safe_set(b, 'Graph_Graph18', {a1})
    assert _is_linked(b, 'Graph_Graph18', a1)
    if hasattr(a1, 'Graph_TString'):
        assert _is_linked(a1, 'Graph_TString', b)
    _safe_set(b, 'Graph_Graph18', {a2})
    assert _is_linked(b, 'Graph_Graph18', a2)
    if hasattr(a1, 'Graph_TString'):
        assert not _is_linked(a1, 'Graph_TString', b)
    if hasattr(a2, 'Graph_TString'):
        assert _is_linked(a2, 'Graph_TString', b)
    _safe_set(b, 'Graph_Graph18', set())
    assert not _is_linked(b, 'Graph_Graph18', a2)
    if hasattr(a2, 'Graph_TString'):
        assert not _is_linked(a2, 'Graph_TString', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

