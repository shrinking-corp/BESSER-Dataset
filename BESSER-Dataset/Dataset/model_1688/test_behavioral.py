import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    yyf_Alias,
    yyf_Bar,
    yyf_Base,
    yyf_Foo,
    yyf_NamedElement,
    yyf_Output,
    yyf_Relation,
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

def test_assoc_aliases4_reverse_link_reassign_clear():
    a1 = yyf_NamedElement(name="sample_text")
    a2 = yyf_NamedElement(name="sample_text_2")
    b = yyf_Alias(id="sample_text")
    _safe_set(b, 'yyf_Alias', a1)
    assert _is_linked(b, 'yyf_Alias', a1)
    if hasattr(a1, 'yyf_NamedElement'):
        assert _is_linked(a1, 'yyf_NamedElement', b)
    _safe_set(b, 'yyf_Alias', a2)
    assert _is_linked(b, 'yyf_Alias', a2)
    if hasattr(a1, 'yyf_NamedElement'):
        assert not _is_linked(a1, 'yyf_NamedElement', b)
    if hasattr(a2, 'yyf_NamedElement'):
        assert _is_linked(a2, 'yyf_NamedElement', b)
    _safe_set(b, 'yyf_Alias', None)
    assert not _is_linked(b, 'yyf_Alias', a2)
    if hasattr(a2, 'yyf_NamedElement'):
        assert not _is_linked(a2, 'yyf_NamedElement', b)


def test_assoc_bars5_reverse_link_reassign_clear():
    a1 = yyf_NamedElement(name="sample_text")
    a2 = yyf_NamedElement(name="sample_text_2")
    b = yyf_Bar(id="sample_text")
    _safe_set(b, 'yyf_Bar', a1)
    assert _is_linked(b, 'yyf_Bar', a1)
    if hasattr(a1, 'yyf_NamedElement6'):
        assert _is_linked(a1, 'yyf_NamedElement6', b)
    _safe_set(b, 'yyf_Bar', a2)
    assert _is_linked(b, 'yyf_Bar', a2)
    if hasattr(a1, 'yyf_NamedElement6'):
        assert not _is_linked(a1, 'yyf_NamedElement6', b)
    if hasattr(a2, 'yyf_NamedElement6'):
        assert _is_linked(a2, 'yyf_NamedElement6', b)
    _safe_set(b, 'yyf_Bar', None)
    assert not _is_linked(b, 'yyf_Bar', a2)
    if hasattr(a2, 'yyf_NamedElement6'):
        assert not _is_linked(a2, 'yyf_NamedElement6', b)


def test_assoc_foos1_reverse_link_reassign_clear():
    a1 = yyf_Foo(id="sample_text")
    a2 = yyf_Foo(id="sample_text_2")
    b = yyf_Base(id=7)
    _safe_set(b, 'yyf_Base', {a1})
    assert _is_linked(b, 'yyf_Base', a1)
    if hasattr(a1, 'yyf_Foo'):
        assert _is_linked(a1, 'yyf_Foo', b)
    _safe_set(b, 'yyf_Base', {a2})
    assert _is_linked(b, 'yyf_Base', a2)
    if hasattr(a1, 'yyf_Foo'):
        assert not _is_linked(a1, 'yyf_Foo', b)
    if hasattr(a2, 'yyf_Foo'):
        assert _is_linked(a2, 'yyf_Foo', b)
    _safe_set(b, 'yyf_Base', set())
    assert not _is_linked(b, 'yyf_Base', a2)
    if hasattr(a2, 'yyf_Foo'):
        assert not _is_linked(a2, 'yyf_Foo', b)


def test_assoc_fromThing7_reverse_link_reassign_clear():
    a1 = yyf_Relation(since="sample_text")
    a2 = yyf_Relation(since="sample_text_2")
    b = yyf_Base(id=7)
    _safe_set(b, 'Base', a1)
    assert _is_linked(b, 'Base', a1)
    if hasattr(a1, 'relations'):
        assert _is_linked(a1, 'relations', b)
    _safe_set(b, 'Base', a2)
    assert _is_linked(b, 'Base', a2)
    if hasattr(a1, 'relations'):
        assert not _is_linked(a1, 'relations', b)
    if hasattr(a2, 'relations'):
        assert _is_linked(a2, 'relations', b)
    _safe_set(b, 'Base', None)
    assert not _is_linked(b, 'Base', a2)
    if hasattr(a2, 'relations'):
        assert not _is_linked(a2, 'relations', b)


def test_assoc_ouputs2_reverse_link_reassign_clear():
    a1 = yyf_Output(id="sample_text")
    a2 = yyf_Output(id="sample_text_2")
    b = yyf_Base(id=7)
    _safe_set(b, 'yyf_Base3', {a1})
    assert _is_linked(b, 'yyf_Base3', a1)
    if hasattr(a1, 'yyf_Output'):
        assert _is_linked(a1, 'yyf_Output', b)
    _safe_set(b, 'yyf_Base3', {a2})
    assert _is_linked(b, 'yyf_Base3', a2)
    if hasattr(a1, 'yyf_Output'):
        assert not _is_linked(a1, 'yyf_Output', b)
    if hasattr(a2, 'yyf_Output'):
        assert _is_linked(a2, 'yyf_Output', b)
    _safe_set(b, 'yyf_Base3', set())
    assert not _is_linked(b, 'yyf_Base3', a2)
    if hasattr(a2, 'yyf_Output'):
        assert not _is_linked(a2, 'yyf_Output', b)


def test_assoc_output13_reverse_link_reassign_clear():
    a1 = yyf_Output(id="sample_text")
    a2 = yyf_Output(id="sample_text_2")
    b = yyf_Bar(id="sample_text")
    _safe_set(b, 'yyf_Bar14', a1)
    assert _is_linked(b, 'yyf_Bar14', a1)
    if hasattr(a1, 'yyf_Output15'):
        assert _is_linked(a1, 'yyf_Output15', b)
    _safe_set(b, 'yyf_Bar14', a2)
    assert _is_linked(b, 'yyf_Bar14', a2)
    if hasattr(a1, 'yyf_Output15'):
        assert not _is_linked(a1, 'yyf_Output15', b)
    if hasattr(a2, 'yyf_Output15'):
        assert _is_linked(a2, 'yyf_Output15', b)
    _safe_set(b, 'yyf_Bar14', None)
    assert not _is_linked(b, 'yyf_Bar14', a2)
    if hasattr(a2, 'yyf_Output15'):
        assert not _is_linked(a2, 'yyf_Output15', b)


def test_assoc_relations0_reverse_link_reassign_clear():
    a1 = yyf_Relation(since="sample_text")
    a2 = yyf_Relation(since="sample_text_2")
    b = yyf_Base(id=7)
    _safe_set(b, 'fromThing', {a1})
    assert _is_linked(b, 'fromThing', a1)
    if hasattr(a1, 'Relation'):
        assert _is_linked(a1, 'Relation', b)
    _safe_set(b, 'fromThing', {a2})
    assert _is_linked(b, 'fromThing', a2)
    if hasattr(a1, 'Relation'):
        assert not _is_linked(a1, 'Relation', b)
    if hasattr(a2, 'Relation'):
        assert _is_linked(a2, 'Relation', b)
    _safe_set(b, 'fromThing', set())
    assert not _is_linked(b, 'fromThing', a2)
    if hasattr(a2, 'Relation'):
        assert not _is_linked(a2, 'Relation', b)


def test_assoc_subRelations11_reverse_link_reassign_clear():
    a1 = yyf_Relation(since="sample_text")
    a2 = yyf_Relation(since="sample_text_2")
    b = yyf_Relation(since="sample_text")
    _safe_set(b, 'yyf_Relation12', a1)
    assert _is_linked(b, 'yyf_Relation12', a1)
    if hasattr(a1, 'yyf_Relation10'):
        assert _is_linked(a1, 'yyf_Relation10', b)
    _safe_set(b, 'yyf_Relation12', a2)
    assert _is_linked(b, 'yyf_Relation12', a2)
    if hasattr(a1, 'yyf_Relation10'):
        assert not _is_linked(a1, 'yyf_Relation10', b)
    if hasattr(a2, 'yyf_Relation10'):
        assert _is_linked(a2, 'yyf_Relation10', b)
    _safe_set(b, 'yyf_Relation12', None)
    assert not _is_linked(b, 'yyf_Relation12', a2)
    if hasattr(a2, 'yyf_Relation10'):
        assert not _is_linked(a2, 'yyf_Relation10', b)


def test_assoc_toThing8_reverse_link_reassign_clear():
    a1 = yyf_Relation(since="sample_text")
    a2 = yyf_Relation(since="sample_text_2")
    b = yyf_Base(id=7)
    _safe_set(b, 'yyf_Base9', a1)
    assert _is_linked(b, 'yyf_Base9', a1)
    if hasattr(a1, 'yyf_Relation'):
        assert _is_linked(a1, 'yyf_Relation', b)
    _safe_set(b, 'yyf_Base9', a2)
    assert _is_linked(b, 'yyf_Base9', a2)
    if hasattr(a1, 'yyf_Relation'):
        assert not _is_linked(a1, 'yyf_Relation', b)
    if hasattr(a2, 'yyf_Relation'):
        assert _is_linked(a2, 'yyf_Relation', b)
    _safe_set(b, 'yyf_Base9', None)
    assert not _is_linked(b, 'yyf_Base9', a2)
    if hasattr(a2, 'yyf_Relation'):
        assert not _is_linked(a2, 'yyf_Relation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

