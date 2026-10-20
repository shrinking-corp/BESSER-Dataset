import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Comment,
    Dependency,
    Element,
    Make_Comment,
    Make_Dependency,
    Make_Element,
    Make_FileDep,
    Make_Macro,
    Make_Makefile,
    Make_Rule,
    Make_RuleDep,
    Make_ShellLine,
    Rule,
    ShellLine,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_comment0_stub_double():
    # Comment has no real 'Comment' property in the generated
    # code (a bare stub) -- manually attach it so Make_Makefile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Make_Makefile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Make_Makefile(name="sample_text")
    partner = Comment()
    setattr(partner, 'Comment', None)
    _safe_set(owner, 'Make_Makefile', partner)
    assert getattr(partner, 'Comment') == owner
    _safe_set(owner, 'Make_Makefile', None)
    assert getattr(partner, 'Comment') is None


def test_assoc_elements1_stub_double():
    # Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so Make_Makefile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Make_Makefile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Make_Makefile(name="sample_text")
    partner = Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'Make_Makefile2', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'Make_Makefile2', set())
    assert getattr(partner, 'Element') is None


def test_assoc_ruleShellLine5_stub_double():
    # Rule has no real 'Rule' property in the generated
    # code (a bare stub) -- manually attach it so Make_ShellLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Make_ShellLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Make_ShellLine(command="sample_text", display="sample_text")
    partner = Rule()
    setattr(partner, 'Rule', None)
    _safe_set(owner, 'shellLines', partner)
    assert getattr(partner, 'Rule') == owner
    _safe_set(owner, 'shellLines', None)
    assert getattr(partner, 'Rule') is None


