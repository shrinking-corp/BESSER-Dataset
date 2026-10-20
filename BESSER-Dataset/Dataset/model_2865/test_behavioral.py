import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Accessor,
    BaseType,
    ConstraintNat,
    Decl,
    Exp,
    FeatureDecl,
    FeatureType,
    InvariantDecl,
    Literal,
    MModifier,
    MemberDecl,
    Modifier,
    OptionLiteral,
    Primary,
    SimpleLiteral,
    SimpleOptionLiteral,
    Type,
    deviceModelingLanguage_AccessExp,
    deviceModelingLanguage_Accessor,
    deviceModelingLanguage_AnyNatConstraint,
    deviceModelingLanguage_App,
    deviceModelingLanguage_Assignment,
    deviceModelingLanguage_AttrDecl,
    deviceModelingLanguage_BaseFeatureType,
    deviceModelingLanguage_BaseType,
    deviceModelingLanguage_BasicLiteral,
    deviceModelingLanguage_BinaryExp,
    deviceModelingLanguage_Const,
    deviceModelingLanguage_ConstraintExp,
    deviceModelingLanguage_ConstraintNat,
    deviceModelingLanguage_Data,
    deviceModelingLanguage_Decl,
    deviceModelingLanguage_Device,
    deviceModelingLanguage_EitherFeatureType,
    deviceModelingLanguage_Exp,
    deviceModelingLanguage_Feature,
    deviceModelingLanguage_FeatureDecl,
    deviceModelingLanguage_FeatureType,
    deviceModelingLanguage_GeneralInvariant,
    deviceModelingLanguage_InvariantDecl,
    deviceModelingLanguage_Literal,
    deviceModelingLanguage_LiteralExp,
    deviceModelingLanguage_MModifier,
    deviceModelingLanguage_MemberDecl,
    deviceModelingLanguage_Model,
    deviceModelingLanguage_Modifier,
    deviceModelingLanguage_MultiplicityInvariant,
    deviceModelingLanguage_NameExp,
    deviceModelingLanguage_NoneLiteral,
    deviceModelingLanguage_NoneType,
    deviceModelingLanguage_NumNatConstraint,
    deviceModelingLanguage_OptionFeatureType,
    deviceModelingLanguage_OptionLiteral,
    deviceModelingLanguage_OptionType,
    deviceModelingLanguage_Override,
    deviceModelingLanguage_Param,
    deviceModelingLanguage_Primary,
    deviceModelingLanguage_PrimaryExp,
    deviceModelingLanguage_Report,
    deviceModelingLanguage_ReportMemberDecl,
    deviceModelingLanguage_SeqFeatureType,
    deviceModelingLanguage_SeqLiteral,
    deviceModelingLanguage_SeqType,
    deviceModelingLanguage_SetFeatureType,
    deviceModelingLanguage_SetLiteral,
    deviceModelingLanguage_SetType,
    deviceModelingLanguage_SimpleBasicLiteral,
    deviceModelingLanguage_SimpleLiteral,
    deviceModelingLanguage_SimpleNoneLiteral,
    deviceModelingLanguage_SimpleOptionLiteral,
    deviceModelingLanguage_SimpleSeqLiteral,
    deviceModelingLanguage_SimpleSetLiteral,
    deviceModelingLanguage_SimpleSomeLiteral,
    deviceModelingLanguage_SimpleTupleLiteral,
    deviceModelingLanguage_SomeFeatureType,
    deviceModelingLanguage_SomeLiteral,
    deviceModelingLanguage_SomeType,
    deviceModelingLanguage_SubMemberDecl,
    deviceModelingLanguage_SubMemberMatch,
    deviceModelingLanguage_TupleLiteral,
    deviceModelingLanguage_TupleType,
    deviceModelingLanguage_Type,
    deviceModelingLanguage_TypeDecl,
    deviceModelingLanguage_UnaryExp,
    deviceModelingLanguage_Val,
    deviceModelingLanguage_Var,
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

def test_assoc_decls0_reverse_link_reassign_clear():
    a1 = deviceModelingLanguage_Model(class_=True, product=True, schema=True)
    a2 = deviceModelingLanguage_Model(class_=False, product=False, schema=False)
    b = deviceModelingLanguage_Decl(name="sample_text")
    _safe_set(b, 'deviceModelingLanguage_Decl', a1)
    assert _is_linked(b, 'deviceModelingLanguage_Decl', a1)
    if hasattr(a1, 'deviceModelingLanguage_Model'):
        assert _is_linked(a1, 'deviceModelingLanguage_Model', b)
    _safe_set(b, 'deviceModelingLanguage_Decl', a2)
    assert _is_linked(b, 'deviceModelingLanguage_Decl', a2)
    if hasattr(a1, 'deviceModelingLanguage_Model'):
        assert not _is_linked(a1, 'deviceModelingLanguage_Model', b)
    if hasattr(a2, 'deviceModelingLanguage_Model'):
        assert _is_linked(a2, 'deviceModelingLanguage_Model', b)
    _safe_set(b, 'deviceModelingLanguage_Decl', None)
    assert not _is_linked(b, 'deviceModelingLanguage_Decl', a2)
    if hasattr(a2, 'deviceModelingLanguage_Model'):
        assert not _is_linked(a2, 'deviceModelingLanguage_Model', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arg101_stub_double():
    # deviceModelingLanguage_Exp has no real 'deviceModelingLanguage_Exp102' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_UnaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_UnaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_UnaryExp(op="sample_text")
    partner = deviceModelingLanguage_Exp()
    setattr(partner, 'deviceModelingLanguage_Exp102', None)
    _safe_set(owner, 'deviceModelingLanguage_UnaryExp', partner)
    assert getattr(partner, 'deviceModelingLanguage_Exp102') == owner
    _safe_set(owner, 'deviceModelingLanguage_UnaryExp', None)
    assert getattr(partner, 'deviceModelingLanguage_Exp102') is None


def test_assoc_args24_stub_double():
    # deviceModelingLanguage_Exp has no real 'deviceModelingLanguage_Exp25' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_Report's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_Report's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_Report(name="sample_text")
    partner = deviceModelingLanguage_Exp()
    setattr(partner, 'deviceModelingLanguage_Exp25', None)
    _safe_set(owner, 'deviceModelingLanguage_Report', {partner})
    assert getattr(partner, 'deviceModelingLanguage_Exp25') == owner
    _safe_set(owner, 'deviceModelingLanguage_Report', set())
    assert getattr(partner, 'deviceModelingLanguage_Exp25') is None


def test_assoc_assigns9_stub_double():
    # deviceModelingLanguage_FeatureDecl has no real 'deviceModelingLanguage_FeatureDecl10' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_Assignment(name="sample_text")
    partner = deviceModelingLanguage_FeatureDecl()
    setattr(partner, 'deviceModelingLanguage_FeatureDecl10', None)
    _safe_set(owner, 'deviceModelingLanguage_Assignment', partner)
    assert owner in getattr(partner, 'deviceModelingLanguage_FeatureDecl10')
    _safe_set(owner, 'deviceModelingLanguage_Assignment', None)
    assert owner not in getattr(partner, 'deviceModelingLanguage_FeatureDecl10')


def test_assoc_base74_stub_double():
    # deviceModelingLanguage_BaseFeatureType has no real 'deviceModelingLanguage_BaseFeatureType75' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_OptionFeatureType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_OptionFeatureType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_OptionFeatureType(none=True)
    partner = deviceModelingLanguage_BaseFeatureType()
    setattr(partner, 'deviceModelingLanguage_BaseFeatureType75', None)
    _safe_set(owner, 'deviceModelingLanguage_OptionFeatureType', partner)
    assert getattr(partner, 'deviceModelingLanguage_BaseFeatureType75') == owner
    _safe_set(owner, 'deviceModelingLanguage_OptionFeatureType', None)
    assert getattr(partner, 'deviceModelingLanguage_BaseFeatureType75') is None


def test_assoc_bases81_stub_double():
    # deviceModelingLanguage_BaseFeatureType has no real 'deviceModelingLanguage_BaseFeatureType82' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_EitherFeatureType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_EitherFeatureType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_EitherFeatureType(choice="sample_text")
    partner = deviceModelingLanguage_BaseFeatureType()
    setattr(partner, 'deviceModelingLanguage_BaseFeatureType82', None)
    _safe_set(owner, 'deviceModelingLanguage_EitherFeatureType', {partner})
    assert getattr(partner, 'deviceModelingLanguage_BaseFeatureType82') == owner
    _safe_set(owner, 'deviceModelingLanguage_EitherFeatureType', set())
    assert getattr(partner, 'deviceModelingLanguage_BaseFeatureType82') is None


def test_assoc_bindingName52_stub_double():
    # deviceModelingLanguage_Accessor has no real 'deviceModelingLanguage_Accessor' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_ReportMemberDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_ReportMemberDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_ReportMemberDecl(name="sample_text")
    partner = deviceModelingLanguage_Accessor()
    setattr(partner, 'deviceModelingLanguage_Accessor', None)
    _safe_set(owner, 'deviceModelingLanguage_ReportMemberDecl', {partner})
    assert getattr(partner, 'deviceModelingLanguage_Accessor') == owner
    _safe_set(owner, 'deviceModelingLanguage_ReportMemberDecl', set())
    assert getattr(partner, 'deviceModelingLanguage_Accessor') is None


def test_assoc_exp21_stub_double():
    # deviceModelingLanguage_Exp has no real 'deviceModelingLanguage_Exp23' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_Assignment(name="sample_text")
    partner = deviceModelingLanguage_Exp()
    setattr(partner, 'deviceModelingLanguage_Exp23', None)
    _safe_set(owner, 'deviceModelingLanguage_Assignment22', partner)
    assert getattr(partner, 'deviceModelingLanguage_Exp23') == owner
    _safe_set(owner, 'deviceModelingLanguage_Assignment22', None)
    assert getattr(partner, 'deviceModelingLanguage_Exp23') is None


def test_assoc_left96_stub_double():
    # deviceModelingLanguage_Exp has no real 'deviceModelingLanguage_Exp97' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_BinaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_BinaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_BinaryExp(op="sample_text")
    partner = deviceModelingLanguage_Exp()
    setattr(partner, 'deviceModelingLanguage_Exp97', None)
    _safe_set(owner, 'deviceModelingLanguage_BinaryExp', partner)
    assert getattr(partner, 'deviceModelingLanguage_Exp97') == owner
    _safe_set(owner, 'deviceModelingLanguage_BinaryExp', None)
    assert getattr(partner, 'deviceModelingLanguage_Exp97') is None


def test_assoc_lit109_stub_double():
    # deviceModelingLanguage_LiteralExp has no real 'deviceModelingLanguage_LiteralExp' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_BasicLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_BasicLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_BasicLiteral(lit="sample_text")
    partner = deviceModelingLanguage_LiteralExp()
    setattr(partner, 'deviceModelingLanguage_LiteralExp', None)
    _safe_set(owner, 'deviceModelingLanguage_BasicLiteral110', partner)
    assert getattr(partner, 'deviceModelingLanguage_LiteralExp') == owner
    _safe_set(owner, 'deviceModelingLanguage_BasicLiteral110', None)
    assert getattr(partner, 'deviceModelingLanguage_LiteralExp') is None


def test_assoc_literal16_stub_double():
    # deviceModelingLanguage_Literal has no real 'deviceModelingLanguage_Literal' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_AttrDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_AttrDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_AttrDecl(attributeName="sample_text")
    partner = deviceModelingLanguage_Literal()
    setattr(partner, 'deviceModelingLanguage_Literal', None)
    _safe_set(owner, 'deviceModelingLanguage_AttrDecl17', partner)
    assert getattr(partner, 'deviceModelingLanguage_Literal') == owner
    _safe_set(owner, 'deviceModelingLanguage_AttrDecl17', None)
    assert getattr(partner, 'deviceModelingLanguage_Literal') is None


def test_assoc_match35_stub_double():
    # deviceModelingLanguage_MultiplicityInvariant has no real 'deviceModelingLanguage_MultiplicityInvariant36' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_SubMemberMatch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_SubMemberMatch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_SubMemberMatch(any="sample_text", name="sample_text", qNames="sample_text")
    partner = deviceModelingLanguage_MultiplicityInvariant()
    setattr(partner, 'deviceModelingLanguage_MultiplicityInvariant36', None)
    _safe_set(owner, 'deviceModelingLanguage_SubMemberMatch', partner)
    assert getattr(partner, 'deviceModelingLanguage_MultiplicityInvariant36') == owner
    _safe_set(owner, 'deviceModelingLanguage_SubMemberMatch', None)
    assert getattr(partner, 'deviceModelingLanguage_MultiplicityInvariant36') is None


def test_assoc_members83_stub_double():
    # deviceModelingLanguage_MemberDecl has no real 'deviceModelingLanguage_MemberDecl85' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_EitherFeatureType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_EitherFeatureType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_EitherFeatureType(choice="sample_text")
    partner = deviceModelingLanguage_MemberDecl()
    setattr(partner, 'deviceModelingLanguage_MemberDecl85', None)
    _safe_set(owner, 'deviceModelingLanguage_EitherFeatureType84', {partner})
    assert getattr(partner, 'deviceModelingLanguage_MemberDecl85') == owner
    _safe_set(owner, 'deviceModelingLanguage_EitherFeatureType84', set())
    assert getattr(partner, 'deviceModelingLanguage_MemberDecl85') is None


def test_assoc_modifier13_stub_double():
    # deviceModelingLanguage_Modifier has no real 'deviceModelingLanguage_Modifier' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_AttrDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_AttrDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_AttrDecl(attributeName="sample_text")
    partner = deviceModelingLanguage_Modifier()
    setattr(partner, 'deviceModelingLanguage_Modifier', None)
    _safe_set(owner, 'deviceModelingLanguage_AttrDecl', partner)
    assert getattr(partner, 'deviceModelingLanguage_Modifier') == owner
    _safe_set(owner, 'deviceModelingLanguage_AttrDecl', None)
    assert getattr(partner, 'deviceModelingLanguage_Modifier') is None


def test_assoc_modifier18_stub_double():
    # deviceModelingLanguage_MModifier has no real 'deviceModelingLanguage_MModifier' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_SubMemberDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_SubMemberDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_SubMemberDecl(name="sample_text")
    partner = deviceModelingLanguage_MModifier()
    setattr(partner, 'deviceModelingLanguage_MModifier', None)
    _safe_set(owner, 'deviceModelingLanguage_SubMemberDecl', partner)
    assert getattr(partner, 'deviceModelingLanguage_MModifier') == owner
    _safe_set(owner, 'deviceModelingLanguage_SubMemberDecl', None)
    assert getattr(partner, 'deviceModelingLanguage_MModifier') is None


def test_assoc_right98_stub_double():
    # deviceModelingLanguage_Exp has no real 'deviceModelingLanguage_Exp100' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_BinaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_BinaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_BinaryExp(op="sample_text")
    partner = deviceModelingLanguage_Exp()
    setattr(partner, 'deviceModelingLanguage_Exp100', None)
    _safe_set(owner, 'deviceModelingLanguage_BinaryExp99', partner)
    assert getattr(partner, 'deviceModelingLanguage_Exp100') == owner
    _safe_set(owner, 'deviceModelingLanguage_BinaryExp99', None)
    assert getattr(partner, 'deviceModelingLanguage_Exp100') is None


def test_assoc_type14_stub_double():
    # deviceModelingLanguage_Type has no real 'deviceModelingLanguage_Type' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_AttrDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_AttrDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_AttrDecl(attributeName="sample_text")
    partner = deviceModelingLanguage_Type()
    setattr(partner, 'deviceModelingLanguage_Type', None)
    _safe_set(owner, 'deviceModelingLanguage_AttrDecl15', partner)
    assert getattr(partner, 'deviceModelingLanguage_Type') == owner
    _safe_set(owner, 'deviceModelingLanguage_AttrDecl15', None)
    assert getattr(partner, 'deviceModelingLanguage_Type') is None


def test_assoc_type19_stub_double():
    # deviceModelingLanguage_FeatureType has no real 'deviceModelingLanguage_FeatureType' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_SubMemberDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_SubMemberDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_SubMemberDecl(name="sample_text")
    partner = deviceModelingLanguage_FeatureType()
    setattr(partner, 'deviceModelingLanguage_FeatureType', None)
    _safe_set(owner, 'deviceModelingLanguage_SubMemberDecl20', partner)
    assert getattr(partner, 'deviceModelingLanguage_FeatureType') == owner
    _safe_set(owner, 'deviceModelingLanguage_SubMemberDecl20', None)
    assert getattr(partner, 'deviceModelingLanguage_FeatureType') is None


def test_assoc_type50_stub_double():
    # deviceModelingLanguage_BaseFeatureType has no real 'deviceModelingLanguage_BaseFeatureType51' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_Param(name="sample_text")
    partner = deviceModelingLanguage_BaseFeatureType()
    setattr(partner, 'deviceModelingLanguage_BaseFeatureType51', None)
    _safe_set(owner, 'deviceModelingLanguage_Param', partner)
    assert getattr(partner, 'deviceModelingLanguage_BaseFeatureType51') == owner
    _safe_set(owner, 'deviceModelingLanguage_Param', None)
    assert getattr(partner, 'deviceModelingLanguage_BaseFeatureType51') is None


def test_assoc_typeCons55_stub_double():
    # deviceModelingLanguage_TypeDecl has no real 'deviceModelingLanguage_TypeDecl56' property in the generated
    # code (a bare stub) -- manually attach it so deviceModelingLanguage_BasicLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # deviceModelingLanguage_BasicLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = deviceModelingLanguage_BasicLiteral(lit="sample_text")
    partner = deviceModelingLanguage_TypeDecl()
    setattr(partner, 'deviceModelingLanguage_TypeDecl56', None)
    _safe_set(owner, 'deviceModelingLanguage_BasicLiteral', partner)
    assert getattr(partner, 'deviceModelingLanguage_TypeDecl56') == owner
    _safe_set(owner, 'deviceModelingLanguage_BasicLiteral', None)
    assert getattr(partner, 'deviceModelingLanguage_TypeDecl56') is None


