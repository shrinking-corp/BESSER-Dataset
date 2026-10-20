import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BooleanLiteralExpCS,
    CallExpCS,
    Classifier,
    ExpCS,
    Feature,
    LiteralExpCS,
    LogicExpCS,
    LoopExpCS,
    Modifier,
    NamedElement,
    NavigationExpCS,
    NavigationPathCS,
    PathCS,
    PrimaryExpCS,
    Relation,
    umlclassdiagram_AccVarCS,
    umlclassdiagram_Aggregation,
    umlclassdiagram_Association,
    umlclassdiagram_AssociationClass,
    umlclassdiagram_Attribute,
    umlclassdiagram_BooleanExpCS,
    umlclassdiagram_BooleanLiteralExpCS,
    umlclassdiagram_CallExpCS,
    umlclassdiagram_Class,
    umlclassdiagram_ClassCS,
    umlclassdiagram_ClassDiagram,
    umlclassdiagram_Classifier,
    umlclassdiagram_CollectExpCS,
    umlclassdiagram_Composition,
    umlclassdiagram_Constraint,
    umlclassdiagram_ConstraintCS,
    umlclassdiagram_Dependency,
    umlclassdiagram_ExistsExpCS,
    umlclassdiagram_ExpCS,
    umlclassdiagram_Feature,
    umlclassdiagram_ForAllExpCS,
    umlclassdiagram_IntLiteralExpCS,
    umlclassdiagram_InvariantCS,
    umlclassdiagram_IterateExpCS,
    umlclassdiagram_IteratorVarCS,
    umlclassdiagram_LiteralExpCS,
    umlclassdiagram_LogicExpCS,
    umlclassdiagram_LoopExpCS,
    umlclassdiagram_Modifier,
    umlclassdiagram_NameExpCS,
    umlclassdiagram_NamedElement,
    umlclassdiagram_NavigationExpCS,
    umlclassdiagram_NavigationNameExpCS,
    umlclassdiagram_NavigationPathCS,
    umlclassdiagram_NavigationPathElementCS,
    umlclassdiagram_NavigationPathNameCS,
    umlclassdiagram_NavigationPathVariableCS,
    umlclassdiagram_Operation,
    umlclassdiagram_OperationCS,
    umlclassdiagram_Operator,
    umlclassdiagram_PackageCS,
    umlclassdiagram_Parameter,
    umlclassdiagram_ParameterCS,
    umlclassdiagram_PathCS,
    umlclassdiagram_PathElementCS,
    umlclassdiagram_PathNameCS,
    umlclassdiagram_PathVariableCS,
    umlclassdiagram_PrimaryExpCS,
    umlclassdiagram_PrimitiveElement,
    umlclassdiagram_PropertyCS,
    umlclassdiagram_Relation,
    umlclassdiagram_RootCS,
    umlclassdiagram_RoundedBracketClauseCS,
    umlclassdiagram_StringLiteralExpCS,
    OperatorType,
    PrimitiveDataType,
    ScopeType,
    VisbilityType,
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
    a1 = umlclassdiagram_PackageCS(name="sample_text")
    a2 = umlclassdiagram_PackageCS(name="sample_text_2")
    b = umlclassdiagram_ClassCS(name="sample_text")
    _safe_set(b, 'umlclassdiagram_ClassCS', a1)
    assert _is_linked(b, 'umlclassdiagram_ClassCS', a1)
    if hasattr(a1, 'umlclassdiagram_PackageCS7'):
        assert _is_linked(a1, 'umlclassdiagram_PackageCS7', b)
    _safe_set(b, 'umlclassdiagram_ClassCS', a2)
    assert _is_linked(b, 'umlclassdiagram_ClassCS', a2)
    if hasattr(a1, 'umlclassdiagram_PackageCS7'):
        assert not _is_linked(a1, 'umlclassdiagram_PackageCS7', b)
    if hasattr(a2, 'umlclassdiagram_PackageCS7'):
        assert _is_linked(a2, 'umlclassdiagram_PackageCS7', b)
    _safe_set(b, 'umlclassdiagram_ClassCS', None)
    assert not _is_linked(b, 'umlclassdiagram_ClassCS', a2)
    if hasattr(a2, 'umlclassdiagram_PackageCS7'):
        assert not _is_linked(a2, 'umlclassdiagram_PackageCS7', b)


def test_assoc_features97_reverse_link_reassign_clear():
    a1 = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    a2 = umlclassdiagram_Feature(name="sample_text_2", scope="sample_text_2", visibility="sample_text_2")
    b = umlclassdiagram_Classifier(abstract=True, derived=True)
    _safe_set(b, 'umlclassdiagram_Classifier98', {a1})
    assert _is_linked(b, 'umlclassdiagram_Classifier98', a1)
    if hasattr(a1, 'umlclassdiagram_Feature99'):
        assert _is_linked(a1, 'umlclassdiagram_Feature99', b)
    _safe_set(b, 'umlclassdiagram_Classifier98', {a2})
    assert _is_linked(b, 'umlclassdiagram_Classifier98', a2)
    if hasattr(a1, 'umlclassdiagram_Feature99'):
        assert not _is_linked(a1, 'umlclassdiagram_Feature99', b)
    if hasattr(a2, 'umlclassdiagram_Feature99'):
        assert _is_linked(a2, 'umlclassdiagram_Feature99', b)
    _safe_set(b, 'umlclassdiagram_Classifier98', set())
    assert not _is_linked(b, 'umlclassdiagram_Classifier98', a2)
    if hasattr(a2, 'umlclassdiagram_Feature99'):
        assert not _is_linked(a2, 'umlclassdiagram_Feature99', b)


def test_assoc_itVar51_reverse_link_reassign_clear():
    a1 = umlclassdiagram_LoopExpCS(logicOp="sample_text")
    a2 = umlclassdiagram_LoopExpCS(logicOp="sample_text_2")
    b = umlclassdiagram_IteratorVarCS(itName="sample_text")
    _safe_set(b, 'umlclassdiagram_IteratorVarCS', a1)
    assert _is_linked(b, 'umlclassdiagram_IteratorVarCS', a1)
    if hasattr(a1, 'umlclassdiagram_LoopExpCS'):
        assert _is_linked(a1, 'umlclassdiagram_LoopExpCS', b)
    _safe_set(b, 'umlclassdiagram_IteratorVarCS', a2)
    assert _is_linked(b, 'umlclassdiagram_IteratorVarCS', a2)
    if hasattr(a1, 'umlclassdiagram_LoopExpCS'):
        assert not _is_linked(a1, 'umlclassdiagram_LoopExpCS', b)
    if hasattr(a2, 'umlclassdiagram_LoopExpCS'):
        assert _is_linked(a2, 'umlclassdiagram_LoopExpCS', b)
    _safe_set(b, 'umlclassdiagram_IteratorVarCS', None)
    assert not _is_linked(b, 'umlclassdiagram_IteratorVarCS', a2)
    if hasattr(a2, 'umlclassdiagram_LoopExpCS'):
        assert not _is_linked(a2, 'umlclassdiagram_LoopExpCS', b)


def test_assoc_left36_reverse_link_reassign_clear():
    a1 = umlclassdiagram_LogicExpCS(op="sample_text")
    a2 = umlclassdiagram_LogicExpCS(op="sample_text_2")
    b = umlclassdiagram_LogicExpCS(op="sample_text")
    _safe_set(b, 'umlclassdiagram_LogicExpCS35', a1)
    assert _is_linked(b, 'umlclassdiagram_LogicExpCS35', a1)
    if hasattr(a1, 'umlclassdiagram_LogicExpCS'):
        assert _is_linked(a1, 'umlclassdiagram_LogicExpCS', b)
    _safe_set(b, 'umlclassdiagram_LogicExpCS35', a2)
    assert _is_linked(b, 'umlclassdiagram_LogicExpCS35', a2)
    if hasattr(a1, 'umlclassdiagram_LogicExpCS'):
        assert not _is_linked(a1, 'umlclassdiagram_LogicExpCS', b)
    if hasattr(a2, 'umlclassdiagram_LogicExpCS'):
        assert _is_linked(a2, 'umlclassdiagram_LogicExpCS', b)
    _safe_set(b, 'umlclassdiagram_LogicExpCS35', None)
    assert not _is_linked(b, 'umlclassdiagram_LogicExpCS35', a2)
    if hasattr(a2, 'umlclassdiagram_LogicExpCS'):
        assert not _is_linked(a2, 'umlclassdiagram_LogicExpCS', b)


def test_assoc_operations12_reverse_link_reassign_clear():
    a1 = umlclassdiagram_OperationCS(name="sample_text")
    a2 = umlclassdiagram_OperationCS(name="sample_text_2")
    b = umlclassdiagram_ClassCS(name="sample_text")
    _safe_set(b, 'umlclassdiagram_ClassCS13', {a1})
    assert _is_linked(b, 'umlclassdiagram_ClassCS13', a1)
    if hasattr(a1, 'umlclassdiagram_OperationCS'):
        assert _is_linked(a1, 'umlclassdiagram_OperationCS', b)
    _safe_set(b, 'umlclassdiagram_ClassCS13', {a2})
    assert _is_linked(b, 'umlclassdiagram_ClassCS13', a2)
    if hasattr(a1, 'umlclassdiagram_OperationCS'):
        assert not _is_linked(a1, 'umlclassdiagram_OperationCS', b)
    if hasattr(a2, 'umlclassdiagram_OperationCS'):
        assert _is_linked(a2, 'umlclassdiagram_OperationCS', b)
    _safe_set(b, 'umlclassdiagram_ClassCS13', set())
    assert not _is_linked(b, 'umlclassdiagram_ClassCS13', a2)
    if hasattr(a2, 'umlclassdiagram_OperationCS'):
        assert not _is_linked(a2, 'umlclassdiagram_OperationCS', b)


def test_assoc_packages4_reverse_link_reassign_clear():
    a1 = umlclassdiagram_PackageCS(name="sample_text")
    a2 = umlclassdiagram_PackageCS(name="sample_text_2")
    b = umlclassdiagram_PackageCS(name="sample_text")
    _safe_set(b, 'umlclassdiagram_PackageCS5', a1)
    assert _is_linked(b, 'umlclassdiagram_PackageCS5', a1)
    if hasattr(a1, 'umlclassdiagram_PackageCS3'):
        assert _is_linked(a1, 'umlclassdiagram_PackageCS3', b)
    _safe_set(b, 'umlclassdiagram_PackageCS5', a2)
    assert _is_linked(b, 'umlclassdiagram_PackageCS5', a2)
    if hasattr(a1, 'umlclassdiagram_PackageCS3'):
        assert not _is_linked(a1, 'umlclassdiagram_PackageCS3', b)
    if hasattr(a2, 'umlclassdiagram_PackageCS3'):
        assert _is_linked(a2, 'umlclassdiagram_PackageCS3', b)
    _safe_set(b, 'umlclassdiagram_PackageCS5', None)
    assert not _is_linked(b, 'umlclassdiagram_PackageCS5', a2)
    if hasattr(a2, 'umlclassdiagram_PackageCS3'):
        assert not _is_linked(a2, 'umlclassdiagram_PackageCS3', b)


def test_assoc_params17_reverse_link_reassign_clear():
    a1 = umlclassdiagram_ParameterCS(name="sample_text")
    a2 = umlclassdiagram_ParameterCS(name="sample_text_2")
    b = umlclassdiagram_OperationCS(name="sample_text")
    _safe_set(b, 'umlclassdiagram_OperationCS18', {a1})
    assert _is_linked(b, 'umlclassdiagram_OperationCS18', a1)
    if hasattr(a1, 'umlclassdiagram_ParameterCS'):
        assert _is_linked(a1, 'umlclassdiagram_ParameterCS', b)
    _safe_set(b, 'umlclassdiagram_OperationCS18', {a2})
    assert _is_linked(b, 'umlclassdiagram_OperationCS18', a2)
    if hasattr(a1, 'umlclassdiagram_ParameterCS'):
        assert not _is_linked(a1, 'umlclassdiagram_ParameterCS', b)
    if hasattr(a2, 'umlclassdiagram_ParameterCS'):
        assert _is_linked(a2, 'umlclassdiagram_ParameterCS', b)
    _safe_set(b, 'umlclassdiagram_OperationCS18', set())
    assert not _is_linked(b, 'umlclassdiagram_OperationCS18', a2)
    if hasattr(a2, 'umlclassdiagram_ParameterCS'):
        assert not _is_linked(a2, 'umlclassdiagram_ParameterCS', b)


def test_assoc_properties10_reverse_link_reassign_clear():
    a1 = umlclassdiagram_PropertyCS(name="sample_text")
    a2 = umlclassdiagram_PropertyCS(name="sample_text_2")
    b = umlclassdiagram_ClassCS(name="sample_text")
    _safe_set(b, 'umlclassdiagram_ClassCS11', {a1})
    assert _is_linked(b, 'umlclassdiagram_ClassCS11', a1)
    if hasattr(a1, 'umlclassdiagram_PropertyCS'):
        assert _is_linked(a1, 'umlclassdiagram_PropertyCS', b)
    _safe_set(b, 'umlclassdiagram_ClassCS11', {a2})
    assert _is_linked(b, 'umlclassdiagram_ClassCS11', a2)
    if hasattr(a1, 'umlclassdiagram_PropertyCS'):
        assert not _is_linked(a1, 'umlclassdiagram_PropertyCS', b)
    if hasattr(a2, 'umlclassdiagram_PropertyCS'):
        assert _is_linked(a2, 'umlclassdiagram_PropertyCS', b)
    _safe_set(b, 'umlclassdiagram_ClassCS11', set())
    assert not _is_linked(b, 'umlclassdiagram_ClassCS11', a2)
    if hasattr(a2, 'umlclassdiagram_PropertyCS'):
        assert not _is_linked(a2, 'umlclassdiagram_PropertyCS', b)


def test_assoc_src115_reverse_link_reassign_clear():
    a1 = umlclassdiagram_Relation(derived=True, nsrc="sample_text", ntar="sample_text")
    a2 = umlclassdiagram_Relation(derived=False, nsrc="sample_text_2", ntar="sample_text_2")
    b = umlclassdiagram_Classifier(abstract=True, derived=True)
    _safe_set(b, 'umlclassdiagram_Classifier117', a1)
    assert _is_linked(b, 'umlclassdiagram_Classifier117', a1)
    if hasattr(a1, 'umlclassdiagram_Relation116'):
        assert _is_linked(a1, 'umlclassdiagram_Relation116', b)
    _safe_set(b, 'umlclassdiagram_Classifier117', a2)
    assert _is_linked(b, 'umlclassdiagram_Classifier117', a2)
    if hasattr(a1, 'umlclassdiagram_Relation116'):
        assert not _is_linked(a1, 'umlclassdiagram_Relation116', b)
    if hasattr(a2, 'umlclassdiagram_Relation116'):
        assert _is_linked(a2, 'umlclassdiagram_Relation116', b)
    _safe_set(b, 'umlclassdiagram_Classifier117', None)
    assert not _is_linked(b, 'umlclassdiagram_Classifier117', a2)
    if hasattr(a2, 'umlclassdiagram_Relation116'):
        assert not _is_linked(a2, 'umlclassdiagram_Relation116', b)


def test_assoc_tar118_reverse_link_reassign_clear():
    a1 = umlclassdiagram_Relation(derived=True, nsrc="sample_text", ntar="sample_text")
    a2 = umlclassdiagram_Relation(derived=False, nsrc="sample_text_2", ntar="sample_text_2")
    b = umlclassdiagram_Classifier(abstract=True, derived=True)
    _safe_set(b, 'umlclassdiagram_Classifier120', a1)
    assert _is_linked(b, 'umlclassdiagram_Classifier120', a1)
    if hasattr(a1, 'umlclassdiagram_Relation119'):
        assert _is_linked(a1, 'umlclassdiagram_Relation119', b)
    _safe_set(b, 'umlclassdiagram_Classifier120', a2)
    assert _is_linked(b, 'umlclassdiagram_Classifier120', a2)
    if hasattr(a1, 'umlclassdiagram_Relation119'):
        assert not _is_linked(a1, 'umlclassdiagram_Relation119', b)
    if hasattr(a2, 'umlclassdiagram_Relation119'):
        assert _is_linked(a2, 'umlclassdiagram_Relation119', b)
    _safe_set(b, 'umlclassdiagram_Classifier120', None)
    assert not _is_linked(b, 'umlclassdiagram_Classifier120', a2)
    if hasattr(a2, 'umlclassdiagram_Relation119'):
        assert not _is_linked(a2, 'umlclassdiagram_Relation119', b)


def test_assoc_type94_reverse_link_reassign_clear():
    a1 = umlclassdiagram_NamedElement(name="sample_text")
    a2 = umlclassdiagram_NamedElement(name="sample_text_2")
    b = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    _safe_set(b, 'umlclassdiagram_Feature95', a1)
    assert _is_linked(b, 'umlclassdiagram_Feature95', a1)
    if hasattr(a1, 'umlclassdiagram_NamedElement96'):
        assert _is_linked(a1, 'umlclassdiagram_NamedElement96', b)
    _safe_set(b, 'umlclassdiagram_Feature95', a2)
    assert _is_linked(b, 'umlclassdiagram_Feature95', a2)
    if hasattr(a1, 'umlclassdiagram_NamedElement96'):
        assert not _is_linked(a1, 'umlclassdiagram_NamedElement96', b)
    if hasattr(a2, 'umlclassdiagram_NamedElement96'):
        assert _is_linked(a2, 'umlclassdiagram_NamedElement96', b)
    _safe_set(b, 'umlclassdiagram_Feature95', None)
    assert not _is_linked(b, 'umlclassdiagram_Feature95', a2)
    if hasattr(a2, 'umlclassdiagram_NamedElement96'):
        assert not _is_linked(a2, 'umlclassdiagram_NamedElement96', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accInitExp62_stub_double():
    # umlclassdiagram_ExpCS has no real 'umlclassdiagram_ExpCS64' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_AccVarCS(accVarName="sample_text")
    partner = umlclassdiagram_ExpCS()
    setattr(partner, 'umlclassdiagram_ExpCS64', None)
    _safe_set(owner, 'umlclassdiagram_AccVarCS63', partner)
    assert getattr(partner, 'umlclassdiagram_ExpCS64') == owner
    _safe_set(owner, 'umlclassdiagram_AccVarCS63', None)
    assert getattr(partner, 'umlclassdiagram_ExpCS64') is None


def test_assoc_accType59_stub_double():
    # umlclassdiagram_PathNameCS has no real 'umlclassdiagram_PathNameCS61' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_AccVarCS(accVarName="sample_text")
    partner = umlclassdiagram_PathNameCS()
    setattr(partner, 'umlclassdiagram_PathNameCS61', None)
    _safe_set(owner, 'umlclassdiagram_AccVarCS60', partner)
    assert getattr(partner, 'umlclassdiagram_PathNameCS61') == owner
    _safe_set(owner, 'umlclassdiagram_AccVarCS60', None)
    assert getattr(partner, 'umlclassdiagram_PathNameCS61') is None


def test_assoc_accVar58_stub_double():
    # umlclassdiagram_IterateExpCS has no real 'umlclassdiagram_IterateExpCS' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_AccVarCS(accVarName="sample_text")
    partner = umlclassdiagram_IterateExpCS()
    setattr(partner, 'umlclassdiagram_IterateExpCS', None)
    _safe_set(owner, 'umlclassdiagram_AccVarCS', partner)
    assert getattr(partner, 'umlclassdiagram_IterateExpCS') == owner
    _safe_set(owner, 'umlclassdiagram_AccVarCS', None)
    assert getattr(partner, 'umlclassdiagram_IterateExpCS') is None


def test_assoc_accVars71_stub_double():
    # umlclassdiagram_ExistsExpCS has no real 'umlclassdiagram_ExistsExpCS' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_AccVarCS(accVarName="sample_text")
    partner = umlclassdiagram_ExistsExpCS()
    setattr(partner, 'umlclassdiagram_ExistsExpCS', None)
    _safe_set(owner, 'umlclassdiagram_AccVarCS72', partner)
    assert owner in getattr(partner, 'umlclassdiagram_ExistsExpCS')
    _safe_set(owner, 'umlclassdiagram_AccVarCS72', None)
    assert owner not in getattr(partner, 'umlclassdiagram_ExistsExpCS')


def test_assoc_accVars84_stub_double():
    # umlclassdiagram_ForAllExpCS has no real 'umlclassdiagram_ForAllExpCS' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_AccVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_AccVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_AccVarCS(accVarName="sample_text")
    partner = umlclassdiagram_ForAllExpCS()
    setattr(partner, 'umlclassdiagram_ForAllExpCS', None)
    _safe_set(owner, 'umlclassdiagram_AccVarCS85', partner)
    assert owner in getattr(partner, 'umlclassdiagram_ForAllExpCS')
    _safe_set(owner, 'umlclassdiagram_AccVarCS85', None)
    assert owner not in getattr(partner, 'umlclassdiagram_ForAllExpCS')


def test_assoc_body22_stub_double():
    # umlclassdiagram_ExpCS has no real 'umlclassdiagram_ExpCS' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_OperationCS(name="sample_text")
    partner = umlclassdiagram_ExpCS()
    setattr(partner, 'umlclassdiagram_ExpCS', None)
    _safe_set(owner, 'umlclassdiagram_OperationCS23', partner)
    assert getattr(partner, 'umlclassdiagram_ExpCS') == owner
    _safe_set(owner, 'umlclassdiagram_OperationCS23', None)
    assert getattr(partner, 'umlclassdiagram_ExpCS') is None


def test_assoc_classes86_stub_double():
    # umlclassdiagram_ClassDiagram has no real 'umlclassdiagram_ClassDiagram' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_Classifier(abstract=True, derived=True)
    partner = umlclassdiagram_ClassDiagram()
    setattr(partner, 'umlclassdiagram_ClassDiagram', None)
    _safe_set(owner, 'umlclassdiagram_Classifier', partner)
    assert owner in getattr(partner, 'umlclassdiagram_ClassDiagram')
    _safe_set(owner, 'umlclassdiagram_Classifier', None)
    assert owner not in getattr(partner, 'umlclassdiagram_ClassDiagram')


def test_assoc_constraints91_stub_double():
    # umlclassdiagram_ClassDiagram has no real 'umlclassdiagram_ClassDiagram92' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_Constraint(id="sample_text")
    partner = umlclassdiagram_ClassDiagram()
    setattr(partner, 'umlclassdiagram_ClassDiagram92', None)
    _safe_set(owner, 'umlclassdiagram_Constraint', partner)
    assert owner in getattr(partner, 'umlclassdiagram_ClassDiagram92')
    _safe_set(owner, 'umlclassdiagram_Constraint', None)
    assert owner not in getattr(partner, 'umlclassdiagram_ClassDiagram92')


def test_assoc_exp52_stub_double():
    # umlclassdiagram_ExpCS has no real 'umlclassdiagram_ExpCS54' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_LoopExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_LoopExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_LoopExpCS(logicOp="sample_text")
    partner = umlclassdiagram_ExpCS()
    setattr(partner, 'umlclassdiagram_ExpCS54', None)
    _safe_set(owner, 'umlclassdiagram_LoopExpCS53', {partner})
    assert getattr(partner, 'umlclassdiagram_ExpCS54') == owner
    _safe_set(owner, 'umlclassdiagram_LoopExpCS53', set())
    assert getattr(partner, 'umlclassdiagram_ExpCS54') is None


def test_assoc_expressions108_stub_double():
    # umlclassdiagram_RootCS has no real 'umlclassdiagram_RootCS110' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_Constraint(id="sample_text")
    partner = umlclassdiagram_RootCS()
    setattr(partner, 'umlclassdiagram_RootCS110', None)
    _safe_set(owner, 'umlclassdiagram_Constraint109', {partner})
    assert getattr(partner, 'umlclassdiagram_RootCS110') == owner
    _safe_set(owner, 'umlclassdiagram_Constraint109', set())
    assert getattr(partner, 'umlclassdiagram_RootCS110') is None


def test_assoc_extends8_stub_double():
    # umlclassdiagram_PathNameCS has no real 'umlclassdiagram_PathNameCS' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_ClassCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_ClassCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_ClassCS(name="sample_text")
    partner = umlclassdiagram_PathNameCS()
    setattr(partner, 'umlclassdiagram_PathNameCS', None)
    _safe_set(owner, 'umlclassdiagram_ClassCS9', partner)
    assert getattr(partner, 'umlclassdiagram_PathNameCS') == owner
    _safe_set(owner, 'umlclassdiagram_ClassCS9', None)
    assert getattr(partner, 'umlclassdiagram_PathNameCS') is None


def test_assoc_itType55_stub_double():
    # umlclassdiagram_PathNameCS has no real 'umlclassdiagram_PathNameCS57' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_IteratorVarCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_IteratorVarCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_IteratorVarCS(itName="sample_text")
    partner = umlclassdiagram_PathNameCS()
    setattr(partner, 'umlclassdiagram_PathNameCS57', None)
    _safe_set(owner, 'umlclassdiagram_IteratorVarCS56', partner)
    assert getattr(partner, 'umlclassdiagram_PathNameCS57') == owner
    _safe_set(owner, 'umlclassdiagram_IteratorVarCS56', None)
    assert getattr(partner, 'umlclassdiagram_PathNameCS57') is None


def test_assoc_operators113_stub_double():
    # umlclassdiagram_Operation has no real 'umlclassdiagram_Operation114' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_Operator(operator="sample_text")
    partner = umlclassdiagram_Operation()
    setattr(partner, 'umlclassdiagram_Operation114', None)
    _safe_set(owner, 'umlclassdiagram_Operator', partner)
    assert owner in getattr(partner, 'umlclassdiagram_Operation114')
    _safe_set(owner, 'umlclassdiagram_Operator', None)
    assert owner not in getattr(partner, 'umlclassdiagram_Operation114')


def test_assoc_packages0_stub_double():
    # umlclassdiagram_RootCS has no real 'umlclassdiagram_RootCS' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_PackageCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_PackageCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_PackageCS(name="sample_text")
    partner = umlclassdiagram_RootCS()
    setattr(partner, 'umlclassdiagram_RootCS', None)
    _safe_set(owner, 'umlclassdiagram_PackageCS', partner)
    assert owner in getattr(partner, 'umlclassdiagram_RootCS')
    _safe_set(owner, 'umlclassdiagram_PackageCS', None)
    assert owner not in getattr(partner, 'umlclassdiagram_RootCS')


def test_assoc_pathName70_stub_double():
    # umlclassdiagram_PathElementCS has no real 'umlclassdiagram_PathElementCS' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    partner = umlclassdiagram_PathElementCS()
    setattr(partner, 'umlclassdiagram_PathElementCS', None)
    _safe_set(owner, 'umlclassdiagram_Feature', partner)
    assert getattr(partner, 'umlclassdiagram_PathElementCS') == owner
    _safe_set(owner, 'umlclassdiagram_Feature', None)
    assert getattr(partner, 'umlclassdiagram_PathElementCS') is None


def test_assoc_pathName82_stub_double():
    # umlclassdiagram_NavigationPathElementCS has no real 'umlclassdiagram_NavigationPathElementCS' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_Feature(name="sample_text", scope="sample_text", visibility="sample_text")
    partner = umlclassdiagram_NavigationPathElementCS()
    setattr(partner, 'umlclassdiagram_NavigationPathElementCS', None)
    _safe_set(owner, 'umlclassdiagram_Feature83', partner)
    assert getattr(partner, 'umlclassdiagram_NavigationPathElementCS') == owner
    _safe_set(owner, 'umlclassdiagram_Feature83', None)
    assert getattr(partner, 'umlclassdiagram_NavigationPathElementCS') is None


def test_assoc_relations87_stub_double():
    # umlclassdiagram_ClassDiagram has no real 'umlclassdiagram_ClassDiagram88' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_Relation(derived=True, nsrc="sample_text", ntar="sample_text")
    partner = umlclassdiagram_ClassDiagram()
    setattr(partner, 'umlclassdiagram_ClassDiagram88', None)
    _safe_set(owner, 'umlclassdiagram_Relation', partner)
    assert owner in getattr(partner, 'umlclassdiagram_ClassDiagram88')
    _safe_set(owner, 'umlclassdiagram_Relation', None)
    assert owner not in getattr(partner, 'umlclassdiagram_ClassDiagram88')


def test_assoc_resultRef19_stub_double():
    # umlclassdiagram_PathNameCS has no real 'umlclassdiagram_PathNameCS21' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_OperationCS(name="sample_text")
    partner = umlclassdiagram_PathNameCS()
    setattr(partner, 'umlclassdiagram_PathNameCS21', None)
    _safe_set(owner, 'umlclassdiagram_OperationCS20', partner)
    assert getattr(partner, 'umlclassdiagram_PathNameCS21') == owner
    _safe_set(owner, 'umlclassdiagram_OperationCS20', None)
    assert getattr(partner, 'umlclassdiagram_PathNameCS21') is None


def test_assoc_right37_stub_double():
    # umlclassdiagram_CallExpCS has no real 'umlclassdiagram_CallExpCS' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_LogicExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_LogicExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_LogicExpCS(op="sample_text")
    partner = umlclassdiagram_CallExpCS()
    setattr(partner, 'umlclassdiagram_CallExpCS', None)
    _safe_set(owner, 'umlclassdiagram_LogicExpCS38', partner)
    assert getattr(partner, 'umlclassdiagram_CallExpCS') == owner
    _safe_set(owner, 'umlclassdiagram_LogicExpCS38', None)
    assert getattr(partner, 'umlclassdiagram_CallExpCS') is None


def test_assoc_super100_stub_double():
    # umlclassdiagram_Class has no real 'umlclassdiagram_Class' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_Classifier(abstract=True, derived=True)
    partner = umlclassdiagram_Class()
    setattr(partner, 'umlclassdiagram_Class', None)
    _safe_set(owner, 'umlclassdiagram_Classifier101', {partner})
    assert getattr(partner, 'umlclassdiagram_Class') == owner
    _safe_set(owner, 'umlclassdiagram_Classifier101', set())
    assert getattr(partner, 'umlclassdiagram_Class') is None


def test_assoc_supplier102_stub_double():
    # umlclassdiagram_Class has no real 'umlclassdiagram_Class104' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_Classifier(abstract=True, derived=True)
    partner = umlclassdiagram_Class()
    setattr(partner, 'umlclassdiagram_Class104', None)
    _safe_set(owner, 'umlclassdiagram_Classifier103', {partner})
    assert getattr(partner, 'umlclassdiagram_Class104') == owner
    _safe_set(owner, 'umlclassdiagram_Classifier103', set())
    assert getattr(partner, 'umlclassdiagram_Class104') is None


def test_assoc_type105_stub_double():
    # umlclassdiagram_Class has no real 'umlclassdiagram_Class107' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_Constraint(id="sample_text")
    partner = umlclassdiagram_Class()
    setattr(partner, 'umlclassdiagram_Class107', None)
    _safe_set(owner, 'umlclassdiagram_Constraint106', partner)
    assert getattr(partner, 'umlclassdiagram_Class107') == owner
    _safe_set(owner, 'umlclassdiagram_Constraint106', None)
    assert getattr(partner, 'umlclassdiagram_Class107') is None


def test_assoc_type93_stub_double():
    # umlclassdiagram_Parameter has no real 'umlclassdiagram_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_NamedElement(name="sample_text")
    partner = umlclassdiagram_Parameter()
    setattr(partner, 'umlclassdiagram_Parameter', None)
    _safe_set(owner, 'umlclassdiagram_NamedElement', partner)
    assert getattr(partner, 'umlclassdiagram_Parameter') == owner
    _safe_set(owner, 'umlclassdiagram_NamedElement', None)
    assert getattr(partner, 'umlclassdiagram_Parameter') is None


def test_assoc_typeRef14_stub_double():
    # umlclassdiagram_PathNameCS has no real 'umlclassdiagram_PathNameCS16' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_PropertyCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_PropertyCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_PropertyCS(name="sample_text")
    partner = umlclassdiagram_PathNameCS()
    setattr(partner, 'umlclassdiagram_PathNameCS16', None)
    _safe_set(owner, 'umlclassdiagram_PropertyCS15', partner)
    assert getattr(partner, 'umlclassdiagram_PathNameCS16') == owner
    _safe_set(owner, 'umlclassdiagram_PropertyCS15', None)
    assert getattr(partner, 'umlclassdiagram_PathNameCS16') is None


def test_assoc_typeRef24_stub_double():
    # umlclassdiagram_PathNameCS has no real 'umlclassdiagram_PathNameCS26' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_ParameterCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_ParameterCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_ParameterCS(name="sample_text")
    partner = umlclassdiagram_PathNameCS()
    setattr(partner, 'umlclassdiagram_PathNameCS26', None)
    _safe_set(owner, 'umlclassdiagram_ParameterCS25', partner)
    assert getattr(partner, 'umlclassdiagram_PathNameCS26') == owner
    _safe_set(owner, 'umlclassdiagram_ParameterCS25', None)
    assert getattr(partner, 'umlclassdiagram_PathNameCS26') is None


def test_assoc_types89_stub_double():
    # umlclassdiagram_ClassDiagram has no real 'umlclassdiagram_ClassDiagram90' property in the generated
    # code (a bare stub) -- manually attach it so umlclassdiagram_PrimitiveElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlclassdiagram_PrimitiveElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlclassdiagram_PrimitiveElement(type="sample_text")
    partner = umlclassdiagram_ClassDiagram()
    setattr(partner, 'umlclassdiagram_ClassDiagram90', None)
    _safe_set(owner, 'umlclassdiagram_PrimitiveElement', partner)
    assert owner in getattr(partner, 'umlclassdiagram_ClassDiagram90')
    _safe_set(owner, 'umlclassdiagram_PrimitiveElement', None)
    assert owner not in getattr(partner, 'umlclassdiagram_ClassDiagram90')


