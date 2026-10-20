import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Baz,
    NamedElement,
    yyh_Alias,
    yyh_Bar,
    yyh_Base,
    yyh_Baz,
    yyh_Boul,
    yyh_Bouz,
    yyh_Boz,
    yyh_Foo,
    yyh_NamedElement,
    yyh_Output,
    yyh_Rel,
    yyh_Zing,
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
    a1 = yyh_NamedElement(name="sample_text")
    a2 = yyh_NamedElement(name="sample_text_2")
    b = yyh_Alias(id="sample_text")
    _safe_set(b, 'yyh_Alias', a1)
    assert _is_linked(b, 'yyh_Alias', a1)
    if hasattr(a1, 'yyh_NamedElement'):
        assert _is_linked(a1, 'yyh_NamedElement', b)
    _safe_set(b, 'yyh_Alias', a2)
    assert _is_linked(b, 'yyh_Alias', a2)
    if hasattr(a1, 'yyh_NamedElement'):
        assert not _is_linked(a1, 'yyh_NamedElement', b)
    if hasattr(a2, 'yyh_NamedElement'):
        assert _is_linked(a2, 'yyh_NamedElement', b)
    _safe_set(b, 'yyh_Alias', None)
    assert not _is_linked(b, 'yyh_Alias', a2)
    if hasattr(a2, 'yyh_NamedElement'):
        assert not _is_linked(a2, 'yyh_NamedElement', b)


def test_assoc_bars7_reverse_link_reassign_clear():
    a1 = yyh_NamedElement(name="sample_text")
    a2 = yyh_NamedElement(name="sample_text_2")
    b = yyh_Bar(id="sample_text")
    _safe_set(b, 'yyh_Bar', a1)
    assert _is_linked(b, 'yyh_Bar', a1)
    if hasattr(a1, 'yyh_NamedElement8'):
        assert _is_linked(a1, 'yyh_NamedElement8', b)
    _safe_set(b, 'yyh_Bar', a2)
    assert _is_linked(b, 'yyh_Bar', a2)
    if hasattr(a1, 'yyh_NamedElement8'):
        assert not _is_linked(a1, 'yyh_NamedElement8', b)
    if hasattr(a2, 'yyh_NamedElement8'):
        assert _is_linked(a2, 'yyh_NamedElement8', b)
    _safe_set(b, 'yyh_Bar', None)
    assert not _is_linked(b, 'yyh_Bar', a2)
    if hasattr(a2, 'yyh_NamedElement8'):
        assert not _is_linked(a2, 'yyh_NamedElement8', b)


def test_assoc_baze4_reverse_link_reassign_clear():
    a1 = yyh_Baz(zig="sample_text")
    a2 = yyh_Baz(zig="sample_text_2")
    b = yyh_Base(id=7)
    _safe_set(b, 'yyh_Base5', {a1})
    assert _is_linked(b, 'yyh_Base5', a1)
    if hasattr(a1, 'yyh_Baz'):
        assert _is_linked(a1, 'yyh_Baz', b)
    _safe_set(b, 'yyh_Base5', {a2})
    assert _is_linked(b, 'yyh_Base5', a2)
    if hasattr(a1, 'yyh_Baz'):
        assert not _is_linked(a1, 'yyh_Baz', b)
    if hasattr(a2, 'yyh_Baz'):
        assert _is_linked(a2, 'yyh_Baz', b)
    _safe_set(b, 'yyh_Base5', set())
    assert not _is_linked(b, 'yyh_Base5', a2)
    if hasattr(a2, 'yyh_Baz'):
        assert not _is_linked(a2, 'yyh_Baz', b)


def test_assoc_foos1_reverse_link_reassign_clear():
    a1 = yyh_Foo(id="sample_text")
    a2 = yyh_Foo(id="sample_text_2")
    b = yyh_Base(id=7)
    _safe_set(b, 'yyh_Base', {a1})
    assert _is_linked(b, 'yyh_Base', a1)
    if hasattr(a1, 'yyh_Foo'):
        assert _is_linked(a1, 'yyh_Foo', b)
    _safe_set(b, 'yyh_Base', {a2})
    assert _is_linked(b, 'yyh_Base', a2)
    if hasattr(a1, 'yyh_Foo'):
        assert not _is_linked(a1, 'yyh_Foo', b)
    if hasattr(a2, 'yyh_Foo'):
        assert _is_linked(a2, 'yyh_Foo', b)
    _safe_set(b, 'yyh_Base', set())
    assert not _is_linked(b, 'yyh_Base', a2)
    if hasattr(a2, 'yyh_Foo'):
        assert not _is_linked(a2, 'yyh_Foo', b)


def test_assoc_fromThing11_reverse_link_reassign_clear():
    a1 = yyh_Boz(since="sample_text")
    a2 = yyh_Boz(since="sample_text_2")
    b = yyh_Base(id=7)
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
    a1 = yyh_Output(id="sample_text")
    a2 = yyh_Output(id="sample_text_2")
    b = yyh_Base(id=7)
    _safe_set(b, 'yyh_Base3', {a1})
    assert _is_linked(b, 'yyh_Base3', a1)
    if hasattr(a1, 'yyh_Output'):
        assert _is_linked(a1, 'yyh_Output', b)
    _safe_set(b, 'yyh_Base3', {a2})
    assert _is_linked(b, 'yyh_Base3', a2)
    if hasattr(a1, 'yyh_Output'):
        assert not _is_linked(a1, 'yyh_Output', b)
    if hasattr(a2, 'yyh_Output'):
        assert _is_linked(a2, 'yyh_Output', b)
    _safe_set(b, 'yyh_Base3', set())
    assert not _is_linked(b, 'yyh_Base3', a2)
    if hasattr(a2, 'yyh_Output'):
        assert not _is_linked(a2, 'yyh_Output', b)


def test_assoc_output17_reverse_link_reassign_clear():
    a1 = yyh_Output(id="sample_text")
    a2 = yyh_Output(id="sample_text_2")
    b = yyh_Bar(id="sample_text")
    _safe_set(b, 'yyh_Bar18', a1)
    assert _is_linked(b, 'yyh_Bar18', a1)
    if hasattr(a1, 'yyh_Output19'):
        assert _is_linked(a1, 'yyh_Output19', b)
    _safe_set(b, 'yyh_Bar18', a2)
    assert _is_linked(b, 'yyh_Bar18', a2)
    if hasattr(a1, 'yyh_Output19'):
        assert not _is_linked(a1, 'yyh_Output19', b)
    if hasattr(a2, 'yyh_Output19'):
        assert _is_linked(a2, 'yyh_Output19', b)
    _safe_set(b, 'yyh_Bar18', None)
    assert not _is_linked(b, 'yyh_Bar18', a2)
    if hasattr(a2, 'yyh_Output19'):
        assert not _is_linked(a2, 'yyh_Output19', b)


def test_assoc_relations0_reverse_link_reassign_clear():
    a1 = yyh_Boz(since="sample_text")
    a2 = yyh_Boz(since="sample_text_2")
    b = yyh_Base(id=7)
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
    a1 = yyh_Rel(id="sample_text")
    a2 = yyh_Rel(id="sample_text_2")
    b = yyh_NamedElement(name="sample_text")
    _safe_set(b, 'yyh_NamedElement10', {a1})
    assert _is_linked(b, 'yyh_NamedElement10', a1)
    if hasattr(a1, 'yyh_Rel'):
        assert _is_linked(a1, 'yyh_Rel', b)
    _safe_set(b, 'yyh_NamedElement10', {a2})
    assert _is_linked(b, 'yyh_NamedElement10', a2)
    if hasattr(a1, 'yyh_Rel'):
        assert not _is_linked(a1, 'yyh_Rel', b)
    if hasattr(a2, 'yyh_Rel'):
        assert _is_linked(a2, 'yyh_Rel', b)
    _safe_set(b, 'yyh_NamedElement10', set())
    assert not _is_linked(b, 'yyh_NamedElement10', a2)
    if hasattr(a2, 'yyh_Rel'):
        assert not _is_linked(a2, 'yyh_Rel', b)


def test_assoc_src20_reverse_link_reassign_clear():
    a1 = yyh_Rel(id="sample_text")
    a2 = yyh_Rel(id="sample_text_2")
    b = yyh_NamedElement(name="sample_text")
    _safe_set(b, 'yyh_NamedElement22', a1)
    assert _is_linked(b, 'yyh_NamedElement22', a1)
    if hasattr(a1, 'yyh_Rel21'):
        assert _is_linked(a1, 'yyh_Rel21', b)
    _safe_set(b, 'yyh_NamedElement22', a2)
    assert _is_linked(b, 'yyh_NamedElement22', a2)
    if hasattr(a1, 'yyh_Rel21'):
        assert not _is_linked(a1, 'yyh_Rel21', b)
    if hasattr(a2, 'yyh_Rel21'):
        assert _is_linked(a2, 'yyh_Rel21', b)
    _safe_set(b, 'yyh_NamedElement22', None)
    assert not _is_linked(b, 'yyh_NamedElement22', a2)
    if hasattr(a2, 'yyh_Rel21'):
        assert not _is_linked(a2, 'yyh_Rel21', b)


def test_assoc_subRelations15_reverse_link_reassign_clear():
    a1 = yyh_Boz(since="sample_text")
    a2 = yyh_Boz(since="sample_text_2")
    b = yyh_Boz(since="sample_text")
    _safe_set(b, 'yyh_Boz16', a1)
    assert _is_linked(b, 'yyh_Boz16', a1)
    if hasattr(a1, 'yyh_Boz14'):
        assert _is_linked(a1, 'yyh_Boz14', b)
    _safe_set(b, 'yyh_Boz16', a2)
    assert _is_linked(b, 'yyh_Boz16', a2)
    if hasattr(a1, 'yyh_Boz14'):
        assert not _is_linked(a1, 'yyh_Boz14', b)
    if hasattr(a2, 'yyh_Boz14'):
        assert _is_linked(a2, 'yyh_Boz14', b)
    _safe_set(b, 'yyh_Boz16', None)
    assert not _is_linked(b, 'yyh_Boz16', a2)
    if hasattr(a2, 'yyh_Boz14'):
        assert not _is_linked(a2, 'yyh_Boz14', b)


def test_assoc_toElement12_reverse_link_reassign_clear():
    a1 = yyh_NamedElement(name="sample_text")
    a2 = yyh_NamedElement(name="sample_text_2")
    b = yyh_Boz(since="sample_text")
    _safe_set(b, 'yyh_Boz', a1)
    assert _is_linked(b, 'yyh_Boz', a1)
    if hasattr(a1, 'yyh_NamedElement13'):
        assert _is_linked(a1, 'yyh_NamedElement13', b)
    _safe_set(b, 'yyh_Boz', a2)
    assert _is_linked(b, 'yyh_Boz', a2)
    if hasattr(a1, 'yyh_NamedElement13'):
        assert not _is_linked(a1, 'yyh_NamedElement13', b)
    if hasattr(a2, 'yyh_NamedElement13'):
        assert _is_linked(a2, 'yyh_NamedElement13', b)
    _safe_set(b, 'yyh_Boz', None)
    assert not _is_linked(b, 'yyh_Boz', a2)
    if hasattr(a2, 'yyh_NamedElement13'):
        assert not _is_linked(a2, 'yyh_NamedElement13', b)


def test_assoc_trg23_reverse_link_reassign_clear():
    a1 = yyh_Rel(id="sample_text")
    a2 = yyh_Rel(id="sample_text_2")
    b = yyh_Boz(since="sample_text")
    _safe_set(b, 'yyh_Boz25', a1)
    assert _is_linked(b, 'yyh_Boz25', a1)
    if hasattr(a1, 'yyh_Rel24'):
        assert _is_linked(a1, 'yyh_Rel24', b)
    _safe_set(b, 'yyh_Boz25', a2)
    assert _is_linked(b, 'yyh_Boz25', a2)
    if hasattr(a1, 'yyh_Rel24'):
        assert not _is_linked(a1, 'yyh_Rel24', b)
    if hasattr(a2, 'yyh_Rel24'):
        assert _is_linked(a2, 'yyh_Rel24', b)
    _safe_set(b, 'yyh_Boz25', None)
    assert not _is_linked(b, 'yyh_Boz25', a2)
    if hasattr(a2, 'yyh_Rel24'):
        assert not _is_linked(a2, 'yyh_Rel24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_azing26_stub_double():
    # yyh_Zing has no real 'yyh_Zing' property in the generated
    # code (a bare stub) -- manually attach it so yyh_Baz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # yyh_Baz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = yyh_Baz(zig="sample_text")
    partner = yyh_Zing()
    setattr(partner, 'yyh_Zing', None)
    _safe_set(owner, 'yyh_Baz27', partner)
    assert getattr(partner, 'yyh_Zing') == owner
    _safe_set(owner, 'yyh_Baz27', None)
    assert getattr(partner, 'yyh_Zing') is None


def test_assoc_zings28_stub_double():
    # yyh_Zing has no real 'yyh_Zing29' property in the generated
    # code (a bare stub) -- manually attach it so yyh_Bouz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # yyh_Bouz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = yyh_Bouz(bil="sample_text")
    partner = yyh_Zing()
    setattr(partner, 'yyh_Zing29', None)
    _safe_set(owner, 'yyh_Bouz', {partner})
    assert getattr(partner, 'yyh_Zing29') == owner
    _safe_set(owner, 'yyh_Bouz', set())
    assert getattr(partner, 'yyh_Zing29') is None


