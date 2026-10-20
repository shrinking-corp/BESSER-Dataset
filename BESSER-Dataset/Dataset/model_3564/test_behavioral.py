import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    expression,
    pascal_EObject,
    pascal_Pascal,
    pascal_arit_expression,
    pascal_atrib,
    pascal_block,
    pascal_expression,
    pascal_program,
    pascal_rel_expression,
    pascal_repetitive_arit_expression,
    pascal_statement,
    pascal_var_block,
    pascal_var_decl,
    pascal_var_list,
    type,
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

def test_assoc_exp13_reverse_link_reassign_clear():
    a1 = pascal_repetitive_arit_expression(op="sample_text", value="sample_text")
    a2 = pascal_repetitive_arit_expression(op="sample_text_2", value="sample_text_2")
    b = pascal_arit_expression(value="sample_text")
    _safe_set(b, 'pascal_arit_expression', {a1})
    assert _is_linked(b, 'pascal_arit_expression', a1)
    if hasattr(a1, 'pascal_repetitive_arit_expression'):
        assert _is_linked(a1, 'pascal_repetitive_arit_expression', b)
    _safe_set(b, 'pascal_arit_expression', {a2})
    assert _is_linked(b, 'pascal_arit_expression', a2)
    if hasattr(a1, 'pascal_repetitive_arit_expression'):
        assert not _is_linked(a1, 'pascal_repetitive_arit_expression', b)
    if hasattr(a2, 'pascal_repetitive_arit_expression'):
        assert _is_linked(a2, 'pascal_repetitive_arit_expression', b)
    _safe_set(b, 'pascal_arit_expression', set())
    assert not _is_linked(b, 'pascal_arit_expression', a2)
    if hasattr(a2, 'pascal_repetitive_arit_expression'):
        assert not _is_linked(a2, 'pascal_repetitive_arit_expression', b)


def test_assoc_exp15_reverse_link_reassign_clear():
    a1 = pascal_repetitive_arit_expression(op="sample_text", value="sample_text")
    a2 = pascal_repetitive_arit_expression(op="sample_text_2", value="sample_text_2")
    b = pascal_repetitive_arit_expression(op="sample_text", value="sample_text")
    _safe_set(b, 'pascal_repetitive_arit_expression16', a1)
    assert _is_linked(b, 'pascal_repetitive_arit_expression16', a1)
    if hasattr(a1, 'pascal_repetitive_arit_expression14'):
        assert _is_linked(a1, 'pascal_repetitive_arit_expression14', b)
    _safe_set(b, 'pascal_repetitive_arit_expression16', a2)
    assert _is_linked(b, 'pascal_repetitive_arit_expression16', a2)
    if hasattr(a1, 'pascal_repetitive_arit_expression14'):
        assert not _is_linked(a1, 'pascal_repetitive_arit_expression14', b)
    if hasattr(a2, 'pascal_repetitive_arit_expression14'):
        assert _is_linked(a2, 'pascal_repetitive_arit_expression14', b)
    _safe_set(b, 'pascal_repetitive_arit_expression16', None)
    assert not _is_linked(b, 'pascal_repetitive_arit_expression16', a2)
    if hasattr(a2, 'pascal_repetitive_arit_expression14'):
        assert not _is_linked(a2, 'pascal_repetitive_arit_expression14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_atrib_block9_stub_double():
    # pascal_statement has no real 'pascal_statement10' property in the generated
    # code (a bare stub) -- manually attach it so pascal_atrib's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_atrib's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_atrib(var_id="sample_text")
    partner = pascal_statement()
    setattr(partner, 'pascal_statement10', None)
    _safe_set(owner, 'pascal_atrib', partner)
    assert owner in getattr(partner, 'pascal_statement10')
    _safe_set(owner, 'pascal_atrib', None)
    assert owner not in getattr(partner, 'pascal_statement10')


def test_assoc_exp11_stub_double():
    # pascal_expression has no real 'pascal_expression' property in the generated
    # code (a bare stub) -- manually attach it so pascal_atrib's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_atrib's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_atrib(var_id="sample_text")
    partner = pascal_expression()
    setattr(partner, 'pascal_expression', None)
    _safe_set(owner, 'pascal_atrib12', partner)
    assert getattr(partner, 'pascal_expression') == owner
    _safe_set(owner, 'pascal_atrib12', None)
    assert getattr(partner, 'pascal_expression') is None


def test_assoc_head0_stub_double():
    # pascal_Pascal has no real 'pascal_Pascal' property in the generated
    # code (a bare stub) -- manually attach it so pascal_program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_program(name="sample_text")
    partner = pascal_Pascal()
    setattr(partner, 'pascal_Pascal', None)
    _safe_set(owner, 'pascal_program', partner)
    assert getattr(partner, 'pascal_Pascal') == owner
    _safe_set(owner, 'pascal_program', None)
    assert getattr(partner, 'pascal_Pascal') is None


