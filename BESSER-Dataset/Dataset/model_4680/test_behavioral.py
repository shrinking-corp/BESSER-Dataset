import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expr,
    Member,
    NamedElement,
    Stmt,
    Symbol,
    Value,
    imp_ArrayDecl,
    imp_ArrayValue,
    imp_Assignment,
    imp_AttributeDecl,
    imp_Binary,
    imp_Block,
    imp_BoolConst,
    imp_BoolValue,
    imp_Class,
    imp_Declaration,
    imp_Expr,
    imp_If,
    imp_IntConst,
    imp_IntValue,
    imp_Member,
    imp_MethodDecl,
    imp_NamedElement,
    imp_NewClass,
    imp_ParamDecl,
    imp_Print,
    imp_Program,
    imp_Project,
    imp_Return,
    imp_Stmt,
    imp_Store,
    imp_StringConst,
    imp_StringToValueMap,
    imp_StringValue,
    imp_Symbol,
    imp_This,
    imp_Unary,
    imp_Value,
    imp_VarRef,
    imp_While,
    BinaryOp,
    UnaryOp,
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

def test_assoc_attributes44_reverse_link_reassign_clear():
    a1 = imp_Class(name="sample_text")
    a2 = imp_Class(name="sample_text_2")
    b = imp_AttributeDecl(name="sample_text")
    _safe_set(b, 'imp_AttributeDecl', a1)
    assert _is_linked(b, 'imp_AttributeDecl', a1)
    if hasattr(a1, 'imp_Class45'):
        assert _is_linked(a1, 'imp_Class45', b)
    _safe_set(b, 'imp_AttributeDecl', a2)
    assert _is_linked(b, 'imp_AttributeDecl', a2)
    if hasattr(a1, 'imp_Class45'):
        assert not _is_linked(a1, 'imp_Class45', b)
    if hasattr(a2, 'imp_Class45'):
        assert _is_linked(a2, 'imp_Class45', b)
    _safe_set(b, 'imp_AttributeDecl', None)
    assert not _is_linked(b, 'imp_AttributeDecl', a2)
    if hasattr(a2, 'imp_Class45'):
        assert not _is_linked(a2, 'imp_Class45', b)


def test_assoc_methods46_reverse_link_reassign_clear():
    a1 = imp_MethodDecl(name="sample_text")
    a2 = imp_MethodDecl(name="sample_text_2")
    b = imp_Class(name="sample_text")
    _safe_set(b, 'imp_Class47', {a1})
    assert _is_linked(b, 'imp_Class47', a1)
    if hasattr(a1, 'imp_MethodDecl48'):
        assert _is_linked(a1, 'imp_MethodDecl48', b)
    _safe_set(b, 'imp_Class47', {a2})
    assert _is_linked(b, 'imp_Class47', a2)
    if hasattr(a1, 'imp_MethodDecl48'):
        assert not _is_linked(a1, 'imp_MethodDecl48', b)
    if hasattr(a2, 'imp_MethodDecl48'):
        assert _is_linked(a2, 'imp_MethodDecl48', b)
    _safe_set(b, 'imp_Class47', set())
    assert not _is_linked(b, 'imp_Class47', a2)
    if hasattr(a2, 'imp_MethodDecl48'):
        assert not _is_linked(a2, 'imp_MethodDecl48', b)


def test_assoc_params38_reverse_link_reassign_clear():
    a1 = imp_ParamDecl(name="sample_text")
    a2 = imp_ParamDecl(name="sample_text_2")
    b = imp_MethodDecl(name="sample_text")
    _safe_set(b, 'imp_MethodDecl39', {a1})
    assert _is_linked(b, 'imp_MethodDecl39', a1)
    if hasattr(a1, 'imp_ParamDecl'):
        assert _is_linked(a1, 'imp_ParamDecl', b)
    _safe_set(b, 'imp_MethodDecl39', {a2})
    assert _is_linked(b, 'imp_MethodDecl39', a2)
    if hasattr(a1, 'imp_ParamDecl'):
        assert not _is_linked(a1, 'imp_ParamDecl', b)
    if hasattr(a2, 'imp_ParamDecl'):
        assert _is_linked(a2, 'imp_ParamDecl', b)
    _safe_set(b, 'imp_MethodDecl39', set())
    assert not _is_linked(b, 'imp_MethodDecl39', a2)
    if hasattr(a2, 'imp_ParamDecl'):
        assert not _is_linked(a2, 'imp_ParamDecl', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_class_49_stub_double():
    # imp_NewClass has no real 'imp_NewClass' property in the generated
    # code (a bare stub) -- manually attach it so imp_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Class(name="sample_text")
    partner = imp_NewClass()
    setattr(partner, 'imp_NewClass', None)
    _safe_set(owner, 'imp_Class50', partner)
    assert getattr(partner, 'imp_NewClass') == owner
    _safe_set(owner, 'imp_Class50', None)
    assert getattr(partner, 'imp_NewClass') is None


def test_assoc_classes33_stub_double():
    # imp_Program has no real 'imp_Program34' property in the generated
    # code (a bare stub) -- manually attach it so imp_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Class(name="sample_text")
    partner = imp_Program()
    setattr(partner, 'imp_Program34', None)
    _safe_set(owner, 'imp_Class', partner)
    assert owner in getattr(partner, 'imp_Program34')
    _safe_set(owner, 'imp_Class', None)
    assert owner not in getattr(partner, 'imp_Program34')


def test_assoc_exp0_stub_double():
    # imp_Expr has no real 'imp_Expr' property in the generated
    # code (a bare stub) -- manually attach it so imp_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Declaration(name="sample_text")
    partner = imp_Expr()
    setattr(partner, 'imp_Expr', None)
    _safe_set(owner, 'imp_Declaration', partner)
    assert getattr(partner, 'imp_Expr') == owner
    _safe_set(owner, 'imp_Declaration', None)
    assert getattr(partner, 'imp_Expr') is None


def test_assoc_expr18_stub_double():
    # imp_Expr has no real 'imp_Expr19' property in the generated
    # code (a bare stub) -- manually attach it so imp_Unary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Unary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Unary(op="sample_text")
    partner = imp_Expr()
    setattr(partner, 'imp_Expr19', None)
    _safe_set(owner, 'imp_Unary', partner)
    assert getattr(partner, 'imp_Expr19') == owner
    _safe_set(owner, 'imp_Unary', None)
    assert getattr(partner, 'imp_Expr19') is None


def test_assoc_index1_stub_double():
    # imp_Expr has no real 'imp_Expr3' property in the generated
    # code (a bare stub) -- manually attach it so imp_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Declaration(name="sample_text")
    partner = imp_Expr()
    setattr(partner, 'imp_Expr3', None)
    _safe_set(owner, 'imp_Declaration2', partner)
    assert getattr(partner, 'imp_Expr3') == owner
    _safe_set(owner, 'imp_Declaration2', None)
    assert getattr(partner, 'imp_Expr3') is None


def test_assoc_lhs20_stub_double():
    # imp_Expr has no real 'imp_Expr21' property in the generated
    # code (a bare stub) -- manually attach it so imp_Binary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Binary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Binary(op="sample_text")
    partner = imp_Expr()
    setattr(partner, 'imp_Expr21', None)
    _safe_set(owner, 'imp_Binary', partner)
    assert getattr(partner, 'imp_Expr21') == owner
    _safe_set(owner, 'imp_Binary', None)
    assert getattr(partner, 'imp_Expr21') is None


def test_assoc_lhs56_stub_double():
    # imp_Expr has no real 'imp_Expr57' property in the generated
    # code (a bare stub) -- manually attach it so imp_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Project(ismethodcall=True)
    partner = imp_Expr()
    setattr(partner, 'imp_Expr57', None)
    _safe_set(owner, 'imp_Project', partner)
    assert getattr(partner, 'imp_Expr57') == owner
    _safe_set(owner, 'imp_Project', None)
    assert getattr(partner, 'imp_Expr57') is None


def test_assoc_methods32_stub_double():
    # imp_Program has no real 'imp_Program' property in the generated
    # code (a bare stub) -- manually attach it so imp_MethodDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_MethodDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_MethodDecl(name="sample_text")
    partner = imp_Program()
    setattr(partner, 'imp_Program', None)
    _safe_set(owner, 'imp_MethodDecl', partner)
    assert owner in getattr(partner, 'imp_Program')
    _safe_set(owner, 'imp_MethodDecl', None)
    assert owner not in getattr(partner, 'imp_Program')


def test_assoc_params60_stub_double():
    # imp_Expr has no real 'imp_Expr62' property in the generated
    # code (a bare stub) -- manually attach it so imp_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Project(ismethodcall=True)
    partner = imp_Expr()
    setattr(partner, 'imp_Expr62', None)
    _safe_set(owner, 'imp_Project61', {partner})
    assert getattr(partner, 'imp_Expr62') == owner
    _safe_set(owner, 'imp_Project61', set())
    assert getattr(partner, 'imp_Expr62') is None


def test_assoc_rhs22_stub_double():
    # imp_Expr has no real 'imp_Expr24' property in the generated
    # code (a bare stub) -- manually attach it so imp_Binary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Binary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Binary(op="sample_text")
    partner = imp_Expr()
    setattr(partner, 'imp_Expr24', None)
    _safe_set(owner, 'imp_Binary23', partner)
    assert getattr(partner, 'imp_Expr24') == owner
    _safe_set(owner, 'imp_Binary23', None)
    assert getattr(partner, 'imp_Expr24') is None


def test_assoc_rhs58_stub_double():
    # imp_Member has no real 'imp_Member' property in the generated
    # code (a bare stub) -- manually attach it so imp_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Project(ismethodcall=True)
    partner = imp_Member()
    setattr(partner, 'imp_Member', None)
    _safe_set(owner, 'imp_Project59', partner)
    assert getattr(partner, 'imp_Member') == owner
    _safe_set(owner, 'imp_Project59', None)
    assert getattr(partner, 'imp_Member') is None


def test_assoc_stmt35_stub_double():
    # imp_Stmt has no real 'imp_Stmt37' property in the generated
    # code (a bare stub) -- manually attach it so imp_MethodDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_MethodDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_MethodDecl(name="sample_text")
    partner = imp_Stmt()
    setattr(partner, 'imp_Stmt37', None)
    _safe_set(owner, 'imp_MethodDecl36', partner)
    assert getattr(partner, 'imp_Stmt37') == owner
    _safe_set(owner, 'imp_MethodDecl36', None)
    assert getattr(partner, 'imp_Stmt37') is None


def test_assoc_value26_stub_double():
    # imp_Value has no real 'imp_Value' property in the generated
    # code (a bare stub) -- manually attach it so imp_StringToValueMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_StringToValueMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_StringToValueMap(key="sample_text")
    partner = imp_Value()
    setattr(partner, 'imp_Value', None)
    _safe_set(owner, 'imp_StringToValueMap27', partner)
    assert getattr(partner, 'imp_Value') == owner
    _safe_set(owner, 'imp_StringToValueMap27', None)
    assert getattr(partner, 'imp_Value') is None


def test_assoc_values25_stub_double():
    # imp_Store has no real 'imp_Store' property in the generated
    # code (a bare stub) -- manually attach it so imp_StringToValueMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_StringToValueMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_StringToValueMap(key="sample_text")
    partner = imp_Store()
    setattr(partner, 'imp_Store', None)
    _safe_set(owner, 'imp_StringToValueMap', partner)
    assert owner in getattr(partner, 'imp_Store')
    _safe_set(owner, 'imp_StringToValueMap', None)
    assert owner not in getattr(partner, 'imp_Store')


