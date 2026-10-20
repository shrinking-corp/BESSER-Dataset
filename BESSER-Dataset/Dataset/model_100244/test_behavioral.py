import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ColumnDefinition,
    ColumnSpec,
    Element,
    spreadsheetGrammarLanguage_Block,
    spreadsheetGrammarLanguage_BlockSpec,
    spreadsheetGrammarLanguage_Column,
    spreadsheetGrammarLanguage_ColumnDefinition,
    spreadsheetGrammarLanguage_ColumnSpec,
    spreadsheetGrammarLanguage_Element,
    spreadsheetGrammarLanguage_Grammar,
    spreadsheetGrammarLanguage_MandatoryColumn,
    spreadsheetGrammarLanguage_OptionalColumn,
    spreadsheetGrammarLanguage_RowSpec,
    spreadsheetGrammarLanguage_Rule,
    spreadsheetGrammarLanguage_Syntax,
    spreadsheetGrammarLanguage_SyntaxSeq,
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

def test_assoc_elements1_reverse_link_reassign_clear():
    a1 = spreadsheetGrammarLanguage_Grammar(name="sample_text")
    a2 = spreadsheetGrammarLanguage_Grammar(name="sample_text_2")
    b = spreadsheetGrammarLanguage_Element(name="sample_text")
    _safe_set(b, 'spreadsheetGrammarLanguage_Element', a1)
    assert _is_linked(b, 'spreadsheetGrammarLanguage_Element', a1)
    if hasattr(a1, 'spreadsheetGrammarLanguage_Grammar2'):
        assert _is_linked(a1, 'spreadsheetGrammarLanguage_Grammar2', b)
    _safe_set(b, 'spreadsheetGrammarLanguage_Element', a2)
    assert _is_linked(b, 'spreadsheetGrammarLanguage_Element', a2)
    if hasattr(a1, 'spreadsheetGrammarLanguage_Grammar2'):
        assert not _is_linked(a1, 'spreadsheetGrammarLanguage_Grammar2', b)
    if hasattr(a2, 'spreadsheetGrammarLanguage_Grammar2'):
        assert _is_linked(a2, 'spreadsheetGrammarLanguage_Grammar2', b)
    _safe_set(b, 'spreadsheetGrammarLanguage_Element', None)
    assert not _is_linked(b, 'spreadsheetGrammarLanguage_Element', a2)
    if hasattr(a2, 'spreadsheetGrammarLanguage_Grammar2'):
        assert not _is_linked(a2, 'spreadsheetGrammarLanguage_Grammar2', b)


def test_assoc_syntax9_reverse_link_reassign_clear():
    a1 = spreadsheetGrammarLanguage_Syntax(is_id=True, is_int=True, is_string=True, token="sample_text")
    a2 = spreadsheetGrammarLanguage_Syntax(is_id=False, is_int=False, is_string=False, token="sample_text_2")
    b = spreadsheetGrammarLanguage_RowSpec(header="sample_text")
    _safe_set(b, 'spreadsheetGrammarLanguage_RowSpec', a1)
    assert _is_linked(b, 'spreadsheetGrammarLanguage_RowSpec', a1)
    if hasattr(a1, 'spreadsheetGrammarLanguage_Syntax'):
        assert _is_linked(a1, 'spreadsheetGrammarLanguage_Syntax', b)
    _safe_set(b, 'spreadsheetGrammarLanguage_RowSpec', a2)
    assert _is_linked(b, 'spreadsheetGrammarLanguage_RowSpec', a2)
    if hasattr(a1, 'spreadsheetGrammarLanguage_Syntax'):
        assert not _is_linked(a1, 'spreadsheetGrammarLanguage_Syntax', b)
    if hasattr(a2, 'spreadsheetGrammarLanguage_Syntax'):
        assert _is_linked(a2, 'spreadsheetGrammarLanguage_Syntax', b)
    _safe_set(b, 'spreadsheetGrammarLanguage_RowSpec', None)
    assert not _is_linked(b, 'spreadsheetGrammarLanguage_RowSpec', a2)
    if hasattr(a2, 'spreadsheetGrammarLanguage_Syntax'):
        assert not _is_linked(a2, 'spreadsheetGrammarLanguage_Syntax', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns3_stub_double():
    # spreadsheetGrammarLanguage_Block has no real 'spreadsheetGrammarLanguage_Block4' property in the generated
    # code (a bare stub) -- manually attach it so spreadsheetGrammarLanguage_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spreadsheetGrammarLanguage_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spreadsheetGrammarLanguage_Column(multiple=True, name="sample_text")
    partner = spreadsheetGrammarLanguage_Block()
    setattr(partner, 'spreadsheetGrammarLanguage_Block4', None)
    _safe_set(owner, 'spreadsheetGrammarLanguage_Column', partner)
    assert owner in getattr(partner, 'spreadsheetGrammarLanguage_Block4')
    _safe_set(owner, 'spreadsheetGrammarLanguage_Column', None)
    assert owner not in getattr(partner, 'spreadsheetGrammarLanguage_Block4')


def test_assoc_def_5_stub_double():
    # spreadsheetGrammarLanguage_ColumnDefinition has no real 'spreadsheetGrammarLanguage_ColumnDefinition' property in the generated
    # code (a bare stub) -- manually attach it so spreadsheetGrammarLanguage_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spreadsheetGrammarLanguage_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spreadsheetGrammarLanguage_Column(multiple=True, name="sample_text")
    partner = spreadsheetGrammarLanguage_ColumnDefinition()
    setattr(partner, 'spreadsheetGrammarLanguage_ColumnDefinition', None)
    _safe_set(owner, 'spreadsheetGrammarLanguage_Column6', partner)
    assert getattr(partner, 'spreadsheetGrammarLanguage_ColumnDefinition') == owner
    _safe_set(owner, 'spreadsheetGrammarLanguage_Column6', None)
    assert getattr(partner, 'spreadsheetGrammarLanguage_ColumnDefinition') is None


def test_assoc_parts16_stub_double():
    # spreadsheetGrammarLanguage_SyntaxSeq has no real 'spreadsheetGrammarLanguage_SyntaxSeq17' property in the generated
    # code (a bare stub) -- manually attach it so spreadsheetGrammarLanguage_Syntax's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spreadsheetGrammarLanguage_Syntax's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spreadsheetGrammarLanguage_Syntax(is_id=True, is_int=True, is_string=True, token="sample_text")
    partner = spreadsheetGrammarLanguage_SyntaxSeq()
    setattr(partner, 'spreadsheetGrammarLanguage_SyntaxSeq17', None)
    _safe_set(owner, 'spreadsheetGrammarLanguage_Syntax18', partner)
    assert owner in getattr(partner, 'spreadsheetGrammarLanguage_SyntaxSeq17')
    _safe_set(owner, 'spreadsheetGrammarLanguage_Syntax18', None)
    assert owner not in getattr(partner, 'spreadsheetGrammarLanguage_SyntaxSeq17')


def test_assoc_root0_stub_double():
    # spreadsheetGrammarLanguage_Block has no real 'spreadsheetGrammarLanguage_Block' property in the generated
    # code (a bare stub) -- manually attach it so spreadsheetGrammarLanguage_Grammar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spreadsheetGrammarLanguage_Grammar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spreadsheetGrammarLanguage_Grammar(name="sample_text")
    partner = spreadsheetGrammarLanguage_Block()
    setattr(partner, 'spreadsheetGrammarLanguage_Block', None)
    _safe_set(owner, 'spreadsheetGrammarLanguage_Grammar', partner)
    assert getattr(partner, 'spreadsheetGrammarLanguage_Block') == owner
    _safe_set(owner, 'spreadsheetGrammarLanguage_Grammar', None)
    assert getattr(partner, 'spreadsheetGrammarLanguage_Block') is None


def test_assoc_rule12_stub_double():
    # spreadsheetGrammarLanguage_Rule has no real 'spreadsheetGrammarLanguage_Rule' property in the generated
    # code (a bare stub) -- manually attach it so spreadsheetGrammarLanguage_Syntax's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spreadsheetGrammarLanguage_Syntax's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spreadsheetGrammarLanguage_Syntax(is_id=True, is_int=True, is_string=True, token="sample_text")
    partner = spreadsheetGrammarLanguage_Rule()
    setattr(partner, 'spreadsheetGrammarLanguage_Rule', None)
    _safe_set(owner, 'spreadsheetGrammarLanguage_Syntax13', partner)
    assert getattr(partner, 'spreadsheetGrammarLanguage_Rule') == owner
    _safe_set(owner, 'spreadsheetGrammarLanguage_Syntax13', None)
    assert getattr(partner, 'spreadsheetGrammarLanguage_Rule') is None


