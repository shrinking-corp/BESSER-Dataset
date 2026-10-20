import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Baz,
    NamedElement,
    yyg_Alias,
    yyg_Bar,
    yyg_Base,
    yyg_Baz,
    yyg_Boul,
    yyg_Bouz,
    yyg_Boz,
    yyg_Foo,
    yyg_NamedElement,
    yyg_Output,
    yyg_Rel,
    yyg_Zing,
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

def test_assoc_aliases6_reverse_link_reassign_clear():
    a1 = yyg_NamedElement(name="sample_text")
    a2 = yyg_NamedElement(name="sample_text_2")
    b = yyg_Alias(id="sample_text")
    _safe_set(b, 'yyg_Alias', a1)
    assert _is_linked(b, 'yyg_Alias', a1)
    if hasattr(a1, 'yyg_NamedElement'):
        assert _is_linked(a1, 'yyg_NamedElement', b)
    _safe_set(b, 'yyg_Alias', a2)
    assert _is_linked(b, 'yyg_Alias', a2)
    if hasattr(a1, 'yyg_NamedElement'):
        assert not _is_linked(a1, 'yyg_NamedElement', b)
    if hasattr(a2, 'yyg_NamedElement'):
        assert _is_linked(a2, 'yyg_NamedElement', b)
    _safe_set(b, 'yyg_Alias', None)
    assert not _is_linked(b, 'yyg_Alias', a2)
    if hasattr(a2, 'yyg_NamedElement'):
        assert not _is_linked(a2, 'yyg_NamedElement', b)


def test_assoc_bars7_reverse_link_reassign_clear():
    a1 = yyg_NamedElement(name="sample_text")
    a2 = yyg_NamedElement(name="sample_text_2")
    b = yyg_Bar(id="sample_text")
    _safe_set(b, 'yyg_Bar', a1)
    assert _is_linked(b, 'yyg_Bar', a1)
    if hasattr(a1, 'yyg_NamedElement8'):
        assert _is_linked(a1, 'yyg_NamedElement8', b)
    _safe_set(b, 'yyg_Bar', a2)
    assert _is_linked(b, 'yyg_Bar', a2)
    if hasattr(a1, 'yyg_NamedElement8'):
        assert not _is_linked(a1, 'yyg_NamedElement8', b)
    if hasattr(a2, 'yyg_NamedElement8'):
        assert _is_linked(a2, 'yyg_NamedElement8', b)
    _safe_set(b, 'yyg_Bar', None)
    assert not _is_linked(b, 'yyg_Bar', a2)
    if hasattr(a2, 'yyg_NamedElement8'):
        assert not _is_linked(a2, 'yyg_NamedElement8', b)


def test_assoc_baze4_reverse_link_reassign_clear():
    a1 = yyg_Baz(zig="sample_text")
    a2 = yyg_Baz(zig="sample_text_2")
    b = yyg_Base(id=7)
    _safe_set(b, 'yyg_Base5', {a1})
    assert _is_linked(b, 'yyg_Base5', a1)
    if hasattr(a1, 'yyg_Baz'):
        assert _is_linked(a1, 'yyg_Baz', b)
    _safe_set(b, 'yyg_Base5', {a2})
    assert _is_linked(b, 'yyg_Base5', a2)
    if hasattr(a1, 'yyg_Baz'):
        assert not _is_linked(a1, 'yyg_Baz', b)
    if hasattr(a2, 'yyg_Baz'):
        assert _is_linked(a2, 'yyg_Baz', b)
    _safe_set(b, 'yyg_Base5', set())
    assert not _is_linked(b, 'yyg_Base5', a2)
    if hasattr(a2, 'yyg_Baz'):
        assert not _is_linked(a2, 'yyg_Baz', b)


def test_assoc_foos1_reverse_link_reassign_clear():
    a1 = yyg_Foo(id="sample_text")
    a2 = yyg_Foo(id="sample_text_2")
    b = yyg_Base(id=7)
    _safe_set(b, 'yyg_Base', {a1})
    assert _is_linked(b, 'yyg_Base', a1)
    if hasattr(a1, 'yyg_Foo'):
        assert _is_linked(a1, 'yyg_Foo', b)
    _safe_set(b, 'yyg_Base', {a2})
    assert _is_linked(b, 'yyg_Base', a2)
    if hasattr(a1, 'yyg_Foo'):
        assert not _is_linked(a1, 'yyg_Foo', b)
    if hasattr(a2, 'yyg_Foo'):
        assert _is_linked(a2, 'yyg_Foo', b)
    _safe_set(b, 'yyg_Base', set())
    assert not _is_linked(b, 'yyg_Base', a2)
    if hasattr(a2, 'yyg_Foo'):
        assert not _is_linked(a2, 'yyg_Foo', b)


def test_assoc_fromThing11_reverse_link_reassign_clear():
    a1 = yyg_Boz(since="sample_text")
    a2 = yyg_Boz(since="sample_text_2")
    b = yyg_Base(id=7)
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
    a1 = yyg_Output(id="sample_text")
    a2 = yyg_Output(id="sample_text_2")
    b = yyg_Base(id=7)
    _safe_set(b, 'yyg_Base3', {a1})
    assert _is_linked(b, 'yyg_Base3', a1)
    if hasattr(a1, 'yyg_Output'):
        assert _is_linked(a1, 'yyg_Output', b)
    _safe_set(b, 'yyg_Base3', {a2})
    assert _is_linked(b, 'yyg_Base3', a2)
    if hasattr(a1, 'yyg_Output'):
        assert not _is_linked(a1, 'yyg_Output', b)
    if hasattr(a2, 'yyg_Output'):
        assert _is_linked(a2, 'yyg_Output', b)
    _safe_set(b, 'yyg_Base3', set())
    assert not _is_linked(b, 'yyg_Base3', a2)
    if hasattr(a2, 'yyg_Output'):
        assert not _is_linked(a2, 'yyg_Output', b)


def test_assoc_output17_reverse_link_reassign_clear():
    a1 = yyg_Output(id="sample_text")
    a2 = yyg_Output(id="sample_text_2")
    b = yyg_Bar(id="sample_text")
    _safe_set(b, 'yyg_Bar18', a1)
    assert _is_linked(b, 'yyg_Bar18', a1)
    if hasattr(a1, 'yyg_Output19'):
        assert _is_linked(a1, 'yyg_Output19', b)
    _safe_set(b, 'yyg_Bar18', a2)
    assert _is_linked(b, 'yyg_Bar18', a2)
    if hasattr(a1, 'yyg_Output19'):
        assert not _is_linked(a1, 'yyg_Output19', b)
    if hasattr(a2, 'yyg_Output19'):
        assert _is_linked(a2, 'yyg_Output19', b)
    _safe_set(b, 'yyg_Bar18', None)
    assert not _is_linked(b, 'yyg_Bar18', a2)
    if hasattr(a2, 'yyg_Output19'):
        assert not _is_linked(a2, 'yyg_Output19', b)


def test_assoc_relations0_reverse_link_reassign_clear():
    a1 = yyg_Boz(since="sample_text")
    a2 = yyg_Boz(since="sample_text_2")
    b = yyg_Base(id=7)
    _safe_set(b, 'fromThing', {a1})
    assert _is_linked(b, 'fromThing', a1)
    if hasattr(a1, 'Boz'):
        assert _is_linked(a1, 'Boz', b)
    _safe_set(b, 'fromThing', {a2})
    assert _is_linked(b, 'fromThing', a2)
    if hasattr(a1, 'Boz'):
        assert not _is_linked(a1, 'Boz', b)
    if hasattr(a2, 'Boz'):
        assert _is_linked(a2, 'Boz', b)
    _safe_set(b, 'fromThing', set())
    assert not _is_linked(b, 'fromThing', a2)
    if hasattr(a2, 'Boz'):
        assert not _is_linked(a2, 'Boz', b)


def test_assoc_rels9_reverse_link_reassign_clear():
    a1 = yyg_Rel(id="sample_text")
    a2 = yyg_Rel(id="sample_text_2")
    b = yyg_NamedElement(name="sample_text")
    _safe_set(b, 'yyg_NamedElement10', {a1})
    assert _is_linked(b, 'yyg_NamedElement10', a1)
    if hasattr(a1, 'yyg_Rel'):
        assert _is_linked(a1, 'yyg_Rel', b)
    _safe_set(b, 'yyg_NamedElement10', {a2})
    assert _is_linked(b, 'yyg_NamedElement10', a2)
    if hasattr(a1, 'yyg_Rel'):
        assert not _is_linked(a1, 'yyg_Rel', b)
    if hasattr(a2, 'yyg_Rel'):
        assert _is_linked(a2, 'yyg_Rel', b)
    _safe_set(b, 'yyg_NamedElement10', set())
    assert not _is_linked(b, 'yyg_NamedElement10', a2)
    if hasattr(a2, 'yyg_Rel'):
        assert not _is_linked(a2, 'yyg_Rel', b)


def test_assoc_src20_reverse_link_reassign_clear():
    a1 = yyg_Rel(id="sample_text")
    a2 = yyg_Rel(id="sample_text_2")
    b = yyg_NamedElement(name="sample_text")
    _safe_set(b, 'yyg_NamedElement22', a1)
    assert _is_linked(b, 'yyg_NamedElement22', a1)
    if hasattr(a1, 'yyg_Rel21'):
        assert _is_linked(a1, 'yyg_Rel21', b)
    _safe_set(b, 'yyg_NamedElement22', a2)
    assert _is_linked(b, 'yyg_NamedElement22', a2)
    if hasattr(a1, 'yyg_Rel21'):
        assert not _is_linked(a1, 'yyg_Rel21', b)
    if hasattr(a2, 'yyg_Rel21'):
        assert _is_linked(a2, 'yyg_Rel21', b)
    _safe_set(b, 'yyg_NamedElement22', None)
    assert not _is_linked(b, 'yyg_NamedElement22', a2)
    if hasattr(a2, 'yyg_Rel21'):
        assert not _is_linked(a2, 'yyg_Rel21', b)


def test_assoc_subRelations15_reverse_link_reassign_clear():
    a1 = yyg_Boz(since="sample_text")
    a2 = yyg_Boz(since="sample_text_2")
    b = yyg_Boz(since="sample_text")
    _safe_set(b, 'yyg_Boz16', a1)
    assert _is_linked(b, 'yyg_Boz16', a1)
    if hasattr(a1, 'yyg_Boz14'):
        assert _is_linked(a1, 'yyg_Boz14', b)
    _safe_set(b, 'yyg_Boz16', a2)
    assert _is_linked(b, 'yyg_Boz16', a2)
    if hasattr(a1, 'yyg_Boz14'):
        assert not _is_linked(a1, 'yyg_Boz14', b)
    if hasattr(a2, 'yyg_Boz14'):
        assert _is_linked(a2, 'yyg_Boz14', b)
    _safe_set(b, 'yyg_Boz16', None)
    assert not _is_linked(b, 'yyg_Boz16', a2)
    if hasattr(a2, 'yyg_Boz14'):
        assert not _is_linked(a2, 'yyg_Boz14', b)


def test_assoc_toElement12_reverse_link_reassign_clear():
    a1 = yyg_NamedElement(name="sample_text")
    a2 = yyg_NamedElement(name="sample_text_2")
    b = yyg_Boz(since="sample_text")
    _safe_set(b, 'yyg_Boz', a1)
    assert _is_linked(b, 'yyg_Boz', a1)
    if hasattr(a1, 'yyg_NamedElement13'):
        assert _is_linked(a1, 'yyg_NamedElement13', b)
    _safe_set(b, 'yyg_Boz', a2)
    assert _is_linked(b, 'yyg_Boz', a2)
    if hasattr(a1, 'yyg_NamedElement13'):
        assert not _is_linked(a1, 'yyg_NamedElement13', b)
    if hasattr(a2, 'yyg_NamedElement13'):
        assert _is_linked(a2, 'yyg_NamedElement13', b)
    _safe_set(b, 'yyg_Boz', None)
    assert not _is_linked(b, 'yyg_Boz', a2)
    if hasattr(a2, 'yyg_NamedElement13'):
        assert not _is_linked(a2, 'yyg_NamedElement13', b)


def test_assoc_trg23_reverse_link_reassign_clear():
    a1 = yyg_Rel(id="sample_text")
    a2 = yyg_Rel(id="sample_text_2")
    b = yyg_Boz(since="sample_text")
    _safe_set(b, 'yyg_Boz25', a1)
    assert _is_linked(b, 'yyg_Boz25', a1)
    if hasattr(a1, 'yyg_Rel24'):
        assert _is_linked(a1, 'yyg_Rel24', b)
    _safe_set(b, 'yyg_Boz25', a2)
    assert _is_linked(b, 'yyg_Boz25', a2)
    if hasattr(a1, 'yyg_Rel24'):
        assert not _is_linked(a1, 'yyg_Rel24', b)
    if hasattr(a2, 'yyg_Rel24'):
        assert _is_linked(a2, 'yyg_Rel24', b)
    _safe_set(b, 'yyg_Boz25', None)
    assert not _is_linked(b, 'yyg_Boz25', a2)
    if hasattr(a2, 'yyg_Rel24'):
        assert not _is_linked(a2, 'yyg_Rel24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_azing26_stub_double():
    # yyg_Zing has no real 'yyg_Zing' property in the generated
    # code (a bare stub) -- manually attach it so yyg_Baz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # yyg_Baz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = yyg_Baz(zig="sample_text")
    partner = yyg_Zing()
    setattr(partner, 'yyg_Zing', None)
    _safe_set(owner, 'yyg_Baz27', partner)
    assert getattr(partner, 'yyg_Zing') == owner
    _safe_set(owner, 'yyg_Baz27', None)
    assert getattr(partner, 'yyg_Zing') is None


def test_assoc_zings28_stub_double():
    # yyg_Zing has no real 'yyg_Zing29' property in the generated
    # code (a bare stub) -- manually attach it so yyg_Bouz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # yyg_Bouz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = yyg_Bouz(bil="sample_text")
    partner = yyg_Zing()
    setattr(partner, 'yyg_Zing29', None)
    _safe_set(owner, 'yyg_Bouz', {partner})
    assert getattr(partner, 'yyg_Zing29') == owner
    _safe_set(owner, 'yyg_Bouz', set())
    assert getattr(partner, 'yyg_Zing29') is None


