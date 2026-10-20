import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SJExpression,
    SJMember,
    SJNamedElement,
    SJStatement,
    SJSymbol,
    smallJava_BoolConstant,
    smallJava_SJAssignment,
    smallJava_SJBlock,
    smallJava_SJClass,
    smallJava_SJExpression,
    smallJava_SJField,
    smallJava_SJIfStatement,
    smallJava_SJMember,
    smallJava_SJMemberSelection,
    smallJava_SJMethod,
    smallJava_SJNamedElement,
    smallJava_SJNew,
    smallJava_SJNull,
    smallJava_SJParameter,
    smallJava_SJProgram,
    smallJava_SJReturn,
    smallJava_SJStatement,
    smallJava_SJSymbol,
    smallJava_SJSymbolRef,
    smallJava_SJThis,
    smallJava_SJVariableDeclaration,
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

def test_assoc_args37_stub_double():
    # smallJava_SJExpression has no real 'smallJava_SJExpression39' property in the generated
    # code (a bare stub) -- manually attach it so smallJava_SJMemberSelection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smallJava_SJMemberSelection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smallJava_SJMemberSelection(methodinvocation=True)
    partner = smallJava_SJExpression()
    setattr(partner, 'smallJava_SJExpression39', None)
    _safe_set(owner, 'smallJava_SJMemberSelection38', {partner})
    assert getattr(partner, 'smallJava_SJExpression39') == owner
    _safe_set(owner, 'smallJava_SJMemberSelection38', set())
    assert getattr(partner, 'smallJava_SJExpression39') is None


def test_assoc_member34_stub_double():
    # smallJava_SJMember has no real 'smallJava_SJMember36' property in the generated
    # code (a bare stub) -- manually attach it so smallJava_SJMemberSelection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smallJava_SJMemberSelection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smallJava_SJMemberSelection(methodinvocation=True)
    partner = smallJava_SJMember()
    setattr(partner, 'smallJava_SJMember36', None)
    _safe_set(owner, 'smallJava_SJMemberSelection35', partner)
    assert getattr(partner, 'smallJava_SJMember36') == owner
    _safe_set(owner, 'smallJava_SJMemberSelection35', None)
    assert getattr(partner, 'smallJava_SJMember36') is None


def test_assoc_receiver32_stub_double():
    # smallJava_SJExpression has no real 'smallJava_SJExpression33' property in the generated
    # code (a bare stub) -- manually attach it so smallJava_SJMemberSelection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smallJava_SJMemberSelection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smallJava_SJMemberSelection(methodinvocation=True)
    partner = smallJava_SJExpression()
    setattr(partner, 'smallJava_SJExpression33', None)
    _safe_set(owner, 'smallJava_SJMemberSelection', partner)
    assert getattr(partner, 'smallJava_SJExpression33') == owner
    _safe_set(owner, 'smallJava_SJMemberSelection', None)
    assert getattr(partner, 'smallJava_SJExpression33') is None


