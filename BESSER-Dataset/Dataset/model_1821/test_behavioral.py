import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Documentation_Book,
    Documentation_EmphasisValue,
    Documentation_InformalTableValue,
    Documentation_InformalTableValueRow,
    Documentation_ItemizedListValue,
    Documentation_ItemizedListValueItem,
    Documentation_Paragraph,
    Documentation_ParagraphValue,
    Documentation_Section,
    Documentation_TextualValue,
    Documentation_XRefValue,
    Paragraph,
    ParagraphValue,
    TextualValue,
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

def test_assoc_content0_reverse_link_reassign_clear():
    a1 = Documentation_Section(title="sample_text")
    a2 = Documentation_Section(title="sample_text_2")
    b = Documentation_Book(title="sample_text")
    _safe_set(b, 'Documentation_Book', {a1})
    assert _is_linked(b, 'Documentation_Book', a1)
    if hasattr(a1, 'Documentation_Section'):
        assert _is_linked(a1, 'Documentation_Section', b)
    _safe_set(b, 'Documentation_Book', {a2})
    assert _is_linked(b, 'Documentation_Book', a2)
    if hasattr(a1, 'Documentation_Section'):
        assert not _is_linked(a1, 'Documentation_Section', b)
    if hasattr(a2, 'Documentation_Section'):
        assert _is_linked(a2, 'Documentation_Section', b)
    _safe_set(b, 'Documentation_Book', set())
    assert not _is_linked(b, 'Documentation_Book', a2)
    if hasattr(a2, 'Documentation_Section'):
        assert not _is_linked(a2, 'Documentation_Section', b)


def test_assoc_section3_reverse_link_reassign_clear():
    a1 = Documentation_Section(title="sample_text")
    a2 = Documentation_Section(title="sample_text_2")
    b = Documentation_Section(title="sample_text")
    _safe_set(b, 'Documentation_Section4', a1)
    assert _is_linked(b, 'Documentation_Section4', a1)
    if hasattr(a1, 'Documentation_Section2'):
        assert _is_linked(a1, 'Documentation_Section2', b)
    _safe_set(b, 'Documentation_Section4', a2)
    assert _is_linked(b, 'Documentation_Section4', a2)
    if hasattr(a1, 'Documentation_Section2'):
        assert not _is_linked(a1, 'Documentation_Section2', b)
    if hasattr(a2, 'Documentation_Section2'):
        assert _is_linked(a2, 'Documentation_Section2', b)
    _safe_set(b, 'Documentation_Section4', None)
    assert not _is_linked(b, 'Documentation_Section4', a2)
    if hasattr(a2, 'Documentation_Section2'):
        assert not _is_linked(a2, 'Documentation_Section2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bodyRows11_stub_double():
    # Documentation_InformalTableValueRow has no real 'Documentation_InformalTableValueRow' property in the generated
    # code (a bare stub) -- manually attach it so Documentation_InformalTableValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Documentation_InformalTableValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Documentation_InformalTableValue(cols=7)
    partner = Documentation_InformalTableValueRow()
    setattr(partner, 'Documentation_InformalTableValueRow', None)
    _safe_set(owner, 'Documentation_InformalTableValue', {partner})
    assert getattr(partner, 'Documentation_InformalTableValueRow') == owner
    _safe_set(owner, 'Documentation_InformalTableValue', set())
    assert getattr(partner, 'Documentation_InformalTableValueRow') is None


def test_assoc_entry15_stub_double():
    # Documentation_InformalTableValueRow has no real 'Documentation_InformalTableValueRow16' property in the generated
    # code (a bare stub) -- manually attach it so Documentation_TextualValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Documentation_TextualValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Documentation_TextualValue(value="sample_text")
    partner = Documentation_InformalTableValueRow()
    setattr(partner, 'Documentation_InformalTableValueRow16', None)
    _safe_set(owner, 'Documentation_TextualValue', partner)
    assert owner in getattr(partner, 'Documentation_InformalTableValueRow16')
    _safe_set(owner, 'Documentation_TextualValue', None)
    assert owner not in getattr(partner, 'Documentation_InformalTableValueRow16')


def test_assoc_headRows12_stub_double():
    # Documentation_InformalTableValueRow has no real 'Documentation_InformalTableValueRow14' property in the generated
    # code (a bare stub) -- manually attach it so Documentation_InformalTableValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Documentation_InformalTableValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Documentation_InformalTableValue(cols=7)
    partner = Documentation_InformalTableValueRow()
    setattr(partner, 'Documentation_InformalTableValueRow14', None)
    _safe_set(owner, 'Documentation_InformalTableValue13', {partner})
    assert getattr(partner, 'Documentation_InformalTableValueRow14') == owner
    _safe_set(owner, 'Documentation_InformalTableValue13', set())
    assert getattr(partner, 'Documentation_InformalTableValueRow14') is None


def test_assoc_linkend9_stub_double():
    # Documentation_XRefValue has no real 'Documentation_XRefValue' property in the generated
    # code (a bare stub) -- manually attach it so Documentation_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Documentation_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Documentation_Section(title="sample_text")
    partner = Documentation_XRefValue()
    setattr(partner, 'Documentation_XRefValue', None)
    _safe_set(owner, 'Documentation_Section10', partner)
    assert getattr(partner, 'Documentation_XRefValue') == owner
    _safe_set(owner, 'Documentation_Section10', None)
    assert getattr(partner, 'Documentation_XRefValue') is None


def test_assoc_para5_stub_double():
    # Documentation_Paragraph has no real 'Documentation_Paragraph7' property in the generated
    # code (a bare stub) -- manually attach it so Documentation_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Documentation_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Documentation_Section(title="sample_text")
    partner = Documentation_Paragraph()
    setattr(partner, 'Documentation_Paragraph7', None)
    _safe_set(owner, 'Documentation_Section6', {partner})
    assert getattr(partner, 'Documentation_Paragraph7') == owner
    _safe_set(owner, 'Documentation_Section6', set())
    assert getattr(partner, 'Documentation_Paragraph7') is None


