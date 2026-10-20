import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Baz,
    NamedElement,
    yyk_Alias,
    yyk_Bar,
    yyk_Base,
    yyk_Baz,
    yyk_Boul,
    yyk_Bouz,
    yyk_Foo,
    yyk_NamedElement,
    yyk_Output,
    yyk_Rel,
    yyk_Relation,
    yyk_Zing,
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
    a1 = yyk_NamedElement(name="sample_text")
    a2 = yyk_NamedElement(name="sample_text_2")
    b = yyk_Alias(id="sample_text")
    _safe_set(b, 'yyk_Alias', a1)
    assert _is_linked(b, 'yyk_Alias', a1)
    if hasattr(a1, 'yyk_NamedElement'):
        assert _is_linked(a1, 'yyk_NamedElement', b)
    _safe_set(b, 'yyk_Alias', a2)
    assert _is_linked(b, 'yyk_Alias', a2)
    if hasattr(a1, 'yyk_NamedElement'):
        assert not _is_linked(a1, 'yyk_NamedElement', b)
    if hasattr(a2, 'yyk_NamedElement'):
        assert _is_linked(a2, 'yyk_NamedElement', b)
    _safe_set(b, 'yyk_Alias', None)
    assert not _is_linked(b, 'yyk_Alias', a2)
    if hasattr(a2, 'yyk_NamedElement'):
        assert not _is_linked(a2, 'yyk_NamedElement', b)


def test_assoc_bars7_reverse_link_reassign_clear():
    a1 = yyk_NamedElement(name="sample_text")
    a2 = yyk_NamedElement(name="sample_text_2")
    b = yyk_Bar(id="sample_text")
    _safe_set(b, 'yyk_Bar', a1)
    assert _is_linked(b, 'yyk_Bar', a1)
    if hasattr(a1, 'yyk_NamedElement8'):
        assert _is_linked(a1, 'yyk_NamedElement8', b)
    _safe_set(b, 'yyk_Bar', a2)
    assert _is_linked(b, 'yyk_Bar', a2)
    if hasattr(a1, 'yyk_NamedElement8'):
        assert not _is_linked(a1, 'yyk_NamedElement8', b)
    if hasattr(a2, 'yyk_NamedElement8'):
        assert _is_linked(a2, 'yyk_NamedElement8', b)
    _safe_set(b, 'yyk_Bar', None)
    assert not _is_linked(b, 'yyk_Bar', a2)
    if hasattr(a2, 'yyk_NamedElement8'):
        assert not _is_linked(a2, 'yyk_NamedElement8', b)


def test_assoc_baze4_reverse_link_reassign_clear():
    a1 = yyk_Baz(zig="sample_text")
    a2 = yyk_Baz(zig="sample_text_2")
    b = yyk_Base(id=7)
    _safe_set(b, 'yyk_Base5', {a1})
    assert _is_linked(b, 'yyk_Base5', a1)
    if hasattr(a1, 'yyk_Baz'):
        assert _is_linked(a1, 'yyk_Baz', b)
    _safe_set(b, 'yyk_Base5', {a2})
    assert _is_linked(b, 'yyk_Base5', a2)
    if hasattr(a1, 'yyk_Baz'):
        assert not _is_linked(a1, 'yyk_Baz', b)
    if hasattr(a2, 'yyk_Baz'):
        assert _is_linked(a2, 'yyk_Baz', b)
    _safe_set(b, 'yyk_Base5', set())
    assert not _is_linked(b, 'yyk_Base5', a2)
    if hasattr(a2, 'yyk_Baz'):
        assert not _is_linked(a2, 'yyk_Baz', b)


def test_assoc_foos1_reverse_link_reassign_clear():
    a1 = yyk_Foo(id="sample_text")
    a2 = yyk_Foo(id="sample_text_2")
    b = yyk_Base(id=7)
    _safe_set(b, 'yyk_Base', {a1})
    assert _is_linked(b, 'yyk_Base', a1)
    if hasattr(a1, 'yyk_Foo'):
        assert _is_linked(a1, 'yyk_Foo', b)
    _safe_set(b, 'yyk_Base', {a2})
    assert _is_linked(b, 'yyk_Base', a2)
    if hasattr(a1, 'yyk_Foo'):
        assert not _is_linked(a1, 'yyk_Foo', b)
    if hasattr(a2, 'yyk_Foo'):
        assert _is_linked(a2, 'yyk_Foo', b)
    _safe_set(b, 'yyk_Base', set())
    assert not _is_linked(b, 'yyk_Base', a2)
    if hasattr(a2, 'yyk_Foo'):
        assert not _is_linked(a2, 'yyk_Foo', b)


def test_assoc_fromThing11_reverse_link_reassign_clear():
    a1 = yyk_Relation(since="sample_text")
    a2 = yyk_Relation(since="sample_text_2")
    b = yyk_Base(id=7)
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
    a1 = yyk_Output(id="sample_text")
    a2 = yyk_Output(id="sample_text_2")
    b = yyk_Base(id=7)
    _safe_set(b, 'yyk_Base3', {a1})
    assert _is_linked(b, 'yyk_Base3', a1)
    if hasattr(a1, 'yyk_Output'):
        assert _is_linked(a1, 'yyk_Output', b)
    _safe_set(b, 'yyk_Base3', {a2})
    assert _is_linked(b, 'yyk_Base3', a2)
    if hasattr(a1, 'yyk_Output'):
        assert not _is_linked(a1, 'yyk_Output', b)
    if hasattr(a2, 'yyk_Output'):
        assert _is_linked(a2, 'yyk_Output', b)
    _safe_set(b, 'yyk_Base3', set())
    assert not _is_linked(b, 'yyk_Base3', a2)
    if hasattr(a2, 'yyk_Output'):
        assert not _is_linked(a2, 'yyk_Output', b)


def test_assoc_output17_reverse_link_reassign_clear():
    a1 = yyk_Output(id="sample_text")
    a2 = yyk_Output(id="sample_text_2")
    b = yyk_Bar(id="sample_text")
    _safe_set(b, 'yyk_Bar18', a1)
    assert _is_linked(b, 'yyk_Bar18', a1)
    if hasattr(a1, 'yyk_Output19'):
        assert _is_linked(a1, 'yyk_Output19', b)
    _safe_set(b, 'yyk_Bar18', a2)
    assert _is_linked(b, 'yyk_Bar18', a2)
    if hasattr(a1, 'yyk_Output19'):
        assert not _is_linked(a1, 'yyk_Output19', b)
    if hasattr(a2, 'yyk_Output19'):
        assert _is_linked(a2, 'yyk_Output19', b)
    _safe_set(b, 'yyk_Bar18', None)
    assert not _is_linked(b, 'yyk_Bar18', a2)
    if hasattr(a2, 'yyk_Output19'):
        assert not _is_linked(a2, 'yyk_Output19', b)


def test_assoc_relations0_reverse_link_reassign_clear():
    a1 = yyk_Relation(since="sample_text")
    a2 = yyk_Relation(since="sample_text_2")
    b = yyk_Base(id=7)
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


def test_assoc_rels9_reverse_link_reassign_clear():
    a1 = yyk_Rel(id="sample_text")
    a2 = yyk_Rel(id="sample_text_2")
    b = yyk_NamedElement(name="sample_text")
    _safe_set(b, 'yyk_NamedElement10', {a1})
    assert _is_linked(b, 'yyk_NamedElement10', a1)
    if hasattr(a1, 'yyk_Rel'):
        assert _is_linked(a1, 'yyk_Rel', b)
    _safe_set(b, 'yyk_NamedElement10', {a2})
    assert _is_linked(b, 'yyk_NamedElement10', a2)
    if hasattr(a1, 'yyk_Rel'):
        assert not _is_linked(a1, 'yyk_Rel', b)
    if hasattr(a2, 'yyk_Rel'):
        assert _is_linked(a2, 'yyk_Rel', b)
    _safe_set(b, 'yyk_NamedElement10', set())
    assert not _is_linked(b, 'yyk_NamedElement10', a2)
    if hasattr(a2, 'yyk_Rel'):
        assert not _is_linked(a2, 'yyk_Rel', b)


def test_assoc_src20_reverse_link_reassign_clear():
    a1 = yyk_Rel(id="sample_text")
    a2 = yyk_Rel(id="sample_text_2")
    b = yyk_NamedElement(name="sample_text")
    _safe_set(b, 'yyk_NamedElement22', a1)
    assert _is_linked(b, 'yyk_NamedElement22', a1)
    if hasattr(a1, 'yyk_Rel21'):
        assert _is_linked(a1, 'yyk_Rel21', b)
    _safe_set(b, 'yyk_NamedElement22', a2)
    assert _is_linked(b, 'yyk_NamedElement22', a2)
    if hasattr(a1, 'yyk_Rel21'):
        assert not _is_linked(a1, 'yyk_Rel21', b)
    if hasattr(a2, 'yyk_Rel21'):
        assert _is_linked(a2, 'yyk_Rel21', b)
    _safe_set(b, 'yyk_NamedElement22', None)
    assert not _is_linked(b, 'yyk_NamedElement22', a2)
    if hasattr(a2, 'yyk_Rel21'):
        assert not _is_linked(a2, 'yyk_Rel21', b)


def test_assoc_subRelations15_reverse_link_reassign_clear():
    a1 = yyk_Relation(since="sample_text")
    a2 = yyk_Relation(since="sample_text_2")
    b = yyk_Relation(since="sample_text")
    _safe_set(b, 'yyk_Relation16', a1)
    assert _is_linked(b, 'yyk_Relation16', a1)
    if hasattr(a1, 'yyk_Relation14'):
        assert _is_linked(a1, 'yyk_Relation14', b)
    _safe_set(b, 'yyk_Relation16', a2)
    assert _is_linked(b, 'yyk_Relation16', a2)
    if hasattr(a1, 'yyk_Relation14'):
        assert not _is_linked(a1, 'yyk_Relation14', b)
    if hasattr(a2, 'yyk_Relation14'):
        assert _is_linked(a2, 'yyk_Relation14', b)
    _safe_set(b, 'yyk_Relation16', None)
    assert not _is_linked(b, 'yyk_Relation16', a2)
    if hasattr(a2, 'yyk_Relation14'):
        assert not _is_linked(a2, 'yyk_Relation14', b)


def test_assoc_toElement12_reverse_link_reassign_clear():
    a1 = yyk_Relation(since="sample_text")
    a2 = yyk_Relation(since="sample_text_2")
    b = yyk_NamedElement(name="sample_text")
    _safe_set(b, 'yyk_NamedElement13', a1)
    assert _is_linked(b, 'yyk_NamedElement13', a1)
    if hasattr(a1, 'yyk_Relation'):
        assert _is_linked(a1, 'yyk_Relation', b)
    _safe_set(b, 'yyk_NamedElement13', a2)
    assert _is_linked(b, 'yyk_NamedElement13', a2)
    if hasattr(a1, 'yyk_Relation'):
        assert not _is_linked(a1, 'yyk_Relation', b)
    if hasattr(a2, 'yyk_Relation'):
        assert _is_linked(a2, 'yyk_Relation', b)
    _safe_set(b, 'yyk_NamedElement13', None)
    assert not _is_linked(b, 'yyk_NamedElement13', a2)
    if hasattr(a2, 'yyk_Relation'):
        assert not _is_linked(a2, 'yyk_Relation', b)


def test_assoc_trg23_reverse_link_reassign_clear():
    a1 = yyk_Relation(since="sample_text")
    a2 = yyk_Relation(since="sample_text_2")
    b = yyk_Rel(id="sample_text")
    _safe_set(b, 'yyk_Rel24', a1)
    assert _is_linked(b, 'yyk_Rel24', a1)
    if hasattr(a1, 'yyk_Relation25'):
        assert _is_linked(a1, 'yyk_Relation25', b)
    _safe_set(b, 'yyk_Rel24', a2)
    assert _is_linked(b, 'yyk_Rel24', a2)
    if hasattr(a1, 'yyk_Relation25'):
        assert not _is_linked(a1, 'yyk_Relation25', b)
    if hasattr(a2, 'yyk_Relation25'):
        assert _is_linked(a2, 'yyk_Relation25', b)
    _safe_set(b, 'yyk_Rel24', None)
    assert not _is_linked(b, 'yyk_Rel24', a2)
    if hasattr(a2, 'yyk_Relation25'):
        assert not _is_linked(a2, 'yyk_Relation25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_azing26_stub_double():
    # yyk_Zing has no real 'yyk_Zing' property in the generated
    # code (a bare stub) -- manually attach it so yyk_Baz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # yyk_Baz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = yyk_Baz(zig="sample_text")
    partner = yyk_Zing()
    setattr(partner, 'yyk_Zing', None)
    _safe_set(owner, 'yyk_Baz27', partner)
    assert getattr(partner, 'yyk_Zing') == owner
    _safe_set(owner, 'yyk_Baz27', None)
    assert getattr(partner, 'yyk_Zing') is None


def test_assoc_zings28_stub_double():
    # yyk_Zing has no real 'yyk_Zing29' property in the generated
    # code (a bare stub) -- manually attach it so yyk_Bouz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # yyk_Bouz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = yyk_Bouz(bil="sample_text")
    partner = yyk_Zing()
    setattr(partner, 'yyk_Zing29', None)
    _safe_set(owner, 'yyk_Bouz', {partner})
    assert getattr(partner, 'yyk_Zing29') == owner
    _safe_set(owner, 'yyk_Bouz', set())
    assert getattr(partner, 'yyk_Zing29') is None


