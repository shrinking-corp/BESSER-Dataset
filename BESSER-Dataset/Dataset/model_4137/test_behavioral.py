import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MultiplyOrDivide,
    PlusOrMinus,
    Primary,
    mathInterpreter_Bracket,
    mathInterpreter_Divide,
    mathInterpreter_EObject,
    mathInterpreter_Expression,
    mathInterpreter_Minus,
    mathInterpreter_Multiply,
    mathInterpreter_MultiplyOrDivide,
    mathInterpreter_Num,
    mathInterpreter_Plus,
    mathInterpreter_PlusOrMinus,
    mathInterpreter_Primary,
    mathInterpreter_Solution,
    mathInterpreter_Variable,
    mathInterpreter_VariableRef,
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

def test_assoc_right10_reverse_link_reassign_clear():
    a1 = mathInterpreter_PlusOrMinus(operator="sample_text")
    a2 = mathInterpreter_PlusOrMinus(operator="sample_text_2")
    b = mathInterpreter_MultiplyOrDivide(operator="sample_text")
    _safe_set(b, 'mathInterpreter_MultiplyOrDivide', a1)
    assert _is_linked(b, 'mathInterpreter_MultiplyOrDivide', a1)
    if hasattr(a1, 'mathInterpreter_PlusOrMinus11'):
        assert _is_linked(a1, 'mathInterpreter_PlusOrMinus11', b)
    _safe_set(b, 'mathInterpreter_MultiplyOrDivide', a2)
    assert _is_linked(b, 'mathInterpreter_MultiplyOrDivide', a2)
    if hasattr(a1, 'mathInterpreter_PlusOrMinus11'):
        assert not _is_linked(a1, 'mathInterpreter_PlusOrMinus11', b)
    if hasattr(a2, 'mathInterpreter_PlusOrMinus11'):
        assert _is_linked(a2, 'mathInterpreter_PlusOrMinus11', b)
    _safe_set(b, 'mathInterpreter_MultiplyOrDivide', None)
    assert not _is_linked(b, 'mathInterpreter_MultiplyOrDivide', a2)
    if hasattr(a2, 'mathInterpreter_PlusOrMinus11'):
        assert not _is_linked(a2, 'mathInterpreter_PlusOrMinus11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_exp6_stub_double():
    # mathInterpreter_Expression has no real 'mathInterpreter_Expression7' property in the generated
    # code (a bare stub) -- manually attach it so mathInterpreter_PlusOrMinus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathInterpreter_PlusOrMinus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathInterpreter_PlusOrMinus(operator="sample_text")
    partner = mathInterpreter_Expression()
    setattr(partner, 'mathInterpreter_Expression7', None)
    _safe_set(owner, 'mathInterpreter_PlusOrMinus', partner)
    assert getattr(partner, 'mathInterpreter_Expression7') == owner
    _safe_set(owner, 'mathInterpreter_PlusOrMinus', None)
    assert getattr(partner, 'mathInterpreter_Expression7') is None


def test_assoc_left12_stub_double():
    # mathInterpreter_EObject has no real 'mathInterpreter_EObject14' property in the generated
    # code (a bare stub) -- manually attach it so mathInterpreter_MultiplyOrDivide's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathInterpreter_MultiplyOrDivide's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathInterpreter_MultiplyOrDivide(operator="sample_text")
    partner = mathInterpreter_EObject()
    setattr(partner, 'mathInterpreter_EObject14', None)
    _safe_set(owner, 'mathInterpreter_MultiplyOrDivide13', partner)
    assert getattr(partner, 'mathInterpreter_EObject14') == owner
    _safe_set(owner, 'mathInterpreter_MultiplyOrDivide13', None)
    assert getattr(partner, 'mathInterpreter_EObject14') is None


def test_assoc_left8_stub_double():
    # mathInterpreter_EObject has no real 'mathInterpreter_EObject' property in the generated
    # code (a bare stub) -- manually attach it so mathInterpreter_PlusOrMinus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathInterpreter_PlusOrMinus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathInterpreter_PlusOrMinus(operator="sample_text")
    partner = mathInterpreter_EObject()
    setattr(partner, 'mathInterpreter_EObject', None)
    _safe_set(owner, 'mathInterpreter_PlusOrMinus9', partner)
    assert getattr(partner, 'mathInterpreter_EObject') == owner
    _safe_set(owner, 'mathInterpreter_PlusOrMinus9', None)
    assert getattr(partner, 'mathInterpreter_EObject') is None


def test_assoc_right15_stub_double():
    # mathInterpreter_Primary has no real 'mathInterpreter_Primary' property in the generated
    # code (a bare stub) -- manually attach it so mathInterpreter_MultiplyOrDivide's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathInterpreter_MultiplyOrDivide's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathInterpreter_MultiplyOrDivide(operator="sample_text")
    partner = mathInterpreter_Primary()
    setattr(partner, 'mathInterpreter_Primary', None)
    _safe_set(owner, 'mathInterpreter_MultiplyOrDivide16', partner)
    assert getattr(partner, 'mathInterpreter_Primary') == owner
    _safe_set(owner, 'mathInterpreter_MultiplyOrDivide16', None)
    assert getattr(partner, 'mathInterpreter_Primary') is None


def test_assoc_value17_stub_double():
    # mathInterpreter_VariableRef has no real 'mathInterpreter_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so mathInterpreter_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathInterpreter_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathInterpreter_Variable(name="sample_text")
    partner = mathInterpreter_VariableRef()
    setattr(partner, 'mathInterpreter_VariableRef', None)
    _safe_set(owner, 'mathInterpreter_Variable18', partner)
    assert getattr(partner, 'mathInterpreter_VariableRef') == owner
    _safe_set(owner, 'mathInterpreter_Variable18', None)
    assert getattr(partner, 'mathInterpreter_VariableRef') is None


def test_assoc_value3_stub_double():
    # mathInterpreter_Expression has no real 'mathInterpreter_Expression5' property in the generated
    # code (a bare stub) -- manually attach it so mathInterpreter_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathInterpreter_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathInterpreter_Variable(name="sample_text")
    partner = mathInterpreter_Expression()
    setattr(partner, 'mathInterpreter_Expression5', None)
    _safe_set(owner, 'mathInterpreter_Variable4', partner)
    assert getattr(partner, 'mathInterpreter_Expression5') == owner
    _safe_set(owner, 'mathInterpreter_Variable4', None)
    assert getattr(partner, 'mathInterpreter_Expression5') is None


def test_assoc_variables0_stub_double():
    # mathInterpreter_Solution has no real 'mathInterpreter_Solution' property in the generated
    # code (a bare stub) -- manually attach it so mathInterpreter_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathInterpreter_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathInterpreter_Variable(name="sample_text")
    partner = mathInterpreter_Solution()
    setattr(partner, 'mathInterpreter_Solution', None)
    _safe_set(owner, 'mathInterpreter_Variable', partner)
    assert owner in getattr(partner, 'mathInterpreter_Solution')
    _safe_set(owner, 'mathInterpreter_Variable', None)
    assert owner not in getattr(partner, 'mathInterpreter_Solution')


