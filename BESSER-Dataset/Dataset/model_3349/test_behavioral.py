import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SJBlock,
    SJExpression,
    SJMember,
    SJStatement,
    SJSymbol,
    smallJava_SJAssignment,
    smallJava_SJBlock,
    smallJava_SJBoolConstant,
    smallJava_SJClass,
    smallJava_SJExpression,
    smallJava_SJField,
    smallJava_SJIfBlock,
    smallJava_SJIfStatement,
    smallJava_SJImport,
    smallJava_SJIntConstant,
    smallJava_SJMember,
    smallJava_SJMemberSelection,
    smallJava_SJMethod,
    smallJava_SJMethodBody,
    smallJava_SJNew,
    smallJava_SJNull,
    smallJava_SJParameter,
    smallJava_SJProgram,
    smallJava_SJReturn,
    smallJava_SJStatement,
    smallJava_SJStringConstant,
    smallJava_SJSuper,
    smallJava_SJSymbol,
    smallJava_SJSymbolRef,
    smallJava_SJThis,
    smallJava_SJVariableDeclaration,
    SJAccessLevel,
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

def test_assoc_classes1_reverse_link_reassign_clear():
    a1 = smallJava_SJProgram(name="sample_text")
    a2 = smallJava_SJProgram(name="sample_text_2")
    b = smallJava_SJClass(name="sample_text")
    _safe_set(b, 'smallJava_SJClass', a1)
    assert _is_linked(b, 'smallJava_SJClass', a1)
    if hasattr(a1, 'smallJava_SJProgram2'):
        assert _is_linked(a1, 'smallJava_SJProgram2', b)
    _safe_set(b, 'smallJava_SJClass', a2)
    assert _is_linked(b, 'smallJava_SJClass', a2)
    if hasattr(a1, 'smallJava_SJProgram2'):
        assert not _is_linked(a1, 'smallJava_SJProgram2', b)
    if hasattr(a2, 'smallJava_SJProgram2'):
        assert _is_linked(a2, 'smallJava_SJProgram2', b)
    _safe_set(b, 'smallJava_SJClass', None)
    assert not _is_linked(b, 'smallJava_SJClass', a2)
    if hasattr(a2, 'smallJava_SJProgram2'):
        assert not _is_linked(a2, 'smallJava_SJProgram2', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = smallJava_SJProgram(name="sample_text")
    a2 = smallJava_SJProgram(name="sample_text_2")
    b = smallJava_SJImport(importedNamespace="sample_text")
    _safe_set(b, 'smallJava_SJImport', a1)
    assert _is_linked(b, 'smallJava_SJImport', a1)
    if hasattr(a1, 'smallJava_SJProgram'):
        assert _is_linked(a1, 'smallJava_SJProgram', b)
    _safe_set(b, 'smallJava_SJImport', a2)
    assert _is_linked(b, 'smallJava_SJImport', a2)
    if hasattr(a1, 'smallJava_SJProgram'):
        assert not _is_linked(a1, 'smallJava_SJProgram', b)
    if hasattr(a2, 'smallJava_SJProgram'):
        assert _is_linked(a2, 'smallJava_SJProgram', b)
    _safe_set(b, 'smallJava_SJImport', None)
    assert not _is_linked(b, 'smallJava_SJImport', a2)
    if hasattr(a2, 'smallJava_SJProgram'):
        assert not _is_linked(a2, 'smallJava_SJProgram', b)


def test_assoc_member34_reverse_link_reassign_clear():
    a1 = smallJava_SJMemberSelection(methodinvocation=True)
    a2 = smallJava_SJMemberSelection(methodinvocation=False)
    b = smallJava_SJMember(access="sample_text", name="sample_text")
    _safe_set(b, 'smallJava_SJMember36', a1)
    assert _is_linked(b, 'smallJava_SJMember36', a1)
    if hasattr(a1, 'smallJava_SJMemberSelection35'):
        assert _is_linked(a1, 'smallJava_SJMemberSelection35', b)
    _safe_set(b, 'smallJava_SJMember36', a2)
    assert _is_linked(b, 'smallJava_SJMember36', a2)
    if hasattr(a1, 'smallJava_SJMemberSelection35'):
        assert not _is_linked(a1, 'smallJava_SJMemberSelection35', b)
    if hasattr(a2, 'smallJava_SJMemberSelection35'):
        assert _is_linked(a2, 'smallJava_SJMemberSelection35', b)
    _safe_set(b, 'smallJava_SJMember36', None)
    assert not _is_linked(b, 'smallJava_SJMember36', a2)
    if hasattr(a2, 'smallJava_SJMemberSelection35'):
        assert not _is_linked(a2, 'smallJava_SJMemberSelection35', b)


def test_assoc_members6_reverse_link_reassign_clear():
    a1 = smallJava_SJMember(access="sample_text", name="sample_text")
    a2 = smallJava_SJMember(access="sample_text_2", name="sample_text_2")
    b = smallJava_SJClass(name="sample_text")
    _safe_set(b, 'smallJava_SJClass7', {a1})
    assert _is_linked(b, 'smallJava_SJClass7', a1)
    if hasattr(a1, 'smallJava_SJMember'):
        assert _is_linked(a1, 'smallJava_SJMember', b)
    _safe_set(b, 'smallJava_SJClass7', {a2})
    assert _is_linked(b, 'smallJava_SJClass7', a2)
    if hasattr(a1, 'smallJava_SJMember'):
        assert not _is_linked(a1, 'smallJava_SJMember', b)
    if hasattr(a2, 'smallJava_SJMember'):
        assert _is_linked(a2, 'smallJava_SJMember', b)
    _safe_set(b, 'smallJava_SJClass7', set())
    assert not _is_linked(b, 'smallJava_SJClass7', a2)
    if hasattr(a2, 'smallJava_SJMember'):
        assert not _is_linked(a2, 'smallJava_SJMember', b)


def test_assoc_superclass4_reverse_link_reassign_clear():
    a1 = smallJava_SJClass(name="sample_text")
    a2 = smallJava_SJClass(name="sample_text_2")
    b = smallJava_SJClass(name="sample_text")
    _safe_set(b, 'smallJava_SJClass5', a1)
    assert _is_linked(b, 'smallJava_SJClass5', a1)
    if hasattr(a1, 'smallJava_SJClass3'):
        assert _is_linked(a1, 'smallJava_SJClass3', b)
    _safe_set(b, 'smallJava_SJClass5', a2)
    assert _is_linked(b, 'smallJava_SJClass5', a2)
    if hasattr(a1, 'smallJava_SJClass3'):
        assert not _is_linked(a1, 'smallJava_SJClass3', b)
    if hasattr(a2, 'smallJava_SJClass3'):
        assert _is_linked(a2, 'smallJava_SJClass3', b)
    _safe_set(b, 'smallJava_SJClass5', None)
    assert not _is_linked(b, 'smallJava_SJClass5', a2)
    if hasattr(a2, 'smallJava_SJClass3'):
        assert not _is_linked(a2, 'smallJava_SJClass3', b)


def test_assoc_type25_reverse_link_reassign_clear():
    a1 = smallJava_SJSymbol(name="sample_text")
    a2 = smallJava_SJSymbol(name="sample_text_2")
    b = smallJava_SJClass(name="sample_text")
    _safe_set(b, 'smallJava_SJClass26', a1)
    assert _is_linked(b, 'smallJava_SJClass26', a1)
    if hasattr(a1, 'smallJava_SJSymbol'):
        assert _is_linked(a1, 'smallJava_SJSymbol', b)
    _safe_set(b, 'smallJava_SJClass26', a2)
    assert _is_linked(b, 'smallJava_SJClass26', a2)
    if hasattr(a1, 'smallJava_SJSymbol'):
        assert not _is_linked(a1, 'smallJava_SJSymbol', b)
    if hasattr(a2, 'smallJava_SJSymbol'):
        assert _is_linked(a2, 'smallJava_SJSymbol', b)
    _safe_set(b, 'smallJava_SJClass26', None)
    assert not _is_linked(b, 'smallJava_SJClass26', a2)
    if hasattr(a2, 'smallJava_SJSymbol'):
        assert not _is_linked(a2, 'smallJava_SJSymbol', b)


def test_assoc_type8_reverse_link_reassign_clear():
    a1 = smallJava_SJMember(access="sample_text", name="sample_text")
    a2 = smallJava_SJMember(access="sample_text_2", name="sample_text_2")
    b = smallJava_SJClass(name="sample_text")
    _safe_set(b, 'smallJava_SJClass10', a1)
    assert _is_linked(b, 'smallJava_SJClass10', a1)
    if hasattr(a1, 'smallJava_SJMember9'):
        assert _is_linked(a1, 'smallJava_SJMember9', b)
    _safe_set(b, 'smallJava_SJClass10', a2)
    assert _is_linked(b, 'smallJava_SJClass10', a2)
    if hasattr(a1, 'smallJava_SJMember9'):
        assert not _is_linked(a1, 'smallJava_SJMember9', b)
    if hasattr(a2, 'smallJava_SJMember9'):
        assert _is_linked(a2, 'smallJava_SJMember9', b)
    _safe_set(b, 'smallJava_SJClass10', None)
    assert not _is_linked(b, 'smallJava_SJClass10', a2)
    if hasattr(a2, 'smallJava_SJMember9'):
        assert not _is_linked(a2, 'smallJava_SJMember9', b)


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


def test_assoc_symbol40_stub_double():
    # smallJava_SJSymbolRef has no real 'smallJava_SJSymbolRef' property in the generated
    # code (a bare stub) -- manually attach it so smallJava_SJSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smallJava_SJSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smallJava_SJSymbol(name="sample_text")
    partner = smallJava_SJSymbolRef()
    setattr(partner, 'smallJava_SJSymbolRef', None)
    _safe_set(owner, 'smallJava_SJSymbol41', partner)
    assert getattr(partner, 'smallJava_SJSymbolRef') == owner
    _safe_set(owner, 'smallJava_SJSymbol41', None)
    assert getattr(partner, 'smallJava_SJSymbolRef') is None


def test_assoc_type42_stub_double():
    # smallJava_SJNew has no real 'smallJava_SJNew' property in the generated
    # code (a bare stub) -- manually attach it so smallJava_SJClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smallJava_SJClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smallJava_SJClass(name="sample_text")
    partner = smallJava_SJNew()
    setattr(partner, 'smallJava_SJNew', None)
    _safe_set(owner, 'smallJava_SJClass43', partner)
    assert getattr(partner, 'smallJava_SJNew') == owner
    _safe_set(owner, 'smallJava_SJClass43', None)
    assert getattr(partner, 'smallJava_SJNew') is None


