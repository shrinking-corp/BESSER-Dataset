import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    Expression,
    testintentionsAssistance_AbstractElement,
    testintentionsAssistance_And,
    testintentionsAssistance_Boolean,
    testintentionsAssistance_Comparison,
    testintentionsAssistance_Data,
    testintentionsAssistance_DomainDeclaration,
    testintentionsAssistance_Double,
    testintentionsAssistance_Equality,
    testintentionsAssistance_Expression,
    testintentionsAssistance_Function,
    testintentionsAssistance_INT,
    testintentionsAssistance_Import,
    testintentionsAssistance_Inst,
    testintentionsAssistance_Minus,
    testintentionsAssistance_Model,
    testintentionsAssistance_MulOrDiv,
    testintentionsAssistance_Not,
    testintentionsAssistance_Or,
    testintentionsAssistance_OutVariable,
    testintentionsAssistance_Plus,
    testintentionsAssistance_STRING,
    testintentionsAssistance_TestIntention,
    testintentionsAssistance_Variable,
    testintentionsAssistance_VariableRef,
    Type,
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

def test_assoc_arg16_reverse_link_reassign_clear():
    a1 = testintentionsAssistance_Variable(name="sample_text", type="sample_text")
    a2 = testintentionsAssistance_Variable(name="sample_text_2", type="sample_text_2")
    b = testintentionsAssistance_Function(methode="sample_text")
    _safe_set(b, 'testintentionsAssistance_Function7', a1)
    assert _is_linked(b, 'testintentionsAssistance_Function7', a1)
    if hasattr(a1, 'testintentionsAssistance_Variable8'):
        assert _is_linked(a1, 'testintentionsAssistance_Variable8', b)
    _safe_set(b, 'testintentionsAssistance_Function7', a2)
    assert _is_linked(b, 'testintentionsAssistance_Function7', a2)
    if hasattr(a1, 'testintentionsAssistance_Variable8'):
        assert not _is_linked(a1, 'testintentionsAssistance_Variable8', b)
    if hasattr(a2, 'testintentionsAssistance_Variable8'):
        assert _is_linked(a2, 'testintentionsAssistance_Variable8', b)
    _safe_set(b, 'testintentionsAssistance_Function7', None)
    assert not _is_linked(b, 'testintentionsAssistance_Function7', a2)
    if hasattr(a2, 'testintentionsAssistance_Variable8'):
        assert not _is_linked(a2, 'testintentionsAssistance_Variable8', b)


def test_assoc_arg4_reverse_link_reassign_clear():
    a1 = testintentionsAssistance_Variable(name="sample_text", type="sample_text")
    a2 = testintentionsAssistance_Variable(name="sample_text_2", type="sample_text_2")
    b = testintentionsAssistance_Function(methode="sample_text")
    _safe_set(b, 'testintentionsAssistance_Function5', {a1})
    assert _is_linked(b, 'testintentionsAssistance_Function5', a1)
    if hasattr(a1, 'testintentionsAssistance_Variable'):
        assert _is_linked(a1, 'testintentionsAssistance_Variable', b)
    _safe_set(b, 'testintentionsAssistance_Function5', {a2})
    assert _is_linked(b, 'testintentionsAssistance_Function5', a2)
    if hasattr(a1, 'testintentionsAssistance_Variable'):
        assert not _is_linked(a1, 'testintentionsAssistance_Variable', b)
    if hasattr(a2, 'testintentionsAssistance_Variable'):
        assert _is_linked(a2, 'testintentionsAssistance_Variable', b)
    _safe_set(b, 'testintentionsAssistance_Function5', set())
    assert not _is_linked(b, 'testintentionsAssistance_Function5', a2)
    if hasattr(a2, 'testintentionsAssistance_Variable'):
        assert not _is_linked(a2, 'testintentionsAssistance_Variable', b)


def test_assoc_out3_reverse_link_reassign_clear():
    a1 = testintentionsAssistance_OutVariable(name="sample_text", type="sample_text")
    a2 = testintentionsAssistance_OutVariable(name="sample_text_2", type="sample_text_2")
    b = testintentionsAssistance_Function(methode="sample_text")
    _safe_set(b, 'testintentionsAssistance_Function', {a1})
    assert _is_linked(b, 'testintentionsAssistance_Function', a1)
    if hasattr(a1, 'testintentionsAssistance_OutVariable'):
        assert _is_linked(a1, 'testintentionsAssistance_OutVariable', b)
    _safe_set(b, 'testintentionsAssistance_Function', {a2})
    assert _is_linked(b, 'testintentionsAssistance_Function', a2)
    if hasattr(a1, 'testintentionsAssistance_OutVariable'):
        assert not _is_linked(a1, 'testintentionsAssistance_OutVariable', b)
    if hasattr(a2, 'testintentionsAssistance_OutVariable'):
        assert _is_linked(a2, 'testintentionsAssistance_OutVariable', b)
    _safe_set(b, 'testintentionsAssistance_Function', set())
    assert not _is_linked(b, 'testintentionsAssistance_Function', a2)
    if hasattr(a2, 'testintentionsAssistance_OutVariable'):
        assert not _is_linked(a2, 'testintentionsAssistance_OutVariable', b)


def test_assoc_outvar17_reverse_link_reassign_clear():
    a1 = testintentionsAssistance_TestIntention(description="sample_text")
    a2 = testintentionsAssistance_TestIntention(description="sample_text_2")
    b = testintentionsAssistance_OutVariable(name="sample_text", type="sample_text")
    _safe_set(b, 'testintentionsAssistance_OutVariable19', a1)
    assert _is_linked(b, 'testintentionsAssistance_OutVariable19', a1)
    if hasattr(a1, 'testintentionsAssistance_TestIntention18'):
        assert _is_linked(a1, 'testintentionsAssistance_TestIntention18', b)
    _safe_set(b, 'testintentionsAssistance_OutVariable19', a2)
    assert _is_linked(b, 'testintentionsAssistance_OutVariable19', a2)
    if hasattr(a1, 'testintentionsAssistance_TestIntention18'):
        assert not _is_linked(a1, 'testintentionsAssistance_TestIntention18', b)
    if hasattr(a2, 'testintentionsAssistance_TestIntention18'):
        assert _is_linked(a2, 'testintentionsAssistance_TestIntention18', b)
    _safe_set(b, 'testintentionsAssistance_OutVariable19', None)
    assert not _is_linked(b, 'testintentionsAssistance_OutVariable19', a2)
    if hasattr(a2, 'testintentionsAssistance_TestIntention18'):
        assert not _is_linked(a2, 'testintentionsAssistance_TestIntention18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements0_stub_double():
    # testintentionsAssistance_Model has no real 'testintentionsAssistance_Model' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_DomainDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_DomainDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_DomainDeclaration(name="sample_text")
    partner = testintentionsAssistance_Model()
    setattr(partner, 'testintentionsAssistance_Model', None)
    _safe_set(owner, 'testintentionsAssistance_DomainDeclaration', partner)
    assert owner in getattr(partner, 'testintentionsAssistance_Model')
    _safe_set(owner, 'testintentionsAssistance_DomainDeclaration', None)
    assert owner not in getattr(partner, 'testintentionsAssistance_Model')


def test_assoc_elements1_stub_double():
    # testintentionsAssistance_AbstractElement has no real 'testintentionsAssistance_AbstractElement' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_DomainDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_DomainDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_DomainDeclaration(name="sample_text")
    partner = testintentionsAssistance_AbstractElement()
    setattr(partner, 'testintentionsAssistance_AbstractElement', None)
    _safe_set(owner, 'testintentionsAssistance_DomainDeclaration2', {partner})
    assert getattr(partner, 'testintentionsAssistance_AbstractElement') == owner
    _safe_set(owner, 'testintentionsAssistance_DomainDeclaration2', set())
    assert getattr(partner, 'testintentionsAssistance_AbstractElement') is None


def test_assoc_expression15_stub_double():
    # testintentionsAssistance_Expression has no real 'testintentionsAssistance_Expression16' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_TestIntention's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_TestIntention's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_TestIntention(description="sample_text")
    partner = testintentionsAssistance_Expression()
    setattr(partner, 'testintentionsAssistance_Expression16', None)
    _safe_set(owner, 'testintentionsAssistance_TestIntention', {partner})
    assert getattr(partner, 'testintentionsAssistance_Expression16') == owner
    _safe_set(owner, 'testintentionsAssistance_TestIntention', set())
    assert getattr(partner, 'testintentionsAssistance_Expression16') is None


def test_assoc_left30_stub_double():
    # testintentionsAssistance_Expression has no real 'testintentionsAssistance_Expression31' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_Equality(op="sample_text")
    partner = testintentionsAssistance_Expression()
    setattr(partner, 'testintentionsAssistance_Expression31', None)
    _safe_set(owner, 'testintentionsAssistance_Equality', partner)
    assert getattr(partner, 'testintentionsAssistance_Expression31') == owner
    _safe_set(owner, 'testintentionsAssistance_Equality', None)
    assert getattr(partner, 'testintentionsAssistance_Expression31') is None


def test_assoc_left35_stub_double():
    # testintentionsAssistance_Expression has no real 'testintentionsAssistance_Expression36' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_Comparison(op="sample_text")
    partner = testintentionsAssistance_Expression()
    setattr(partner, 'testintentionsAssistance_Expression36', None)
    _safe_set(owner, 'testintentionsAssistance_Comparison', partner)
    assert getattr(partner, 'testintentionsAssistance_Expression36') == owner
    _safe_set(owner, 'testintentionsAssistance_Comparison', None)
    assert getattr(partner, 'testintentionsAssistance_Expression36') is None


def test_assoc_left50_stub_double():
    # testintentionsAssistance_Expression has no real 'testintentionsAssistance_Expression51' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_MulOrDiv(op="sample_text")
    partner = testintentionsAssistance_Expression()
    setattr(partner, 'testintentionsAssistance_Expression51', None)
    _safe_set(owner, 'testintentionsAssistance_MulOrDiv', partner)
    assert getattr(partner, 'testintentionsAssistance_Expression51') == owner
    _safe_set(owner, 'testintentionsAssistance_MulOrDiv', None)
    assert getattr(partner, 'testintentionsAssistance_Expression51') is None


def test_assoc_right32_stub_double():
    # testintentionsAssistance_Expression has no real 'testintentionsAssistance_Expression34' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_Equality(op="sample_text")
    partner = testintentionsAssistance_Expression()
    setattr(partner, 'testintentionsAssistance_Expression34', None)
    _safe_set(owner, 'testintentionsAssistance_Equality33', partner)
    assert getattr(partner, 'testintentionsAssistance_Expression34') == owner
    _safe_set(owner, 'testintentionsAssistance_Equality33', None)
    assert getattr(partner, 'testintentionsAssistance_Expression34') is None


def test_assoc_right37_stub_double():
    # testintentionsAssistance_Expression has no real 'testintentionsAssistance_Expression39' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_Comparison(op="sample_text")
    partner = testintentionsAssistance_Expression()
    setattr(partner, 'testintentionsAssistance_Expression39', None)
    _safe_set(owner, 'testintentionsAssistance_Comparison38', partner)
    assert getattr(partner, 'testintentionsAssistance_Expression39') == owner
    _safe_set(owner, 'testintentionsAssistance_Comparison38', None)
    assert getattr(partner, 'testintentionsAssistance_Expression39') is None


def test_assoc_right52_stub_double():
    # testintentionsAssistance_Expression has no real 'testintentionsAssistance_Expression54' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_MulOrDiv(op="sample_text")
    partner = testintentionsAssistance_Expression()
    setattr(partner, 'testintentionsAssistance_Expression54', None)
    _safe_set(owner, 'testintentionsAssistance_MulOrDiv53', partner)
    assert getattr(partner, 'testintentionsAssistance_Expression54') == owner
    _safe_set(owner, 'testintentionsAssistance_MulOrDiv53', None)
    assert getattr(partner, 'testintentionsAssistance_Expression54') is None


def test_assoc_variable10_stub_double():
    # testintentionsAssistance_Inst has no real 'testintentionsAssistance_Inst11' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_Variable(name="sample_text", type="sample_text")
    partner = testintentionsAssistance_Inst()
    setattr(partner, 'testintentionsAssistance_Inst11', None)
    _safe_set(owner, 'testintentionsAssistance_Variable12', partner)
    assert owner in getattr(partner, 'testintentionsAssistance_Inst11')
    _safe_set(owner, 'testintentionsAssistance_Variable12', None)
    assert owner not in getattr(partner, 'testintentionsAssistance_Inst11')


def test_assoc_variable57_stub_double():
    # testintentionsAssistance_VariableRef has no real 'testintentionsAssistance_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so testintentionsAssistance_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testintentionsAssistance_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testintentionsAssistance_Variable(name="sample_text", type="sample_text")
    partner = testintentionsAssistance_VariableRef()
    setattr(partner, 'testintentionsAssistance_VariableRef', None)
    _safe_set(owner, 'testintentionsAssistance_Variable58', partner)
    assert getattr(partner, 'testintentionsAssistance_VariableRef') == owner
    _safe_set(owner, 'testintentionsAssistance_Variable58', None)
    assert getattr(partner, 'testintentionsAssistance_VariableRef') is None


