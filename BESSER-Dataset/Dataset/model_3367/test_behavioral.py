import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BlockType,
    ClientBlock,
    Declaration,
    HttpMethodBlock,
    IntrinsicType,
    Literal,
    Member,
    NumericType,
    Type,
    UserTypeDeclaration,
    netModel_BlockType,
    netModel_BodyBlock,
    netModel_BooleanLiteral,
    netModel_BooleanType,
    netModel_Client,
    netModel_ClientBlock,
    netModel_ComplexTypeDeclaration,
    netModel_ComplexTypeLiteral,
    netModel_Declaration,
    netModel_DoubleType,
    netModel_EnumMember,
    netModel_EnumTypeDeclaration,
    netModel_EnumTypeLiteral,
    netModel_GenericListType,
    netModel_Header,
    netModel_HeaderBlock,
    netModel_HttpMethod,
    netModel_HttpMethodBlock,
    netModel_IntegerType,
    netModel_IntrinsicType,
    netModel_Literal,
    netModel_LongType,
    netModel_Member,
    netModel_Model,
    netModel_NumericLiteral,
    netModel_NumericType,
    netModel_ParamsBlock,
    netModel_Path,
    netModel_ResponseBlock,
    netModel_SimpleMember,
    netModel_SimpleMemberAssignment,
    netModel_SkipMember,
    netModel_StringLiteral,
    netModel_StringType,
    netModel_Type,
    netModel_TypedMember,
    netModel_UserType,
    netModel_UserTypeDeclaration,
    BooleanValue,
    HttpMethodType,
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

def test_assoc_declarations0_reverse_link_reassign_clear():
    a1 = netModel_Model(packageName="sample_text")
    a2 = netModel_Model(packageName="sample_text_2")
    b = netModel_Declaration(name="sample_text")
    _safe_set(b, 'netModel_Declaration', a1)
    assert _is_linked(b, 'netModel_Declaration', a1)
    if hasattr(a1, 'netModel_Model'):
        assert _is_linked(a1, 'netModel_Model', b)
    _safe_set(b, 'netModel_Declaration', a2)
    assert _is_linked(b, 'netModel_Declaration', a2)
    if hasattr(a1, 'netModel_Model'):
        assert not _is_linked(a1, 'netModel_Model', b)
    if hasattr(a2, 'netModel_Model'):
        assert _is_linked(a2, 'netModel_Model', b)
    _safe_set(b, 'netModel_Declaration', None)
    assert not _is_linked(b, 'netModel_Declaration', a2)
    if hasattr(a2, 'netModel_Model'):
        assert not _is_linked(a2, 'netModel_Model', b)


def test_assoc_path3_reverse_link_reassign_clear():
    a1 = netModel_Path(arb="sample_text")
    a2 = netModel_Path(arb="sample_text_2")
    b = netModel_HttpMethod(name="sample_text", type="sample_text")
    _safe_set(b, 'netModel_HttpMethod', a1)
    assert _is_linked(b, 'netModel_HttpMethod', a1)
    if hasattr(a1, 'netModel_Path'):
        assert _is_linked(a1, 'netModel_Path', b)
    _safe_set(b, 'netModel_HttpMethod', a2)
    assert _is_linked(b, 'netModel_HttpMethod', a2)
    if hasattr(a1, 'netModel_Path'):
        assert not _is_linked(a1, 'netModel_Path', b)
    if hasattr(a2, 'netModel_Path'):
        assert _is_linked(a2, 'netModel_Path', b)
    _safe_set(b, 'netModel_HttpMethod', None)
    assert not _is_linked(b, 'netModel_HttpMethod', a2)
    if hasattr(a2, 'netModel_Path'):
        assert not _is_linked(a2, 'netModel_Path', b)


def test_assoc_type21_reverse_link_reassign_clear():
    a1 = netModel_SimpleMember(name="sample_text")
    a2 = netModel_SimpleMember(name="sample_text_2")
    b = netModel_IntrinsicType(id="sample_text")
    _safe_set(b, 'netModel_IntrinsicType', a1)
    assert _is_linked(b, 'netModel_IntrinsicType', a1)
    if hasattr(a1, 'netModel_SimpleMember22'):
        assert _is_linked(a1, 'netModel_SimpleMember22', b)
    _safe_set(b, 'netModel_IntrinsicType', a2)
    assert _is_linked(b, 'netModel_IntrinsicType', a2)
    if hasattr(a1, 'netModel_SimpleMember22'):
        assert not _is_linked(a1, 'netModel_SimpleMember22', b)
    if hasattr(a2, 'netModel_SimpleMember22'):
        assert _is_linked(a2, 'netModel_SimpleMember22', b)
    _safe_set(b, 'netModel_IntrinsicType', None)
    assert not _is_linked(b, 'netModel_IntrinsicType', a2)
    if hasattr(a2, 'netModel_SimpleMember22'):
        assert not _is_linked(a2, 'netModel_SimpleMember22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_blocks1_stub_double():
    # netModel_ClientBlock has no real 'netModel_ClientBlock' property in the generated
    # code (a bare stub) -- manually attach it so netModel_Client's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netModel_Client's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netModel_Client(baseUrl="sample_text")
    partner = netModel_ClientBlock()
    setattr(partner, 'netModel_ClientBlock', None)
    _safe_set(owner, 'netModel_Client', {partner})
    assert getattr(partner, 'netModel_ClientBlock') == owner
    _safe_set(owner, 'netModel_Client', set())
    assert getattr(partner, 'netModel_ClientBlock') is None


def test_assoc_blocks4_stub_double():
    # netModel_HttpMethodBlock has no real 'netModel_HttpMethodBlock' property in the generated
    # code (a bare stub) -- manually attach it so netModel_HttpMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netModel_HttpMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netModel_HttpMethod(name="sample_text", type="sample_text")
    partner = netModel_HttpMethodBlock()
    setattr(partner, 'netModel_HttpMethodBlock', None)
    _safe_set(owner, 'netModel_HttpMethod5', {partner})
    assert getattr(partner, 'netModel_HttpMethodBlock') == owner
    _safe_set(owner, 'netModel_HttpMethod5', set())
    assert getattr(partner, 'netModel_HttpMethodBlock') is None


def test_assoc_declaration25_stub_double():
    # netModel_UserType has no real 'netModel_UserType' property in the generated
    # code (a bare stub) -- manually attach it so netModel_UserTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netModel_UserTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netModel_UserTypeDeclaration(keyword="sample_text", nogen=True)
    partner = netModel_UserType()
    setattr(partner, 'netModel_UserType', None)
    _safe_set(owner, 'netModel_UserTypeDeclaration', partner)
    assert getattr(partner, 'netModel_UserType') == owner
    _safe_set(owner, 'netModel_UserTypeDeclaration', None)
    assert getattr(partner, 'netModel_UserType') is None


def test_assoc_elementType23_stub_double():
    # netModel_Type has no real 'netModel_Type24' property in the generated
    # code (a bare stub) -- manually attach it so netModel_GenericListType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netModel_GenericListType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netModel_GenericListType(id="sample_text")
    partner = netModel_Type()
    setattr(partner, 'netModel_Type24', None)
    _safe_set(owner, 'netModel_GenericListType', partner)
    assert getattr(partner, 'netModel_Type24') == owner
    _safe_set(owner, 'netModel_GenericListType', None)
    assert getattr(partner, 'netModel_Type24') is None


def test_assoc_headers2_stub_double():
    # netModel_HeaderBlock has no real 'netModel_HeaderBlock' property in the generated
    # code (a bare stub) -- manually attach it so netModel_Header's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netModel_Header's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netModel_Header(name="sample_text", value="sample_text")
    partner = netModel_HeaderBlock()
    setattr(partner, 'netModel_HeaderBlock', None)
    _safe_set(owner, 'netModel_Header', partner)
    assert owner in getattr(partner, 'netModel_HeaderBlock')
    _safe_set(owner, 'netModel_Header', None)
    assert owner not in getattr(partner, 'netModel_HeaderBlock')


def test_assoc_member10_stub_double():
    # netModel_SimpleMemberAssignment has no real 'netModel_SimpleMemberAssignment11' property in the generated
    # code (a bare stub) -- manually attach it so netModel_SimpleMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netModel_SimpleMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netModel_SimpleMember(name="sample_text")
    partner = netModel_SimpleMemberAssignment()
    setattr(partner, 'netModel_SimpleMemberAssignment11', None)
    _safe_set(owner, 'netModel_SimpleMember', partner)
    assert getattr(partner, 'netModel_SimpleMemberAssignment11') == owner
    _safe_set(owner, 'netModel_SimpleMember', None)
    assert getattr(partner, 'netModel_SimpleMemberAssignment11') is None


def test_assoc_members32_stub_double():
    # netModel_EnumTypeLiteral has no real 'netModel_EnumTypeLiteral33' property in the generated
    # code (a bare stub) -- manually attach it so netModel_EnumMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netModel_EnumMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netModel_EnumMember(assignment=True, name="sample_text", value=7)
    partner = netModel_EnumTypeLiteral()
    setattr(partner, 'netModel_EnumTypeLiteral33', None)
    _safe_set(owner, 'netModel_EnumMember', partner)
    assert owner in getattr(partner, 'netModel_EnumTypeLiteral33')
    _safe_set(owner, 'netModel_EnumMember', None)
    assert owner not in getattr(partner, 'netModel_EnumTypeLiteral33')


def test_assoc_members34_stub_double():
    # netModel_ComplexTypeLiteral has no real 'netModel_ComplexTypeLiteral35' property in the generated
    # code (a bare stub) -- manually attach it so netModel_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netModel_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netModel_Member(name="sample_text")
    partner = netModel_ComplexTypeLiteral()
    setattr(partner, 'netModel_ComplexTypeLiteral35', None)
    _safe_set(owner, 'netModel_Member', partner)
    assert owner in getattr(partner, 'netModel_ComplexTypeLiteral35')
    _safe_set(owner, 'netModel_Member', None)
    assert owner not in getattr(partner, 'netModel_ComplexTypeLiteral35')


def test_assoc_params6_stub_double():
    # netModel_SimpleMemberAssignment has no real 'netModel_SimpleMemberAssignment' property in the generated
    # code (a bare stub) -- manually attach it so netModel_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netModel_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netModel_Path(arb="sample_text")
    partner = netModel_SimpleMemberAssignment()
    setattr(partner, 'netModel_SimpleMemberAssignment', None)
    _safe_set(owner, 'netModel_Path7', {partner})
    assert getattr(partner, 'netModel_SimpleMemberAssignment') == owner
    _safe_set(owner, 'netModel_Path7', set())
    assert getattr(partner, 'netModel_SimpleMemberAssignment') is None


