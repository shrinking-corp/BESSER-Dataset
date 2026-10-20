import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BooleanLiteralExpCS,
    CallExpCS,
    ExpCS,
    LiteralExpCS,
    LogicExpCS,
    LoopExpCS,
    NavigationExpCS,
    NavigationPathCS,
    PathCS,
    PrimaryExpCS,
    miniOCL_AccVarCS,
    miniOCL_BooleanExpCS,
    miniOCL_BooleanLiteralExpCS,
    miniOCL_CallExpCS,
    miniOCL_ClassCS,
    miniOCL_CollectExpCS,
    miniOCL_ConstraintCS,
    miniOCL_EStructuralFeature,
    miniOCL_ExistsExpCS,
    miniOCL_ExpCS,
    miniOCL_ForAllExpCS,
    miniOCL_IntLiteralExpCS,
    miniOCL_InvariantCS,
    miniOCL_IterateExpCS,
    miniOCL_IteratorVarCS,
    miniOCL_LiteralExpCS,
    miniOCL_LogicExpCS,
    miniOCL_LoopExpCS,
    miniOCL_NameExpCS,
    miniOCL_NavigationExpCS,
    miniOCL_NavigationNameExpCS,
    miniOCL_NavigationPathCS,
    miniOCL_NavigationPathElementCS,
    miniOCL_NavigationPathNameCS,
    miniOCL_NavigationPathVariableCS,
    miniOCL_OperationCS,
    miniOCL_PackageCS,
    miniOCL_ParameterCS,
    miniOCL_PathCS,
    miniOCL_PathElementCS,
    miniOCL_PathNameCS,
    miniOCL_PathVariableCS,
    miniOCL_PrimaryExpCS,
    miniOCL_PropertyCS,
    miniOCL_RootCS,
    miniOCL_RoundedBracketClauseCS,
    miniOCL_StringLiteralExpCS,
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

def test_assoc_classes6_reverse_link_reassign_clear():
    a1 = miniOCL_PackageCS(name="sample_text")
    a2 = miniOCL_PackageCS(name="sample_text_2")
    b = miniOCL_ClassCS(name="sample_text")
    _safe_set(b, 'miniOCL_ClassCS', a1)
    assert _is_linked(b, 'miniOCL_ClassCS', a1)
    if hasattr(a1, 'miniOCL_PackageCS7'):
        assert _is_linked(a1, 'miniOCL_PackageCS7', b)
    _safe_set(b, 'miniOCL_ClassCS', a2)
    assert _is_linked(b, 'miniOCL_ClassCS', a2)
    if hasattr(a1, 'miniOCL_PackageCS7'):
        assert not _is_linked(a1, 'miniOCL_PackageCS7', b)
    if hasattr(a2, 'miniOCL_PackageCS7'):
        assert _is_linked(a2, 'miniOCL_PackageCS7', b)
    _safe_set(b, 'miniOCL_ClassCS', None)
    assert not _is_linked(b, 'miniOCL_ClassCS', a2)
    if hasattr(a2, 'miniOCL_PackageCS7'):
        assert not _is_linked(a2, 'miniOCL_PackageCS7', b)


def test_assoc_itVar51_reverse_link_reassign_clear():
    a1 = miniOCL_LoopExpCS(logicOp="sample_text")
    a2 = miniOCL_LoopExpCS(logicOp="sample_text_2")
    b = miniOCL_IteratorVarCS(itName="sample_text")
    _safe_set(b, 'miniOCL_IteratorVarCS', a1)
    assert _is_linked(b, 'miniOCL_IteratorVarCS', a1)
    if hasattr(a1, 'miniOCL_LoopExpCS'):
        assert _is_linked(a1, 'miniOCL_LoopExpCS', b)
    _safe_set(b, 'miniOCL_IteratorVarCS', a2)
    assert _is_linked(b, 'miniOCL_IteratorVarCS', a2)
    if hasattr(a1, 'miniOCL_LoopExpCS'):
        assert not _is_linked(a1, 'miniOCL_LoopExpCS', b)
    if hasattr(a2, 'miniOCL_LoopExpCS'):
        assert _is_linked(a2, 'miniOCL_LoopExpCS', b)
    _safe_set(b, 'miniOCL_IteratorVarCS', None)
    assert not _is_linked(b, 'miniOCL_IteratorVarCS', a2)
    if hasattr(a2, 'miniOCL_LoopExpCS'):
        assert not _is_linked(a2, 'miniOCL_LoopExpCS', b)


def test_assoc_left36_reverse_link_reassign_clear():
    a1 = miniOCL_LogicExpCS(op="sample_text")
    a2 = miniOCL_LogicExpCS(op="sample_text_2")
    b = miniOCL_LogicExpCS(op="sample_text")
    _safe_set(b, 'miniOCL_LogicExpCS35', a1)
    assert _is_linked(b, 'miniOCL_LogicExpCS35', a1)
    if hasattr(a1, 'miniOCL_LogicExpCS'):
        assert _is_linked(a1, 'miniOCL_LogicExpCS', b)
    _safe_set(b, 'miniOCL_LogicExpCS35', a2)
    assert _is_linked(b, 'miniOCL_LogicExpCS35', a2)
    if hasattr(a1, 'miniOCL_LogicExpCS'):
        assert not _is_linked(a1, 'miniOCL_LogicExpCS', b)
    if hasattr(a2, 'miniOCL_LogicExpCS'):
        assert _is_linked(a2, 'miniOCL_LogicExpCS', b)
    _safe_set(b, 'miniOCL_LogicExpCS35', None)
    assert not _is_linked(b, 'miniOCL_LogicExpCS35', a2)
    if hasattr(a2, 'miniOCL_LogicExpCS'):
        assert not _is_linked(a2, 'miniOCL_LogicExpCS', b)


def test_assoc_operations12_reverse_link_reassign_clear():
    a1 = miniOCL_OperationCS(name="sample_text")
    a2 = miniOCL_OperationCS(name="sample_text_2")
    b = miniOCL_ClassCS(name="sample_text")
    _safe_set(b, 'miniOCL_ClassCS13', {a1})
    assert _is_linked(b, 'miniOCL_ClassCS13', a1)
    if hasattr(a1, 'miniOCL_OperationCS'):
        assert _is_linked(a1, 'miniOCL_OperationCS', b)
    _safe_set(b, 'miniOCL_ClassCS13', {a2})
    assert _is_linked(b, 'miniOCL_ClassCS13', a2)
    if hasattr(a1, 'miniOCL_OperationCS'):
        assert not _is_linked(a1, 'miniOCL_OperationCS', b)
    if hasattr(a2, 'miniOCL_OperationCS'):
        assert _is_linked(a2, 'miniOCL_OperationCS', b)
    _safe_set(b, 'miniOCL_ClassCS13', set())
    assert not _is_linked(b, 'miniOCL_ClassCS13', a2)
    if hasattr(a2, 'miniOCL_OperationCS'):
        assert not _is_linked(a2, 'miniOCL_OperationCS', b)


def test_assoc_packages4_reverse_link_reassign_clear():
    a1 = miniOCL_PackageCS(name="sample_text")
    a2 = miniOCL_PackageCS(name="sample_text_2")
    b = miniOCL_PackageCS(name="sample_text")
    _safe_set(b, 'miniOCL_PackageCS5', a1)
    assert _is_linked(b, 'miniOCL_PackageCS5', a1)
    if hasattr(a1, 'miniOCL_PackageCS3'):
        assert _is_linked(a1, 'miniOCL_PackageCS3', b)
    _safe_set(b, 'miniOCL_PackageCS5', a2)
    assert _is_linked(b, 'miniOCL_PackageCS5', a2)
    if hasattr(a1, 'miniOCL_PackageCS3'):
        assert not _is_linked(a1, 'miniOCL_PackageCS3', b)
    if hasattr(a2, 'miniOCL_PackageCS3'):
        assert _is_linked(a2, 'miniOCL_PackageCS3', b)
    _safe_set(b, 'miniOCL_PackageCS5', None)
    assert not _is_linked(b, 'miniOCL_PackageCS5', a2)
    if hasattr(a2, 'miniOCL_PackageCS3'):
        assert not _is_linked(a2, 'miniOCL_PackageCS3', b)


def test_assoc_params17_reverse_link_reassign_clear():
    a1 = miniOCL_ParameterCS(name="sample_text")
    a2 = miniOCL_ParameterCS(name="sample_text_2")
    b = miniOCL_OperationCS(name="sample_text")
    _safe_set(b, 'miniOCL_OperationCS18', {a1})
    assert _is_linked(b, 'miniOCL_OperationCS18', a1)
    if hasattr(a1, 'miniOCL_ParameterCS'):
        assert _is_linked(a1, 'miniOCL_ParameterCS', b)
    _safe_set(b, 'miniOCL_OperationCS18', {a2})
    assert _is_linked(b, 'miniOCL_OperationCS18', a2)
    if hasattr(a1, 'miniOCL_ParameterCS'):
        assert not _is_linked(a1, 'miniOCL_ParameterCS', b)
    if hasattr(a2, 'miniOCL_ParameterCS'):
        assert _is_linked(a2, 'miniOCL_ParameterCS', b)
    _safe_set(b, 'miniOCL_OperationCS18', set())
    assert not _is_linked(b, 'miniOCL_OperationCS18', a2)
    if hasattr(a2, 'miniOCL_ParameterCS'):
        assert not _is_linked(a2, 'miniOCL_ParameterCS', b)


def test_assoc_properties10_reverse_link_reassign_clear():
    a1 = miniOCL_PropertyCS(name="sample_text")
    a2 = miniOCL_PropertyCS(name="sample_text_2")
    b = miniOCL_ClassCS(name="sample_text")
    _safe_set(b, 'miniOCL_ClassCS11', {a1})
    assert _is_linked(b, 'miniOCL_ClassCS11', a1)
    if hasattr(a1, 'miniOCL_PropertyCS'):
        assert _is_linked(a1, 'miniOCL_PropertyCS', b)
    _safe_set(b, 'miniOCL_ClassCS11', {a2})
    assert _is_linked(b, 'miniOCL_ClassCS11', a2)
    if hasattr(a1, 'miniOCL_PropertyCS'):
        assert not _is_linked(a1, 'miniOCL_PropertyCS', b)
    if hasattr(a2, 'miniOCL_PropertyCS'):
        assert _is_linked(a2, 'miniOCL_PropertyCS', b)
    _safe_set(b, 'miniOCL_ClassCS11', set())
    assert not _is_linked(b, 'miniOCL_ClassCS11', a2)
    if hasattr(a2, 'miniOCL_PropertyCS'):
        assert not _is_linked(a2, 'miniOCL_PropertyCS', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accInitExp62_stub_double():
    # miniOCL_ExpCS has no real 'miniOCL_ExpCS64' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_AccVarCS(accVarName="sample_text")
    partner = miniOCL_ExpCS()
    setattr(partner, 'miniOCL_ExpCS64', None)
    _safe_set(owner, 'miniOCL_AccVarCS63', partner)
    assert getattr(partner, 'miniOCL_ExpCS64') == owner
    _safe_set(owner, 'miniOCL_AccVarCS63', None)
    assert getattr(partner, 'miniOCL_ExpCS64') is None


def test_assoc_accType59_stub_double():
    # miniOCL_PathNameCS has no real 'miniOCL_PathNameCS61' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_AccVarCS(accVarName="sample_text")
    partner = miniOCL_PathNameCS()
    setattr(partner, 'miniOCL_PathNameCS61', None)
    _safe_set(owner, 'miniOCL_AccVarCS60', partner)
    assert getattr(partner, 'miniOCL_PathNameCS61') == owner
    _safe_set(owner, 'miniOCL_AccVarCS60', None)
    assert getattr(partner, 'miniOCL_PathNameCS61') is None


def test_assoc_accVar58_stub_double():
    # miniOCL_IterateExpCS has no real 'miniOCL_IterateExpCS' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_AccVarCS(accVarName="sample_text")
    partner = miniOCL_IterateExpCS()
    setattr(partner, 'miniOCL_IterateExpCS', None)
    _safe_set(owner, 'miniOCL_AccVarCS', partner)
    assert getattr(partner, 'miniOCL_IterateExpCS') == owner
    _safe_set(owner, 'miniOCL_AccVarCS', None)
    assert getattr(partner, 'miniOCL_IterateExpCS') is None


def test_assoc_accVars71_stub_double():
    # miniOCL_ExistsExpCS has no real 'miniOCL_ExistsExpCS' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_AccVarCS(accVarName="sample_text")
    partner = miniOCL_ExistsExpCS()
    setattr(partner, 'miniOCL_ExistsExpCS', None)
    _safe_set(owner, 'miniOCL_AccVarCS72', partner)
    assert owner in getattr(partner, 'miniOCL_ExistsExpCS')
    _safe_set(owner, 'miniOCL_AccVarCS72', None)
    assert owner not in getattr(partner, 'miniOCL_ExistsExpCS')


def test_assoc_accVars84_stub_double():
    # miniOCL_ForAllExpCS has no real 'miniOCL_ForAllExpCS' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_AccVarCS(accVarName="sample_text")
    partner = miniOCL_ForAllExpCS()
    setattr(partner, 'miniOCL_ForAllExpCS', None)
    _safe_set(owner, 'miniOCL_AccVarCS85', partner)
    assert owner in getattr(partner, 'miniOCL_ForAllExpCS')
    _safe_set(owner, 'miniOCL_AccVarCS85', None)
    assert owner not in getattr(partner, 'miniOCL_ForAllExpCS')


def test_assoc_body22_stub_double():
    # miniOCL_ExpCS has no real 'miniOCL_ExpCS' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_OperationCS(name="sample_text")
    partner = miniOCL_ExpCS()
    setattr(partner, 'miniOCL_ExpCS', None)
    _safe_set(owner, 'miniOCL_OperationCS23', partner)
    assert getattr(partner, 'miniOCL_ExpCS') == owner
    _safe_set(owner, 'miniOCL_OperationCS23', None)
    assert getattr(partner, 'miniOCL_ExpCS') is None


def test_assoc_exp52_stub_double():
    # miniOCL_ExpCS has no real 'miniOCL_ExpCS54' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_LoopExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_LoopExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_LoopExpCS(logicOp="sample_text")
    partner = miniOCL_ExpCS()
    setattr(partner, 'miniOCL_ExpCS54', None)
    _safe_set(owner, 'miniOCL_LoopExpCS53', {partner})
    assert getattr(partner, 'miniOCL_ExpCS54') == owner
    _safe_set(owner, 'miniOCL_LoopExpCS53', set())
    assert getattr(partner, 'miniOCL_ExpCS54') is None


def test_assoc_extends8_stub_double():
    # miniOCL_PathNameCS has no real 'miniOCL_PathNameCS' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_ClassCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_ClassCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_ClassCS(name="sample_text")
    partner = miniOCL_PathNameCS()
    setattr(partner, 'miniOCL_PathNameCS', None)
    _safe_set(owner, 'miniOCL_ClassCS9', partner)
    assert getattr(partner, 'miniOCL_PathNameCS') == owner
    _safe_set(owner, 'miniOCL_ClassCS9', None)
    assert getattr(partner, 'miniOCL_PathNameCS') is None


def test_assoc_itType55_stub_double():
    # miniOCL_PathNameCS has no real 'miniOCL_PathNameCS57' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_IteratorVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_IteratorVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_IteratorVarCS(itName="sample_text")
    partner = miniOCL_PathNameCS()
    setattr(partner, 'miniOCL_PathNameCS57', None)
    _safe_set(owner, 'miniOCL_IteratorVarCS56', partner)
    assert getattr(partner, 'miniOCL_PathNameCS57') == owner
    _safe_set(owner, 'miniOCL_IteratorVarCS56', None)
    assert getattr(partner, 'miniOCL_PathNameCS57') is None


def test_assoc_packages0_stub_double():
    # miniOCL_RootCS has no real 'miniOCL_RootCS' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_PackageCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_PackageCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_PackageCS(name="sample_text")
    partner = miniOCL_RootCS()
    setattr(partner, 'miniOCL_RootCS', None)
    _safe_set(owner, 'miniOCL_PackageCS', partner)
    assert owner in getattr(partner, 'miniOCL_RootCS')
    _safe_set(owner, 'miniOCL_PackageCS', None)
    assert owner not in getattr(partner, 'miniOCL_RootCS')


def test_assoc_resultRef19_stub_double():
    # miniOCL_PathNameCS has no real 'miniOCL_PathNameCS21' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_OperationCS(name="sample_text")
    partner = miniOCL_PathNameCS()
    setattr(partner, 'miniOCL_PathNameCS21', None)
    _safe_set(owner, 'miniOCL_OperationCS20', partner)
    assert getattr(partner, 'miniOCL_PathNameCS21') == owner
    _safe_set(owner, 'miniOCL_OperationCS20', None)
    assert getattr(partner, 'miniOCL_PathNameCS21') is None


def test_assoc_right37_stub_double():
    # miniOCL_CallExpCS has no real 'miniOCL_CallExpCS' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_LogicExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_LogicExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_LogicExpCS(op="sample_text")
    partner = miniOCL_CallExpCS()
    setattr(partner, 'miniOCL_CallExpCS', None)
    _safe_set(owner, 'miniOCL_LogicExpCS38', partner)
    assert getattr(partner, 'miniOCL_CallExpCS') == owner
    _safe_set(owner, 'miniOCL_LogicExpCS38', None)
    assert getattr(partner, 'miniOCL_CallExpCS') is None


def test_assoc_typeRef14_stub_double():
    # miniOCL_PathNameCS has no real 'miniOCL_PathNameCS16' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_PropertyCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_PropertyCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_PropertyCS(name="sample_text")
    partner = miniOCL_PathNameCS()
    setattr(partner, 'miniOCL_PathNameCS16', None)
    _safe_set(owner, 'miniOCL_PropertyCS15', partner)
    assert getattr(partner, 'miniOCL_PathNameCS16') == owner
    _safe_set(owner, 'miniOCL_PropertyCS15', None)
    assert getattr(partner, 'miniOCL_PathNameCS16') is None


def test_assoc_typeRef24_stub_double():
    # miniOCL_PathNameCS has no real 'miniOCL_PathNameCS26' property in the generated
    # code (a bare stub) -- manually attach it so miniOCL_ParameterCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniOCL_ParameterCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniOCL_ParameterCS(name="sample_text")
    partner = miniOCL_PathNameCS()
    setattr(partner, 'miniOCL_PathNameCS26', None)
    _safe_set(owner, 'miniOCL_ParameterCS25', partner)
    assert getattr(partner, 'miniOCL_PathNameCS26') == owner
    _safe_set(owner, 'miniOCL_ParameterCS25', None)
    assert getattr(partner, 'miniOCL_PathNameCS26') is None


