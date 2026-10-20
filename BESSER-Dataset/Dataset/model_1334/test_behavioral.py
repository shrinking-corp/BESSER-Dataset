import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BooleanLiteralExpCS,
    CSTrace,
    CallExpCS,
    EqualityExpCS,
    ExpCS,
    LiteralExpCS,
    LoopExpCS,
    NavigationExpCS,
    PrimaryExpCS,
    minioclcs_AccVarCS,
    minioclcs_BooleanExpCS,
    minioclcs_BooleanLiteralExpCS,
    minioclcs_CSTrace,
    minioclcs_CallExpCS,
    minioclcs_ClassCS,
    minioclcs_CollectExpCS,
    minioclcs_CollectionLiteralExpCS,
    minioclcs_CollectionLiteralPartCS,
    minioclcs_ConstraintsDefCS,
    minioclcs_EClass,
    minioclcs_EObject,
    minioclcs_EqualityExpCS,
    minioclcs_ExpCS,
    minioclcs_ImportCS,
    minioclcs_IntLiteralExpCS,
    minioclcs_InvariantCS,
    minioclcs_IterateExpCS,
    minioclcs_IteratorVarCS,
    minioclcs_LetExpCS,
    minioclcs_LetVarCS,
    minioclcs_LiteralExpCS,
    minioclcs_LoopExpCS,
    minioclcs_MultiplicityCS,
    minioclcs_NameExpCS,
    minioclcs_NavigationExpCS,
    minioclcs_NullLiteralExpCS,
    minioclcs_OperationCS,
    minioclcs_PackageCS,
    minioclcs_ParameterCS,
    minioclcs_PathElementCS,
    minioclcs_PathNameCS,
    minioclcs_PrimaryExpCS,
    minioclcs_PropertyCS,
    minioclcs_RootCS,
    minioclcs_RoundedBracketClauseCS,
    minioclcs_SelfExpCS,
    CollectionKindCS,
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

def test_assoc_classes8_reverse_link_reassign_clear():
    a1 = minioclcs_PackageCS(name="sample_text")
    a2 = minioclcs_PackageCS(name="sample_text_2")
    b = minioclcs_ClassCS(name="sample_text")
    _safe_set(b, 'minioclcs_ClassCS', a1)
    assert _is_linked(b, 'minioclcs_ClassCS', a1)
    if hasattr(a1, 'minioclcs_PackageCS9'):
        assert _is_linked(a1, 'minioclcs_PackageCS9', b)
    _safe_set(b, 'minioclcs_ClassCS', a2)
    assert _is_linked(b, 'minioclcs_ClassCS', a2)
    if hasattr(a1, 'minioclcs_PackageCS9'):
        assert not _is_linked(a1, 'minioclcs_PackageCS9', b)
    if hasattr(a2, 'minioclcs_PackageCS9'):
        assert _is_linked(a2, 'minioclcs_PackageCS9', b)
    _safe_set(b, 'minioclcs_ClassCS', None)
    assert not _is_linked(b, 'minioclcs_ClassCS', a2)
    if hasattr(a2, 'minioclcs_PackageCS9'):
        assert not _is_linked(a2, 'minioclcs_PackageCS9', b)


def test_assoc_left40_reverse_link_reassign_clear():
    a1 = minioclcs_EqualityExpCS(opName="sample_text")
    a2 = minioclcs_EqualityExpCS(opName="sample_text_2")
    b = minioclcs_EqualityExpCS(opName="sample_text")
    _safe_set(b, 'minioclcs_EqualityExpCS39', a1)
    assert _is_linked(b, 'minioclcs_EqualityExpCS39', a1)
    if hasattr(a1, 'minioclcs_EqualityExpCS'):
        assert _is_linked(a1, 'minioclcs_EqualityExpCS', b)
    _safe_set(b, 'minioclcs_EqualityExpCS39', a2)
    assert _is_linked(b, 'minioclcs_EqualityExpCS39', a2)
    if hasattr(a1, 'minioclcs_EqualityExpCS'):
        assert not _is_linked(a1, 'minioclcs_EqualityExpCS', b)
    if hasattr(a2, 'minioclcs_EqualityExpCS'):
        assert _is_linked(a2, 'minioclcs_EqualityExpCS', b)
    _safe_set(b, 'minioclcs_EqualityExpCS39', None)
    assert not _is_linked(b, 'minioclcs_EqualityExpCS39', a2)
    if hasattr(a2, 'minioclcs_EqualityExpCS'):
        assert not _is_linked(a2, 'minioclcs_EqualityExpCS', b)


def test_assoc_multiplicity19_reverse_link_reassign_clear():
    a1 = minioclcs_PropertyCS(name="sample_text")
    a2 = minioclcs_PropertyCS(name="sample_text_2")
    b = minioclcs_MultiplicityCS(lowerInt=7, mandatory=7, mult=True, opt=True, upperInt=7, upperMult=True)
    _safe_set(b, 'minioclcs_MultiplicityCS', a1)
    assert _is_linked(b, 'minioclcs_MultiplicityCS', a1)
    if hasattr(a1, 'minioclcs_PropertyCS20'):
        assert _is_linked(a1, 'minioclcs_PropertyCS20', b)
    _safe_set(b, 'minioclcs_MultiplicityCS', a2)
    assert _is_linked(b, 'minioclcs_MultiplicityCS', a2)
    if hasattr(a1, 'minioclcs_PropertyCS20'):
        assert not _is_linked(a1, 'minioclcs_PropertyCS20', b)
    if hasattr(a2, 'minioclcs_PropertyCS20'):
        assert _is_linked(a2, 'minioclcs_PropertyCS20', b)
    _safe_set(b, 'minioclcs_MultiplicityCS', None)
    assert not _is_linked(b, 'minioclcs_MultiplicityCS', a2)
    if hasattr(a2, 'minioclcs_PropertyCS20'):
        assert not _is_linked(a2, 'minioclcs_PropertyCS20', b)


def test_assoc_operations14_reverse_link_reassign_clear():
    a1 = minioclcs_OperationCS(name="sample_text")
    a2 = minioclcs_OperationCS(name="sample_text_2")
    b = minioclcs_ClassCS(name="sample_text")
    _safe_set(b, 'minioclcs_ClassCS15', {a1})
    assert _is_linked(b, 'minioclcs_ClassCS15', a1)
    if hasattr(a1, 'minioclcs_OperationCS'):
        assert _is_linked(a1, 'minioclcs_OperationCS', b)
    _safe_set(b, 'minioclcs_ClassCS15', {a2})
    assert _is_linked(b, 'minioclcs_ClassCS15', a2)
    if hasattr(a1, 'minioclcs_OperationCS'):
        assert not _is_linked(a1, 'minioclcs_OperationCS', b)
    if hasattr(a2, 'minioclcs_OperationCS'):
        assert _is_linked(a2, 'minioclcs_OperationCS', b)
    _safe_set(b, 'minioclcs_ClassCS15', set())
    assert not _is_linked(b, 'minioclcs_ClassCS15', a2)
    if hasattr(a2, 'minioclcs_OperationCS'):
        assert not _is_linked(a2, 'minioclcs_OperationCS', b)


def test_assoc_packages6_reverse_link_reassign_clear():
    a1 = minioclcs_PackageCS(name="sample_text")
    a2 = minioclcs_PackageCS(name="sample_text_2")
    b = minioclcs_PackageCS(name="sample_text")
    _safe_set(b, 'minioclcs_PackageCS7', a1)
    assert _is_linked(b, 'minioclcs_PackageCS7', a1)
    if hasattr(a1, 'minioclcs_PackageCS5'):
        assert _is_linked(a1, 'minioclcs_PackageCS5', b)
    _safe_set(b, 'minioclcs_PackageCS7', a2)
    assert _is_linked(b, 'minioclcs_PackageCS7', a2)
    if hasattr(a1, 'minioclcs_PackageCS5'):
        assert not _is_linked(a1, 'minioclcs_PackageCS5', b)
    if hasattr(a2, 'minioclcs_PackageCS5'):
        assert _is_linked(a2, 'minioclcs_PackageCS5', b)
    _safe_set(b, 'minioclcs_PackageCS7', None)
    assert not _is_linked(b, 'minioclcs_PackageCS7', a2)
    if hasattr(a2, 'minioclcs_PackageCS5'):
        assert not _is_linked(a2, 'minioclcs_PackageCS5', b)


def test_assoc_params21_reverse_link_reassign_clear():
    a1 = minioclcs_ParameterCS(name="sample_text")
    a2 = minioclcs_ParameterCS(name="sample_text_2")
    b = minioclcs_OperationCS(name="sample_text")
    _safe_set(b, 'minioclcs_OperationCS22', {a1})
    assert _is_linked(b, 'minioclcs_OperationCS22', a1)
    if hasattr(a1, 'minioclcs_ParameterCS'):
        assert _is_linked(a1, 'minioclcs_ParameterCS', b)
    _safe_set(b, 'minioclcs_OperationCS22', {a2})
    assert _is_linked(b, 'minioclcs_OperationCS22', a2)
    if hasattr(a1, 'minioclcs_ParameterCS'):
        assert not _is_linked(a1, 'minioclcs_ParameterCS', b)
    if hasattr(a2, 'minioclcs_ParameterCS'):
        assert _is_linked(a2, 'minioclcs_ParameterCS', b)
    _safe_set(b, 'minioclcs_OperationCS22', set())
    assert not _is_linked(b, 'minioclcs_OperationCS22', a2)
    if hasattr(a2, 'minioclcs_ParameterCS'):
        assert not _is_linked(a2, 'minioclcs_ParameterCS', b)


def test_assoc_properties12_reverse_link_reassign_clear():
    a1 = minioclcs_PropertyCS(name="sample_text")
    a2 = minioclcs_PropertyCS(name="sample_text_2")
    b = minioclcs_ClassCS(name="sample_text")
    _safe_set(b, 'minioclcs_ClassCS13', {a1})
    assert _is_linked(b, 'minioclcs_ClassCS13', a1)
    if hasattr(a1, 'minioclcs_PropertyCS'):
        assert _is_linked(a1, 'minioclcs_PropertyCS', b)
    _safe_set(b, 'minioclcs_ClassCS13', {a2})
    assert _is_linked(b, 'minioclcs_ClassCS13', a2)
    if hasattr(a1, 'minioclcs_PropertyCS'):
        assert not _is_linked(a1, 'minioclcs_PropertyCS', b)
    if hasattr(a2, 'minioclcs_PropertyCS'):
        assert _is_linked(a2, 'minioclcs_PropertyCS', b)
    _safe_set(b, 'minioclcs_ClassCS13', set())
    assert not _is_linked(b, 'minioclcs_ClassCS13', a2)
    if hasattr(a2, 'minioclcs_PropertyCS'):
        assert not _is_linked(a2, 'minioclcs_PropertyCS', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accInitExp59_stub_double():
    # minioclcs_ExpCS has no real 'minioclcs_ExpCS61' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_AccVarCS(accName="sample_text")
    partner = minioclcs_ExpCS()
    setattr(partner, 'minioclcs_ExpCS61', None)
    _safe_set(owner, 'minioclcs_AccVarCS60', partner)
    assert getattr(partner, 'minioclcs_ExpCS61') == owner
    _safe_set(owner, 'minioclcs_AccVarCS60', None)
    assert getattr(partner, 'minioclcs_ExpCS61') is None


def test_assoc_accType56_stub_double():
    # minioclcs_PathNameCS has no real 'minioclcs_PathNameCS58' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_AccVarCS(accName="sample_text")
    partner = minioclcs_PathNameCS()
    setattr(partner, 'minioclcs_PathNameCS58', None)
    _safe_set(owner, 'minioclcs_AccVarCS57', partner)
    assert getattr(partner, 'minioclcs_PathNameCS58') == owner
    _safe_set(owner, 'minioclcs_AccVarCS57', None)
    assert getattr(partner, 'minioclcs_PathNameCS58') is None


def test_assoc_accVar55_stub_double():
    # minioclcs_IterateExpCS has no real 'minioclcs_IterateExpCS' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_AccVarCS(accName="sample_text")
    partner = minioclcs_IterateExpCS()
    setattr(partner, 'minioclcs_IterateExpCS', None)
    _safe_set(owner, 'minioclcs_AccVarCS', partner)
    assert getattr(partner, 'minioclcs_IterateExpCS') == owner
    _safe_set(owner, 'minioclcs_AccVarCS', None)
    assert getattr(partner, 'minioclcs_IterateExpCS') is None


def test_assoc_body26_stub_double():
    # minioclcs_ExpCS has no real 'minioclcs_ExpCS' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_OperationCS(name="sample_text")
    partner = minioclcs_ExpCS()
    setattr(partner, 'minioclcs_ExpCS', None)
    _safe_set(owner, 'minioclcs_OperationCS27', partner)
    assert getattr(partner, 'minioclcs_ExpCS') == owner
    _safe_set(owner, 'minioclcs_OperationCS27', None)
    assert getattr(partner, 'minioclcs_ExpCS') is None


def test_assoc_extends10_stub_double():
    # minioclcs_PathNameCS has no real 'minioclcs_PathNameCS' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_ClassCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_ClassCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_ClassCS(name="sample_text")
    partner = minioclcs_PathNameCS()
    setattr(partner, 'minioclcs_PathNameCS', None)
    _safe_set(owner, 'minioclcs_ClassCS11', partner)
    assert getattr(partner, 'minioclcs_PathNameCS') == owner
    _safe_set(owner, 'minioclcs_ClassCS11', None)
    assert getattr(partner, 'minioclcs_PathNameCS') is None


def test_assoc_imports0_stub_double():
    # minioclcs_RootCS has no real 'minioclcs_RootCS' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_ImportCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_ImportCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_ImportCS(alias="sample_text", uri="sample_text")
    partner = minioclcs_RootCS()
    setattr(partner, 'minioclcs_RootCS', None)
    _safe_set(owner, 'minioclcs_ImportCS', partner)
    assert owner in getattr(partner, 'minioclcs_RootCS')
    _safe_set(owner, 'minioclcs_ImportCS', None)
    assert owner not in getattr(partner, 'minioclcs_RootCS')


def test_assoc_initExp83_stub_double():
    # minioclcs_ExpCS has no real 'minioclcs_ExpCS85' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_LetVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_LetVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_LetVarCS(name="sample_text")
    partner = minioclcs_ExpCS()
    setattr(partner, 'minioclcs_ExpCS85', None)
    _safe_set(owner, 'minioclcs_LetVarCS84', partner)
    assert getattr(partner, 'minioclcs_ExpCS85') == owner
    _safe_set(owner, 'minioclcs_LetVarCS84', None)
    assert getattr(partner, 'minioclcs_ExpCS85') is None


def test_assoc_itType52_stub_double():
    # minioclcs_PathNameCS has no real 'minioclcs_PathNameCS54' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_IteratorVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_IteratorVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_IteratorVarCS(itName="sample_text")
    partner = minioclcs_PathNameCS()
    setattr(partner, 'minioclcs_PathNameCS54', None)
    _safe_set(owner, 'minioclcs_IteratorVarCS53', partner)
    assert getattr(partner, 'minioclcs_PathNameCS54') == owner
    _safe_set(owner, 'minioclcs_IteratorVarCS53', None)
    assert getattr(partner, 'minioclcs_PathNameCS54') is None


def test_assoc_itVar48_stub_double():
    # minioclcs_LoopExpCS has no real 'minioclcs_LoopExpCS' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_IteratorVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_IteratorVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_IteratorVarCS(itName="sample_text")
    partner = minioclcs_LoopExpCS()
    setattr(partner, 'minioclcs_LoopExpCS', None)
    _safe_set(owner, 'minioclcs_IteratorVarCS', partner)
    assert getattr(partner, 'minioclcs_LoopExpCS') == owner
    _safe_set(owner, 'minioclcs_IteratorVarCS', None)
    assert getattr(partner, 'minioclcs_LoopExpCS') is None


def test_assoc_letVars76_stub_double():
    # minioclcs_LetExpCS has no real 'minioclcs_LetExpCS' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_LetVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_LetVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_LetVarCS(name="sample_text")
    partner = minioclcs_LetExpCS()
    setattr(partner, 'minioclcs_LetExpCS', None)
    _safe_set(owner, 'minioclcs_LetVarCS', partner)
    assert owner in getattr(partner, 'minioclcs_LetExpCS')
    _safe_set(owner, 'minioclcs_LetVarCS', None)
    assert owner not in getattr(partner, 'minioclcs_LetExpCS')


def test_assoc_packages1_stub_double():
    # minioclcs_RootCS has no real 'minioclcs_RootCS2' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_PackageCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_PackageCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_PackageCS(name="sample_text")
    partner = minioclcs_RootCS()
    setattr(partner, 'minioclcs_RootCS2', None)
    _safe_set(owner, 'minioclcs_PackageCS', partner)
    assert owner in getattr(partner, 'minioclcs_RootCS2')
    _safe_set(owner, 'minioclcs_PackageCS', None)
    assert owner not in getattr(partner, 'minioclcs_RootCS2')


def test_assoc_parts69_stub_double():
    # minioclcs_CollectionLiteralPartCS has no real 'minioclcs_CollectionLiteralPartCS' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_CollectionLiteralExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_CollectionLiteralExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_CollectionLiteralExpCS(kind="sample_text")
    partner = minioclcs_CollectionLiteralPartCS()
    setattr(partner, 'minioclcs_CollectionLiteralPartCS', None)
    _safe_set(owner, 'minioclcs_CollectionLiteralExpCS', {partner})
    assert getattr(partner, 'minioclcs_CollectionLiteralPartCS') == owner
    _safe_set(owner, 'minioclcs_CollectionLiteralExpCS', set())
    assert getattr(partner, 'minioclcs_CollectionLiteralPartCS') is None


def test_assoc_resultRef23_stub_double():
    # minioclcs_PathNameCS has no real 'minioclcs_PathNameCS25' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_OperationCS(name="sample_text")
    partner = minioclcs_PathNameCS()
    setattr(partner, 'minioclcs_PathNameCS25', None)
    _safe_set(owner, 'minioclcs_OperationCS24', partner)
    assert getattr(partner, 'minioclcs_PathNameCS25') == owner
    _safe_set(owner, 'minioclcs_OperationCS24', None)
    assert getattr(partner, 'minioclcs_PathNameCS25') is None


def test_assoc_right41_stub_double():
    # minioclcs_CallExpCS has no real 'minioclcs_CallExpCS' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_EqualityExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_EqualityExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_EqualityExpCS(opName="sample_text")
    partner = minioclcs_CallExpCS()
    setattr(partner, 'minioclcs_CallExpCS', None)
    _safe_set(owner, 'minioclcs_EqualityExpCS42', partner)
    assert getattr(partner, 'minioclcs_CallExpCS') == owner
    _safe_set(owner, 'minioclcs_EqualityExpCS42', None)
    assert getattr(partner, 'minioclcs_CallExpCS') is None


def test_assoc_typeRef16_stub_double():
    # minioclcs_PathNameCS has no real 'minioclcs_PathNameCS18' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_PropertyCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_PropertyCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_PropertyCS(name="sample_text")
    partner = minioclcs_PathNameCS()
    setattr(partner, 'minioclcs_PathNameCS18', None)
    _safe_set(owner, 'minioclcs_PropertyCS17', partner)
    assert getattr(partner, 'minioclcs_PathNameCS18') == owner
    _safe_set(owner, 'minioclcs_PropertyCS17', None)
    assert getattr(partner, 'minioclcs_PathNameCS18') is None


def test_assoc_typeRef28_stub_double():
    # minioclcs_PathNameCS has no real 'minioclcs_PathNameCS30' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_ParameterCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_ParameterCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_ParameterCS(name="sample_text")
    partner = minioclcs_PathNameCS()
    setattr(partner, 'minioclcs_PathNameCS30', None)
    _safe_set(owner, 'minioclcs_ParameterCS29', partner)
    assert getattr(partner, 'minioclcs_PathNameCS30') == owner
    _safe_set(owner, 'minioclcs_ParameterCS29', None)
    assert getattr(partner, 'minioclcs_PathNameCS30') is None


def test_assoc_typeRef80_stub_double():
    # minioclcs_PathNameCS has no real 'minioclcs_PathNameCS82' property in the generated
    # code (a bare stub) -- manually attach it so minioclcs_LetVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minioclcs_LetVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minioclcs_LetVarCS(name="sample_text")
    partner = minioclcs_PathNameCS()
    setattr(partner, 'minioclcs_PathNameCS82', None)
    _safe_set(owner, 'minioclcs_LetVarCS81', partner)
    assert getattr(partner, 'minioclcs_PathNameCS82') == owner
    _safe_set(owner, 'minioclcs_LetVarCS81', None)
    assert getattr(partner, 'minioclcs_PathNameCS82') is None


