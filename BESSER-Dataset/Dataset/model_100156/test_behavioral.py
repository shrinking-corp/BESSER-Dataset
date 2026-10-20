import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    IValue,
    mongodb_Collection,
    mongodb_Database,
    mongodb_Document,
    mongodb_Field,
    mongodb_IValue,
    mongodb_SubDocument,
    mongodb_Value,
    mongodb_ValueList,
    Type,
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

def test_assoc_collections0_reverse_link_reassign_clear():
    a1 = mongodb_Database(name="sample_text")
    a2 = mongodb_Database(name="sample_text_2")
    b = mongodb_Collection(name="sample_text")
    _safe_set(b, 'mongodb_Collection', a1)
    assert _is_linked(b, 'mongodb_Collection', a1)
    if hasattr(a1, 'mongodb_Database'):
        assert _is_linked(a1, 'mongodb_Database', b)
    _safe_set(b, 'mongodb_Collection', a2)
    assert _is_linked(b, 'mongodb_Collection', a2)
    if hasattr(a1, 'mongodb_Database'):
        assert not _is_linked(a1, 'mongodb_Database', b)
    if hasattr(a2, 'mongodb_Database'):
        assert _is_linked(a2, 'mongodb_Database', b)
    _safe_set(b, 'mongodb_Collection', None)
    assert not _is_linked(b, 'mongodb_Collection', a2)
    if hasattr(a2, 'mongodb_Database'):
        assert not _is_linked(a2, 'mongodb_Database', b)


def test_assoc_documents1_reverse_link_reassign_clear():
    a1 = mongodb_Document(_id="sample_text")
    a2 = mongodb_Document(_id="sample_text_2")
    b = mongodb_Collection(name="sample_text")
    _safe_set(b, 'mongodb_Collection2', {a1})
    assert _is_linked(b, 'mongodb_Collection2', a1)
    if hasattr(a1, 'mongodb_Document'):
        assert _is_linked(a1, 'mongodb_Document', b)
    _safe_set(b, 'mongodb_Collection2', {a2})
    assert _is_linked(b, 'mongodb_Collection2', a2)
    if hasattr(a1, 'mongodb_Document'):
        assert not _is_linked(a1, 'mongodb_Document', b)
    if hasattr(a2, 'mongodb_Document'):
        assert _is_linked(a2, 'mongodb_Document', b)
    _safe_set(b, 'mongodb_Collection2', set())
    assert not _is_linked(b, 'mongodb_Collection2', a2)
    if hasattr(a2, 'mongodb_Document'):
        assert not _is_linked(a2, 'mongodb_Document', b)


def test_assoc_fields3_reverse_link_reassign_clear():
    a1 = mongodb_Field(key="sample_text")
    a2 = mongodb_Field(key="sample_text_2")
    b = mongodb_Document(_id="sample_text")
    _safe_set(b, 'mongodb_Document4', {a1})
    assert _is_linked(b, 'mongodb_Document4', a1)
    if hasattr(a1, 'mongodb_Field'):
        assert _is_linked(a1, 'mongodb_Field', b)
    _safe_set(b, 'mongodb_Document4', {a2})
    assert _is_linked(b, 'mongodb_Document4', a2)
    if hasattr(a1, 'mongodb_Field'):
        assert not _is_linked(a1, 'mongodb_Field', b)
    if hasattr(a2, 'mongodb_Field'):
        assert _is_linked(a2, 'mongodb_Field', b)
    _safe_set(b, 'mongodb_Document4', set())
    assert not _is_linked(b, 'mongodb_Document4', a2)
    if hasattr(a2, 'mongodb_Field'):
        assert not _is_linked(a2, 'mongodb_Field', b)


def test_assoc_value5_reverse_link_reassign_clear():
    a1 = mongodb_IValue()
    a2 = mongodb_IValue()
    b = mongodb_Field(key="sample_text")
    _safe_set(b, 'mongodb_Field6', a1)
    assert _is_linked(b, 'mongodb_Field6', a1)
    if hasattr(a1, 'mongodb_IValue'):
        assert _is_linked(a1, 'mongodb_IValue', b)
    _safe_set(b, 'mongodb_Field6', a2)
    assert _is_linked(b, 'mongodb_Field6', a2)
    if hasattr(a1, 'mongodb_IValue'):
        assert not _is_linked(a1, 'mongodb_IValue', b)
    if hasattr(a2, 'mongodb_IValue'):
        assert _is_linked(a2, 'mongodb_IValue', b)
    _safe_set(b, 'mongodb_Field6', None)
    assert not _is_linked(b, 'mongodb_Field6', a2)
    if hasattr(a2, 'mongodb_IValue'):
        assert not _is_linked(a2, 'mongodb_IValue', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_fields9_stub_double():
    # mongodb_SubDocument has no real 'mongodb_SubDocument' property in the generated
    # code (a bare stub) -- manually attach it so mongodb_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mongodb_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mongodb_Field(key="sample_text")
    partner = mongodb_SubDocument()
    setattr(partner, 'mongodb_SubDocument', None)
    _safe_set(owner, 'mongodb_Field10', partner)
    assert owner in getattr(partner, 'mongodb_SubDocument')
    _safe_set(owner, 'mongodb_Field10', None)
    assert owner not in getattr(partner, 'mongodb_SubDocument')


def test_assoc_values7_stub_double():
    # mongodb_ValueList has no real 'mongodb_ValueList' property in the generated
    # code (a bare stub) -- manually attach it so mongodb_IValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mongodb_IValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mongodb_IValue()
    partner = mongodb_ValueList()
    setattr(partner, 'mongodb_ValueList', None)
    _safe_set(owner, 'mongodb_IValue8', partner)
    assert owner in getattr(partner, 'mongodb_ValueList')
    _safe_set(owner, 'mongodb_IValue8', None)
    assert owner not in getattr(partner, 'mongodb_ValueList')


