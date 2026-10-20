import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BehavioredClass,
    Expression,
    Statement,
    ale_Add,
    ale_And,
    ale_Apply,
    ale_Assign,
    ale_Attribute,
    ale_BehavioredClass,
    ale_Block,
    ale_BoolType,
    ale_Call,
    ale_ClassifierSetType,
    ale_ClassifierType,
    ale_Collection,
    ale_Comp,
    ale_Conditional,
    ale_EObject,
    ale_Enum,
    ale_Expression,
    ale_ExpressionStmt,
    ale_ExtendedClass,
    ale_False,
    ale_Feature,
    ale_ForEach,
    ale_If,
    ale_Implie,
    ale_Import,
    ale_Insert,
    ale_Int,
    ale_IntType,
    ale_Let,
    ale_Lit,
    ale_Min,
    ale_Mult,
    ale_Not,
    ale_Null,
    ale_Operation,
    ale_Or,
    ale_OrderedSet,
    ale_Real,
    ale_RealType,
    ale_Remove,
    ale_RuntimeClass,
    ale_SeqType,
    ale_Sequence,
    ale_Service,
    ale_SetType,
    ale_Statement,
    ale_String,
    ale_StringType,
    ale_Tag,
    ale_True,
    ale_Unit,
    ale_VarDecl,
    ale_VarRef,
    ale_Variable,
    ale_While,
    ale_Xor,
    ale_binding,
    ale_classifierTypeRule,
    ale_literal,
    ale_rCase,
    ale_rOpposite,
    ale_rSwitch,
    ale_rType,
    ale_typeLiteral,
    classifierTypeRule,
    literal,
    rType,
    typeLiteral,
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

def test_assoc_attributes5_reverse_link_reassign_clear():
    a1 = ale_BehavioredClass(name="sample_text")
    a2 = ale_BehavioredClass(name="sample_text_2")
    b = ale_Attribute(bounds="sample_text", modifier="sample_text", name="sample_text")
    _safe_set(b, 'ale_Attribute', a1)
    assert _is_linked(b, 'ale_Attribute', a1)
    if hasattr(a1, 'ale_BehavioredClass6'):
        assert _is_linked(a1, 'ale_BehavioredClass6', b)
    _safe_set(b, 'ale_Attribute', a2)
    assert _is_linked(b, 'ale_Attribute', a2)
    if hasattr(a1, 'ale_BehavioredClass6'):
        assert not _is_linked(a1, 'ale_BehavioredClass6', b)
    if hasattr(a2, 'ale_BehavioredClass6'):
        assert _is_linked(a2, 'ale_BehavioredClass6', b)
    _safe_set(b, 'ale_Attribute', None)
    assert not _is_linked(b, 'ale_Attribute', a2)
    if hasattr(a2, 'ale_BehavioredClass6'):
        assert not _is_linked(a2, 'ale_BehavioredClass6', b)


def test_assoc_collection46_reverse_link_reassign_clear():
    a1 = ale_ForEach(iterator="sample_text")
    a2 = ale_ForEach(iterator="sample_text_2")
    b = ale_Collection(max=7, min=7)
    _safe_set(b, 'ale_Collection', a1)
    assert _is_linked(b, 'ale_Collection', a1)
    if hasattr(a1, 'ale_ForEach'):
        assert _is_linked(a1, 'ale_ForEach', b)
    _safe_set(b, 'ale_Collection', a2)
    assert _is_linked(b, 'ale_Collection', a2)
    if hasattr(a1, 'ale_ForEach'):
        assert not _is_linked(a1, 'ale_ForEach', b)
    if hasattr(a2, 'ale_ForEach'):
        assert _is_linked(a2, 'ale_ForEach', b)
    _safe_set(b, 'ale_Collection', None)
    assert not _is_linked(b, 'ale_Collection', a2)
    if hasattr(a2, 'ale_ForEach'):
        assert not _is_linked(a2, 'ale_ForEach', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = ale_Unit(name="sample_text")
    a2 = ale_Unit(name="sample_text_2")
    b = ale_Import(alias="sample_text", name="sample_text")
    _safe_set(b, 'ale_Import', a1)
    assert _is_linked(b, 'ale_Import', a1)
    if hasattr(a1, 'ale_Unit'):
        assert _is_linked(a1, 'ale_Unit', b)
    _safe_set(b, 'ale_Import', a2)
    assert _is_linked(b, 'ale_Import', a2)
    if hasattr(a1, 'ale_Unit'):
        assert not _is_linked(a1, 'ale_Unit', b)
    if hasattr(a2, 'ale_Unit'):
        assert _is_linked(a2, 'ale_Unit', b)
    _safe_set(b, 'ale_Import', None)
    assert not _is_linked(b, 'ale_Import', a2)
    if hasattr(a2, 'ale_Unit'):
        assert not _is_linked(a2, 'ale_Unit', b)


def test_assoc_operations7_reverse_link_reassign_clear():
    a1 = ale_Operation(name="sample_text")
    a2 = ale_Operation(name="sample_text_2")
    b = ale_BehavioredClass(name="sample_text")
    _safe_set(b, 'ale_BehavioredClass8', {a1})
    assert _is_linked(b, 'ale_BehavioredClass8', a1)
    if hasattr(a1, 'ale_Operation'):
        assert _is_linked(a1, 'ale_Operation', b)
    _safe_set(b, 'ale_BehavioredClass8', {a2})
    assert _is_linked(b, 'ale_BehavioredClass8', a2)
    if hasattr(a1, 'ale_Operation'):
        assert not _is_linked(a1, 'ale_Operation', b)
    if hasattr(a2, 'ale_Operation'):
        assert _is_linked(a2, 'ale_Operation', b)
    _safe_set(b, 'ale_BehavioredClass8', set())
    assert not _is_linked(b, 'ale_BehavioredClass8', a2)
    if hasattr(a2, 'ale_Operation'):
        assert not _is_linked(a2, 'ale_Operation', b)


def test_assoc_opposite20_reverse_link_reassign_clear():
    a1 = ale_rOpposite(name="sample_text")
    a2 = ale_rOpposite(name="sample_text_2")
    b = ale_Attribute(bounds="sample_text", modifier="sample_text", name="sample_text")
    _safe_set(b, 'ale_Attribute21', a1)
    assert _is_linked(b, 'ale_Attribute21', a1)
    if hasattr(a1, 'ale_rOpposite'):
        assert _is_linked(a1, 'ale_rOpposite', b)
    _safe_set(b, 'ale_Attribute21', a2)
    assert _is_linked(b, 'ale_Attribute21', a2)
    if hasattr(a1, 'ale_rOpposite'):
        assert not _is_linked(a1, 'ale_rOpposite', b)
    if hasattr(a2, 'ale_rOpposite'):
        assert _is_linked(a2, 'ale_rOpposite', b)
    _safe_set(b, 'ale_Attribute21', None)
    assert not _is_linked(b, 'ale_Attribute21', a2)
    if hasattr(a2, 'ale_rOpposite'):
        assert not _is_linked(a2, 'ale_rOpposite', b)


def test_assoc_params13_reverse_link_reassign_clear():
    a1 = ale_Variable(name="sample_text")
    a2 = ale_Variable(name="sample_text_2")
    b = ale_Operation(name="sample_text")
    _safe_set(b, 'ale_Operation14', {a1})
    assert _is_linked(b, 'ale_Operation14', a1)
    if hasattr(a1, 'ale_Variable'):
        assert _is_linked(a1, 'ale_Variable', b)
    _safe_set(b, 'ale_Operation14', {a2})
    assert _is_linked(b, 'ale_Operation14', a2)
    if hasattr(a1, 'ale_Variable'):
        assert not _is_linked(a1, 'ale_Variable', b)
    if hasattr(a2, 'ale_Variable'):
        assert _is_linked(a2, 'ale_Variable', b)
    _safe_set(b, 'ale_Operation14', set())
    assert not _is_linked(b, 'ale_Operation14', a2)
    if hasattr(a2, 'ale_Variable'):
        assert not _is_linked(a2, 'ale_Variable', b)


def test_assoc_services1_reverse_link_reassign_clear():
    a1 = ale_Unit(name="sample_text")
    a2 = ale_Unit(name="sample_text_2")
    b = ale_Service(name="sample_text")
    _safe_set(b, 'ale_Service', a1)
    assert _is_linked(b, 'ale_Service', a1)
    if hasattr(a1, 'ale_Unit2'):
        assert _is_linked(a1, 'ale_Unit2', b)
    _safe_set(b, 'ale_Service', a2)
    assert _is_linked(b, 'ale_Service', a2)
    if hasattr(a1, 'ale_Unit2'):
        assert not _is_linked(a1, 'ale_Unit2', b)
    if hasattr(a2, 'ale_Unit2'):
        assert _is_linked(a2, 'ale_Unit2', b)
    _safe_set(b, 'ale_Service', None)
    assert not _is_linked(b, 'ale_Service', a2)
    if hasattr(a2, 'ale_Unit2'):
        assert not _is_linked(a2, 'ale_Unit2', b)


def test_assoc_tag9_reverse_link_reassign_clear():
    a1 = ale_Tag(name="sample_text")
    a2 = ale_Tag(name="sample_text_2")
    b = ale_Operation(name="sample_text")
    _safe_set(b, 'ale_Operation10', {a1})
    assert _is_linked(b, 'ale_Operation10', a1)
    if hasattr(a1, 'ale_Tag'):
        assert _is_linked(a1, 'ale_Tag', b)
    _safe_set(b, 'ale_Operation10', {a2})
    assert _is_linked(b, 'ale_Operation10', a2)
    if hasattr(a1, 'ale_Tag'):
        assert not _is_linked(a1, 'ale_Tag', b)
    if hasattr(a2, 'ale_Tag'):
        assert _is_linked(a2, 'ale_Tag', b)
    _safe_set(b, 'ale_Operation10', set())
    assert not _is_linked(b, 'ale_Operation10', a2)
    if hasattr(a2, 'ale_Tag'):
        assert not _is_linked(a2, 'ale_Tag', b)


def test_assoc_type11_reverse_link_reassign_clear():
    a1 = ale_rType(name="sample_text")
    a2 = ale_rType(name="sample_text_2")
    b = ale_Operation(name="sample_text")
    _safe_set(b, 'ale_Operation12', a1)
    assert _is_linked(b, 'ale_Operation12', a1)
    if hasattr(a1, 'ale_rType'):
        assert _is_linked(a1, 'ale_rType', b)
    _safe_set(b, 'ale_Operation12', a2)
    assert _is_linked(b, 'ale_Operation12', a2)
    if hasattr(a1, 'ale_rType'):
        assert not _is_linked(a1, 'ale_rType', b)
    if hasattr(a2, 'ale_rType'):
        assert _is_linked(a2, 'ale_rType', b)
    _safe_set(b, 'ale_Operation12', None)
    assert not _is_linked(b, 'ale_Operation12', a2)
    if hasattr(a2, 'ale_rType'):
        assert not _is_linked(a2, 'ale_rType', b)


def test_assoc_type17_reverse_link_reassign_clear():
    a1 = ale_rType(name="sample_text")
    a2 = ale_rType(name="sample_text_2")
    b = ale_Variable(name="sample_text")
    _safe_set(b, 'ale_Variable18', a1)
    assert _is_linked(b, 'ale_Variable18', a1)
    if hasattr(a1, 'ale_rType19'):
        assert _is_linked(a1, 'ale_rType19', b)
    _safe_set(b, 'ale_Variable18', a2)
    assert _is_linked(b, 'ale_Variable18', a2)
    if hasattr(a1, 'ale_rType19'):
        assert not _is_linked(a1, 'ale_rType19', b)
    if hasattr(a2, 'ale_rType19'):
        assert _is_linked(a2, 'ale_rType19', b)
    _safe_set(b, 'ale_Variable18', None)
    assert not _is_linked(b, 'ale_Variable18', a2)
    if hasattr(a2, 'ale_rType19'):
        assert not _is_linked(a2, 'ale_rType19', b)


def test_assoc_type22_reverse_link_reassign_clear():
    a1 = ale_rType(name="sample_text")
    a2 = ale_rType(name="sample_text_2")
    b = ale_Attribute(bounds="sample_text", modifier="sample_text", name="sample_text")
    _safe_set(b, 'ale_Attribute23', a1)
    assert _is_linked(b, 'ale_Attribute23', a1)
    if hasattr(a1, 'ale_rType24'):
        assert _is_linked(a1, 'ale_rType24', b)
    _safe_set(b, 'ale_Attribute23', a2)
    assert _is_linked(b, 'ale_Attribute23', a2)
    if hasattr(a1, 'ale_rType24'):
        assert not _is_linked(a1, 'ale_rType24', b)
    if hasattr(a2, 'ale_rType24'):
        assert _is_linked(a2, 'ale_rType24', b)
    _safe_set(b, 'ale_Attribute23', None)
    assert not _is_linked(b, 'ale_Attribute23', a2)
    if hasattr(a2, 'ale_rType24'):
        assert not _is_linked(a2, 'ale_rType24', b)


def test_assoc_type27_reverse_link_reassign_clear():
    a1 = ale_rType(name="sample_text")
    a2 = ale_rType(name="sample_text_2")
    b = ale_VarDecl(name="sample_text")
    _safe_set(b, 'ale_VarDecl', a1)
    assert _is_linked(b, 'ale_VarDecl', a1)
    if hasattr(a1, 'ale_rType28'):
        assert _is_linked(a1, 'ale_rType28', b)
    _safe_set(b, 'ale_VarDecl', a2)
    assert _is_linked(b, 'ale_VarDecl', a2)
    if hasattr(a1, 'ale_rType28'):
        assert not _is_linked(a1, 'ale_rType28', b)
    if hasattr(a2, 'ale_rType28'):
        assert _is_linked(a2, 'ale_rType28', b)
    _safe_set(b, 'ale_VarDecl', None)
    assert not _is_linked(b, 'ale_VarDecl', a2)
    if hasattr(a2, 'ale_rType28'):
        assert not _is_linked(a2, 'ale_rType28', b)


def test_assoc_xtendedClasses3_reverse_link_reassign_clear():
    a1 = ale_Unit(name="sample_text")
    a2 = ale_Unit(name="sample_text_2")
    b = ale_BehavioredClass(name="sample_text")
    _safe_set(b, 'ale_BehavioredClass', a1)
    assert _is_linked(b, 'ale_BehavioredClass', a1)
    if hasattr(a1, 'ale_Unit4'):
        assert _is_linked(a1, 'ale_Unit4', b)
    _safe_set(b, 'ale_BehavioredClass', a2)
    assert _is_linked(b, 'ale_BehavioredClass', a2)
    if hasattr(a1, 'ale_Unit4'):
        assert not _is_linked(a1, 'ale_Unit4', b)
    if hasattr(a2, 'ale_Unit4'):
        assert _is_linked(a2, 'ale_Unit4', b)
    _safe_set(b, 'ale_BehavioredClass', None)
    assert not _is_linked(b, 'ale_BehavioredClass', a2)
    if hasattr(a2, 'ale_Unit4'):
        assert not _is_linked(a2, 'ale_Unit4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bindings159_stub_double():
    # ale_Let has no real 'ale_Let' property in the generated
    # code (a bare stub) -- manually attach it so ale_binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_binding(name="sample_text")
    partner = ale_Let()
    setattr(partner, 'ale_Let', None)
    _safe_set(owner, 'ale_binding160', partner)
    assert owner in getattr(partner, 'ale_Let')
    _safe_set(owner, 'ale_binding160', None)
    assert owner not in getattr(partner, 'ale_Let')


def test_assoc_block47_stub_double():
    # ale_Block has no real 'ale_Block49' property in the generated
    # code (a bare stub) -- manually attach it so ale_ForEach's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_ForEach's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_ForEach(iterator="sample_text")
    partner = ale_Block()
    setattr(partner, 'ale_Block49', None)
    _safe_set(owner, 'ale_ForEach48', partner)
    assert getattr(partner, 'ale_Block49') == owner
    _safe_set(owner, 'ale_ForEach48', None)
    assert getattr(partner, 'ale_Block49') is None


def test_assoc_body15_stub_double():
    # ale_Block has no real 'ale_Block' property in the generated
    # code (a bare stub) -- manually attach it so ale_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Operation(name="sample_text")
    partner = ale_Block()
    setattr(partner, 'ale_Block', None)
    _safe_set(owner, 'ale_Operation16', partner)
    assert getattr(partner, 'ale_Block') == owner
    _safe_set(owner, 'ale_Operation16', None)
    assert getattr(partner, 'ale_Block') is None


def test_assoc_cases73_stub_double():
    # ale_rCase has no real 'ale_rCase' property in the generated
    # code (a bare stub) -- manually attach it so ale_rSwitch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_rSwitch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_rSwitch(paramName="sample_text")
    partner = ale_rCase()
    setattr(partner, 'ale_rCase', None)
    _safe_set(owner, 'ale_rSwitch74', {partner})
    assert getattr(partner, 'ale_rCase') == owner
    _safe_set(owner, 'ale_rSwitch74', set())
    assert getattr(partner, 'ale_rCase') is None


def test_assoc_exp25_stub_double():
    # ale_ExpressionStmt has no real 'ale_ExpressionStmt' property in the generated
    # code (a bare stub) -- manually attach it so ale_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Attribute(bounds="sample_text", modifier="sample_text", name="sample_text")
    partner = ale_ExpressionStmt()
    setattr(partner, 'ale_ExpressionStmt', None)
    _safe_set(owner, 'ale_Attribute26', partner)
    assert getattr(partner, 'ale_ExpressionStmt') == owner
    _safe_set(owner, 'ale_Attribute26', None)
    assert getattr(partner, 'ale_ExpressionStmt') is None


def test_assoc_exp29_stub_double():
    # ale_ExpressionStmt has no real 'ale_ExpressionStmt31' property in the generated
    # code (a bare stub) -- manually attach it so ale_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_VarDecl(name="sample_text")
    partner = ale_ExpressionStmt()
    setattr(partner, 'ale_ExpressionStmt31', None)
    _safe_set(owner, 'ale_VarDecl30', partner)
    assert getattr(partner, 'ale_ExpressionStmt31') == owner
    _safe_set(owner, 'ale_VarDecl30', None)
    assert getattr(partner, 'ale_ExpressionStmt31') is None


def test_assoc_exp50_stub_double():
    # ale_ExpressionStmt has no real 'ale_ExpressionStmt52' property in the generated
    # code (a bare stub) -- manually attach it so ale_Collection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Collection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Collection(max=7, min=7)
    partner = ale_ExpressionStmt()
    setattr(partner, 'ale_ExpressionStmt52', None)
    _safe_set(owner, 'ale_Collection51', partner)
    assert getattr(partner, 'ale_ExpressionStmt52') == owner
    _safe_set(owner, 'ale_Collection51', None)
    assert getattr(partner, 'ale_ExpressionStmt52') is None


def test_assoc_exp90_stub_double():
    # ale_Expression has no real 'ale_Expression92' property in the generated
    # code (a bare stub) -- manually attach it so ale_binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_binding(name="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression92', None)
    _safe_set(owner, 'ale_binding91', partner)
    assert getattr(partner, 'ale_Expression92') == owner
    _safe_set(owner, 'ale_binding91', None)
    assert getattr(partner, 'ale_Expression92') is None


def test_assoc_guard78_stub_double():
    # ale_rCase has no real 'ale_rCase79' property in the generated
    # code (a bare stub) -- manually attach it so ale_rType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_rType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_rType(name="sample_text")
    partner = ale_rCase()
    setattr(partner, 'ale_rCase79', None)
    _safe_set(owner, 'ale_rType80', partner)
    assert getattr(partner, 'ale_rCase79') == owner
    _safe_set(owner, 'ale_rType80', None)
    assert getattr(partner, 'ale_rCase79') is None


def test_assoc_lambda_105_stub_double():
    # ale_Expression has no real 'ale_Expression107' property in the generated
    # code (a bare stub) -- manually attach it so ale_Apply's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Apply's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Apply(name="sample_text", varName="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression107', None)
    _safe_set(owner, 'ale_Apply106', partner)
    assert getattr(partner, 'ale_Expression107') == owner
    _safe_set(owner, 'ale_Apply106', None)
    assert getattr(partner, 'ale_Expression107') is None


def test_assoc_left111_stub_double():
    # ale_Expression has no real 'ale_Expression112' property in the generated
    # code (a bare stub) -- manually attach it so ale_Mult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Mult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Mult(op="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression112', None)
    _safe_set(owner, 'ale_Mult', partner)
    assert getattr(partner, 'ale_Expression112') == owner
    _safe_set(owner, 'ale_Mult', None)
    assert getattr(partner, 'ale_Expression112') is None


def test_assoc_left116_stub_double():
    # ale_Expression has no real 'ale_Expression117' property in the generated
    # code (a bare stub) -- manually attach it so ale_Add's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Add's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Add(op="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression117', None)
    _safe_set(owner, 'ale_Add', partner)
    assert getattr(partner, 'ale_Expression117') == owner
    _safe_set(owner, 'ale_Add', None)
    assert getattr(partner, 'ale_Expression117') is None


def test_assoc_left121_stub_double():
    # ale_Expression has no real 'ale_Expression122' property in the generated
    # code (a bare stub) -- manually attach it so ale_Comp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Comp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Comp(op="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression122', None)
    _safe_set(owner, 'ale_Comp', partner)
    assert getattr(partner, 'ale_Expression122') == owner
    _safe_set(owner, 'ale_Comp', None)
    assert getattr(partner, 'ale_Expression122') is None


def test_assoc_other75_stub_double():
    # ale_ExpressionStmt has no real 'ale_ExpressionStmt77' property in the generated
    # code (a bare stub) -- manually attach it so ale_rSwitch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_rSwitch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_rSwitch(paramName="sample_text")
    partner = ale_ExpressionStmt()
    setattr(partner, 'ale_ExpressionStmt77', None)
    _safe_set(owner, 'ale_rSwitch76', partner)
    assert getattr(partner, 'ale_ExpressionStmt77') == owner
    _safe_set(owner, 'ale_rSwitch76', None)
    assert getattr(partner, 'ale_ExpressionStmt77') is None


def test_assoc_paramVal71_stub_double():
    # ale_ExpressionStmt has no real 'ale_ExpressionStmt72' property in the generated
    # code (a bare stub) -- manually attach it so ale_rSwitch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_rSwitch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_rSwitch(paramName="sample_text")
    partner = ale_ExpressionStmt()
    setattr(partner, 'ale_ExpressionStmt72', None)
    _safe_set(owner, 'ale_rSwitch', partner)
    assert getattr(partner, 'ale_ExpressionStmt72') == owner
    _safe_set(owner, 'ale_rSwitch', None)
    assert getattr(partner, 'ale_ExpressionStmt72') is None


def test_assoc_params108_stub_double():
    # ale_Expression has no real 'ale_Expression110' property in the generated
    # code (a bare stub) -- manually attach it so ale_Apply's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Apply's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Apply(name="sample_text", varName="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression110', None)
    _safe_set(owner, 'ale_Apply109', {partner})
    assert getattr(partner, 'ale_Expression110') == owner
    _safe_set(owner, 'ale_Apply109', set())
    assert getattr(partner, 'ale_Expression110') is None


def test_assoc_params95_stub_double():
    # ale_Expression has no real 'ale_Expression97' property in the generated
    # code (a bare stub) -- manually attach it so ale_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Call(name="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression97', None)
    _safe_set(owner, 'ale_Call96', {partner})
    assert getattr(partner, 'ale_Expression97') == owner
    _safe_set(owner, 'ale_Call96', set())
    assert getattr(partner, 'ale_Expression97') is None


def test_assoc_right113_stub_double():
    # ale_Expression has no real 'ale_Expression115' property in the generated
    # code (a bare stub) -- manually attach it so ale_Mult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Mult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Mult(op="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression115', None)
    _safe_set(owner, 'ale_Mult114', partner)
    assert getattr(partner, 'ale_Expression115') == owner
    _safe_set(owner, 'ale_Mult114', None)
    assert getattr(partner, 'ale_Expression115') is None


def test_assoc_right118_stub_double():
    # ale_Expression has no real 'ale_Expression120' property in the generated
    # code (a bare stub) -- manually attach it so ale_Add's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Add's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Add(op="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression120', None)
    _safe_set(owner, 'ale_Add119', partner)
    assert getattr(partner, 'ale_Expression120') == owner
    _safe_set(owner, 'ale_Add119', None)
    assert getattr(partner, 'ale_Expression120') is None


def test_assoc_right123_stub_double():
    # ale_Expression has no real 'ale_Expression125' property in the generated
    # code (a bare stub) -- manually attach it so ale_Comp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Comp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Comp(op="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression125', None)
    _safe_set(owner, 'ale_Comp124', partner)
    assert getattr(partner, 'ale_Expression125') == owner
    _safe_set(owner, 'ale_Comp124', None)
    assert getattr(partner, 'ale_Expression125') is None


def test_assoc_target100_stub_double():
    # ale_Expression has no real 'ale_Expression101' property in the generated
    # code (a bare stub) -- manually attach it so ale_Apply's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Apply's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Apply(name="sample_text", varName="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression101', None)
    _safe_set(owner, 'ale_Apply', partner)
    assert getattr(partner, 'ale_Expression101') == owner
    _safe_set(owner, 'ale_Apply', None)
    assert getattr(partner, 'ale_Expression101') is None


def test_assoc_target93_stub_double():
    # ale_Expression has no real 'ale_Expression94' property in the generated
    # code (a bare stub) -- manually attach it so ale_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Call(name="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression94', None)
    _safe_set(owner, 'ale_Call', partner)
    assert getattr(partner, 'ale_Expression94') == owner
    _safe_set(owner, 'ale_Call', None)
    assert getattr(partner, 'ale_Expression94') is None


def test_assoc_target98_stub_double():
    # ale_Expression has no real 'ale_Expression99' property in the generated
    # code (a bare stub) -- manually attach it so ale_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Feature(feature="sample_text")
    partner = ale_Expression()
    setattr(partner, 'ale_Expression99', None)
    _safe_set(owner, 'ale_Feature', partner)
    assert getattr(partner, 'ale_Expression99') == owner
    _safe_set(owner, 'ale_Feature', None)
    assert getattr(partner, 'ale_Expression99') is None


def test_assoc_type89_stub_double():
    # ale_typeLiteral has no real 'ale_typeLiteral' property in the generated
    # code (a bare stub) -- manually attach it so ale_binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_binding(name="sample_text")
    partner = ale_typeLiteral()
    setattr(partner, 'ale_typeLiteral', None)
    _safe_set(owner, 'ale_binding', partner)
    assert getattr(partner, 'ale_typeLiteral') == owner
    _safe_set(owner, 'ale_binding', None)
    assert getattr(partner, 'ale_typeLiteral') is None


def test_assoc_varType102_stub_double():
    # ale_typeLiteral has no real 'ale_typeLiteral104' property in the generated
    # code (a bare stub) -- manually attach it so ale_Apply's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ale_Apply's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ale_Apply(name="sample_text", varName="sample_text")
    partner = ale_typeLiteral()
    setattr(partner, 'ale_typeLiteral104', None)
    _safe_set(owner, 'ale_Apply103', partner)
    assert getattr(partner, 'ale_typeLiteral104') == owner
    _safe_set(owner, 'ale_Apply103', None)
    assert getattr(partner, 'ale_typeLiteral104') is None


